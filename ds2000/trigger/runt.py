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

from ds2000.common import SFunc, channel_as_enum
from ds2000.common import SSFunc
from ds2000.common import check_input
from ds2000.common import check_level
from ds2000.enums import TriggerRuntWhenEnum, ChannelEnum, \
    TriggerRuntPolarityEnum
from ds2000.errors import DS2000StateError


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class RuntSource(SSFunc):
    def set_channel_1(self) -> None:
        """Select the trigger source of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:SOURce <source>
        :TRIGger:RUNT:SOURce?

        **Description**

        Select the trigger source of runt trigger.
        Query the current trigger source of runt trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RUNT:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:RUNT:SOURce CHANnel1")

    def set_channel_2(self) -> None:
        """Select the trigger source of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:SOURce <source>
        :TRIGger:RUNT:SOURce?

        **Description**

        Select the trigger source of runt trigger.
        Query the current trigger source of runt trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RUNT:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:RUNT:SOURce CHANnel2")

    def status(self) -> ChannelEnum:
        """Query the current trigger source of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:SOURce <source>
        :TRIGger:RUNT:SOURce?

        **Description**

        Select the trigger source of runt trigger.
        Query the current trigger source of runt trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RUNT:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(self.instrument.ask(":TRIGger:RUNT:SOURce?"))


class RuntWhen(SSFunc):
    def set_none(self) -> None:
        """Select the qualifier of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:RUNT:WHEN NONE")

    def set_greater(self) -> None:
        """Select the qualifier of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:RUNT:WHEN GREater")

    def set_less(self) -> None:
        """Select the qualifier of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:RUNT:WHEN LESS")

    def set_between(self) -> None:
        """Select the qualifier of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        self.instrument.ask(":TRIGger:RUNT:WHEN GLESs")

    def status(self) -> TriggerRuntWhenEnum:
        """Query the current qualifier of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        answer: str = self.instrument.ask(":TRIGger:RUNT:WHEN?")
        if answer == "NONE":
            return TriggerRuntWhenEnum.NONE
        if answer == "GRE":
            return TriggerRuntWhenEnum.GREATER
        if answer == "LESS":
            return TriggerRuntWhenEnum.LESS
        if answer == "GLES":
            return TriggerRuntWhenEnum.BETWEEN
        raise DS2000StateError()


class RuntPolarity(SSFunc):
    def set_positive(self) -> None:
        """Select the pulse polarity of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:POLarity <polarity>
        :TRIGger:RUNT:POLarity?

        **Description**

        Select the pulse polarity of runt trigger.
        Query the current pulse polarity of runt trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:RUNT:POLarity NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:RUNT:POLarity POSitive")

    def set_negative(self) -> None:
        """Select the pulse polarity of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:POLarity <polarity>
        :TRIGger:RUNT:POLarity?

        **Description**

        Select the pulse polarity of runt trigger.
        Query the current pulse polarity of runt trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:RUNT:POLarity NEGative
        The query returns NEG.
        """
        self.instrument.ask(":TRIGger:RUNT:POLarity NEGative")

    def status(self) -> TriggerRuntPolarityEnum:
        """Query the current pulse polarity of runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:POLarity <polarity>
        :TRIGger:RUNT:POLarity?

        **Description**

        Select the pulse polarity of runt trigger.
        Query the current pulse polarity of runt trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:RUNT:POLarity NEGative
        The query returns NEG.
        """
        answer = self.instrument.ask(":TRIGger:RUNT:POLarity?")
        if answer == "POS":
            return TriggerRuntPolarityEnum.POSITIVE
        if answer == "NEG":
            return TriggerRuntPolarityEnum.NEGATIVE
        raise DS2000StateError()


class Runt(SFunc):
    def __init__(self, device):
        super(Runt, self).__init__(device)
        self.source: RuntSource = RuntSource(self)
        self.when: RuntWhen = RuntWhen(self)
        self.polarity: RuntPolarity = RuntPolarity(self)

    def set_lower_limit(self, time: float = 1.0e-6) -> None:
        """Set the lower limit of the pulse width in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WLOWer <NR3>
        :TRIGger:RUNT:WLOWer?

        **Description**

        Set the lower limit of the pulse width in runt trigger.
        Query the current lower limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  1μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the lower limit of the
        pulse width is from 2ns to 3.99s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to GREater or GLESs.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WLOWer 0.02
        The query returns 2.000000e-02.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:RUNT:WLOWer {time}")

    def get_lower_limit(self) -> float:
        """Query the current lower limit of the pulse width in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WLOWer <NR3>
        :TRIGger:RUNT:WLOWer?

        **Description**

        Set the lower limit of the pulse width in runt trigger.
        Query the current lower limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  1μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the lower limit of the
        pulse width is from 2ns to 3.99s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to GREater or GLESs.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WLOWer 0.02
        The query returns 2.000000e-02.
        """
        return float(self.instrument.ask(":TRIGger:RUNT:WLOWer?"))

    def set_upper_limit(self, time: float = 2.0e-6) -> None:
        """Set the upper limit of the pulse width in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WUPPer <NR3>
        :TRIGger:RUNT:WUPPer?

        **Description**

        Set the upper limit of the pulse width in runt trigger.
        Query the current upper limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  2μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the upper limit of the
        pulse width is from 10ns to 4s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WUPPer 0.02
        The query returns 2.000000e-02.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.ask(f":TRIGger:RUNT:WUPPer {time}")

    def get_upper_limit(self) -> float:
        """Query the current upper limit of the pulse width in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WUPPer <NR3>
        :TRIGger:RUNT:WUPPer?

        **Description**

        Set the upper limit of the pulse width in runt trigger.
        Query the current upper limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  2μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the upper limit of the
        pulse width is from 10ns to 4s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WUPPer 0.02
        The query returns 2.000000e-02.
        """
        return float(self.instrument.ask(":TRIGger:RUNT:WUPPer?"))

    def set_upper_limit_trigger_level(self, level: float = 0.0) -> None:
        """Set the upper limit of the trigger level in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:ALEVel <level>
        :TRIGger:RUNT:ALEVel?

        **Description**

        Set the upper limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current upper limit of the trigger level in runt trigger.

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

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:ALEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source.status()
        if channel == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:RUNT:ALEVel {level}")

    def get_upper_limit_trigger_level(self) -> float:
        """Query the current upper limit of the trigger level in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:ALEVel <level>
        :TRIGger:RUNT:ALEVel?

        **Description**

        Set the upper limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current upper limit of the trigger level in runt trigger.

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

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:ALEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:RUNT:ALEVel?"))

    def set_lower_limit_trigger_level(self, level: float = 0.0) -> None:
        """Set the lower limit of the trigger level in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:BLEVel <level>
        :TRIGger:RUNT:BLEVel?

        **Description**

        Set the lower limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current lower limit of the trigger level in runt trigger.

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

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source.status()
        if channel == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:RUNT:BLEVel {level}")

    def get_lower_limit_trigger_level(self) -> float:
        """Query the current lower limit of the trigger level in runt trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:BLEVel <level>
        :TRIGger:RUNT:BLEVel?

        **Description**

        Set the lower limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current lower limit of the trigger level in runt trigger.

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

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:RUNT:BLEVel?"))
