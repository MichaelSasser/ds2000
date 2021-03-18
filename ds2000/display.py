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

import math

from .common import Func
from .common import SFunc
from .common import check_input
from .errors import DS2000Error


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class DisplayType(SFunc):
    def set_vectors(self):
        """Set the display mode of the waveform on the screen.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:TYPE <type>
        :DISPlay:TYPE?

        **Description**

        Set the display mode of the waveform on the screen.
        Query the current display mode of the waveform on the screen.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <type>  Discrete  {VECTors,DOTS}  VECTors
        ======= ========= =============== =======

        **Explanation**

        VECTors: the sample points are connected by lines and displayed.
        Normally, this mode can provide the most vivid waveform to view the
        steep edge of the waveform (such as square waveform).

        DOTS: display the sample points directly. You can directly view each
        sample point and use the cursor to measure the X and Y values of the
        sample point.

        **Return Format**

        The query returns VECT or DOTS.

        **Example**

        :DISPlay:TYPE DOTS
        The query returns DOTS.
        """
        self.instrument.say(":DISPlay:TYPE VECTors")

    def set_dots(self):
        """Set the display mode of the waveform on the screen.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:TYPE <type>
        :DISPlay:TYPE?

        **Description**

        Set the display mode of the waveform on the screen.
        Query the current display mode of the waveform on the screen.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <type>  Discrete  {VECTors,DOTS}  VECTors
        ======= ========= =============== =======

        **Explanation**

        VECTors: the sample points are connected by lines and displayed.
        Normally, this mode can provide the most vivid waveform to view the
        steep edge of the waveform (such as square waveform).
        DOTS: display the sample points directly. You can directly view each
        sample point and use the cursor to measure the X and Y values of the
        sample point.

        **Return Format**

        The query returns VECT or DOTS.

        **Example**

        :DISPlay:TYPE DOTS
        The query returns DOTS.
        """
        self.instrument.say(":DISPlay:TYPE DOTS")

    def status(self):
        """Query the display mode of the waveform on the screen.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:TYPE <type>
        :DISPlay:TYPE?

        **Description**

        Set the display mode of the waveform on the screen.
        Query the current display mode of the waveform on the screen.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <type>  Discrete  {VECTors,DOTS}  VECTors
        ======= ========= =============== =======

        **Explanation**

        VECTors: the sample points are connected by lines and displayed.
        Normally, this mode can provide the most vivid waveform to view the
        steep edge of the waveform (such as square waveform).
        DOTS: display the sample points directly. You can directly view each
        sample point and use the cursor to measure the X and Y values of the
        sample point.

        **Return Format**

        The query returns VECT or DOTS.

        **Example**

        :DISPlay:TYPE DOTS
        The query returns DOTS.
        """
        display_type = self.instrument.ask(":DISPlay:TYPE?").lower()
        if display_type in ("dots", "vectors"):
            return display_type
        raise DS2000Error("Unknown type of display grid.")


class DisplayGrid(SFunc):
    def set_full(self):
        """Set the grid type of screen display.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRID <grid>
        :DISPlay:GRID?

        **Description**

        Set the grid type of screen display.
        Query the current grid type of screen display.

        **Parameter**

        ======= ========= ================= =======
        Name    Type      Range             Default
        ======= ========= ================= =======
        <grid>  Discrete  {FULL,HALF,NONE}  FULL
        ======= ========= ================= =======

        **Explanation**

        **FULL**: turn the background grid and coordinate on.

        **HALF**: turn the background grid off.

        **NONE**: turn the background grid and coordinate off.

        **Return Format**

        The query returns FULL, HALF or NONE.

        **Example**

        :DISPlay:GRID NONE
        The query returns NONE.
        """
        self.instrument.say(":DISPlay:GRID FULL")

    def set_half(self):
        """Set the grid type of screen display.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRID <grid>
        :DISPlay:GRID?

        **Description**

        Set the grid type of screen display.
        Query the current grid type of screen display.

        **Parameter**

        ======= ========= ================= =======
        Name    Type      Range             Default
        ======= ========= ================= =======
        <grid>  Discrete  {FULL,HALF,NONE}  FULL
        ======= ========= ================= =======

        **Explanation**

        **FULL**: turn the background grid and coordinate on.

        **HALF**: turn the background grid off.

        **NONE**: turn the background grid and coordinate off.

        **Return Format**

        The query returns FULL, HALF or NONE.

        **Example**

        :DISPlay:GRID NONE
        The query returns NONE.
        """
        self.instrument.say(":DISPlay:GRID HALF")

    def set_none(self):
        """Set the grid type of screen display.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRID <grid>
        :DISPlay:GRID?

        **Description**

        Set the grid type of screen display.
        Query the current grid type of screen display.

        **Parameter**

        ======= ========= ================= =======
        Name    Type      Range             Default
        ======= ========= ================= =======
        <grid>  Discrete  {FULL,HALF,NONE}  FULL
        ======= ========= ================= =======

        **Explanation**

        **FULL**: turn the background grid and coordinate on.

        **HALF**: turn the background grid off.

        **NONE**: turn the background grid and coordinate off.

        **Return Format**

        The query returns FULL, HALF or NONE.

        **Example**

        :DISPlay:GRID NONE
        The query returns NONE.
        """
        self.instrument.say(":DISPlay:GRID NONE")

    def status(self) -> str:
        """Query the grid type of screen display.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRID <grid>
        :DISPlay:GRID?

        **Description**

        Set the grid type of screen display.
        Query the current grid type of screen display.

        **Parameter**

        ======= ========= ================= =======
        Name    Type      Range             Default
        ======= ========= ================= =======
        <grid>  Discrete  {FULL,HALF,NONE}  FULL
        ======= ========= ================= =======

        **Explanation**

        **FULL**: turn the background grid and coordinate on.

        **HALF**: turn the background grid off.

        **NONE**: turn the background grid and coordinate off.

        **Return Format**

        The query returns FULL, HALF or NONE.

        **Example**

        :DISPlay:GRID NONE
        The query returns NONE.
        """
        return self.instrument.ask(":DISPlay:GRID?").lower()


