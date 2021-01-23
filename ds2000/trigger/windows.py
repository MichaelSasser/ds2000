#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020-2021  Michael Sasser <Michael@MichaelSasser.org>

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
from __future__ import annotations

from ds2000.common import SFunc
from ds2000.common import SSFunc
from ds2000.common import check_input


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class WindowsSlope(SSFunc):
    def set_positive(self) -> None:
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
        self.instrument.ask(":TRIGger:WINDows:SLOPe POSitive")

    def set_negative(self) -> None:
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
        self.instrument.ask(":TRIGger:WINDows:SLOPe NEGative")

    def set_rfali(self) -> None:  # ToDo: what is rfali?
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
        self.instrument.ask(":TRIGger:WINDows:SLOPe RFALl")

    def status(self) -> str:
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
        return self.instrument.ask(":TRIGger:WINDows:SLOPe?")


class WindowsPosition(SSFunc):
    def set_exit(self) -> None:
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
        self.instrument.ask(":TRIGger:WINDows:POSition EXIT")

    def set_enter(self) -> None:
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
        self.instrument.ask(":TRIGger:WINDows:POSition ENTER")

    def set_time(self) -> None:
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
        self.instrument.ask(":TRIGger:WINDows:POSition TIMe")

    def status(self) -> str:
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
        return self.instrument.ask(":TRIGger:WINDows:POSition?")


class Windows(SFunc):
    def __init__(self, device):
        super(Windows, self).__init__(device)
        self.slope: WindowsSlope = WindowsSlope(self)
        self.position: WindowsPosition = WindowsPosition(self)

    def set_source(self, channel: int = 1) -> None:
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
        check_input(channel, "channel", 1, 2)
        self.instrument.ask(f":TRIGger:WINDows:SOURce CHANnel{channel}")

    def get_source(self) -> str:
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
        return self.instrument.ask(":TRIGger:WINDows:SOURce?")

    def set_time(self, time: float = 1.0e-6) -> None:
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
        check_input(time, "time", float, 16.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:WINDows:TIMe {time}")

    def get_time(self) -> float:
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
        return float(self.instrument.ask(":TRIGger:WINDows:TIMe?"))
