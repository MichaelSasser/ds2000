#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.de>

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

from ds2000.controller import BaseController, SubController , Ds2000Exception

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

__all__ = ["Bus", ]


class Mode(SubController):
    def parallel(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:MODE <mode>
        :BUS<n>:MODE?

        Description
        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        Parameter
        Name     Type       Range                      Default
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel

        Return Format
        The query returns PAR, RS232, IIC or SPI.

        Example
        :BUS1:MODE SPI
        The query returns SPI.

        :return:
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:MODE PARallel")

    def rs232(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:MODE <mode>
        :BUS<n>:MODE?

        Description
        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        Parameter
        Name     Type       Range                      Default
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel

        Return Format
        The query returns PAR, RS232, IIC or SPI.

        Example
        :BUS1:MODE SPI
        The query returns SPI.

        :return:
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE RS232")

    def i2c(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:MODE <mode>
        :BUS<n>:MODE?

        Description
        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        Parameter
        Name     Type       Range                      Default
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel

        Return Format
        The query returns PAR, RS232, IIC or SPI.

        Example
        :BUS1:MODE SPI
        The query returns SPI.

        :return:
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE IIC")

    def spi(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:MODE <mode>
        :BUS<n>:MODE?

        Description
        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        Parameter
        Name     Type       Range                      Default
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel

        Return Format
        The query returns PAR, RS232, IIC or SPI.

        Example
        :BUS1:MODE SPI
        The query returns SPI.

        :return:
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE SPI")

    def get(self) -> str:
        answer = self.subdevice.ask(f":BUS{self.subdevice.busnumber}:MODE?")
        if answer == "PAR":
            return "Parallel"
        elif answer == "RS232":
            return "RS232"
        elif answer == "IIC":
            return "I2C"
        elif answer == "SPI":
            return "SPI"
        else:
            raise Ds2000Exception("Unknown Bus Mode")

    def __str__(self) -> str:
        return str(self.get)

    def __repr__(self) -> str:
        return str(self.get())


class Format(SubController):
    def hex(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:FORMat <format>
        :BUS<n>:FORMat?

        Description
        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary or ASCII.
        Query the current display format of bus 1 or 2.

        Parameter
        Name       Type       Range                 Default
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX

        Return Format
        The query returns HEX, DEC, BIN or ASC.

        Example
        :BUS1:FORMat DEC
        The query returns DEC.

        :return:
        """
        self.subdevice.device.ask(
                f":BUS{self.subdevice.__busnumber}:FORMAT HEX")

    def dec(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:FORMat <format>
        :BUS<n>:FORMat?

        Description
        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary or ASCII.
        Query the current display format of bus 1 or 2.

        Parameter
        Name       Type       Range                 Default
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX

        Return Format
        The query returns HEX, DEC, BIN or ASC.

        Example
        :BUS1:FORMat DEC
        The query returns DEC.

        :return:
        """
        self.subdevice.device.ask(
                f":BUS{self.subdevice.__busnumber}:FORMAT DEC")

    def bin(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:FORMat <format>
        :BUS<n>:FORMat?

        Description
        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary or ASCII.
        Query the current display format of bus 1 or 2.

        Parameter
        Name       Type       Range                 Default
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX

        Return Format
        The query returns HEX, DEC, BIN or ASC.

        Example
        :BUS1:FORMat DEC
        The query returns DEC.

        :return:
        """
        self.subdevice.device.ask(
                f":BUS{self.subdevice.__busnumber}:FORMAT BIN")

    def ascii(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:FORMat <format>
        :BUS<n>:FORMat?

        Description
        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary or ASCII.
        Query the current display format of bus 1 or 2.

        Parameter
        Name       Type       Range                 Default
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX

        Return Format
        The query returns HEX, DEC, BIN or ASC.

        Example
        :BUS1:FORMat DEC
        The query returns DEC.

        :return:
        """
        self.subdevice.device.ask(
                f":BUS{self.subdevice.__busnumber}:FORMAT ASCii")

    def get(self) -> str:
        answer = self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:FORMAT?")
        if answer == "HEX":
            return "HEX"
        elif answer == "DEC":
            return "DEC"
        elif answer == "BIN":
            return "BIN"
        elif answer == "ASC":
            return "ASCII"
        else:
            raise Ds2000Exception("Unknown Bus Format")

    def __str__(self) -> str:
        return str(self.get)

    def __repr__(self) -> str:
        return str(self.get())


class Bus(BaseController):
    def __init__(self, device, busnumber):
        super(Bus, self).__init__(device)
        self.__busnumber = busnumber

        # Device Subclasses
        self.mode: Mode = Mode(self)
        self.format: Mode = Format(self)

    @property
    def display(self) -> bool:
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:DISPlay <bool>
        :BUS<n>:DISPlay?

        Description
        Enable or disable the display of bus 1 or 2.
        Query the current display status of bus 1 or 2.

        Parameter
        Name     Type       Range              Default
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF

        Return Format
        The query returns 0 or 1.

        Example
        :BUS1:DISPlay ON
        The query returns 1.

        :return:
        """
        return True if self.device.ask(
                f":BUS{self.__busnumber}:DISPlay?") == 1 else False

    @display.setter
    def display(self, enable: bool = True):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:DISPlay <bool>
        :BUS<n>:DISPlay?

        Description
        Enable or disable the display of bus 1 or 2.
        Query the current display status of bus 1 or 2.

        Parameter
        Name     Type       Range              Default
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF

        Return Format
        The query returns 0 or 1.

        Example
        :BUS1:DISPlay ON
        The query returns 1.

        :return:
        """
        assert isinstance(enable, bool)
        self.device.ask(f":BUS{self.__busnumber}:DISPlay {1 if enable else 0}")

    @property
    def eventtable(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:EVENt <bool>
        :BUS<n>:EVENt?

        Description
        Enable or disable the event table of bus 1 or bus 2.
        Query the current status of the event table of bus 1 or bus 2.

        Parameter
        Name     Type       Range              Default
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF

        Return Format
        The query returns 0 or 1.

        Example
        :BUS1:EVENt ON
        The query returns 1.

        :return:
        """
        return True if self.device.ask(
                f":BUS{self.__busnumber}:EVENt?") == 1 else False

    @eventtable.setter
    def eventtable(self, enable: bool = True):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:EVENt <bool>
        :BUS<n>:EVENt?

        Description
        Enable or disable the event table of bus 1 or bus 2.
        Query the current status of the event table of bus 1 or bus 2.

        Parameter
        Name     Type       Range              Default
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF

        Return Format
        The query returns 0 or 1.

        Example
        :BUS1:EVENt ON
        The query returns 1.

        :return:
        """
        assert isinstance(enable, bool)
        self.device.ask(f":BUS{self.__busnumber}:EVENt {1 if enable else 0}")

    def export_eventtable_to_usb(self):
        """

        Rigol Programming Guide:

        Syntax
        :BUS<n>:EEXPort

        Description
        Export the event table of bus 1 or 2.

        Parameter
        Name   Type       Range   Default
        <n>    Discrete   {1|2}   --

        Explanation
        The data list can be exported to external USB storage device in CSV
        format if USB storage device is currently connected.

        :return:
        """
        self.device.ask(f":BUS{self.__busnumber}:EEXPort")

    # ToDo: Page 51


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())