class Display(Func):
    # 0.0 for MIN and -1.0 or math.inf for INFINITE
    GRID_GRADING_TIMES = (
        0.0,
        0.05,
        0.1,
        0.2,
        0.5,
        1,
        2,
        5,
        10,
        20,
        -1.0,
        math.inf,
    )

    MENU_DISPLAY_TIME = (1, 2, 5, 10, 20, -1)  # -1 means INFINITE

    def __init__(self, dev) -> None:
        super(Display, self).__init__(dev)
        self.type: DisplayType = DisplayType(self)
        self.grid: DisplayGrid = DisplayGrid(self)

    def clear(self) -> None:
        """Clear all the waveforms on the screen.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:CLEar

        **Description**

        Clear all the waveforms on the screen.

        **Explanation**

        If the oscilloscope is in RUN state (refer to the :RUN command), new
        waveforms will be displayed.
        You can also use the :CLEar command to clear all the waveforms on the
        screen.
        """
        self.dev.write(":DISPlay:CLEar")

    def get_persistence_time(self) -> float:
        """Set the persistence time and the unit is s.

        :return: The persistence in s, where 0.0 means Minimum and math.inf is
                 infinite.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRADing:TIME <time>
        :DISPlay:GRADing:TIME?

        **Description**

        Set the persistence time and the unit is s.
        Query the current persistence time.

        **Parameter**

        ======= ========= ============================================ =======
        Name    Type      Range                                        Default
        ======= ========= ============================================ =======
        <time>  Discrete  {MIN,0.05,0.1,0.2,0.5,1,2,5,10,20,INFinite}  MIN
        ======= ========= ============================================ =======

        **Explanation**

        **MIN**: set the persistence time to its minimum to view the waveform
        changing in high refresh rate.

        **Specific Values**: a certain value between 0.05 s and 20 s, enable to
        observe glitch that changes relatively slowly or glitch with low
        occurrence probability.

        **INFinite**: in this mode, the oscilloscope displays the newly
        acquired waveform without clearing the waveform formerly acquired.
        Enable to measure noise and jitter as well as capture incidental
        events.

        **Return Format**

        The query returns the persistence time set.

        **Example**

        :DISPlay:GRADing:TIME 0.1
        The query returns 0.1.
        """
        payload: str = self.instrument.ask(":DISPlay:CLEar")

        try:
            return float(payload)
        except ValueError:
            if payload.lower() == "min":
                return -1.0
            elif payload.lower() == "infinite":
                return 0.0
        raise DS2000Error()

    def set_persistence_time(self, time: float = 0.0) -> None:
        """Set the persistence time and the unit is s.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GRADing:TIME <time>
        :DISPlay:GRADing:TIME?

        **Description**

        Set the persistence time and the unit is s.
        Query the current persistence time.

        **Parameter**

        ======= ========= ============================================ =======
        Name    Type      Range                                        Default
        ======= ========= ============================================ =======
        <time>  Discrete  {MIN,0.05,0.1,0.2,0.5,1,2,5,10,20,INFinite}  MIN
        ======= ========= ============================================ =======

        **Explanation**

        MIN: set the persistence time to its minimum to view the waveform
        changing in high refresh rate.
        Specific Values: a certain value between 0.05 s and 20 s, enable to
        observe glitch that changes relatively slowly or glitch with low
        occurrence probability.
        INFinite: in this mode, the oscilloscope displays the newly acquired
        waveform without clearing the waveform formerly acquired. Enable to
        measure noise and jitter as well as capture incidental events.

        **Return Format**

        The query returns the persistence time set.

        **Example**

        :DISPlay:GRADing:TIME 0.1
        The query returns 0.1.
        """
        # Assertion
        if (not isinstance(time, float)) or (
            time not in Display.GRID_GRADING_TIMES
        ):
            ValueError(
                '"time" must be of type "float" '
                f"and in {str(Display.GRID_GRADING_TIMES)}"
            )

        if time == Display.GRID_GRADING_TIMES[1]:
            self.instrument.say(":DISPlay:GRADing:TIME MIN")
        elif time in Display.GRID_GRADING_TIMES[-2:-1]:
            self.instrument.say(":DISPlay:GRADing:TIME INFinite")
        elif time in Display.GRID_GRADING_TIMES:
            self.instrument.say(f":DISPlay:GRADing:TIME {time}")

    def get_waveform_brightness(self) -> int:
        """Query the waveform brightness and the unit is %.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:WBRightness <time>
        :DISPlay:WBRightness?

        **Description**

        Set the waveform brightness and the unit is %.
        Query the current waveform brightness.

        **Parameter**

        ======= ======== ========= =======
        Name    Type     Range     Default
        ======= ======== ========= =======
        <time>  Integer  0 to 100  50
        ======= ======== ========= =======

        **Return Format**

        The query returns an integer between 0 and 100.

        **Example**

        :DISPlay:WBRightness 60
        The query returns 60.
        """
        return int(self.instrument.ask(":DISPlay:WBRightness?"))

    def set_waveform_brightness(self, brightness: int = 50) -> None:
        """Set the waveform brightness and the unit is %.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:WBRightness <time>
        :DISPlay:WBRightness?

        **Description**

        Set the waveform brightness and the unit is %.
        Query the current waveform brightness.

        **Parameter**

        ======= ======== ========= =======
        Name    Type     Range     Default
        ======= ======== ========= =======
        <time>  Integer  0 to 100  50
        ======= ======== ========= =======

        **Return Format**

        The query returns an integer between 0 and 100.

        **Example**

        :DISPlay:WBRightness 60
        The query returns 60.
        """
        check_input(brightness, "brightness", int, 0, 100, "%")
        self.instrument.say(f":DISPlay:WBRightness {brightness}")

    def get_grid_brightness(self) -> int:
        """Query the brightness of the screen grid and the unit is %.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GBRightness <brightness>
        :DISPlay:GBRightness?

        **Description**

        Set the brightness of the screen grid and the unit is %.
        Query the current brightness of the screen grid.

        **Parameter**

        ============= ======== ========= =======
        Name          Type     Range     Default
        ============= ======== ========= =======
        <brightness>  Integer  0 to 100  50
        ============= ======== ========= =======

        **Return Format**

        The query retruns an integer between 0 and 100.

        **Example**

        :DISPlay:GBRightness 60
        The query returns 60.
        """
        return int(self.instrument.ask(":DISPlay:GBRightness?"))

    def set_grid_brightness(self, brightness: int = 50) -> None:
        """Query the brightness of the screen grid and the unit is %.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:GBRightness <brightness>
        :DISPlay:GBRightness?

        **Description**

        Set the brightness of the screen grid and the unit is %.
        Query the current brightness of the screen grid.

        **Parameter**

        ============= ======== ========= =======
        Name          Type     Range     Default
        ============= ======== ========= =======
        <brightness>  Integer  0 to 100  50
        ============= ======== ========= =======

        **Return Format**

        The query retruns an integer between 0 and 100.

        **Example**

        :DISPlay:GBRightness 60
        The query returns 60.
        """
        check_input(brightness, "brightness", int, 0, 100, "%")
        self.instrument.say(f":DISPlay:GBRightness {brightness}")

    def set_menu_display_time(self, time: int = -1) -> None:
        """Query the menu display time and the unit is s.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:MPERsistence <time>
        :DISPlay:MPERsistence?

        **Description**

        Set the menu display time and the unit is s.
        Query the current menu display time.

        **Parameter**

        ======= ========= ======================= ========
        Name    Type      Range                   Default
        ======= ========= ======================= ========
        <time>  Discrete  {1,2,5,10,20,INFinite}  INFinite
        ======= ========= ======================= ========

        **Return Format**

        Query the menu display time set.

        **Example**

        :DISPlay:MPERsistence 20
        The query returns 20.
        """
        # Assertion
        check_input(time, "time", int)

        if time == -1:
            self.instrument.say(":DISPlay:MPERsistence INFinite")
        elif time in Display.MENU_DISPLAY_TIME:
            self.instrument.say(f":DISPlay:GRADing:TIME {time}")

    def data(self) -> bytearray:  # Screenshot bitmap raw data stream
        """Read the bitmap data stream of the image currently displayed.

        **Rigol Programming Guide**

        **Syntax**

        :DISPlay:DATA?

        **Description**

        Read the bitmap data stream of the image currently displayed.

        **Explanation**

        The command is sent from the PC to the instrument through the VISA
        interface. The instrument responds to the command and directly returns
        the bitmap data stream of the image currently displayed to the buffer
        area of the PC.

        **Return Format**

        The format of the bitmap data stream:

        ============== ================================= =================
        Component      TMC Blockheader                   BMP Data
        ============== ================================= =================
        Size (length)  N +2                              800*480*3+54=1152054
        Example        #9001152054                       BM...
        Explanation    |tmc_explanation|                 Specific bitmap
        ============== ================================= =================

        .. |tmc_explanation| replace::
           TMC Blockheader ::= #NXXXXXX is used to describe the length
           of the data stream. Wherein, ``#`` is the start denoter
           of the data stream; N is less than or equal to 9 and the N
           figures following it denotes the length of the data stream
           in bytes.  For example, #9001152054; wherein, N is 9
           and 001152054 denotes that the data stream contains 1152054
           bytes of effective data.

        .. note::
           Size - TMC Blockheader: N is the width used to describe the data
           length in the TMC header. For example, #90000.


        .. note::
           Size - BMP Data: The width is 800, the height is 480, the bit
           depth is 24Bit = 3Byte, 54 is the size of the bitmap file header.


        **Example**

        1. Make sure that the buffer is large enough to receive the data
           stream, otherwise the program might be abnormal when reading the
           data stream.
        2. The returned data stream contains TMC data header and you need to
           remove the data header to make the data stream a standard bitmap
           data stream.
        3. When the data size is larger than 1 M and the communication speed of
           the interface is not fast enough, you need to set an appropriate
           timeout time
        4. The terminator `\\n` (0x0A) at the end of the data should be removed.
        """
        # Write Data
        try:
            self.dev.write(":DISPlay:DATA?")
        except Exception:
            raise DS2000Error("Write Operation was not successful.")

        # Read (RAW) data from the oscilloscope (Head + Bitmap)
        try:
            payload = self.dev.read_raw()
        except Exception:
            raise DS2000Error("Raw read Operation was not successful.")

        # Get and check the payload head len.
        # #NXXXXXX    (format)
        # #9001152054 (example)
        size_len_pos_offset = 2
        size_len_from_payload = int(payload[1])
        if payload[0] != b"#" and size_len_from_payload <= 0:
            raise DS2000Error("Could not identify the incoming data.")

        # Get the bitmap stream size after the head
        try:
            size_len_pos_start: int = size_len_pos_offset
            size_len_pos_stop: int = (
                size_len_from_payload + size_len_pos_offset
            )

            bpm_size = int(payload[size_len_pos_start:size_len_pos_stop])
        except Exception:
            raise DS2000Error(
                "Could not get the bitmap stream size."
                "The datastream was corrupted."
            )

        try:
            stream_start = size_len_pos_stop + 1
            stream_end = stream_start + bpm_size - 1  # -1 is "Line Feed"

            stream = payload[stream_start:stream_end]
        except Exception:
            raise DS2000Error(
                "Could not get the bitmap stream."
                "The datastream was corrupted."
            )

        # Checks, if the header of the bitmap stream is included.
        try:
            if stream[0:1] != b"BM":  # \n
                raise DS2000Error()
        except Exception:
            raise DS2000Error(
                "The start of the datastream could not be "
                "matched. The datastream was corrupted."
            )

        # Checks if the "Line Feed" character at the end of the bitmap sile
        # steram is present, to make sure everything is in the payload
        # and the size was right.
        try:
            if payload[stream_end + 1] != bytearray.fromhex("0x0A"):  # \n
                raise DS2000Error()
        except Exception:
            raise DS2000Error(
                "The end of the datastream could not be "
                "matched. The datastream was corrupted."
            )

        if bpm_size - 1 != len(stream):
            raise DS2000Error(
                "The size from the head does not match "
                "the number of received bytes."
            )

        return stream
