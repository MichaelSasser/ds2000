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
from enum import Enum
from typing import Union

from ds2000.common import SubController, SubSubController, check_input

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class DelayTypeEnum(Enum):
    GRE = "greater"  # GREater
    LESS = "less"  # LESS
    GLES = "between"  # GLESs
    GOUT = "outside"  # GOUT


class DelayType(SubSubController):
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:DELay:TYPe GREater")

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
        self.subsubdevice.subdevice.device.ask(":TRIGger:DELay:TYPe LESS")

    def between(self) -> None:
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
        self.subsubdevice.subdevice.device.ask(":TRIGger:DELay:TYPe GLESs")

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
        self.subsubdevice.subdevice.device.ask(":TRIGger:DELay:TYPe GOUT")

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
        ret: str = self.subsubdevice.subdevice.device.ask(
            ":TRIGger:DELay:TYPe?"
        )

        if ret == "GRE":
            return DelayTypeEnum.GRE
        elif ret == "LESS":
            return DelayTypeEnum.LESS
        elif ret == "GLES":
            return DelayTypeEnum.GLES
        elif ret == "GOUT":
            return DelayTypeEnum.GOUT


class Delay(SubController):
    def __init__(self, device):
        super(Delay, self).__init__(device)
        self.type: DelayType = DelayType(self)

    def set_signal(
        self, source: Union[str, int], channel: int
    ) -> None:  # SA/SB
        """
        source must be "a", "b", "A", "B" 1 or 2
        channel must be 1 or 2

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SA <Source>
        :TRIGger:DELay:SA?

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

        :TRIGger:DELay:SA CHANnel2
        The query returns CHAN2.

        :TRIGger:DELay:SB CHANnel2
        The query returns CHAN2.
        """
        if isinstance(source, int):
            if source == 1:
                source = "A"
            elif source == 2:
                source = "B"

        self.subdevice.device.ask(f":TRIGger:DELay:S{source} CHANnel{channel}")

    def get_signal(self, source: Union[str, int]) -> int:  # SA/SB
        """
        source must be "a", "b", "A", "B" 1 or 2
        channel must be 1 or 2

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SA <Source>
        :TRIGger:DELay:SA?

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

        :TRIGger:DELay:SA CHANnel2
        The query returns CHAN2.

        :TRIGger:DELay:SB CHANnel2
        The query returns CHAN2.
        """
        return int(self.subdevice.device.ask(f":TRIGger:DELay:S{source}?")[-1])

    def set_slope(self, source, positive: bool = True) -> None:  # SLOPA/SLOPB
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
        if source == 1:
            source = "A"
        elif source == 2:
            source = "B"

        self.subdevice.device.ask(
            f":TRIGger:DELay:SLOP{source} "
            f"{'POSitive' if positive else 'NEGative'}"
        )

    def slope_is_positive(self, source) -> bool:  # SLOPA/SLOPB
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
        if source == 1:
            source = "A"
        elif source == 2:
            source = "B"

        return (
            True
            if self.subdevice.device.ask(f":TRIGger:DELay:SLOP{source}?")
            == "POS"
            else False
        )

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
            DelayTypeEnum.GOUT,
            DelayTypeEnum.GLES,
        ):
            raise TypeError(
                "To set the upper limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.GOUT.value}, "
                "or "
                f"{DelayTypeEnum.GLES.value} "
            )

        if delay_type in (DelayTypeEnum.GLES, DelayTypeEnum.GOUT):
            check_input(time, "time", float, 12.0e-9, 4.0, "s")
        else:
            check_input(time, "time", float, 2.0e-9, 4.0, "s")

        self.subdevice.device.ask(f":TRIGger:DELay:TUPPer {time}")

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
            DelayTypeEnum.GOUT,
            DelayTypeEnum.GLES,
        ):
            raise TypeError(
                "To get the upper limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.GOUT.value}, "
                "or "
                f"{DelayTypeEnum.GLES.value}"
            )

        return float(self.subdevice.device.ask(f":TRIGger:DELay:TUPPer?"))

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
            DelayTypeEnum.GOUT,
            DelayTypeEnum.GLES,
        ):
            raise TypeError(
                "To set the lower limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.GOUT.value}, "
                "or "
                f"{DelayTypeEnum.GLES.value} "
            )

        check_input(time, "time", float, 2.0e-9, 3.99, "s")

        self.subdevice.device.ask(f":TRIGger:DELay:TLOWer {time}")

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
            DelayTypeEnum.GOUT,
            DelayTypeEnum.GLES,
        ):
            raise TypeError(
                "To set the lower limit your delay type has to be: "
                f"{DelayTypeEnum.LESS.value}, "
                f"{DelayTypeEnum.GOUT.value}, "
                "or "
                f"{DelayTypeEnum.GLES.value} "
            )

        return float(self.subdevice.device.ask(f":TRIGger:DELay:TLOWer?"))
