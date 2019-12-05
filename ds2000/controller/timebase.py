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

__all__ = ["Timebase", ]


class Timebase(BaseController):
    def mode(self):
        """
        Rigol Programming Guide:

        :TIMebase:MODE
        Command Format:
        :TIMebase:MODE <mode>
        :TIMebase:MODE?
        Function Explanation:
        The commands set and query the scan mode of horizontal timebase. <mode> could be MAIN (main timebase) or DELayed (delayed scan).
        Returned Format:
        The query returns MAIN or DELAYED.
        Example:
        :TIM:MODE MAIN Setup the horizontal timebase as MAIN.
        :TIM:MODE? The query returns MAIN.

        :return:
        """
        raise NotImplementedError()

    def offset(self):
        """
        Rigol Programming Guide:

        :TIMebase[:DELayed]:OFFSet
        Command Format:
        :TIMebase[:DELayed]:OFFSet <offset>
        :TIMebase[:DELayed]:OFFSet?
        Function Explanation:
        The commands set and query the offset of the MAIN or DELayed timebase (that is offset of the waveform position relative to the trigger midpoint.). Thereinto,
        In NORMAL mode, the range of <scale_val> is 1s ~ end of the memory;
        In STOP mode, the range of <scale_val> is -500s ~ +500s;
        In SCAN mode, the range of <scale_val> is -6*Scale ~ +6*Scale; (Note: Scale indicates the current horizontal scale, the unit is s/div.)
        In MAIN state, the item [:DELayed] should be omitted.
        Returned Format:
        The query returns the setting value of the <offset> in s.
        Example:
        :TIM:MODE MAIN Setup the scan mode of horizontal timebase as MAIN.
        :TIM:OFFS 1 Setup the offset as 1s.
        :TIM:OFFS? The query returns 1.000e+00.

        :return:
        """
        raise NotImplementedError()

    def delayed_scale(self):
        """
        Rigol Programming Guide:

        :TIMebase[:DELayed]:SCALe
        Command Format:
        :TIMebase[:DELayed]:SCALe <scale_val>
        :TIMebase[:DELayed]:SCALe?
        Function Explanation:
        The commands set and query the horizontal scale for MAIN or DELayed timebase, the unit is s/div (seconds/grid), thereinto:
        In YT mode, the range of <scale_val> is 2ns - 50s;
        In ROLL mode, the range of <scale_val> is 500ms - 50s;
        In MAIN state, the item [:DELayed] should be omitted.
        Returned Format:
        The query returns the setting value of <scale_val> in s.
        Example:
        :TIM:MODE MAIN Setup the timebase as MAIN.
        :TIM:SCAL 2 Setup its scale as 2s.
        :TIM:SCAL? The query returns 2.000e+00.

        :return:
        """
        raise NotImplementedError()

    @property
    def scale(self) -> float:
        """
        Rigol Programming Guide:

        Syntax
        :TIMebase[:MAIN]:SCALe <scale_value>
        :TIMebase[:MAIN]:SCALe?

        Description
        Set the scale of the main time base and the unit is s/div.
        Query the current scale of the main time base.

        Name            Type    Range                   Default
        <scale_value>   Real    Depend on the time      1μs
                                base mode [1]:
                                Normal: 2ns[2] to 1ks
                                ROLL:   200ms to 1ks

        Note[1]: refer to the :TIMebase:MODE command.
        Note[2]: this value is different for different model. For DS2072 and
                 DS2012, the value is 5 ns.

        Return Format
        The query returns the current scale of the main time base in scientific notation.

        Example
        :TIMebase:MAIN:SCALe 0.0002
        The query returns 2.000000e-04.

        :return:
        """
        return float(self.device.ask(":TIMebase:MAIN:SCALe?"))

    def format(self):
        """
        Rigol Programming Guide:

        :TIMebase:FORMat
        Command Format:
        :TIMebase:FORMat <value>
        :TIMebase:FORMat?
        Function Explanation:
        The commands set and query the horizontal timebase. <value> could be XY, YT or SCANning.
        Returned Format:
        The query returns X-Y, Y-T or SCANNING.
        Example:
        :TIM:FORM YT Setup the form of grid as YT.
        :TIM:FORM? The query returns Y-T.

        :return:
        """
        raise NotImplementedError()


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())
