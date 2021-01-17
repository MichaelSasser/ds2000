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

__all__ = [
    "Timeout",
]


class TimeoutSlope(SSFunc):
    def rising_edge(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(
            ":TRIGger:TIMeout:SLOPe POSitive"
        )

    def falling_edge(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(
            ":TRIGger:TIMeout:SLOPe NEGative"
        )

    def both_edges(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:TIMeout:SLOPe RFALl")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        status: str = self.instrument.ask(
            ":TRIGger:TIMeout:SLOPe?"
        )
        if status == "POS":
            return "rising edge"
        if status == "NEG":
            return "falling edge"
        if status == "RFAL":
            return "both edges"
        raise DS2000StateError()


class TimeoutChannel(SSFunc):
    def channel1(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SOURce <source>
        :TRIGger:TIMeout:SOURce?

        **Description**

        Select the trigger source of timeout trigger.
        Query the current trigger source of timeout trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:TIMeout:SOURce CHANnel2
        The query returns CHAN2.
        """

        self.instrument.ask(
            ":TRIGger:TIMeout:SOURce CHANnel1"
        )

    def channel2(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SOURce <source>
        :TRIGger:TIMeout:SOURce?

        **Description**

        Select the trigger source of timeout trigger.
        Query the current trigger source of timeout trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:TIMeout:SOURce CHANnel2
        The query returns CHAN2.
        """

        self.instrument.ask(
            ":TRIGger:TIMeout:SOURce CHANnel2"
        )

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SOURce <source>
        :TRIGger:TIMeout:SOURce?

        **Description**

        Select the trigger source of timeout trigger.
        Query the current trigger source of timeout trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:TIMeout:SOURce CHANnel2
        The query returns CHAN2.
        """

        status: str = self.instrument.ask(
            ":TRIGger:TIMeout:SOURce?"
        ).lower()

        if status == "chan1":
            return "channel 1"
        if status == "chan2":
            return "channel 2"
        raise DS2000StateError()


class Timeout(SFunc):
    def __init__(self, device):
        super(Timeout, self).__init__(device)
        self.slope: TimeoutSlope = TimeoutSlope(self)
        self.channel: TimeoutChannel = TimeoutChannel(self)

    def get_time(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:TIMe <NR3>
        :TRIGger:TIMeout:TIMe?

        **Description**

        Set the timeout time of timeout trigger.
        Query the current timeout time of timeout trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:TIMeout:TIMe 0.002
        The query returns 2.000000e+06.
        """
        return float(self.instrument.ask(":TRIGger:TIMeout:TIMe?"))

    def set_time(self, time: float = 1.0e-6) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:TIMe <NR3>
        :TRIGger:TIMeout:TIMe?

        **Description**

        Set the timeout time of timeout trigger.
        Query the current timeout time of timeout trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:TIMeout:TIMe 0.002
        The query returns 2.000000e+06.
        """
        check_input(time, "time", float, 16.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:TIMeout:TIMe {time}")
