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

from .common import Func


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class IEEE(Func):
    def __init__(self, dev):
        """Use "low level" functions which are barely untouched.

        :param dev:
        """
        super(IEEE, self).__init__(dev)

    def idn(self) -> str:
        """Get the ID chars of the device_address as Instrument Tuple.


        **Rigol Programming Guide**

        **Syntax**

        *IDN?

        **Description**

        Query the current dev information.

        **Return Format**

        Rigol Technologies,<model>,<serial number>,X.XX.XX
        <model>: the model number of the instrument.
        <serial number>: the serial number of the instrument.
        X.XX.XX: the software version of the instrument.

        **Example**

        *IDN?

        The query returns RIGOL TECHNOLOGIES,DS2202,DS2xxx,00.00.01. Instrument
        """
        return self.instrument.ask("*IDN?")

    def rst(self):
        """Restore the instrument to the default values.

        **Rigol Programming Guide**

        **Syntax**

        *RST

        **Description**

        Restore the instrument to the default values.
        """
        self.instrument.ask("*RST")
