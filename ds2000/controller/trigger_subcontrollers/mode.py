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
    "Mode",
]


class Mode(SubController):
    def edge(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def pulse(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def runt(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def wind(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def nedge(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def video(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def pattern(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def delay(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def timeout(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def duration(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def shold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def rs232(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def iic(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def spi(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def usb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()
