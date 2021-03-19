#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018-2021  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

from logging import debug
from types import TracebackType
from typing import List
from typing import Optional
from typing import Type

from .acquire import Acquire
from .channel import Channel
from .display import Display
from .errors import DS2000DriverNotFoundError
from .ieee import IEEE
from .timebase import Timebase
from .trigger import Trigger
from .visa.debug_driver import DebugDriver
from .visa.driver import InstrumentInfo
from .visa.driver import VISABase
from .visa.driver import VISADriver
from .waveform import Waveform


Available_Drivers: List[VISADriver] = [VISADriver.DEBUG_DRIVER]

# TODO: Remove NotImplementedError
try:
    from .visa.vxi11 import VXI11

    Available_Drivers.append(VISADriver.VXI11)
    debug("Driver: VXI11 is now available.")
except (ImportError, NotImplementedError):
    debug("Driver: VXI11 is not installed.")

# TODO:
try:
    from .visa.pyvisa import PYVISA

    Available_Drivers.append(VISADriver.PYVISA)
    debug("Driver: PYVISA is now available.")
except (ImportError, NotImplementedError):
    debug("Driver: PYVISA is not installed.")

try:
    from .visa.pyvisapy import PYVISAPY

    Available_Drivers.append(VISADriver.PYVISA_PY)
    debug("Driver: PYVISAPY is now available.")
except (ImportError, NotImplementedError):
    debug("Driver: PYVISAPY is not installed.")

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

DEBUGGING: bool = False


class DS2000(object):
    def __init__(
        self,
        address: str,
        driver: VISADriver = VISADriver.VXI11,
    ):
        global Available_Drivers
        self.instrument: VISABase
        if (
            driver == VISADriver.VXI11
            and VISADriver.VXI11 in Available_Drivers
        ):
            self.instrument = VXI11(address)
        elif (
            driver == VISADriver.PYVISA
            and VISADriver.PYVISA in Available_Drivers
        ):
            self.instrument = PYVISA(address)
        elif (
            driver == VISADriver.DEBUG_DRIVER
            and VISADriver.DEBUG_DRIVER in Available_Drivers
        ):
            self.instrument = DebugDriver(address)
        else:
            raise DS2000DriverNotFoundError(driver, Available_Drivers)

        # Subclasses
        self.acquire: Acquire = Acquire(self)
        self.display: Display = Display(self)
        self.timebase: Timebase = Timebase(self)
        self.ieee: IEEE = IEEE(self)
        self.trigger: Trigger = Trigger(self)
        self.waveform: Waveform = Waveform(self)
        self.channel1: Channel = Channel(self, 1)
        self.channel2: Channel = Channel(self, 2)

        self.instrument.connect()

    def __enter__(self) -> DS2000:
        return self

    def __exit__(
        self,
        _: Optional[Type[BaseException]],  # exc_type
        __: Optional[BaseException],  # exc_val
        ___: Optional[TracebackType],  # exc_tb
    ) -> None:
        self.instrument.disconnect()

    # SYSTem Commands
    def info(self) -> InstrumentInfo:
        return self.instrument.info

    def autoscale(self) -> None:
        """Enable the auto setting function.

        **Rigol Programming Guide**

        **Syntax**

        :AUToscale

        **Description**

        Enable the auto setting function.

        **Explanation**

        This command is not available when the current state of the Pass/Fail
        function is “Enable Test”. For details, refer to the :MASK:ENABle
        command.

        The oscilloscope will adjust the vertical scale, horizontal time base
        and trigger mode for optimum display of the waveform. Note that to use
        the auto setting, the frequency of the signal under test should be no
        lower than 50 Hz, the duty cycle be greater than 1% and the amplitude
        be at least 20 mVpp.
        """
        self.instrument.say(":AUToscale")

    def clear(self) -> None:
        """Clear all the waveforms on the screen.

        **Rigol Programming Guide**

        **Syntax**

        :CLEar

        **Description**

        Clear all the waveforms on the screen.

        **Explanation**

        Waveform will still be displayed if the oscilloscope is in RUN state.
        """
        self.instrument.say(":AUToscale")

    def run(self) -> None:
        """Start the oscilloscope.

        **Rigol Programming Guide**

        **Syntax**

        :RUN

        **Description**

        Start the oscilloscope.

        **Explanation**

        You can use the :STOP command to set the oscilloscope to STOP.
        """
        self.instrument.say(":RUN")

    def single(self):
        """Set the oscilloscope to single trigger mode.

        **Rigol Programming Guide**

        **Syntax**

        :SINGle

        **Description**

        Set the oscilloscope to single trigger mode.

        **Explanation**

        In single trigger mode, the oscilloscope triggers once the trigger
        conditions are met and then stops.
        In single trigger mode, using the :TFORce command can generate a
        trigger signal forcefully.

        You can use the :RUN and :STOP command to set the oscilloscope to
        Auto trigger mode or STOP state respectively.
        """
        self.instrument.ask(":SINGle")

    def stop(self) -> None:
        """Stop the oscilloscope.

        **Rigol Programming Guide**

        **Syntax**

        :STOP

        **Description**

        Stop the oscilloscope.

        **Explanation**

        You can use the :RUN command to set the oscilloscope to Run.
        """
        self.instrument.write(":STOP")

    def force(self) -> None:
        """Generate a trigger signal forcefully.

        **Rigol Programming Guide**

        **Syntax**

        :TFORce

        **Description**

        Generate a trigger signal forcefully.

        **Explanation**

        Force trigger is applicable to normal and single trigger modes.
        """
        self.instrument.say(":TFORce")

    def level50(self) -> None:
        """Set the trigger level to the vertical midpoint.

        **Rigol Programming Guide**

        **Syntax**

        :TLHAlf

        **Description**

        Set the trigger level to the vertical midpoint of the trigger signal
        amplitude.
        """
        self.instrument.say(":TLHAlf")

    def reset(self):
        self.ieee.rst()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.instrument.info.serial})"


# vim: set ft=python :
