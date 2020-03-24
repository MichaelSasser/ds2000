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

from ds2000.controller import SubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Spi",
]


class Spi(SubController):
    def __init__(self, device):
        super(Spi, self).__init__(device)

    def scl_source(self):
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
        raise NotImplementedError()

    def sda_source(self):
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
        raise NotImplementedError()

    def width(self):
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
        raise NotImplementedError()

    def data(self):
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
        raise NotImplementedError()

    def timeout(self):
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
        <time_value>  Real  100ns to 1s  1us
        ============= ===== ============ =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:SPI:TIMeout 0.000002
        The query returns 2.000000e-06.
        """
        raise NotImplementedError()

    def slope(self, positive:  bool = True):
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
        raise NotImplementedError()

    def scl_trigger_level(self):
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
        raise NotImplementedError()

    def sda_trigger_level(self):
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
        raise NotImplementedError()
