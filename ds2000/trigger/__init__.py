#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020-2021  Michael Sasser <Michael@MichaelSasser.org>
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

from ds2000.common import Func

from .coupling import Coupling
from .delay import Delay
from .duration import Duration
from .edge import Edge
from .i2c import I2C
from .mode import Mode
from .nth_edge import NthEdge
from .pattern import Pattern
from .pulse import Pulse
from .rs232 import RS232
from .runt import Runt
from .setup_hold import SetupHold
from .slope import Slope
from .spi import SPI
from .sweep import Sweep
from .timeout import Timeout
from .usb import USB
from .video import Video
from .windows import Windows


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Trigger(Func):
    def __init__(self, dev):
        super(Trigger, self).__init__(dev)
        self.mode: Mode = Mode(self)
        self.coupling: Coupling = Coupling(self)
        self.sweep: Sweep = Sweep(self)
        self.edge: Edge = Edge(self)
        self.pulse: Pulse = Pulse(self)
        self.runt: Runt = Runt(self)
        self.windows: Windows = Windows(self)
        self.nth_edge: NthEdge = NthEdge(self)
        self.slope: Slope = Slope(self)
        self.video: Video = Video(self)
        self.pattern: Pattern = Pattern(self)
        self.delay: Delay = Delay(self)
        self.timeout: Timeout = Timeout(self)
        self.duration: Duration = Duration(self)
        self.setup_hold: SetupHold = SetupHold(self)
        self.rs232: RS232 = RS232(self)
        self.iic: I2C = I2C(self)  # change to i2c
        self.spi: SPI = SPI(self)
        self.usb: USB = USB(self)

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        TRIGger:STATus?

        **Description**

        Query the current trigger status.

        **Return Format**

        The query returns TD, WAIT, RUN, AUTO or STOP.
        """
        return self.dev.ask("TRIGger:STATus?").lower()

    def get_holdoff(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:HOLDoff <value>
        :TRIGger:HOLDoff?

        **Description**

        Set the trigger holdoff time and the unit is s.
        Query the current trigger holdoff time.

        **Parameter**

        ======== ===== ============= =======
        Name     Type  Range         Default
        ======== ===== ============= =======
        <value>  Real  100ns to 10s  100ns
        ======== ===== ============= =======

        **Explanation**

        This setting is not available for the Nth edge trigger, video trigger,
        RS232 trigger, IIC trigger, SPI trigger and USB trigger.

        **Return Format**

        The query returns the trigger holdoff time in scientific notation.

        Example

        :TRIGger:HOLDoff 0.0000002
        The query returns 2.000000e-07.
        """
        return float(self.dev.ask(":TRIGger:HOLDoff?"))

    def set_holdoff(self, time: float = 100.0e-9) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:HOLDoff <value>
        :TRIGger:HOLDoff?

        **Description**

        Set the trigger holdoff time and the unit is s.
        Query the current trigger holdoff time.

        **Parameter**

        ======== ===== ============= =======
        Name     Type  Range         Default
        ======== ===== ============= =======
        <value>  Real  100ns to 10s  100ns
        ======== ===== ============= =======

        **Explanation**

        This setting is not available for the Nth edge trigger, video trigger,
        RS232 trigger, IIC trigger, SPI trigger and USB trigger.

        **Return Format**

        The query returns the trigger holdoff time in scientific notation.

        Example

        :TRIGger:HOLDoff 0.0000002
        The query returns 2.000000e-07.
        """
        if not isinstance(time, float) or not 100.0e-9 <= time <= 10:
            ValueError(
                f'"time" must be of type float and between '
                f"100ns..10s. You entered {type(time)}."
            )
        self.dev.ask(f":TRIGger:HOLDoff {time}")

    def get_noise_reject(self) -> bool:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NREJect <bool>
        :TRIGger:NREJect?

        **Description**

        Enable or disable noise reject.
        Query the current status of noise reject.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        ++Example**

        :TRIGger:NREJect ON
        The query returns 1.
        """
        return bool(int(self.dev.ask(":TRIGger:NREJect?")))

    def set_noise_reject(self, enable: bool = False) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NREJect <bool>
        :TRIGger:NREJect?

        **Description**

        Enable or disable noise reject.
        Query the current status of noise reject.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        ++Example**

        :TRIGger:NREJect ON
        The query returns 1.
        """
        if not isinstance(enable, bool):
            ValueError(
                f'"enable" must be of type bool, you entered '
                f"{type(enable)}."
            )
        self.dev.ask(f":TRIGger:NREJect {enable}")
