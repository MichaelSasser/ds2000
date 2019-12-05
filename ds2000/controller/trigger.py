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

from ds2000.controller import BaseController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

__all__ = ["Trigger", ]


class Edge(BaseController):
    def slope(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sensitivity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()


class Pulse(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sensitivity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def width(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

class Video(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def polarity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def standard(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def line(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sensitivity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

class Slope(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def time(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sensitivity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def window(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level_a(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level_b(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()


class Pattern(BaseController):
    def pattern(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

class Duration(BaseController):
    def pattern(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def time(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def qualifier(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

class Alternation(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def source(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def type(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def timescale(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def timeoffset(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def slope(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def time(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def polarity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def standard(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def line(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def window(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()
    def level_a(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level_b(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def coupling(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def holdoff(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sensitivity(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()


class Trigger(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def source(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def level50(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def sweep(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def coupling(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def holdoff(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def status(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()

    def force(self):
        """
        Rigol Programming Guide:



        :return:
        """
        raise NotImplementedError()


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())
