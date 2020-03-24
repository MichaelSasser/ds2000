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
from typing import Union

from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = [
    "Cursor", "CURSOR_A", "CURSOR_B",
]

CURSOR_A = 1
CURSOR_B = 2

Cursortype = Union[str, int]


def evaluate_cursor(cursor: Cursortype) -> int:
    """
    This function evaluates cursor A and B to a int representation of the
    cursor.
    """
    if isinstance(cursor, int):
        if (cursor >= CURSOR_A) and (cursor <= CURSOR_B):
            return cursor
        raise ValueError("If you use int values for cursor A and B, make sure"
                         f"cursor A := {CURSOR_A} and cursor B := {CURSOR_B}.")
    if isinstance(cursor, str):
        cursor = cursor.lower()
        if cursor == "a":
            return CURSOR_A
        elif cursor == "b":
            return CURSOR_B
        raise ValueError("If you use str values for cursor A and B, make sure"
                         "cursor A := A or a and cursor B := B or b.")
    raise ValueError("You need to use a str or int value for the cursors.\n"
                     f"cursor A := {CURSOR_A} or A or a.\n"
                     f"cursor B := {CURSOR_B} or B or b.\n"
                     "Alternativly there are futureproof variables:\n"
                     "cursor A := CURSOR_A.\n"
                     "cursor B := CURSOR_B.\n")


def is_cursor_a(cursor: Cursortype) -> bool:
    """Is true, if cursor is cursor A"""
    return evaluate_cursor(cursor) == CURSOR_A


def is_cursor_b(cursor: Cursortype) -> bool:
    """Is true, if cursor is cursor B"""
    return evaluate_cursor(cursor) == CURSOR_B


