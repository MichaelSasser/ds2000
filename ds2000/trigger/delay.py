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
from enum import Enum
from typing import Union

from ds2000.common import SFunc, channel_as_int
from ds2000.common import SSFunc
from ds2000.common import check_input


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

from ds2000.errors import DS2000StateError


class DelayTypeEnum(Enum):
    GREATER = "greater"  # GREater
    LESS = "less"  # LESS
    INSIDE = "inside"  # GLESs
    OUTSIDE = "outside"  # GOUT


class DelaySlopeEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


class DelayType(SSFunc):
    def greater(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        self.instrument.ask(":TRIGger:DELay:TYPe GREater")

    def less(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        self.instrument.ask(":TRIGger:DELay:TYPe LESS")

    def inside(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        self.instrument.ask(":TRIGger:DELay:TYPe GLESs")

    def outside(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        self.instrument.ask(":TRIGger:DELay:TYPe GOUT")

    def status(self) -> DelayTypeEnum:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        ret: str = self.instrument.ask(
            ":TRIGger:DELay:TYPe?"
        )

        if ret == "GRE":
            return DelayTypeEnum.GREATER
        elif ret == "LESS":
            return DelayTypeEnum.LESS
        elif ret == "GLES":
            return DelayTypeEnum.INSIDE
        elif ret == "GOUT":
            return DelayTypeEnum.OUTSIDE
        raise DS2000StateError(f"got {ret}")


class DelaySlope(SSFunc):
    def __init__(self, device, signal_source: str):
        super(DelaySlope, self).__init__(device)
        self.source: str = signal_source

    def set_positive(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**
        :TRIGger:DELay:SLOPA <slope>
        :TRIGger:DELay:SLOPA?

        **Description**

        Set the edge type of edge A of delay trigger.
        Query the current edge type of edge A of delay trigger.

        Set the edge type of edge B of delay trigger.
        Query the current edge type of edge B of delay trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:DELay:SLOPA NEGative
        The query returns NEG.

        :TRIGger:DELay:SLOPB NEGative
        The query returns NEG.
        """

        self.instrument.ask(f":TRIGger:DELay:SLOP{self.source} POSitive")

    def set_negative(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**
        :TRIGger:DELay:SLOPA <slope>
        :TRIGger:DELay:SLOPA?

        :TRIGger:DELay:SLOPB <slope>
        :TRIGger:DELay:SLOPB?

        **Description**

        Set the edge type of edge A of delay trigger.
        Query the current edge type of edge A of delay trigger.

        Set the edge type of edge B of delay trigger.
        Query the current edge type of edge B of delay trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:DELay:SLOPA NEGative
        The query returns NEG.

        :TRIGger:DELay:SLOPB NEGative
        The query returns NEG.
        """

        self.instrument.ask(f":TRIGger:DELay:SLOP{self.source} NEGative")

    def status(self) -> DelaySlopeEnum:
        """

        **Rigol Programming Guide**

        **Syntax**
        :TRIGger:DELay:SLOPA <slope>
        :TRIGger:DELay:SLOPA?

        :TRIGger:DELay:SLOPB <slope>
        :TRIGger:DELay:SLOPB?

        **Description**

        Set the edge type of edge A of delay trigger.
        Query the current edge type of edge A of delay trigger.

        Set the edge type of edge B of delay trigger.
        Query the current edge type of edge B of delay trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:DELay:SLOPA NEGative
        The query returns NEG.

        :TRIGger:DELay:SLOPB NEGative
        The query returns NEG.
        """
        answer: str = self.instrument.ask(f":TRIGger:DELay:SLOP{self.source}?")
        if answer == "POS":
            return DelaySlopeEnum.POSITIVE
        elif answer == "NEG":
            return DelaySlopeEnum.NEGATIVE
        raise DS2000StateError()


class Delay(SFunc):
    def __init__(self, device):
        super(Delay, self).__init__(device)
        self.type: DelayType = DelayType(self)
        self.slope_a: DelaySlope = DelaySlope(self, "A")
        self.slope_b: DelaySlope = DelaySlope(self, "B")

    def set_channel_signal_source_a(self, channel: int) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SA <Source>
        :TRIGger:DELay:SA?

        **Description**

        Select the trigger source of signal source A in delay trigger.
        Query the current trigger source of signal source A in delay trigger.


        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DELay:SA CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.instrument.ask(f":TRIGger:DELay:SA CHANnel{channel}")

    def get_channel_signal_source_a(self) -> int:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SA <Source>
        :TRIGger:DELay:SA?

        **Description**

        Select the trigger source of signal source A in delay trigger.
        Query the current trigger source of signal source A in delay trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DELay:SA CHANnel2
        The query returns CHAN2.
        """
        return channel_as_int(self.instrument.ask(f":TRIGger:DELay:SA?"))

    def set_channel_signal_source_b(self, channel: int) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SB <Source>
        :TRIGger:DELay:SB?

        **Description**

        Select the trigger source of signal source B in delay trigger.
        Query the current trigger source of signal source B in delay trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DELay:SB CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.instrument.ask(f":TRIGger:DELay:SB CHANnel{channel}")

    def get_channel_signal_source_b(self) -> int:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SB <Source>
        :TRIGger:DELay:SB?

        **Description**

        Select the trigger source of signal source A in delay trigger.
        Query the current trigger source of signal source A in delay trigger.

        Select the trigger source of signal source B in delay trigger.
        Query the current trigger source of signal source B in delay trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DELay:SB CHANnel2
        The query returns CHAN2.
        """
        return channel_as_int(self.instrument.ask(f":TRIGger:DELay:SB?"))

    def set_upper_limit(self, time: float = 2.0e-9) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TUPPer <NR3>
        :TRIGger:DELay:TUPPer?

        **Description**

        Set the upper limit of the delay time in delay trigger.
        Query the current upper limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  2μs
        ====== ===== ========== =======

        Note: when the delay type is GLESs or GOUT, the range is
        from 12ns to 4s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the upper limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TUPPer 0.002
        The query returns 2.000000e-03.
        """
        delay_type: DelayTypeEnum = self.type.status()
        if delay_type not in (
            DelayTypeEnum.LESS,
            DelayTypeEnum.OUTSIDE,
            DelayTypeEnum.INSIDE,
        ):
            raise TypeError(
                "To set the upper limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.OUTSIDE.value}, "
                "or "
                f"{DelayTypeEnum.INSIDE.value} "
            )

        if delay_type in (DelayTypeEnum.INSIDE, DelayTypeEnum.OUTSIDE):
            check_input(time, "time", float, 12.0e-9, 4.0, "s")
        else:
            check_input(time, "time", float, 2.0e-9, 4.0, "s")

        self.instrument.ask(f":TRIGger:DELay:TUPPer {time}")

    def get_upper_limit(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TUPPer <NR3>
        :TRIGger:DELay:TUPPer?

        **Description**

        Set the upper limit of the delay time in delay trigger.
        Query the current upper limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  2μs
        ====== ===== ========== =======

        Note: when the delay type is GLESs or GOUT, the range is
        from 12ns to 4s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the upper limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TUPPer 0.002
        The query returns 2.000000e-03.
        """
        delay_type: DelayTypeEnum = self.type.status()
        if delay_type not in (
            DelayTypeEnum.LESS,
            DelayTypeEnum.OUTSIDE,
            DelayTypeEnum.INSIDE,
        ):
            raise TypeError(
                "To get the upper limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.OUTSIDE.value}, "
                "or "
                f"{DelayTypeEnum.INSIDE.value}"
            )

        return float(self.instrument.ask(f":TRIGger:DELay:TUPPer?"))

    def set_lower_limit(self, time: float = 1.0e-6) -> None:
        """
        ToDo: The range in the note is the same as in the table?
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TLOWer <NR3>
        :TRIGger:DELay:TLOWer?

        **Description**

        Set the lower limit of the delay time in delay trigger.
        Query the current lower limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ============= =======
        Name   Type  Range         Default
        ====== ===== ============= =======
        <NR3>  Real  2ns to 3.99s  1μs
        ====== ===== ============= =======

        Note: when the delay type is GLESs or GOUT, the range is from 2ns
        to 3.99s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the lower limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TLOWer 0.002
        The query returns 2.000000e-03.
        """
        delay_type: DelayTypeEnum = self.type.status()
        if delay_type not in (
            DelayTypeEnum.LESS,
            DelayTypeEnum.OUTSIDE,
            DelayTypeEnum.INSIDE,
        ):
            raise TypeError(
                "To set the lower limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.OUTSIDE.value}, "
                "or "
                f"{DelayTypeEnum.INSIDE.value} "
            )

        check_input(time, "time", float, 2.0e-9, 3.99, "s")

        self.instrument.ask(f":TRIGger:DELay:TLOWer {time}")

    def get_lower_limit(self) -> float:
        """
        ToDo: The range in the note is the same as in the table?
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TLOWer <NR3>
        :TRIGger:DELay:TLOWer?

        **Description**

        Set the lower limit of the delay time in delay trigger.
        Query the current lower limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ============= =======
        Name   Type  Range         Default
        ====== ===== ============= =======
        <NR3>  Real  2ns to 3.99s  1μs
        ====== ===== ============= =======

        Note: when the delay type is GLESs or GOUT, the range is from 2ns
        to 3.99s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the lower limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TLOWer 0.002
        The query returns 2.000000e-03.
        """
        delay_type: DelayTypeEnum = self.type.status()
        if delay_type not in (
            DelayTypeEnum.LESS,
            DelayTypeEnum.OUTSIDE,
            DelayTypeEnum.INSIDE,
        ):
            raise TypeError(
                "To set the lower limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.OUTSIDE.value}, "
                "or "
                f"{DelayTypeEnum.INSIDE.value} "
            )

        return float(self.instrument.ask(f":TRIGger:DELay:TLOWer?"))
