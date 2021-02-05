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

from typing import Tuple
from typing import List
from typing import Union

from ds2000.common import SFunc, channel_as_enum
from ds2000.common import SSFunc
from ds2000.common import check_input
from ds2000.errors import DS2000StateError
from ds2000.enums import TriggerDurationWhenEnum


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class DurationWhen(SSFunc):
    def set_greater(self) -> None:
        """Select the trigger condition of duration trigger.

        The duration of the pattern is greater the lower limit.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:WHEN <when>
        :TRIGger:DURATion:WHEN?

        **Description**

        Select the trigger condition of duration trigger.
        Query the current trigger condition of duration trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <when>  Discrete  {GREater|LESS|GLESs}  PGReater
        ======= ========= ===================== ========

        **Explanation**

        GREater: you need to specify a time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is greater than the preset time.

        LESS: you need to specify a time (refer to the :TRIGger:DURATion:TUPPer
        command). The oscilloscope triggers when the duration of the pattern is
        lower than the preset time.

        GLESs: you need to specify a upper limit of time (refer to the
        :TRIGger:DURATion:TUPPer command) and lower limit of time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is lower than the preset upper limit of time
        and greater than the preset lower limit of time.

        **Return Format**

        The query returns GRE, LESS or GLES.

        **Example**

        :TRIGger:DURATion:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:DURATion:WHEN GREater")

    def set_less(self) -> None:
        """Select the trigger condition of duration trigger.

        The duration of the pattern is lower then the upper limit.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:WHEN <when>
        :TRIGger:DURATion:WHEN?

        **Description**

        Select the trigger condition of duration trigger.
        Query the current trigger condition of duration trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <when>  Discrete  {GREater|LESS|GLESs}  PGReater
        ======= ========= ===================== ========

        **Explanation**

        GREater: you need to specify a time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is greater than the preset time.

        LESS: you need to specify a time (refer to the :TRIGger:DURATion:TUPPer
        command). The oscilloscope triggers when the duration of the pattern is
        lower than the preset time.

        GLESs: you need to specify a upper limit of time (refer to the
        :TRIGger:DURATion:TUPPer command) and lower limit of time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is lower than the preset upper limit of time
        and greater than the preset lower limit of time.

        **Return Format**

        The query returns GRE, LESS or GLES.

        **Example**

        :TRIGger:DURATion:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:DURATion:WHEN LESS")

    def set_between(self) -> None:
        """Select the trigger condition of duration trigger.

        The duration of the pattern is between the lower and the upper limit.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:WHEN <when>
        :TRIGger:DURATion:WHEN?

        **Description**

        Select the trigger condition of duration trigger.
        Query the current trigger condition of duration trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <when>  Discrete  {GREater|LESS|GLESs}  PGReater
        ======= ========= ===================== ========

        **Explanation**

        GREater: you need to specify a time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is greater than the preset time.

        LESS: you need to specify a time (refer to the :TRIGger:DURATion:TUPPer
        command). The oscilloscope triggers when the duration of the pattern is
        lower than the preset time.

        GLESs: you need to specify a upper limit of time (refer to the
        :TRIGger:DURATion:TUPPer command) and lower limit of time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is lower than the preset upper limit of time
        and greater than the preset lower limit of time.

        **Return Format**

        The query returns GRE, LESS or GLES.

        **Example**

        :TRIGger:DURATion:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:DURATion:WHEN GLESs")

    def status(self) -> TriggerDurationWhenEnum:
        """Query the current trigger condition of duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:WHEN <when>
        :TRIGger:DURATion:WHEN?

        **Description**

        Select the trigger condition of duration trigger.
        Query the current trigger condition of duration trigger.

        **Parameter**

        ======= ========= ===================== ========
        Name    Type      Range                 Default
        ======= ========= ===================== ========
        <when>  Discrete  {GREater|LESS|GLESs}  PGReater
        ======= ========= ===================== ========

        **Explanation**

        GREater: you need to specify a time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is greater than the preset time.

        LESS: you need to specify a time (refer to the :TRIGger:DURATion:TUPPer
        command). The oscilloscope triggers when the duration of the pattern is
        lower than the preset time.

        GLESs: you need to specify a upper limit of time (refer to the
        :TRIGger:DURATion:TUPPer command) and lower limit of time (refer to the
        :TRIGger:DURATion:TLOWer command). The oscilloscope triggers when the
        duration of the pattern is lower than the preset upper limit of time
        and greater than the preset lower limit of time.

        **Return Format**

        The query returns GRE, LESS or GLES.

        **Example**

        :TRIGger:DURATion:WHEN LESS
        The query returns LESS.
        """
        answer: str = self.instrument.ask(":TRIGger:DURATion:WHEN?")
        if answer == "GRE":
            return TriggerDurationWhenEnum.GREATER
        if answer == "LESS":
            return TriggerDurationWhenEnum.LESS
        if answer == "GLES":
            return TriggerDurationWhenEnum.BETWEEN
        raise DS2000StateError()


class DurationSource(SSFunc):
    def channel_1(self):
        """Select the trigger source of duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:SOURce <source>
        :TRIGger:DURATion:SOURce?

        **Description**

        Select the trigger source of duration trigger.
        Query the current trigger source of duration trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DURATion:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:DURATion:SOURce CHANnel1")

    def channel_2(self):
        """Select the trigger source of duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:SOURce <source>
        :TRIGger:DURATion:SOURce?

        **Description**

        Select the trigger source of duration trigger.
        Query the current trigger source of duration trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DURATion:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:DURATion:SOURce CHANnel2")

    def status(self):
        """Select the trigger source of duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:SOURce <source>
        :TRIGger:DURATion:SOURce?

        **Description**

        Select the trigger source of duration trigger.
        Query the current trigger source of duration trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DURATion:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(
            self.instrument.ask(":TRIGger:DURATion:SOURce?")
        )

