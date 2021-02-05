#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020-2021  Michael Sasser <Michael@MichaelSasser.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ds2000.common import SFunc, SSFunc, channel_as_enum
from ds2000.common import check_input
from ds2000.common import check_level
from ds2000.enums import ChannelEnum, TriggerSPISlopeEnum
from ds2000.errors import DS2000StateError


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"




class SPISource(SSFunc):
    def __init__(self, device, source: str):
        super(SPISource, self).__init__(device)
        self.src: str = source

    def set_channel_1(self) -> None:
        """Select the channel source in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SCL <source>
        :TRIGger:SPI:SCL?

        :TRIGger:SPI:SDA <source>
        :TRIGger:SPI:SDA?

        **Description**

        Select the SCL channel source in SPI trigger.
        Query the current SCL channel source in SPI trigger.

        Select the SDA channel source in SPI trigger.
        Query the current SDA channel source in SPI trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SPI:SCL CHANnel2
        The query returns CHAN2.

        :TRIGger:SPI:SDA CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:SPI:{self.src} CHANnel1")

    def set_channel_2(self) -> None:
        """Select the channel source in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SCL <source>
        :TRIGger:SPI:SCL?

        :TRIGger:SPI:SDA <source>
        :TRIGger:SPI:SDA?

        **Description**

        Select the SCL channel source in SPI trigger.
        Query the current SCL channel source in SPI trigger.

        Select the SDA channel source in SPI trigger.
        Query the current SDA channel source in SPI trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SPI:SCL CHANnel2
        The query returns CHAN2.

        :TRIGger:SPI:SDA CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:SPI:{self.src} CHANnel2")

    def status(self) -> ChannelEnum:
        """Select the channel source in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SCL <source>
        :TRIGger:SPI:SCL?

        :TRIGger:SPI:SDA <source>
        :TRIGger:SPI:SDA?

        **Description**

        Select the SCL channel source in SPI trigger.
        Query the current SCL channel source in SPI trigger.

        Select the SDA channel source in SPI trigger.
        Query the current SDA channel source in SPI trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SPI:SCL CHANnel2
        The query returns CHAN2.

        :TRIGger:SPI:SDA CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(
            self.instrument.ask(f":TRIGger:SPI:{self.src}?")
        )


class SPISlope(SSFunc):
    def set_positive(self) -> None:
        """Set the trigger edge of the clock signal in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SLOPe <slope>
        :TRIGger:SPI:SLOPe?

        **Description**

        Set the trigger edge of the clock signal in SPI trigger.
        Query the current trigger edge of the clock signal in SPI trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SPI:SLOPe POSitive
        The query returns POS.
        """
        self.instrument.ask(":TRIGger:SPI:SLOPe POSitive")

    def set_negative(self) -> None:
        """Set the trigger edge of the clock signal in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SLOPe <slope>
        :TRIGger:SPI:SLOPe?

        **Description**

        Set the trigger edge of the clock signal in SPI trigger.
        Query the current trigger edge of the clock signal in SPI trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SPI:SLOPe POSitive
        The query returns POS.
        """
        self.instrument.ask(":TRIGger:SPI:SLOPe NEGative")

    def status(self) -> TriggerSPISlopeEnum:
        """Query the current trigger edge of the clock signal in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SLOPe <slope>
        :TRIGger:SPI:SLOPe?

        **Description**

        Set the trigger edge of the clock signal in SPI trigger.
        Query the current trigger edge of the clock signal in SPI trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SPI:SLOPe POSitive
        The query returns POS.
        """
        answer: str = self.instrument.ask(":TRIGger:SPI:SLOPe?")
        if answer == "POS":
            return TriggerSPISlopeEnum.POSITIVE
        if answer == "NEG":
            return TriggerSPISlopeEnum.NEGATIVE
        raise DS2000StateError()


class SPI(SFunc):
    def __init__(self, device):
        super(SPI, self).__init__(device)
        self.source_scl: SPISource = SPISource(self, "SCL")
        self.source_sda: SPISource = SPISource(self, "SDA")

    def set_width(self, width: int = 8) -> None:
        """Set the bits of SDA in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:WIDTh <width>
        :TRIGger:SPI:WIDTh?

        **Description**

        Set the bits of SDA in SPI trigger.
        Query the current bits of SDA in SPI trigger.

        **Parameter**

        ======== ======== ======== =======
        Name     Type     Range    Default
        ======== ======== ======== =======
        <width>  Integer  4 to 32  8
        ======== ======== ======== =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:SPI:WIDTh 10
        The query returns 10.
        """
        check_input(width, "width", int, 4, 32)
        self.instrument.ask(f":TRIGger:SPI:WIDTh {width}")

    def get_width(self) -> int:
        """Query the current bits of SDA in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:WIDTh <width>
        :TRIGger:SPI:WIDTh?

        **Description**

        Set the bits of SDA in SPI trigger.
        Query the current bits of SDA in SPI trigger.

        **Parameter**

        ======== ======== ======== =======
        Name     Type     Range    Default
        ======== ======== ======== =======
        <width>  Integer  4 to 32  8
        ======== ======== ======== =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:SPI:WIDTh 10
        The query returns 10.
        """
        return int(self.instrument.ask(":TRIGger:SPI:WIDTh?"))

    def set_data(self, data: int = 0) -> None:
        """Set the data value in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:DATA <data>
        :TRIGger:SPI:DATA?

        **Description**

        Set the data value in SPI trigger.
        Query the current data value in SPI trigger.

        **Parameter**

        ======= ======== =================== =======
        Name    Type     Range               Default
        ======= ======== =================== =======
        <data>  Integer  0 to $ 2^{n} – 1 $  0
        ======= ======== =================== =======

        Note: in the expression 2n-1, n is the current data bits (refer to the
        :TRIGger:SPI:WIDTh command).

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:SPI:DATA 5
        The query returns 5.
        """
        check_input(data, "data", int, 0, 2 ** self.get_width() - 1)
        self.instrument.ask(f":TRIGger:SPI:DATA {data}")

    def get_data(self) -> int:
        """Query the current data value in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:DATA <data>
        :TRIGger:SPI:DATA?

        **Description**

        Set the data value in SPI trigger.
        Query the current data value in SPI trigger.

        **Parameter**

        ======= ======== =================== =======
        Name    Type     Range               Default
        ======= ======== =================== =======
        <data>  Integer  0 to $ 2^{n} – 1 $  0
        ======= ======== =================== =======

        Note: in the expression 2n-1, n is the current data bits (refer to the
        :TRIGger:SPI:WIDTh command).

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:SPI:DATA 5
        The query returns 5.
        """
        return int(self.instrument.ask(":TRIGger:SPI:DATA?"))

    def set_timeout(self, time: float = 1.0e-6) -> None:
        """Set the timeout time in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:TIMeout <time_value>
        :TRIGger:SPI:TIMeout?

        **Description**

        Set the timeout time in SPI trigger when the trigger condition is
        Timeout and the unit is s.
        Query the current timeout time in SPI trigger when the trigger
        condition is Timeout.

        **Parameter**

        ============= ===== ============ =======
        Name          Type  Range        Default
        ============= ===== ============ =======
        <time_value>  Real  100ns to 1s  1µs
        ============= ===== ============ =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:SPI:TIMeout 0.000002
        The query returns 2.000000e-06.
        """
        check_input(time, "time", float, 100.0e-9, 1.0, "s")
        self.instrument.ask(f":TRIGger:SPI:TIMeout {time}")

    def get_timeout(self) -> float:
        """Query the current timeout time in SPI trigge.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:TIMeout <time_value>
        :TRIGger:SPI:TIMeout?

        **Description**

        Set the timeout time in SPI trigger when the trigger condition is
        Timeout and the unit is s.
        Query the current timeout time in SPI trigger when the trigger
        condition is Timeout.

        **Parameter**

        ============= ===== ============ =======
        Name          Type  Range        Default
        ============= ===== ============ =======
        <time_value>  Real  100ns to 1s  1µs
        ============= ===== ============ =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:SPI:TIMeout 0.000002
        The query returns 2.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:SPI:TIMeout?"))

    def set_scl_trigger_level(self, level: float = 0.0) -> None:
        """Set the trigger level of SCL in SPI trigge.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:CLEVel <level>
        :TRIGger:SPI:CLEVel?

        **Description**

        Set the trigger level of SCL in SPI trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SCL in SPI trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source_scl.status()
        if channel == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:SPI:CLEVel {level}")

    def get_scl_trigger_level(self) -> float:
        """Query the current trigger level of SCL in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:CLEVel <level>
        :TRIGger:SPI:CLEVel?

        **Description**

        Set the trigger level of SCL in SPI trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SCL in SPI trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:SPI:CLEVel?"))

    def set_sda_trigger_level(self, level: float = 0.0) -> None:
        """Set the trigger level of SDA in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:DLEVel <level>
        :TRIGger:SPI:DLEVel?

        **Description**

        Set the trigger level of SDA in SPI trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SDA in SPI trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source_sda.status()
        if channel == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:SPI:DLEVel {level}")

    def get_sda_trigger_level(self) -> float:
        """Query the current trigger level of SDA in SPI trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:DLEVel <level>
        :TRIGger:SPI:DLEVel?

        **Description**

        Set the trigger level of SDA in SPI trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SDA in SPI trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:SPI:DLEVel?"))
