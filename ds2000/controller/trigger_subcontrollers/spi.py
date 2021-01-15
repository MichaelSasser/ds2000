#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020  Michael Sasser <Michael@MichaelSasser.org>

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

from ds2000.controller import SubController, check_input, check_level

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Spi",
]


class Spi(SubController):
    # def __init__(self, device) -> None:
    #     super(Spi, self).__init__(device)

    def set_scl_source(self, channel: int = 1) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SCL <source>
        :TRIGger:SPI:SCL?

        **Description**

        Select the SCL channel source in SPI trigger.
        Query the current SCL channel source in SPI trigger.

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
        """
        check_input(channel, "channel", int, 1, 2)
        self.subdevice.device.ask(f":TRIGger:SPI:SCL CHANnel{channel}")

    def get_scl_source(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SCL <source>
        :TRIGger:SPI:SCL?

        **Description**

        Select the SCL channel source in SPI trigger.
        Query the current SCL channel source in SPI trigger.

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
        """
        return self.subdevice.device.ask(":TRIGger:SPI:SCL?")

    def set_sda_source(self, channel: int = 2) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SDA <source>
        :TRIGger:SPI:SDA?

        **Description**

        Select the SDA channel source in SPI trigger.
        Query the current SDA channel source in SPI trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SPI:SDA CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.subdevice.device.ask(f":TRIGger:SPI:SDA CHANnel{channel}")

    def get_sda_source(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SPI:SDA <source>
        :TRIGger:SPI:SDA?

        **Description**

        Select the SDA channel source in SPI trigger.
        Query the current SDA channel source in SPI trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SPI:SDA CHANnel2
        The query returns CHAN2.
        """
        return self.subdevice.device.ask(":TRIGger:SPI:SDA?")

    def set_width(self, width: int = 8) -> None:
        """
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
        self.subdevice.device.ask(f":TRIGger:SPI:WIDTh {width}")

    def get_width(self) -> int:
        """
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
        return int(self.subdevice.device.ask(":TRIGger:SPI:WIDTh?"))

    def set_data(self, data: int = 0) -> None:
        """
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
        self.subdevice.device.ask(f":TRIGger:SPI:DATA {data}")

    def get_data(self) -> int:
        """
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
        return int(self.subdevice.device.ask(":TRIGger:SPI:DATA?"))

    def set_timeout(self, time: float = 1.0e-6) -> None:
        """
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
        self.subdevice.device.ask(f":TRIGger:SPI:TIMeout {time}")

    def get_timeout(self) -> float:
        """
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
        return float(self.subdevice.device.ask(":TRIGger:SPI:TIMeout?"))

    def set_slope_positive(self) -> None:
        """
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
        self.subdevice.device.ask(":TRIGger:SPI:SLOPe POSitive")

    def set_slope_negative(self) -> None:
        """
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
        self.subdevice.device.ask(":TRIGger:SPI:SLOPe NEGative")

    def get_slope(self) -> str:
        """
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
        return self.subdevice.device.ask(":TRIGger:SPI:SLOPe?")

    def set_scl_trigger_level(self, level: float = 0.0) -> None:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_scl_source()
        if channel == "CHANnel1":
            scale = self.subdevice.device.channel1.get_scale()
            offset = self.subdevice.device.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.subdevice.device.channel2.scale()
            offset = self.subdevice.device.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.subdevice.device.ask(f":TRIGger:SPI:CLEVel {level}")

    def get_scl_trigger_level(self) -> float:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.subdevice.device.ask(":TRIGger:SPI:CLEVel?"))

    def set_sda_trigger_level(self, level: float = 0.0) -> None:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_sda_source()
        if channel == "CHANnel1":
            scale = self.subdevice.device.channel1.get_scale()
            offset = self.subdevice.device.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.subdevice.device.channel2.scale()
            offset = self.subdevice.device.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.subdevice.device.ask(f":TRIGger:SPI:DLEVel {level}")

    def get_sda_trigger_level(self) -> float:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:SPI:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.subdevice.device.ask(":TRIGger:SPI:DLEVel?"))
