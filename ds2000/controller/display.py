#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>
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

from ds2000.controller import BaseController, Ds2000Exception

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Display",
]


class Display(BaseController):
    def type_vector(self):
        """

        Rigol Programming Guide:

        :DISPlay:TYPE
        Command Format:
        :DISPlay:TYPE <type>
        :DISPlay:TYPE?
        Function Explanation:
        The commands set and query the display type between sampling points.
        <type> could be VECTors (vectir display) or DOTS (point display).
        Returned Format:
        The query returns VECTORS or DOTS.
        Example:
        :DISP:TYPE VECT Setup the display type as VECTors.
        :DISP:TYPE? The query returns VECTORS.

        :return:
        """
        self.device.ask(":DISPlay:TYPE VECTors")

    def type_dot(self):
        """

        Rigol Programming Guide:

        :DISPlay:TYPE
        Command Format:
        :DISPlay:TYPE <type>
        :DISPlay:TYPE?
        Function Explanation:
        The commands set and query the display type between sampling points.
        <type> could be VECTors (vectir display) or DOTS (point display).
        Returned Format:
        The query returns VECTORS or DOTS.
        Example:
        :DISP:TYPE VECT Setup the display type as VECTors.
        :DISP:TYPE? The query returns VECTORS.

        :return:
        """
        self.device.ask(":DISPlay:TYPE DOTS")

    def type(self):
        """

        Rigol Programming Guide:

        :DISPlay:TYPE
        Command Format:
        :DISPlay:TYPE <type>
        :DISPlay:TYPE?
        Function Explanation:
        The commands set and query the display type between sampling points.
        <type> could be VECTors (vectir display) or DOTS (point display).
        Returned Format:
        The query returns VECTORS or DOTS.
        Example:
        :DISP:TYPE VECT Setup the display type as VECTors.
        :DISP:TYPE? The query returns VECTORS.

        :return:
        """
        display_type = self.device.ask(":DISPlay:TYPE?")
        if display_type == "DOTS":
            return "dot"
        elif display_type == "VECTORS":
            return "vector"
        raise Ds2000Exception("Unknown display type.")

    @property
    def grid(self) -> str:
        """

        Rigol Programming Guide:

        :DISPlay:GRID
        Command Format:
        :DISPlay:GRID <grid>
        :DISPlay:GRID?
        Function Explanation:
        The commands set and query the state of the screen grid. <grid> could
        be FULL (open the background grid and coordinates), HALF (turn off the
        background grid) or NONE (turn off the background grid and
        coordinates).
        Returned Format:
        The query returns FULL, HALF or NONE.
        Example:
        :DISP:GRID FULL Open the background grid and coordinates.
        :DISP:GRID? The query returns FULL.

        :return:
        """
        return self.device.ask(":DISPlay:GRID?").lower()

    def persist(self):
        """

        Rigol Programming Guide:

        :DISPlay:PERSist
        Command Format:
        :DISPlay:PERSist {ON|OFF}
        :DISPlay:PERSist?
        Function Explanation:
        The commands set and query the state of the waveform persist. “ON”
        denotes the record points hold until disable the presist, “OFF”
        denotes the record point varies in high refresh rate.
        Returned Format:
        The query returns ON or OFF.
        Example:
        :DISP:PERS ON Enable the waveform persist.
        :DISP:PERS? The query returns ON.

        :return:
        """
        raise NotImplementedError()

    def menu_display(self):
        """

        Rigol Programming Guide:

        :DISPlay:MNUDisplay
        Command Format:
        :DISPlay:MNUDisplay <time>
        :DISPlay:MNUDisplay?
        Function Explanation:
        The commands set and query the time for hiding menus automatically.
        <time> could be 1s, 2s, 5s, 10s, 20s or Infinite.
        Returned Format:
        The query returns 1s, 2s, 5s, 10s, 20s or Infinite.
        Example:
        :DISP:MNUD 10 Setup the display time of menu as 10s.
        :DISP:MNUD? The query returns 10s.

        :return:
        """
        raise NotImplementedError()

    def menu_status(self):
        """

        Rigol Programming Guide:

        :DISPlay:MNUStatus
        Command Format:
        :DISPlay:MNUStatus {ON|OFF}
        :DISPlay:MNUStaus?
        Function Explanation:
        The commands set and query the state of the operation menu.
        Returned Format:
        The query returns ON or OFF.
        Example:
        :DISP:MNUS ON Open menu for current operation.
        :DISP:MNUS? The query returns ON

        :return:
        """
        raise NotImplementedError()

    def clear(self):
        """

        Rigol Programming Guide:

        :DISPlay:CLEar
        Command Format:
        :DISPlay:CLEar
        Function Explanation:
        The command clears out of date waveforms on the screen during waveform
        persist.

        :return:
        """
        raise NotImplementedError()

    def brightness(self):
        """

        Rigol Programming Guide:

        :DISPlay:BRIGhtness
        Command Format:
        :DISPlay:BRIGhtness <ncount>
        :DISPlay:BRIGhtness?
        Function Explanation:
        The commands set and query the brightness of the grid. The range of
        <ncount> is from 0 to 32 (from dark to bright).
        Returned Format:
        The query returns the setting value of <ncount>.
        Example:
        :DISP:BRIG 10 Setup the grid brightness as 10.
        :DISP:BRIG? The query returns 10.

        :return:
        """
        raise NotImplementedError()

    def intensity(self):
        """

        Rigol Programming Guide:

        :DISPlay:INTensity
        Command Format:
        :DISPlay:INTensity <count>
        :DISPlay:INTensity?
        Function Explanation:
        The commands set and query the brightness of the waveform. <count>
        could be the integer between 0 and 32.
        Returned Format:
        The query returns the setting value of <count>.
        Example:
        :DISP:INT 12 Setup the waveform brightness as 12.
        :DISP:INT? The query returns 12.

        :return:
        """
        raise NotImplementedError()
