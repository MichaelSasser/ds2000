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
from ds2000.common import channel_as_enum
from ds2000.common import check_level
from ds2000.enums import ChannelEnum
from ds2000.enums import SlopeEnum
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class EdgeSource(SSFunc):
    def set_channel_1(self) -> None:
        """Select the trigger source of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:EDGe:SOURce CHANnel1")

    def set_channel_2(self) -> None:
        """Select the trigger source of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:EDGe:SOURce CHANnel2")

    def set_ext(self) -> None:
        """Select the trigger source of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:EDGe:SOURce EXT")

    def set_ac_line(self) -> None:
        """Select the trigger source of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:EDGe:SOURce ACLine")

    def status(self) -> ChannelEnum:
        """Query the current trigger source of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(self.instrument.ask(":TRIGger:EDGe:SOURce?"))


class EdgeSlope(SSFunc):
    def set_positive(self) -> None:
        """Select the edge type of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SLOPe <slope>
        :TRIGger:EDGe:SLOPe?

        **Description**

        Select the edge type of edge trigger.
        Query the current edge type of edge trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:EDGe:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:EDGe:SLOPe POSitive")

    def set_negative(self) -> None:
        """Select the edge type of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SLOPe <slope>
        :TRIGger:EDGe:SLOPe?

        **Description**

        Select the edge type of edge trigger.
        Query the current edge type of edge trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:EDGe:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:EDGe:SLOPe NEGative")

    def set_both(self) -> None:
        """Select the edge type of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SLOPe <slope>
        :TRIGger:EDGe:SLOPe?

        **Description**

        Select the edge type of edge trigger.
        Query the current edge type of edge trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:EDGe:SLOPe NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:EDGe:SLOPe RFALl")

    def status(self) -> SlopeEnum:
        """Query the current edge type of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SLOPe <slope>
        :TRIGger:EDGe:SLOPe?

        **Description**

        Select the edge type of edge trigger.
        Query the current edge type of edge trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:EDGe:SLOPe NEGative
        The query returns NEG.
        """
        status: str = self.instrument.ask(":TRIGger:EDGe:SLOPe?")
        if status == "POS":
            return SlopeEnum.POSITIVE
        if status == "NEG":
            return SlopeEnum.NEGATIVE
        elif status == "RFAL":
            return SlopeEnum.BOTH
        raise DS2000StateError()


class Edge(SFunc):
    def __init__(self, device):
        super(Edge, self).__init__(device)
        self.source: EdgeSource = EdgeSource(self)
        self.slope: EdgeSlope = EdgeSlope(self)

    def set_level(self, level: float = 0.0) -> None:
        """Set the trigger level of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:LEVel <level>
        :TRIGger:EDGe:LEVel?

        **Description**

        Set the trigger level of edge trigger and the unit is the same with the
        current amplitude unit.
        Query the current trigger level of edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:EDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        # ToDo: What is with ext and acline? Is this the center?
        source: ChannelEnum = self.source.status()
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
        self.instrument.ask(f":TRIGger:EDGe:LEVel {level}")

    def get_level(self) -> float:
        """Query the trigger level of edge trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:LEVel <level>
        :TRIGger:EDGe:LEVel?

        **Description**

        Set the trigger level of edge trigger and the unit is the same with the
        current amplitude unit.
        Query the current trigger level of edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:EDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:EDGe:LEVel?"))
