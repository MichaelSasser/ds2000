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

from typing import List
from typing import Tuple
from typing import Union

from ds2000.common import SFunc
from ds2000.common import check_level


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Pattern(SFunc):
    def set_pattern(
        self, pattern: Union[List[str], Tuple[str, ...]] = ("H", "L")
    ) -> None:
        """Set the pattern code of each channel in pattern trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PATTern:PATTern <pattern>
        :TRIGger:PATTern:PATTern?

        **Description**

        Set the pattern code of each channel in pattern trigger.
        Query the current pattern code of each channel in pattern trigger.

        **Parameter**

        ========== ========= ============ =======
        Name       Type      Range        Default
        ========== ========= ============ =======
        <pattern>  Discrete  {H,L,X,R,F}  H,L
        ========== ========= ============ =======

        Note: they are the default pattern codes for CH1 and CH2 from the left
        to the right.

        **Explanation**

        In the pattern, you can only specify one rising edge or falling edge.
        If one edge item is currently defined and then another edge item is
        defined in the other channel in the pattern, the former edge item
        defined will be replaced by X.

        **Return Format**

        The query returns the current pattern codes of both the channels.

        **Example**

        :TRIGger:PATTern:PATTern H,R
        The query returns H,R.
        """
        # TODO validate pattern
        pattern = [b.upper() for b in pattern]
        for b in pattern:
            if b not in ("H", "L", "X", "R", "F"):
                raise ValueError(
                    'The pattern must only contain "H", "L", "X", "R" or "F".'
                )
        self.instrument.say(f":TRIGger:PATTern:PATTern {','.join(pattern)}")

    def get_pattern(self) -> Tuple[str, ...]:
        """Query the current pattern code of each channel in pattern trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PATTern:PATTern <pattern>
        :TRIGger:PATTern:PATTern?

        **Description**

        Set the pattern code of each channel in pattern trigger.
        Query the current pattern code of each channel in pattern trigger.

        **Parameter**

        ========== ========= ============ =======
        Name       Type      Range        Default
        ========== ========= ============ =======
        <pattern>  Discrete  {H,L,X,R,F}  H,L
        ========== ========= ============ =======

        Note: they are the default pattern codes for CH1 and CH2 from the left
        to the right.

        **Explanation**

        In the pattern, you can only specify one rising edge or falling edge.
        If one edge item is currently defined and then another edge item is
        defined in the other channel in the pattern, the former edge item
        defined will be replaced by X.

        **Return Format**

        The query returns the current pattern codes of both the channels.

        **Example**

        :TRIGger:PATTern:PATTern H,R
        The query returns H,R.
        """
        return tuple(
            self.instrument.ask(":TRIGger:PATTern:PATTern?").split(",")
        )

    def set_level(self, channel: int = 1, level: float = 0) -> None:
        """Set the trigger level of each channel in pattern trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PATTern:LEVel <chan>,<level>
        :TRIGger:PATTern:LEVel? <chan>

        **Description**

        Set the trigger level of each channel in pattern trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of each channel in pattern trigger.

        **Parameter**

        ======== ========= ========================= ========
        Name     Type      Range                     Default
        ======== ========= ========================= ========
        <chan>   Discrete  {CHANnel1,CHANnel2}       CHANnel1
        <level>  Real      ± 5 × VerticalScale from  0
                           the screen - OFFSet
        ======== ========= ========================= ========

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:PATTern:LEVel CHANnel2,0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        if channel == 1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == 2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.instrument.say(f":TRIGger:PATTern:LEVel CHANnel{channel},{level}")

    def get_level(self, channel: int = 1) -> float:
        """Query the current trigger level of each channel in pattern trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PATTern:LEVel <chan>,<level>
        :TRIGger:PATTern:LEVel? <chan>

        **Description**

        Set the trigger level of each channel in pattern trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of each channel in pattern trigger.

        **Parameter**

        ======== ========= ========================= ========
        Name     Type      Range                     Default
        ======== ========= ========================= ========
        <chan>   Discrete  {CHANnel1,CHANnel2}       CHANnel1
        <level>  Real      ± 5 × VerticalScale from  0
                           the screen - OFFSet
        ======== ========= ========================= ========

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:PATTern:LEVel CHANnel2,0.16
        The query returns 1.600000e-01.
        """
        return float(
            self.instrument.ask(f":TRIGger:PATTern:LEVel? CHANnel{channel}")
        )
