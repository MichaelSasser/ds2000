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
from ds2000.common import channel_as_enum
from ds2000.common import check_input
from ds2000.common import check_level
from ds2000.enums import ChannelEnum
from ds2000.enums import TriggerNthEdgeSlopeEnum
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class NthEdgeSource(SSFunc):
    def set_channel_1(self) -> None:
        """Select the trigger source of Nth egde trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SOURce <source>
        :TRIGger:NEDGe:SOURce?

        **Description**

        Select the trigger source of Nth egde trigger.
        Query the current trigger source of Nth edge trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:NEDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:NEDGe:SOURce CHANnel1")

    def set_channel_2(self) -> None:
        """Select the trigger source of Nth egde trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SOURce <source>
        :TRIGger:NEDGe:SOURce?

        **Description**

        Select the trigger source of Nth egde trigger.
        Query the current trigger source of Nth edge trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:NEDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:NEDGe:SOURce CHANnel2")

    def status(self) -> ChannelEnum:
        """Select the trigger source of Nth egde trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SOURce <source>
        :TRIGger:NEDGe:SOURce?

        **Description**

        Select the trigger source of Nth egde trigger.
        Query the current trigger source of Nth edge trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:NEDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(self.instrument.ask(":TRIGger:NEDGe:SOURce?"))


class NthEdgeSlope(SSFunc):
    def set_positive(self) -> None:
        """Select the edge type of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SLOPe <slope>
        :TRIGger:NEDGe:SLOPe?

        **Description**

        Select the edge type of Nth edge trigger.
        Query the current edge type of Nth edge trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POSitive or NEGative.

        **Example**

        :TRIGger:NEDGe:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:NEDGe:SLOPe POSitive")

    def set_negative(self) -> None:
        """Select the edge type of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SLOPe <slope>
        :TRIGger:NEDGe:SLOPe?

        **Description**

        Select the edge type of Nth edge trigger.
        Query the current edge type of Nth edge trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POSitive or NEGative.

        **Example**

        :TRIGger:NEDGe:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(f":TRIGger:NEDGe:SLOPe NEGative")

    def status(self) -> TriggerNthEdgeSlopeEnum:
        """Query the current edge type of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SLOPe <slope>
        :TRIGger:NEDGe:SLOPe?

        **Description**

        Select the edge type of Nth edge trigger.
        Query the current edge type of Nth edge trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POSitive or NEGative.

        **Example**

        :TRIGger:NEDGe:SLOPe NEGative
        The query returns NEG.
        """
        answer: str = self.instrument.ask(":TRIGger:NEDGe:SLOPe?")
        if answer == "POS":
            return TriggerNthEdgeSlopeEnum.POSITIVE
        if answer == "NEG":
            return TriggerNthEdgeSlopeEnum.NEGATIVE


class NthEdge(SFunc):
    def __init__(self, device):
        super(NthEdge, self).__init__(device)
        self.source: NthEdgeSource = NthEdgeSource(self)
        self.slope: NthEdgeSlope = NthEdgeSlope(self)

    def set_idle(self, time: float = 1.0e-9) -> None:
        """Set the idle time of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:IDLE <NR3>
        :TRIGger:NEDGe:IDLE?

        **Description**

        Set the idle time of Nth edge trigger.
        Query the current idle time of Nth edge trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the idle time value in scientific notation.

        **Example**

        :TRIGger:NEDGe:IDLE 0.002
        The query returns 2.000000e-03.
        """
        check_input(time, "time", float, 16.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:NEDGe:IDLE {time}")

    def get_idle(self) -> float:
        """Query the current idle time of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:IDLE <NR3>
        :TRIGger:NEDGe:IDLE?

        **Description**

        Set the idle time of Nth edge trigger.
        Query the current idle time of Nth edge trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the idle time value in scientific notation.

        **Example**

        :TRIGger:NEDGe:IDLE 0.002
        The query returns 2.000000e-03.
        """
        return float(self.instrument.ask(":TRIGger:NEDGe:IDLE?"))

    def set_edge(self, number: int = 2) -> None:
        """Set the edge number of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:EDGE <NR1>
        :TRIGger:NEDGe:EDGE?

        **Description**

        Set the edge number of Nth edge trigger.
        Query the current edge number of Nth edge trigger.

        **Parameter**

        ====== ======== =========== =======
        Name   Type     Range       Default
        ====== ======== =========== =======
        <NR1>  Integer  1 to 65535  2
        ====== ======== =========== =======

        **Return Format**

        The query returns an integer between 1 and 65535.

        **Example**

        :TRIGger:NEDGe:EDGE
        """
        check_input(number, "number", int, 1, 65535, "")
        self.instrument.ask(f":TRIGger:NEDGe:EDGE {number}")

    def get_edge(self) -> int:
        """Query the current edge number of Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:EDGE <NR1>
        :TRIGger:NEDGe:EDGE?

        **Description**

        Set the edge number of Nth edge trigger.
        Query the current edge number of Nth edge trigger.

        **Parameter**

        ====== ======== =========== =======
        Name   Type     Range       Default
        ====== ======== =========== =======
        <NR1>  Integer  1 to 65535  2
        ====== ======== =========== =======

        **Return Format**

        The query returns an integer between 1 and 65535.

        **Example**

        :TRIGger:NEDGe:EDGE
        """
        return int(self.instrument.ask(":TRIGger:NEDGe:EDGE?"))

    def set_level(self, level: int = 0) -> None:
        """Set the trigger level in Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:LEVel <level>
        :TRIGger:NEDGe:LEVel?

        **Description**

        Set the trigger level in Nth edge trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in Nth edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:NEDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        source = self.source.status()
        if source == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif source == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??

        check_level(level, scale, offset)

        self.instrument.ask(f":TRIGger:NEDGe:LEVel {level}")

    def get_level(self) -> int:
        """Query the current trigger level in Nth edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:LEVel <level>
        :TRIGger:NEDGe:LEVel?

        **Description**

        Set the trigger level in Nth edge trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in Nth edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:NEDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return int(self.instrument.ask(":TRIGger:NEDGe:LEVel?"))
