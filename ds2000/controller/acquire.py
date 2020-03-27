#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>
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

from collections import namedtuple
from typing import Tuple

from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Acquire",
]

AcquireType = namedtuple("AcquireType", "type average_count")


class Type(SubController):
    def normal(self) -> None:
        """
          **Rigol Programming Guide**

          **Syntax**

          :ACQuire:TYPE <type>

          :ACQuire:TYPE?

          **Description**

          Set the acquisition mode of the sample.
          Query the current acquisition mode of the sample.

          **Parameter**

          ======= ========== ==================================== =======
          Name    Type       Range                                Default
          ======= ========== ==================================== =======
          <type>  Discrete   {NORMal|AVERages|PEAK|HRESolution}   NORMal
          ======= ========== ==================================== =======

          **Explanation**

          When AVERages is selected, use the :ACQuire:AVERages command to set
          the number of averages.

          **Return Format**
          The query returns NORM, AVER, PEAK or HRES.

          **Example**

          :ACQuire:TYPE AVERages

          The query returns AVER.
          """
        self.subdevice.device.ask(":ACQuire:TYPE NORMal")

    def average(self) -> None:
        """
          **Rigol Programming Guide**

          **Syntax**

          :ACQuire:TYPE <type>
          :ACQuire:TYPE?

          **Description**

          Set the acquisition mode of the sample.
          Query the current acquisition mode of the sample.

          **Parameter**

          ======= ========== ==================================== =======
          Name    Type       Range                                Default
          ======= ========== ==================================== =======
          <type>  Discrete   {NORMal|AVERages|PEAK|HRESolution}   NORMal
          ======= ========== ==================================== =======

          **Explanation**

          When AVERages is selected, use the :ACQuire:AVERages command to set
          the number of averages.

          **Return Format**

          The query returns NORM, AVER, PEAK or HRES.

          **Example**

          :ACQuire:TYPE AVERages

          The query returns AVER.
          """
        self.subdevice.device.ask(":ACQuire:TYPE AVERages")

    def peakdetect(self) -> None:
        """
          **Rigol Programming Guide**

          **Syntax**

          :ACQuire:TYPE <type>

          :ACQuire:TYPE?

          **Description**

          Set the acquisition mode of the sample.
          Query the current acquisition mode of the sample.

          **Parameter**

          ======= ========== ==================================== =======
          Name    Type       Range                                Default
          ======= ========== ==================================== =======
          <type>  Discrete   {NORMal|AVERages|PEAK|HRESolution}   NORMal
          ======= ========== ==================================== =======

          **Explanation**
          
          When AVERages is selected, use the :ACQuire:AVERages command to set
          the number of averages.

          **Return Format**

          The query returns NORM, AVER, PEAK or HRES.

          **Example**

          :ACQuire:TYPE AVERages

          The query returns AVER.
          """
        self.subdevice.device.ask(":ACQuire:TYPE PEAK")

    def highres(self) -> None:
        """
          **Rigol Programming Guide**

          **Syntax**

          :ACQuire:TYPE <type>

          :ACQuire:TYPE?

          **Description**

          Set the acquisition mode of the sample.
          Query the current acquisition mode of the sample.

          **Parameter**

          ======= ========== ==================================== =======
          Name    Type       Range                                Default
          ======= ========== ==================================== =======
          <type>  Discrete   {NORMal|AVERages|PEAK|HRESolution}   NORMal
          ======= ========== ==================================== =======

          **Explanation**

          When AVERages is selected, use the :ACQuire:AVERages command to set
          the number of averages.

          **Return Format**

          The query returns NORM, AVER, PEAK or HRES.

          **Example**

          :ACQuire:TYPE AVERages

          The query returns AVER.
          """
        self.subdevice.device.ask(":ACQuire:TYPE HRESolution")

    def status(self):
        answer: str = self.subdevice.device.ask(":ACQuire:TYPE?")
        if answer == "NORM":
            return "Normal"
        elif answer == "AVER":
            return "Average"
        elif answer == "PEAK":
            return "Peak"
        elif answer == "HRES":
            return "High Resolution"
        raise Ds2000Exception("Unknown Return Value")

    def __str__(self) -> str:
        return self.status()

    def __repr__(self) -> str:
        return self.status()


