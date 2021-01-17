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
from ds2000.common import check_input
from ds2000.common import check_level


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


# ToDo: shorter method names.
class SlopeWhen(SSFunc):
    def set_positive_slope_time_greater_than_specified_lower_limit(
        self,
    ) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN PGReater")

    def set_positive_slope_time_lower_than_specified_upper_limit(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN PLESs")

    def set_negative_slope_time_greater_than_specified_lower_limit(
        self,
    ) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN NGReater")

    def set_negative_slope_time_lower_than_specified_upper_limit(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN NLESs")

    def set_positive_slope_time_between_specified_lower_and_upper_limit(
        self,
    ) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN PGLess")

    def set_negative_slope_time_between_specified_lower_and_upper_limit(
        self,
    ) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.ask(":TRIGger:SLOPe:WHEN NGLess")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WHEN <when>
        :TRIGger:SLOPe:WHEN?

        **Description**

        Select the trigger condition of slope trigger.
        Query the current trigger condition of slope trigger.

        **Parameter**

        ======= ========= ========================= ========
        Name    Type      Range                     Default
        ======= ========= ========================= ========
        <when>  Discrete  {PGReater|PLESs|NGReater  PGReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= ========

        **Explanation**

        PGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        positive slope time of the input signal is greater than the specified
        time.

        PLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        positive slope time of the input signal is lower than the specified
        time.

        NGReater: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TLOWer command). The oscilloscope triggers when the
        negative slope time of the input signal is greater than the specified
        time.

        NLESs: you need to specify a time value (refer to the
        :TRIGger:SLOPe:TUPPer command). The oscilloscope triggers when the
        negative slope time of the input signal is lower than the specified
        time.

        PGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWer command) of time. The oscilloscope triggers when
        the positive slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        NGLess: you need to specify an upper limit (refer to the
        :TRIGger:SLOPe:TUPPer command) and a lower limit (refer to the
        :TRIGger:SLOPe:TLOWercommand) of time. The oscilloscope triggers when
        the negative slope time of the input signal is greater than the
        specified lower limit and lower than the specified upper limit.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:SLOPe:WHEN PGReater
        The query returns PGR.
        """
        return self.instrument.ask(":TRIGger:SLOPe:WHEN?")


# ToDo: shorter method names.
class SlopeWindow(SSFunc):
    def set_adjust_upper_limit_of_trigger_level(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WINDow <window>
        :TRIGger:SLOPe:WINDow?

        **Description**

        Set the type of the vertical window in slope trigger.
        Query the current type of the vertical window in slope trigger.

        **Parameter**

        ========= ========= ============ =======
        Name      Type      Range        Default
        ========= ========= ============ =======
        <window>  Discrete  {TA|TB|TAB}  TA
        ========= ========= ============ =======

        **Explanation**

        Different vertical windows correspond to different trigger level
        adjustment modes.

        TA: only adjust the upper limit of the trigger level. Refer to the
        :TRIGger:SLOPe:ALEVel command.

        TB: only adjust the lower limit of the trigger level. Refer to the
        :TRIGger:SLOPe:BLEVel command.

        TAB: adjust the upper and lower limits of the trigger level at the
        same time. Refer to the :TRIGger:SLOPe:ALEVel and :TRIGger:SLOPe:BLEVel
        commands.

        **Return Format**

        The query returns TA, TB or TAB.

        **Example**

        :TRIGger:SLOPe:WINDow TB
        The query returns TB.
        """
        self.instrument.ask(":TRIGger:SLOPe:WINDow TA")

    def set_adjust_lower_limit_of_trigger_level(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WINDow <window>
        :TRIGger:SLOPe:WINDow?

        **Description**

        Set the type of the vertical window in slope trigger.
        Query the current type of the vertical window in slope trigger.

        **Parameter**

        ========= ========= ============ =======
        Name      Type      Range        Default
        ========= ========= ============ =======
        <window>  Discrete  {TA|TB|TAB}  TA
        ========= ========= ============ =======

        **Explanation**

        Different vertical windows correspond to different trigger level
        adjustment modes.

        TA: only adjust the upper limit of the trigger level. Refer to the
        :TRIGger:SLOPe:ALEVel command.

        TB: only adjust the lower limit of the trigger level. Refer to the
        :TRIGger:SLOPe:BLEVel command.

        TAB: adjust the upper and lower limits of the trigger level at the
        same time. Refer to the :TRIGger:SLOPe:ALEVel and :TRIGger:SLOPe:BLEVel
        commands.

        **Return Format**

        The query returns TA, TB or TAB.

        **Example**

        :TRIGger:SLOPe:WINDow TB
        The query returns TB.
        """
        self.instrument.ask(":TRIGger:SLOPe:WINDow TB")

    def set_adjust_upper_and_lower_limit_of_trigger_level(self) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WINDow <window>
        :TRIGger:SLOPe:WINDow?

        **Description**

        Set the type of the vertical window in slope trigger.
        Query the current type of the vertical window in slope trigger.

        **Parameter**

        ========= ========= ============ =======
        Name      Type      Range        Default
        ========= ========= ============ =======
        <window>  Discrete  {TA|TB|TAB}  TA
        ========= ========= ============ =======

        **Explanation**

        Different vertical windows correspond to different trigger level
        adjustment modes.

        TA: only adjust the upper limit of the trigger level. Refer to the
        :TRIGger:SLOPe:ALEVel command.

        TB: only adjust the lower limit of the trigger level. Refer to the
        :TRIGger:SLOPe:BLEVel command.

        TAB: adjust the upper and lower limits of the trigger level at the
        same time. Refer to the :TRIGger:SLOPe:ALEVel and :TRIGger:SLOPe:BLEVel
        commands.

        **Return Format**

        The query returns TA, TB or TAB.

        **Example**

        :TRIGger:SLOPe:WINDow TB
        The query returns TB.
        """
        self.instrument.ask(":TRIGger:SLOPe:WINDow TAB")

    def status(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:WINDow <window>
        :TRIGger:SLOPe:WINDow?

        **Description**

        Set the type of the vertical window in slope trigger.
        Query the current type of the vertical window in slope trigger.

        **Parameter**

        ========= ========= ============ =======
        Name      Type      Range        Default
        ========= ========= ============ =======
        <window>  Discrete  {TA|TB|TAB}  TA
        ========= ========= ============ =======

        **Explanation**

        Different vertical windows correspond to different trigger level
        adjustment modes.

        TA: only adjust the upper limit of the trigger level. Refer to the
        :TRIGger:SLOPe:ALEVel command.

        TB: only adjust the lower limit of the trigger level. Refer to the
        :TRIGger:SLOPe:BLEVel command.

        TAB: adjust the upper and lower limits of the trigger level at the
        same time. Refer to the :TRIGger:SLOPe:ALEVel and :TRIGger:SLOPe:BLEVel
        commands.

        **Return Format**

        The query returns TA, TB or TAB.

        **Example**

        :TRIGger:SLOPe:WINDow TB
        The query returns TB.
        """
        return self.instrument.ask(":TRIGger:SLOPe:WINDow?")


class Slope(SFunc):
    def __init__(self, device):
        super(Slope, self).__init__(device)
        self.when: SlopeWhen = SlopeWhen(self)
        self.window: SlopeWindow = SlopeWindow(self)

    def set_source(self, channel: int = 1) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:SOURce <source>
        :TRIGger:SLOPe:SOURce?

        **Description**

        Select the trigger source of slope trigger.
        Query the current trigger source of slope trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SLOPe:SOURce CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.instrument.ask(":TRIGger:SLOPe:SOURce CHANnel{channel}")

    def get_source(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:SOURce <source>
        :TRIGger:SLOPe:SOURce?

        **Description**

        Select the trigger source of slope trigger.
        Query the current trigger source of slope trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:SLOPe:SOURce CHANnel2
        The query returns CHAN2.
        """
        return self.instrument.ask(":TRIGger:SLOPe:SOURce?")

    def set_upper_limit(self, time: float = 2.0e-6) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:TUPPer <time>
        :TRIGger:SLOPe:TUPPer?

        **Description**

        Set the upper limit of time in slope trigger and the unit is s.
        Query the current upper limit of time in slope trigger.

        **Parameter**

        ======= ===== =========== =======
        Name    Type  Range       Default
        ======= ===== =========== =======
        <time>  Real  10ns to 1s  2μs
        ======= ===== =========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 20ns to 1s.

        **Explanation**

        This command is only available when the trigger condition (refer to the
        :TRIGger:SLOPe:WHEN command) is PLESs, NLESs, PGLess or NGLess.

        **Return Format**

        The query returns the upper limit of time in scientific notation.

        **Example**

        :TRIGger:SLOPe:TUPPer 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 10.0e-9, 2.0, "s")
        self.instrument.ask(f":TRIGger:SLOPe:TUPPer {time}")

    def get_upper_limit(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:TUPPer <time>
        :TRIGger:SLOPe:TUPPer?

        **Description**

        Set the upper limit of time in slope trigger and the unit is s.
        Query the current upper limit of time in slope trigger.

        **Parameter**

        ======= ===== =========== =======
        Name    Type  Range       Default
        ======= ===== =========== =======
        <time>  Real  10ns to 1s  2μs
        ======= ===== =========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 20ns to 1s.

        **Explanation**

        This command is only available when the trigger condition (refer to the
        :TRIGger:SLOPe:WHEN command) is PLESs, NLESs, PGLess or NGLess.

        **Return Format**

        The query returns the upper limit of time in scientific notation.

        **Example**

        :TRIGger:SLOPe:TUPPer 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:SLOPe:TUPPer?"))

    def set_lower_limit(self, time: float = 1.0e-6) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:TLOWer <time>
        :TRIGger:SLOPe:TLOWer?

        **Description**

        Set the lower limit of time in slope trigger and the unit is s.
        Query the current lower limit of time in slope trigger.

        **Parameter**

        ======= ===== =========== =======
        Name    Type  Range       Default
        ======= ===== =========== =======
        <time>  Real  10ns to 1s  1μs
        ======= ===== =========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 10ns to 999ms.

        **Explanation**

        This command is only available when the trigger condition (refer to the
        :TRIGger:SLOPe:WHEN command) is PGReater, NGReater, PGLess or NGLess.

        **Return Format**

        The query returns the lower limit of time in scientific notation.

        **Example**

        :TRIGger:SLOPe:TLOWer 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 10.0e-9, 1.0, "s")
        self.instrument.ask(f":TRIGger:SLOPe:TLOWer {time}")

    def get_lower_limit(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:TLOWer <time>
        :TRIGger:SLOPe:TLOWer?

        **Description**

        Set the lower limit of time in slope trigger and the unit is s.
        Query the current lower limit of time in slope trigger.

        **Parameter**

        ======= ===== =========== =======
        Name    Type  Range       Default
        ======= ===== =========== =======
        <time>  Real  10ns to 1s  1μs
        ======= ===== =========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 10ns to 999ms.

        **Explanation**

        This command is only available when the trigger condition (refer to the
        :TRIGger:SLOPe:WHEN command) is PGReater, NGReater, PGLess or NGLess.

        **Return Format**

        The query returns the lower limit of time in scientific notation.

        **Example**

        :TRIGger:SLOPe:TLOWer 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:SLOPe:TLOWer?"))

    def set_upper_limit_trigger_level(self, level: float = 0.0) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:ALEVel <level>
        :TRIGger:SLOPe:ALEVel?

        **Description**

        Set the upper limit of the trigger level in slope trigger and the unit
        is the same with the current amplitude unit.
        Query the current upper limit of the trigger level in slope trigger.

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

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:SLOPe:ALEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_source()
        if channel == "CHANnel1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.instrument.ask(":TRIGger:SLOPe:ALEVel {level}")

    def get_upper_limit_trigger_level(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:ALEVel <level>
        :TRIGger:SLOPe:ALEVel?

        **Description**

        Set the upper limit of the trigger level in slope trigger and the unit
        is the same with the current amplitude unit.
        Query the current upper limit of the trigger level in slope trigger.

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

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:SLOPe:ALEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:SLOPe:ALEVel?"))

    def set_lower_limit_trigger_level(self, level: float = 0.0) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:BLEVel <level>
        :TRIGger:SLOPe:BLEVel?

        **Description**

        Set the lower limit of the trigger level in slope trigger and the unit
        is the same with the current amplitude unit.
        Query the current lower limit of the trigger level in slope trigger.

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

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:SLOPe:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_source()
        if channel == "CHANnel1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:SLOPe:BLEVel {level}")

    def get_lower_limit_trigger_level(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SLOPe:BLEVel <level>
        :TRIGger:SLOPe:BLEVel?

        **Description**

        Set the lower limit of the trigger level in slope trigger and the unit
        is the same with the current amplitude unit.
        Query the current lower limit of the trigger level in slope trigger.

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

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:SLOPe:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:SLOPe:BLEVel?"))
