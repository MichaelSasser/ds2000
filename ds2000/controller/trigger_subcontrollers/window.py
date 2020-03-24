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

from ds2000.controller import SubController, SubSubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Window",
]


class WindowSlope(SubSubController):
    def positive(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def negative(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def rfali(self):  # ToDo: what is rfali?
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()


class WindowPosition(SubSubController):
    def exit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()

    def enter(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()


class Window(SubController):
    def __init__(self, device):
        super(Window, self).__init__(device)
        self.slope: WindowSlope = WindowSlope(self)
        self.position: WindowPosition = WindowPosition(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SOURce <source>
        :TRIGger:WINDows:SOURce?

        **Description**

        Select the trigger source of windows trigger.
        Query the current trigger source of windows trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:WINDows:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:TIMe <NR3>
        :TRIGger:RUNT:TIMe?

        **Description**

        Select the windows time of windows trigger.
        Query the current windows time of windows trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Explanation**

        This command is only available when the trigger position of windows
        trigger (refer to the :TRIGger:Windows:POSition command) is set to
        TIMe.

        **Return Format**

        The query returns the windows time in scientific notation.

        **Example**

        :TRIGger:WINDows:TIMe 0.002
        The query returns 2.000000e-03.
        """
        raise NotImplementedError()