class Acquire(BaseController):
    AVERAGES: Tuple[int] = (
        2,
        4,
        8,
        16,
        32,
        64,
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
    )
    MEMDEPTH_SINGLE: Tuple[int] = (14000, 140000, 1400000, 14000000, 56000000)
    MEMDEPTH_DUAL: Tuple[int] = (7000, 70000, 700000, 7000000, 28000000)

    def __init__(self, device):
        super(Acquire, self).__init__(device)
        self.type: Type = Type(self)

    def get_averages(self) -> int:
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:AVERages <count>

        :ACQuire:AVERages?

        **Description**

        Set the number of averages and the value should be a power function
        of 2. Query the current number of averages of the oscilloscope.

        **Parameter**

        ========= ========= =========== =======
        Name      Type      Range       Default
        ========= ========= =========== =======
        <count>   Integer   2 to 8192   2
        ========= ========= =========== =======

        **Explanation**

        Use the :ACQuire:TYPE command to select the average acquisition mode.
        In this mode, the oscilloscope averages the waveforms from multiple
        samples to reduce the random noise of the input signal and improve the
        vertical resolution. The greater the number of averages is, the lower
        the noise will be and the higher the vertical resolution will be but
        the slower the response of the displayed waveform to the waveform
        changes will be.

        **Return Format**

        The query returns an integer between 2 and 8192.

        **Example**
        
        :ACQuire:AVERages 128

        The query returns 128.
        """
        return self.device.ask(":ACQuire:AVERages?")

    def set_averages(self, count: int = 2):
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:AVERages <count>

        :ACQuire:AVERages?

        **Description**
        Set the number of averages and the value should be a power function
        of 2. Query the current number of averages of the oscilloscope.

        **Parameter**
        
        ========= ========= =========== =======
        Name      Type      Range       Default
        ========= ========= =========== =======
        <count>   Integer   2 to 8192   2
        ========= ========= =========== =======

        **Explanation**

        Use the :ACQuire:TYPE command to select the average acquisition mode.
        In this mode, the oscilloscope averages the waveforms from multiple
        samples to reduce the random noise of the input signal and improve the
        vertical resolution. The greater the number of averages is, the lower
        the noise will be and the higher the vertical resolution will be but
        the slower the response of the displayed waveform to the waveform
        changes will be.

        **Return Format**

        The query returns an integer between 2 and 8192.

        **Example**

        :ACQuire:AVERages 128

        The query returns 128.
        """
        assert isinstance(count, int)
        if count == 0:
            return
        elif count in Acquire.AVERAGES:
            self.device.ask(f":ACQuire:AVERages {count}")
        raise ValueError(
            'The "count" must be 0, to leave the count'
            f"untouched or set it to {Acquire.AVERAGES}."
        )  # TODO HERE

    def get_memorydepth(self) -> int:
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:MDEPth <mdep>

        :ACQuire:MDEPth?

        **Description**

        Set the memory depth of the oscilloscope namely the number of
        waveform points that can be stored in a single trigger sample.
        Query the current memory depth of the oscilloscope.

        **Parameter**

        ======== ========== ====================== =======
        Name     Type       Range                  Default
        ======== ========== ====================== =======
        <mdep>   Discrete   Refer to Explanation   AUTO
        ======== ========== ====================== =======

        **Explanation**

        When a single channel is on:
        <mdep> can be set to AUTO|14000|140000|1400000|14000000|56000000.

        When dual channels are on:
        <mdep> can be set to AUTO|7000|70000|700000|7000000|28000000.

        **Return Format**

        The query returns the actual number of points (integer) or AUTO.

        **Example**

        :ACQuire:MDEPth 1400000

        The query returns 1400000.
        """
        return self.device.ask(":ACQuire:MDEPth?")

    def set_memorydepth(self, memdepth: int = 0):
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:MDEPth <mdep>

        :ACQuire:MDEPth?

        **Description**

        Set the memory depth of the oscilloscope namely the number of
        waveform points that can be stored in a single trigger sample.
        Query the current memory depth of the oscilloscope.

        **Parameter**

        ======== ========== ====================== =======
        Name     Type       Range                  Default
        ======== ========== ====================== =======
        <mdep>   Discrete   Refer to Explanation   AUTO
        ======== ========== ====================== =======

        **Explanation**

        When a single channel is on:

        <mdep> can be set to AUTO|14000|140000|1400000|14000000|56000000.

        When dual channels are on:

        <mdep> can be set to AUTO|7000|70000|700000|7000000|28000000.

        **Return Format**

        The query returns the actual number of points (integer) or AUTO.

        **Example**

        :ACQuire:MDEPth 1400000

        The query returns 1400000.
        """
        assert isinstance(memdepth, int)
        if memdepth == 0:
            self.device.ask(":ACQuire:MEMDepth AUTO")
        # ToDo: Check if osc uses one or two channels
        elif memdepth in Acquire.MEMDEPTH_SINGLE:
            self.device.ask(f":ACQuire:MDEPth {memdepth}")
        elif memdepth in Acquire.MEMDEPTH_DUAL:
            self.device.ask(f":ACQuire:MDEPth {memdepth}")

    def get_samplerate(self) -> int:
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:SRATe?

        **Description**

        Query the current sample rate.

        **Return Format**

        The query returns the sample rate in scientific notation.

        **Example**

        :ACQuire:SRATe?

        The query returns 2.000000e+09.
        """
        return int(self.device.ask(":ACQuire:SRATe?"))

    def get_antialiasing(self) -> bool:
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:AALias <bool>

        :ACQuire:AALias?

        **Description**

        Enable or disable the antialiasing function of the oscilloscope.
        The query returns the current state of the antialiasing function of the
        oscilloscope.

        **Parameter**

        ======== ====== ================== =======
        Name     Type   Range              Default
        ======== ====== ================== =======
        <bool>   Bool   {{0|OFF}|{1|ON}}   0|OFF
        ======== ====== ================== =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :ACQuire:AALias ON

        The query returns 1.
        """
        return bool(self.device.ask(":ACQuire:AALias?"))

    def set_antialiasing(self, enabled: bool = False):
        """
        **Rigol Programming Guide**

        **Syntax**

        :ACQuire:AALias <bool>

        :ACQuire:AALias?

        **Description**

        Enable or disable the antialiasing function of the oscilloscope.
        The query returns the current state of the antialiasing function of the
        oscilloscope.

        **Parameter**

        ======== ====== ================== =======
        Name     Type   Range              Default
        ======== ====== ================== =======
        <bool>   Bool   {{0|OFF}|{1|ON}}   0|OFF
        ======== ====== ================== =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :ACQuire:AALias ON

        The query returns 1.
        """
        assert isinstance(enabled, bool)
        self.device.ask(f":ACQuire:AALias {1 if enabled else 0}")
