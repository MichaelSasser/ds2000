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
    def edge(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE EDGE")

    def pulse(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE PULSe")

    def runt(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE RUNT")

    def windows(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE WIND")

    def nth_edge(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE NEDG")

    def slope(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE SLOPe")

    def video(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE VIDeo")

    def pattern(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE PATTern")

    def delay(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE DELay")

    def timeout(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE TIMeout")

    def duration(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE DURATion")

    def setup_hold(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE SHOLd")

    def rs232(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE RS232")

    def i2c(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE IIC")

    def spi(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE SPI")

    def usb(self) -> None:
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
        self.subdevice.device.ask(":TRIGger:MODE USB")

    def status(self) -> str:
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
        status = self.subdevice.device.ask(":TRIGger:MODE?").lower()
        if status in ("edge", "pulse", "runt", "slope", "video", "pattern",
                      "delay", "timeout", "duration", "rs232", "spi", "usb"):
            return status
        if status == "wind":
            return "windows"
        if status == "nedg":
            return "nth edge"
        if status == "shold":
            return "setup/hold"
        if status == "iic":
            return "i2c"

