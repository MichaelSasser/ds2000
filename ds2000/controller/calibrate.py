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
from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = [
    "Calibrate",
]


class Calibrate(BaseController):
    def __init__(self, device):
        super(Calibrate, self).__init__(device)

    def date(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALibrate:DATE?

        **Description**

        Query the date of the last calibration.

        **Return Format**

        The query returns the date in <year>,<month>,<day> format.
        Wherein, <day> and <month> are double-digit figures and <year> is a
        four-digit figure.

        **Example**

        :CALibrate:DATE?

        The query returns the date of the last calibration, for example,
        2012,03,09.
        """
        raise NotImplementedError()

    def start(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALibrate:STARt

        **Description**

        The oscilloscope starts to execute self-calibration.

        **Explanation**

        The self-calibration can make the oscilloscope quickly reach its
        optimum working state to obtain the most accurate measurement values.
        The functions of most of the keys are disabled during the
        self-calibration.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALibrate:TIME?

        **Description**

        Query the time used by the last calibration.

        **Return Format**

        The query returns the time in <hours>,<minutes>,<seconds> format.
        Wherein, <hours>, <minutes> and <seconds> are all double-digit figures.

        **Example**

        :CALibrate:TIME?

        The query returns the time used by the last calibration, for example,
        13,57,38, namely 13 hours, 57 minutes and 38 seconds.
        """
        raise NotImplementedError()

    def quit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALibrate:QUIT

        **Description**

        Exit the calibration at any time.
        """
        raise NotImplementedError()