class Mode(SubController):
    def off(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MODE <mode>
        :CURSor:MODE?

        **Description**

        Set the mode of cursor measurement.
        Query the current mode of cursor measurement.

        **Parameter**

        ========== ========== ======================== ========
        Name       Type       Range                    Default
        ========== ========== ======================== ========
        <mode>     Discrete   {OFF|MANual|TRACk|AUTO}  OFF
        ========== ========== ======================== ========

        **Explanation**

        OFF: disable the cursor measurement.
        MANual: enable the manual cursor measurement.
        TRACk: enable the track cursor measurement.
        AUTO: enable the auto cursor measurement.

        **Return Format**

        The query returns OFF, MAN, TRAC or AUTO.

        **Example**

        :CURSor:MODE MANual

        The query returns MAN.
        """
        raise NotImplementedError()

    def manual(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MODE <mode>
        :CURSor:MODE?

        **Description**

        Set the mode of cursor measurement.
        Query the current mode of cursor measurement.

        **Parameter**

        ========== ========== ======================== ========
        Name       Type       Range                    Default
        ========== ========== ======================== ========
        <mode>     Discrete   {OFF|MANual|TRACk|AUTO}  OFF
        ========== ========== ======================== ========

        **Explanation**

        OFF: disable the cursor measurement.
        MANual: enable the manual cursor measurement.
        TRACk: enable the track cursor measurement.
        AUTO: enable the auto cursor measurement.

        **Return Format**

        The query returns OFF, MAN, TRAC or AUTO.

        **Example**

        :CURSor:MODE MANual

        The query returns MAN.
        """
        raise NotImplementedError()

    def track(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MODE <mode>
        :CURSor:MODE?

        **Description**

        Set the mode of cursor measurement.
        Query the current mode of cursor measurement.

        **Parameter**

        ========== ========== ======================== ========
        Name       Type       Range                    Default
        ========== ========== ======================== ========
        <mode>     Discrete   {OFF|MANual|TRACk|AUTO}  OFF
        ========== ========== ======================== ========

        **Explanation**

        OFF: disable the cursor measurement.
        MANual: enable the manual cursor measurement.
        TRACk: enable the track cursor measurement.
        AUTO: enable the auto cursor measurement.

        **Return Format**

        The query returns OFF, MAN, TRAC or AUTO.

        **Example**

        :CURSor:MODE MANual

        The query returns MAN.
        """
        raise NotImplementedError()

    def auto(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MODE <mode>
        :CURSor:MODE?

        **Description**

        Set the mode of cursor measurement.
        Query the current mode of cursor measurement.

        **Parameter**

        ========== ========== ======================== ========
        Name       Type       Range                    Default
        ========== ========== ======================== ========
        <mode>     Discrete   {OFF|MANual|TRACk|AUTO}  OFF
        ========== ========== ======================== ========

        **Explanation**

        OFF: disable the cursor measurement.
        MANual: enable the manual cursor measurement.
        TRACk: enable the track cursor measurement.
        AUTO: enable the auto cursor measurement.

        **Return Format**

        The query returns OFF, MAN, TRAC or AUTO.

        **Example**

        :CURSor:MODE MANual

        The query returns MAN.
        """
        raise NotImplementedError()


class CursorBase(SubController):
    def horizontal_position_cursor_a(self, cursor: Cursortype):  # cax
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:CAX <ax>
        :CURSor:MANual:CAX?

        :CURSor:MANual:CBX <bx>
        :CURSor:MANual:CBX?

        :CURSor:TRACk:CAX <ax>
        :CURSor:TRACk:CAX?

        :CURSor:TRACk:CBX <ax>
        :CURSor:TRACk:CBX?

        **Description**

        Set the horizontal position of cursor A/B in manual cursor measurement.
        Query the current horizontal position of cursor A/B in manual cursor
        measurement.

        **Parameter**

        =========== =========== ============ ========
        Name        Type        Range        Default
        =========== =========== ============ ========
        <ax>        Integer     0 to 699     150
        <bx>        Integer     0 to 699     550
        =========== =========== ============ ========

        **Return Format**

        (CAX) The query returns an integer between 0 and 699.
        (CBX) The query returns an integer between 0 and 699.

        **Example**

        :CURSor:MANual:CAX 200
        The query returns 200.

        :CURSor:MANual:CBX 200
        The query returns 200.

        :CURSor:TRACk:CAX 200
        The query returns 200.

        :CURSor:TRACk:CBX 200
        The query returns 200.
        """
        if is_cursor_a(cursor):
            pass
        elif is_cursor_a(cursor):
            pass
        raise NotImplementedError()

    def vertical_position_cursor(self, cursor: Cursortype = CURSOR_A):  # cay
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:CAY <ay>
        :CURSor:MANual:CAY?

        :CURSor:MANual:CBY <by>
        :CURSor:MANual:CBY?

        :CURSor:TRACk:CAY?  # !!!

        :CURSor:TRACk:CBY?  # !!!

        Description

        Set the vertical position of cursor A in manual cursor measurement.
        Query the current vertical position of cursor A in manual cursor
        measurement.

        Parameter

        Name        Type        Range        Default
        <ay>        Integer     0 to 399     100
        <by>        Integer     0 to 399     300

        Return Format

        The query returns an integer between 0 and 399.

        Example

        :CURSor:MANual:CAY 200
        The query returns 200.

        :CURSor:MANual:CBY 200
        The query returns 200.

        :CURSor:TRACk:CAY?
        The query returns 300.

        :CURSor:TRACk:CBY?
        The query returns 100.
        """
        if is_cursor_a(cursor):
            pass
        elif is_cursor_a(cursor):
            pass
        raise NotImplementedError()

    def x_value(self, cursor: Cursortype = CURSOR_A):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:AXValue?

        :CURSor:MANual:BXValue?

        :CURSor:TRACk:AXValue?

        :CURSor:TRACk:BXValue?

        **Description**

        Query the X value at cursor A in manual cursor measurement.

        Track: Query the X value at cursor A in track cursor measurement
        and the unit is s.

        **Explanation**

        For the horizontal position of cursor A, refer to the
        :CURSor:MANual:CAX command.
        The unit is determined by the horizontal unit currently selected
        (refer to the :CURSor:MANual:TUNit command).

        For the horizontal position of cursor B, refer to the
        :CURSor:MANual:CBX command.
        The unit is determined by the horizontal unit currently selected
        (refer to the :CURSor:MANual:TUNit command).

        **Return Format**

        The query returns the X value at cursor A in scientific notation.
        The query returns the X value at cursor B in scientific notation.

        **Explanation**

        For the horizontal position of cursor A, refer to the :CURSor:TRACk:CAX
        command.

        **Example**

        :CURSor:MANual:AXValue?
        The query returns -4.000000e-06.

        :CURSor:MANual:BXValue?
        The query returns 5.120000e-06.

        :CURSor:TRACk:AXValue?
        The query returns -3.820000e-06.

        :CURSor:TRACk:BXValue?
        The query returns 4.000000e-06.

        """
        if is_cursor_a(cursor):
            pass
        elif is_cursor_a(cursor):
            pass
        raise NotImplementedError()

    def y_value(self, cursor: Cursortype = CURSOR_A):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:AYValue?

        :CURSor:MANual:BYValue?

        :CURSor:TRACk:AYValue?

        :CURSor:TRACk:BYValue?

        **Description**

        Query the Y value at cursor A/B in manual cursor measurement.

        **Explanation**

        Manual:
        For the vertical position of cursor A, refer to the :CURSor:MANual:CAY
        command.
        For the vertical position of cursor B, refer to the :CURSor:MANual:CBY
        command.

        The unit is determined by the vertical unit currently selected
        (refer to the :CURSor:MANual:VUNit command).

        Track:
        For the vertical position of cursor A, refer to the :CURSor:TRACk:CAY?
        command.
        The unit is determined by the unit (refer to the
        :CHANnel<n>:UNITs command) selected by the signal source (refer to
         the :CURSor:TRACk:SOURce1 command) of cursor A.

        **Return Format**

        The query returns the Y value at cursor A/B in scientific notation.

        **Example**

        :CURSor:MANual:AYValue?
        The query returns 3.400000e-01.

        :CURSor:MANual:BYValue?
        The query returns -4.360000e+00.

        :CURSor:TRACk:AYValue?
        The query returns 4.000000e-02.

        :CURSor:TRACk:BYValue?
        The query returns -4.360000e+00.
        """
        if is_cursor_a(cursor):
            pass
        elif is_cursor_a(cursor):
            pass
        raise NotImplementedError()

    def delta_x_ab(self, reciprocal: bool = False):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:XDELta?

        :CURSor:MANual:IXDelta?

        :CURSor:TRACk:XDELta?

        :CURSor:TRACk:IXDelta?

        **Description**

        * Query the difference △X between the X values at cursor A and cursor B
          in manual cursor measurement.

        * Query the reciprocal (1/△X) of the difference between the X values
          at cursor A and cursor B in manual cursor measurement.

        **Explanation**

        Manual:

        For the horizontal position of cursor A, refer to
        the :CURSor:MANual:CAX command.
        For the horizontal position of cursor B, refer to
        the :CURSor:MANual:CBX command.
        The unit is determined by the horizontal unit currently
        selected (refer to the :CURSor:MANual:TUNit command).

        Track:

        For the horizontal position of cursor A, refer to the :CURSor:TRACk:CAX
        command.
        For the horizontal position of cursor B, refer to the :CURSor:TRACk:CBX
        command.

        **Return Format**

        * The query returns the current difference △X in scientific notation.

        * The query returns the 1/△X value in scientific notation.

        **Example**

        :CURSor:MANual:XDELta?
        The query returns 9.120000e-06.

        :CURSor:MANual:IXDelta?
        The query returns 1.096491e+05.

        :CURSor:TRACk:XDELta?
        The query returns 7.820000e-06.

        :CURSor:TRACk:IXDelta?
        The query returns 1.278772e+05.

        """
        raise NotImplementedError()

    def delta_y_ab(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:YDELta?

        :CURSor:TRACk:YDELta?

        **Description**

        Query the difference △Y between the Y values at cursor A and cursor B
        in manual cursor measurement.

        **Explanation**

        Manual:

        For the vertical position of cursor A, refer to the :CURSor:MANual:CAY
        command.
        For the vertical position of cursor B, refer to the :CURSor:MANual:CBY
        command.
        The unit is determined by the vertical unit currently selected (refer
        to the :CURSor:MANual:VUNit command).

        Track:
        For the vertical position of cursor A, refer to the :CURSor:TRACk:CAY?
        command.
        For the vertical position of cursor B, refer to the :CURSor:TRACk:CBY?
        command.
        The unit is determined by the unit (refer to the :CHANnel<n>:UNITs
        command) of the current signal source.

        **Return Format**

        The query returns the current difference △Y in scientific notation.

        **Example**

        :CURSor:MANual:YDELta?
        The query returns -4.700000e+00.

        :CURSor:TRACk:YDELta?
        The query returns -4.000000e-02.
        """
        raise NotImplementedError()


class Manual(CursorBase):
    def type(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:TYPE <type>
        :CURSor:MANual:TYPE?

        **Description**

        Select the cursor type of manual cursor measurement.
        Query the current cursor type of manual cursor measurement.

        **Parameter**

        ======= ========= ================= ========
        Name    Type      Range             Default
        ======= ========= ================= ========
        <type>  Discrete  {TIME|AMPLitude}  TIME
        ======= ========= ================= ========

        **Explanation**

        TIME: select X cursors which are usually used to measure time
        parameters.
        AMPLitude: select Y cursors which are usually used to measure voltage
        parameters.

        **Return Format**

        The query returns TIME or AMPL.

        **Example**

        :CURSor:MANual:TYPE AMPLitude

        The query returns AMPL.
        """
        raise NotImplementedError()

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:SOURce <source>
        :CURSor:MANual:SOURce?

        **Description**

        Set the channel source of manual cursor measurement.
        Query the current channel source of manual cursor measurement.

        **Parameter**

        ========= ========= ============================== ========
        Name      Type      Range                          Default
        ========= ========= ============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|MATH|NONE}  CHANnel1
        ========= ========= ============================== ========

        Note: only channels currently enabled can be selected as the channel
        source.

        **Explanation**

        CHANnel1, CHANnel2: select CH1 or CH2 as the measurement source of
        cursor A.

        MATH: select the waveform of the math operation channel as the
        measurement source of cursor A.
        NONE: do not use cursor A.

        **Return Format**

        The query returns CHAN1, CHAN2, MATH or NONE.

        **Example**
        :CURSor:MANual:SOURce CHANnel2

        The query returns CHAN2.

        """
        raise NotImplementedError()

    def horizontal_unit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:TUNit <unit>
        :CURSor:MANual:TUNit?

        **Description**

        Set the horizontal unit in manual cursor measurement.
        Query the current horizontal unit in manual cursor measurement.

        **Parameter**

        ======= ========= ============================== ========
        Name    Type      Range                          Default
        ======= ========= ============================== ========
        <unit>  Discrete  {SECond|HZ|PERCentage|DEGRee}  SECond
        ======= ========= ============================== ========

        **Explanation**

        SECond: when this unit is selected, in the measurement results, CurA,
        CurB and △X are in s and 1/△X is in Hz.
        HZ: when this unit is selected, in the measurement results, CurA, CurB
        and △X are in Hz and 1/△X is in s.
        PERCentage: when this unit is selected, in the measurement results,
        CurA, CurB and △X are in %.
        DEGRee: when this unit is selected, in the measurement results, CurA,
        CurB and △X are in °.

        **Return Format**

        The query returns SEC, HZ, PERC or DEGR.

        **Example**

        :CURSor:MANual:TUNit DEGRee

        The query returns DEGR.
        """
        raise NotImplementedError()

    def vertical_unit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:MANual:VUNit <unit>
        :CURSor:MANual:VUNit?

        **Description**

        Set the vertical unit in manual cursor measurement.
        Query the current vertical unit in manual cursor measurement.

        **Parameter**

        ======= ======== ================= ========
        Name    Type      Range            Default
        ======= ======== ================= ========
        <unit>  Discrete  {SUNit|PERCent}  SUNit
        ======= ======== ================= ========

        **Explanation**

        SUNit: when this unit is selected, in the measurement results, the
        units of CurA, CurB and △Y will automatically be set to the unit of
        the current signal source.
        PERCent: when this unit is selected, in the measurement results, CurA,
        CurB and △Y are in %.

        **Return Format**

        The query returns SUN or PERC.

        **Example**

        :CURSor:MANual:VUNit PERCent

        The query returns PERC.

        """
        raise NotImplementedError()


class Track(CursorBase):
    def source(self, src: int = 1):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CURSor:TRACk:SOURce1 <source>
        :CURSor:TRACk:SOURce1?

        :CURSor:TRACk:SOURce2 <source>
        :CURSor:TRACk:SOURce2?

        **Description**

        Set the channel source of manual cursor measurement.
        Query the current channel source of manual cursor measurement.

        **Parameter**

        ========= ========= ============================== ========
        Name      Type      Range                          Default
        ========= ========= ============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|MATH|NONE}  CHANnel1
        ========= ========= ============================== ========

        Note: only channels currently enabled can be selected as the channel
        source.

        **Explanation**

        CHANnel1, CHANnel2: select CH1 or CH2 as the measurement source of
        cursor A.

        MATH: select the waveform of the math operation channel as the
        measurement source of cursor A.
        NONE: do not use cursor A.

        **Return Format**

        The query returns CHAN1, CHAN2, MATH or NONE.

        **Example**

        :CURSor:TRACk:SOURce1 CHANnel2

        The query returns CHAN2.

        :CURSor:TRACk:SOURce2 CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()


class Cursor(BaseController):
    def __init__(self, device):
        super(Cursor, self).__init__(device)
        self.mode: Mode = Mode(self)
        self.manual: Manual = Manual(self)
        self.track: Track = Track(self)
