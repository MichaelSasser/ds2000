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
    "Sweep",
]


class Sweep(SubController):
    def auto(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()

    def normal(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()

    def single(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()