class Duration(SFunc):
    def __init__(self, device):
        super(Duration, self).__init__(device)
        self.when: DurationWhen = DurationWhen(self)

    # TODO
    def set_type(self,
                 pattern: Union[List[str], Tuple[str]] = ("H", "L")
                 ) -> None:
        """Set the current patterns of the channels.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TYPe <type>
        :TRIGger:DURATion:TYPe?

        **Description**

        Set the current patterns of the channels.
        Query the current patterns of the channels.

        **Parameter**

        ======= ========= ======== =======
        Name    Type      Range    Default
        ======= ========= ======== =======
        <type>  Discrete  {H,L,X}  H,L
        ======= ========= ======== =======

        Note: the default patterns of CH1 and CH2 from the left to right.

        **Return Format**

        The query returns the current patterns of the two channels.

        **Example**

        :TRIGger:DURATion:TYPe L,X
        The query returns L,X.
        """
        for p in pattern:
            if p not in ("H", "L", "X", ","):
                raise ValueError("Pattern is not valid.")
        self.instrument.ask(f':TRIGger:DURATion:TYPe {",".join(pattern)}')

    def get_type(self) -> Tuple[str]:
        """Query the current patterns of the channels.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TYPe <type>
        :TRIGger:DURATion:TYPe?

        **Description**

        Set the current patterns of the channels.
        Query the current patterns of the channels.

        **Parameter**

        ======= ========= ======== =======
        Name    Type      Range    Default
        ======= ========= ======== =======
        <type>  Discrete  {H,L,X}  H,L
        ======= ========= ======== =======

        Note: the default patterns of CH1 and CH2 from the left to right.

        **Return Format**

        The query returns the current patterns of the two channels.

        **Example**

        :TRIGger:DURATion:TYPe L,X
        The query returns L,X.
        """
        return tuple(self.instrument.ask(":TRIGger:DURATion:TYPe?").split(","))

    def set_upper_limit(self, time: float = 2.0e-6) -> None:
        """Set the upper limit of the duration.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TUPPer <NR3>
        :TRIGger:DURATion:TUPPer?

        **Description**

        Set the upper limit of the duration in duration trigger and the
        unit is s.
        Query the current upper limit of the duration in duration trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  2μs
        ====== ===== ========== =======

        Note: when the trigger condition is GLESs, the range is
        from 12ns to 4s.

        **Explanation**

        This command is available when the trigger condition
        (refer to the :TRIGger:DURATion:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the duration in scientific
        notation.

        **Example**

        :TRIGger:DURATion:TUPPer 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:DURATion:TUPPer {time}")

    def get_upper_limit(self) -> float:
        """Query the current upper limit of the duration in duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TUPPer <NR3>
        :TRIGger:DURATion:TUPPer?

        **Description**

        Set the upper limit of the duration in duration trigger and the
        unit is s.
        Query the current upper limit of the duration in duration trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  2μs
        ====== ===== ========== =======

        Note: when the trigger condition is GLESs, the range is
        from 12ns to 4s.

        **Explanation**

        This command is available when the trigger condition
        (refer to the :TRIGger:DURATion:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the duration in scientific
        notation.

        **Example**

        :TRIGger:DURATion:TUPPer 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:DURATion:TUPPer?"))

    def set_lower_limit(self, time: float = 1.0e-6) -> None:
        """Set the lower limit of the duration in duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TLOWer <NR3>
        :TRIGger:DURATion:TLOWer?

        **Description**

        Set the lower limit of the duration in duration trigger and the
        unit is s.
        Query the current lower limit of the duration in duration trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  1μs
        ====== ===== ========== =======

        .. note::
           when the trigger condition is GLESs, the range is from 2ns to 3.99s.

        **Explanation**

        This command is available when the trigger condition
        (refer to the :TRIGger:DURATion:WHEN command) is set to GREater or
        GLESs.

        **Return Format**

        The query returns the lower limit of the duration in scientific
        notation.

        **Example**

        :TRIGger:DURATion:TLOWer 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:DURATion:TLOWer {time}")

    def get_lower_limit(self) -> float:
        """Query the current lower limit of the duration in duration trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DURATion:TLOWer <NR3>
        :TRIGger:DURATion:TLOWer?

        **Description**

        Set the lower limit of the duration in duration trigger and the
        unit is s.
        Query the current lower limit of the duration in duration trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  1μs
        ====== ===== ========== =======

        Note: when the trigger condition is GLESs, the range is
        from 2ns to 3.99s.

        **Explanation**

        This command is available when the trigger condition
        (refer to the :TRIGger:DURATion:WHEN command) is set to GREater or
        GLESs.

        **Return Format**

        The query returns the lower limit of the duration in scientific
        notation.

        **Example**

        :TRIGger:DURATion:TLOWer 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:DURATion:TLOWer?"))
