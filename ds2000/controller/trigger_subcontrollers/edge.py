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

from ds2000.controller import SubController, SubSubController, Ds2000StateError

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Edge",
]


class EdgeSource(SubSubController):
    def channel1(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SOURce CHANnel1")

    def channel2(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SOURce CHANnel2")

    def ext(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SOURce EXT")

    def ac_line(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SOURce ACLine")

    def status(self) -> str:
        """
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
        status: str = self.subsubdevice.subdevice.device.ask(
                ":TRIGger:EDGe:SOURce?").lower()
        if status == "chan1":
            return "channel 1"
        if status == "chan2":
            return "channel 2"
        if status == "ext":
            return "ext"
        if status == "acl":
            return "ac line"


class EdgeSlope(SubSubController):
    def rising_edge(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SLOPe POSitive")

    def falling_edge(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SLOPe NEGative")

    def both_edges(self) -> None:
        """
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SLOPe RFALl")

    def status(self) -> str:
        """
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
        status = self.subsubdevice.subdevice.device.ask(":TRIGger:EDGe:SLOPe?")
        if status == "POS":
            return "rising edge"
        if status == "NEG":
            return "falling edge"
        if status == "RFAL":
            return "both edges"


class Edge(SubController):
    def __init__(self, device):
        super(Edge, self).__init__(device)
        self.source: EdgeSource = EdgeSource(self)
        self.slope: EdgeSlope = EdgeSlope(self)

    def get_level(self) -> float:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:EDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.subdevice.device.ask(":TRIGger:EDGe:LEVel?"))

    def set_level(self, level: float = 0.0) -> None:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:EDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        # ToDo: What is with ext and acline? Is this the center?
        scale: float = -1.0
        offset: float = -1.0
        source = self.source.status()
        if source == "channel 1":
            scale = self.subdevice.device.channel1.get_scale()
            offset = self.subdevice.device.channel1.get_offset()
        elif source == "channel 2":
            scale = self.subdevice.device.channel2.scale()
            offset = self.subdevice.device.channel2.get_offset()
        else:
            Ds2000StateError("The level coul'd only be set, if the source is"
                             "Channel 1 or Channel 2.")  # ToDo: Right??

        min_rng = -5 * scale - offset
        max_rng = -5 * scale - offset

        if not isinstance(level, float) or not min_rng <= level <= max_rng:
            ValueError(f"\"level\" must be of type float and between "
                       f"{min_rng}..{max_rng}. You entered type {type(level)}.")

        self.subdevice.device.ask(f":TRIGger:EDGe:LEVel {level}")

