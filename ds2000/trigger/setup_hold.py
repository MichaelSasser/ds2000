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

from ds2000.common import SFunc
from ds2000.common import SSFunc
from ds2000.common import check_input
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class SetupHoldType(SSFunc):
    def setup(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:TYPe <type>
        :TRIGger:SHOLd:TYPe?

        **Description**

        Set the hold type of setup/hold trigger.
        Query the current hold type of setup/hold trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <type>  Discrete  {SETup|HOLd|SETHOLd}  SETup
        ======= ========= ===================== ========

        **Explanation**

        SETup: set the time (refer to the :TRIGger:SHOLd:STIMe command) that
        the data stays stable and constant before the clock edge appears.

        HOLd: set the time (refer to the :TRIGger:SHOLd:HTIMe command) that
        the data stays stable and constant after the clock edge appears.

        SETHOLd: set the time (refer to the :TRIGger:SHOLd:STIMe and
        :TRIGger:SHOLd:HTIMe commands) that the data stays stable and constant
        before and after the clock edge appears.

        **Return Format**

        The query returns SETup, HOL or SETHOL.

        **Example**

        :TRIGger:SHOLd:TYPe SETHOLd
        The query returns SETHOL.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:TYPe SETup")

    def hold(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:TYPe <type>
        :TRIGger:SHOLd:TYPe?

        **Description**

        Set the hold type of setup/hold trigger.
        Query the current hold type of setup/hold trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <type>  Discrete  {SETup|HOLd|SETHOLd}  SETup
        ======= ========= ===================== ========

        **Explanation**

        SETup: set the time (refer to the :TRIGger:SHOLd:STIMe command) that
        the data stays stable and constant before the clock edge appears.

        HOLd: set the time (refer to the :TRIGger:SHOLd:HTIMe command) that
        the data stays stable and constant after the clock edge appears.

        SETHOLd: set the time (refer to the :TRIGger:SHOLd:STIMe and
        :TRIGger:SHOLd:HTIMe commands) that the data stays stable and constant
        before and after the clock edge appears.

        **Return Format**

        The query returns SETup, HOL or SETHOL.

        **Example**

        :TRIGger:SHOLd:TYPe SETHOLd
        The query returns SETHOL.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:TYPe HOLd")

    def setup_hold(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:TYPe <type>
        :TRIGger:SHOLd:TYPe?

        **Description**

        Set the hold type of setup/hold trigger.
        Query the current hold type of setup/hold trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <type>  Discrete  {SETup|HOLd|SETHOLd}  SETup
        ======= ========= ===================== ========

        **Explanation**

        SETup: set the time (refer to the :TRIGger:SHOLd:STIMe command) that
        the data stays stable and constant before the clock edge appears.

        HOLd: set the time (refer to the :TRIGger:SHOLd:HTIMe command) that
        the data stays stable and constant after the clock edge appears.

        SETHOLd: set the time (refer to the :TRIGger:SHOLd:STIMe and
        :TRIGger:SHOLd:HTIMe commands) that the data stays stable and constant
        before and after the clock edge appears.

        **Return Format**

        The query returns SETup, HOL or SETHOL.

        **Example**

        :TRIGger:SHOLd:TYPe SETHOLd
        The query returns SETHOL.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:TYPe SETHOLd")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:TYPe <type>
        :TRIGger:SHOLd:TYPe?

        **Description**

        Set the hold type of setup/hold trigger.
        Query the current hold type of setup/hold trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <type>  Discrete  {SETup|HOLd|SETHOLd}  SETup
        ======= ========= ===================== ========

        **Explanation**

        SETup: set the time (refer to the :TRIGger:SHOLd:STIMe command) that
        the data stays stable and constant before the clock edge appears.

        HOLd: set the time (refer to the :TRIGger:SHOLd:HTIMe command) that
        the data stays stable and constant after the clock edge appears.

        SETHOLd: set the time (refer to the :TRIGger:SHOLd:STIMe and
        :TRIGger:SHOLd:HTIMe commands) that the data stays stable and constant
        before and after the clock edge appears.

        **Return Format**

        The query returns SETup, HOL or SETHOL.

        **Example**

        :TRIGger:SHOLd:TYPe SETHOLd
        The query returns SETHOL.
        """
        status = self.ssdev.sdev.dev.ask(
            ":TRIGger:SHOLd:TYPe?"
        ).lower()

        if status == "setup":
            return "setup"
        if status == "hold":
            return "hold"
        if status == "sethold":
            return "setup hold"
        raise DS2000StateError()


class SetupHoldDataSource(SSFunc):
    def channel1(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:DSrc <source>
        :TRIGger:SHOLd:DSrc?

        **Description**

        Set the data source of setup/hold trigger.
        Query the current data source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:DSrc CHANnel1
        The query returns CHAN2.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:DSrc CHANel1")

    def channel2(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:DSrc <source>
        :TRIGger:SHOLd:DSrc?

        **Description**

        Set the data source of setup/hold trigger.
        Query the current data source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:DSrc CHANnel1
        The query returns CHAN2.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:DSrc CHANel2")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:DSrc <source>
        :TRIGger:SHOLd:DSrc?

        **Description**

        Set the data source of setup/hold trigger.
        Query the current data source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:DSrc CHANnel1
        The query returns CHAN2.
        """
        status = self.ssdev.sdev.dev.ask(
            ":TRIGger:SHOLd:DSrc?"
        ).lower()

        if status == "chan1":
            return "channel 1"
        if status == "chan2":
            return "channel 2"
        raise DS2000StateError()


class SetupHoldClockSource(SSFunc):
    def channel1(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:CSrc <source>
        :TRIGger:SHOLd:CSrc?

        **Description**

        Set the clock source of setup/hold trigger.
        Query the current clock source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:CSrc CHANnel2
        The query returns CHAN2.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:CSrc CHANel1")

    def channel2(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:CSrc <source>
        :TRIGger:SHOLd:CSrc?

        **Description**

        Set the clock source of setup/hold trigger.
        Query the current clock source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:CSrc CHANnel2
        The query returns CHAN2.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:CSrc CHANel2")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:CSrc <source>
        :TRIGger:SHOLd:CSrc?

        **Description**

        Set the clock source of setup/hold trigger.
        Query the current clock source of setup/hold trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SHOLd:CSrc CHANnel2
        The query returns CHAN2.
        """
        status = self.ssdev.sdev.dev.ask(
            ":TRIGger:SHOLd:CSrc?"
        ).lower()

        if status == "chan1":
            return "channel 1"
        if status == "chan2":
            return "channel 2"
        raise DS2000StateError()


class SetupHoldSlope(SSFunc):
    def rising_edge(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:SLOPe <slope>
        :TRIGger:SHOLd:SLOPe?

        **Description**

        Set the edge type of setup/hold trigger to the rising edge or falling
        edge.
        Query the current edge type of setup/hold trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SHOLd:SLOPe NEGative
        The query returns NEG.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:SLOPe POSitive")

    def falling_edge(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:SLOPe <slope>
        :TRIGger:SHOLd:SLOPe?

        **Description**

        Set the edge type of setup/hold trigger to the rising edge or falling
        edge.
        Query the current edge type of setup/hold trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SHOLd:SLOPe NEGative
        The query returns NEG.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:SLOPe NEGative")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:SLOPe <slope>
        :TRIGger:SHOLd:SLOPe?

        **Description**

        Set the edge type of setup/hold trigger to the rising edge or falling
        edge.
        Query the current edge type of setup/hold trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:SHOLd:SLOPe NEGative
        The query returns NEG.
        """
        status: str = self.ssdev.sdev.dev.ask(
            ":TRIGger:SHOLd:SLOPe?"
        ).lower()
        if status == "POSitive":
            return "rising edge"
        if status == "NEGative":
            return "falling edge"
        raise DS2000StateError()


class SetupHoldPattern(SSFunc):
    def high(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:PATTern <pattern>
        :TRIGger:SHOLd:PATTern?

        **Description**

        Set the data type of setup/hold trigger.
        Query the current data type of setup/hold trigger.

        **Parameter**

        ========== ========= ====== =======
        Name       Type      Range  Default
        ========== ========= ====== =======
        <pattern>  Discrete  {H|L}  H
        ========== ========= ====== =======

        **Return Format**

        The query returns the pattern currently set for each channel.

        **Example**

        :TRIGger:SHOLd:PATTern L
        The query returns L.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:PATTern H")

    def low(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:PATTern <pattern>
        :TRIGger:SHOLd:PATTern?

        **Description**

        Set the data type of setup/hold trigger.
        Query the current data type of setup/hold trigger.

        **Parameter**

        ========== ========= ====== =======
        Name       Type      Range  Default
        ========== ========= ====== =======
        <pattern>  Discrete  {H|L}  H
        ========== ========= ====== =======

        **Return Format**

        The query returns the pattern currently set for each channel.

        **Example**

        :TRIGger:SHOLd:PATTern L
        The query returns L.
        """
        self.ssdev.sdev.dev.ask(":TRIGger:SHOLd:PATTern L")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:PATTern <pattern>
        :TRIGger:SHOLd:PATTern?

        **Description**

        Set the data type of setup/hold trigger.
        Query the current data type of setup/hold trigger.

        **Parameter**

        ========== ========= ====== =======
        Name       Type      Range  Default
        ========== ========= ====== =======
        <pattern>  Discrete  {H|L}  H
        ========== ========= ====== =======

        **Return Format**

        The query returns the pattern currently set for each channel.

        **Example**

        :TRIGger:SHOLd:PATTern L
        The query returns L.
        """
        return self.ssdev.sdev.dev.ask(
            ":TRIGger:SHOLd:PATTern?"
        ).lower()


class SetupHold(SFunc):
    def __init__(self, device):
        super(SetupHold, self).__init__(device)
        self.type: SetupHoldType = SetupHoldType(self)
        self.data_source: SetupHoldDataSource = SetupHoldDataSource(self)
        self.clock_source: SetupHoldClockSource = SetupHoldClockSource(self)
        self.slope: SetupHoldSlope = SetupHoldSlope(self)
        self.pattern: SetupHoldPattern = SetupHoldPattern(self)

    def get_setup_time(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:STIMe <NR3>
        :TRIGger:SHOLd:STIMe?

        **Description**

        Set the setup time of setup/hold trigger.
        Query the current setup time of setup/hold trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 1s  50ns
        ====== ===== ========== =======

        **Explanation**

        This command is available when the hold type (refer to the
        :TRIGger:SHOLd:TYPe command) is set to SETup or SETHOLd.
        Reuturn Format
        The query returns the setup time in scientific notation.

        **Example**

        :TRIGger:SHOLd:STIMe 0.002
        The query returns 2.000000e-03.
        """
        return float(self.sdev.dev.ask(":TRIGger:SHOLd:STIMe?"))

    def set_setup_time(self, time: float = 50.0e-9) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:STIMe <NR3>
        :TRIGger:SHOLd:STIMe?

        **Description**

        Set the setup time of setup/hold trigger.
        Query the current setup time of setup/hold trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 1s  50ns
        ====== ===== ========== =======

        **Explanation**

        This command is available when the hold type (refer to the
        :TRIGger:SHOLd:TYPe command) is set to SETup or SETHOLd.
        Reuturn Format
        The query returns the setup time in scientific notation.

        **Example**

        :TRIGger:SHOLd:STIMe 0.002
        The query returns 2.000000e-03.
        """
        check_input(time, "time", float, 2.0e-9, 1.0, "s")
        self.sdev.dev.ask(f":TRIGger:SHOLd:STIMe {time}")

    def get_hold_time(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:HTIMe <NR3>
        :TRIGger:SHOLd:HTIMe?

        **Description**

        Set the hold time of setup/hold trigger.
        Query the current hold time of setup/hold trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 1s  50ns
        ====== ===== ========== =======

        **Explanation**

        This command is available when the hold type (refer to the
        :TRIGger:SHOLd:TYPe command) is set to HOLd or SETHOLd.
        Reuturn Format
        The query returns the hold time in scientific notation.

        **Example**

        :TRIGger:SHOLd:HTIMe 0.002
        The query returns 2.000000e-03.
        """
        return float(self.sdev.dev.ask(":TRIGger:SHOLd:HTIMe?"))

    def set_hold_time(self, time: float = 50.0e-9) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SHOLd:HTIMe <NR3>
        :TRIGger:SHOLd:HTIMe?

        **Description**

        Set the hold time of setup/hold trigger.
        Query the current hold time of setup/hold trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 1s  50ns
        ====== ===== ========== =======

        **Explanation**

        This command is available when the hold type (refer to the
        :TRIGger:SHOLd:TYPe command) is set to HOLd or SETHOLd.
        Reuturn Format
        The query returns the hold time in scientific notation.

        **Example**

        :TRIGger:SHOLd:HTIMe 0.002
        The query returns 2.000000e-03.
        """
        check_input(time, "time", float, 2.0e-9, 1.0, "s")
        self.sdev.dev.ask(f":TRIGger:SHOLd:HTIMe {time}")
