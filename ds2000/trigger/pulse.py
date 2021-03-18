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
from ds2000.enums import TriggerPulseWhenEnum

# ToDo: Shorter function names!!!
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class PulseSource(SSFunc):
    def set_channel_1(self) -> None:
        """Select the trigger source in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:SOURce <source>
        :TRIGger:PULSe:SOURce?

        **Description**

        Select the trigger source in pulse trigger.
        Query the current trigger source in pulse trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1,CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:PULSe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.say(":TRIGger:PULSe:SOURce CHANnel1")

    def set_channel_2(self) -> None:
        """Select the trigger source in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:SOURce <source>
        :TRIGger:PULSe:SOURce?

        **Description**

        Select the trigger source in pulse trigger.
        Query the current trigger source in pulse trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1,CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:PULSe:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.say(":TRIGger:PULSe:SOURce CHANnel2")

    def status(self) -> ChannelEnum:
        """Query the current trigger source in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:SOURce <source>
        :TRIGger:PULSe:SOURce?

        **Description**

        Select the trigger source in pulse trigger.
        Query the current trigger source in pulse trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1,CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:PULSe:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(self.instrument.ask(":TRIGger:PULSe:SOURce?"))


class PulseWhen(SSFunc):
    def set_positive_greater(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.say(":TRIGger:PULSe:WHEN GReater")

    def set_positive_less(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """

        self.instrument.say(":TRIGger:PULSe:WHEN PLESs")

    def set_negative_greater(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.say(":TRIGger:PULSe:WHEN NGReater")

    def set_negative_less(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.say(":TRIGger:PULSe:WHEN NLESs")

    def set_positive_between(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.say(":TRIGger:PULSe:WHEN PGLess")

    def set_negative_between(self) -> None:
        """Select the trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        self.instrument.say(":TRIGger:PULSe:WHEN NGLess")

    def status(self) -> TriggerPulseWhenEnum:
        """Query the current trigger condition of pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater,PLESs,NGReater  GReater
                          ,NLESs,PGLess,NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        answer: str = self.instrument.ask(":TRIGger:PULSe:WHEN?")
        if answer == "PGR":
            return TriggerPulseWhenEnum.POSIVE_GREATER
        if answer == "PLES":
            return TriggerPulseWhenEnum.POSITIVE_LESS
        if answer == "NGR":
            return TriggerPulseWhenEnum.NEGATIVE_GREATER
        if answer == "NLES":
            return TriggerPulseWhenEnum.NEGATIVE_LESS
        if answer == "PGL":
            return TriggerPulseWhenEnum.POSITIVE_BETWEEN
        if answer == "NGL":
            return TriggerPulseWhenEnum.NEGATIVE_BETWEEN
        raise DS2000StateError()


class Pulse(SFunc):
    def __init__(self, device):
        super(Pulse, self).__init__(device)
        self.source: PulseSource = PulseSource(self)
        self.when: PulseWhen = PulseWhen(self)

    def set_upper_pulse_width(self, time: float = 2.0e-6) -> None:
        """Set the upper limit of the pulse width in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:UWIDth <width>
        :TRIGger:PULSe:UWIDth?

        **Description**

        Set the upper limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current upper limit of the pulse width in pulse trigger.

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  2μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 10ns to 4s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PLESs, NLESs, PGLess or NGLess.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:UWIDth 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.say(f":TRIGger:PULSe:UWIDth {time}")

    def get_upper_pulse_width(self) -> float:
        """Query the current upper limit of the pulse width in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:UWIDth <width>
        :TRIGger:PULSe:UWIDth?

        **Description**

        Set the upper limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current upper limit of the pulse width in pulse trigger.

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  2μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 10ns to 4s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PLESs, NLESs, PGLess or NGLess.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:UWIDth 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:PULSe:UWIDth?"))

    def set_lower_pulse_width(self, time: float = 1.0e-6) -> None:
        """Set the lower limit of the pulse width in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LWIDth <width>
        :TRIGger:PULSe:LWIDth?

        **Description**

        Set the lower limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current lower limit of the pulse width in pulse trigger

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  1μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 2ns to 3.99s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PGReater, NGReater, PGLess or NGLess.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:LWIDth 0.000003
        The query returns 3.000000e-06.
        """
        check_input(time, "time", float, 2.0e-9, 4.0, "s")
        self.instrument.say(f":TRIGger:PULSe:LWIDth {time}")

    def get_lower_pulse_width(self) -> float:
        """Query the current lower limit of the pulse width in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LWIDth <width>
        :TRIGger:PULSe:LWIDth?

        **Description**

        Set the lower limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current lower limit of the pulse width in pulse trigger

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  1μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 2ns to 3.99s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PGReater, NGReater, PGLess or NGLess.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:LWIDth 0.000003
        The query returns 3.000000e-06.
        """
        return float(self.instrument.ask(":TRIGger:PULSe:LWIDth?"))

    def set_level(self, level: float = 0.0) -> None:
        """Set the trigger level in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LEVel <level>
        :TRIGger:PULSe:LEVel?

        **Description**

        Set the trigger level in pulse trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in pulse trigger.

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

        :TRIGger:PULSe:LEVel 0.16
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
        self.instrument.say(f":TRIGger:PULSe:LEVel {level}")

    def get_level(self) -> float:
        """Query the current trigger level in pulse trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LEVel <level>
        :TRIGger:PULSe:LEVel?

        **Description**

        Set the trigger level in pulse trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in pulse trigger.

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

        :TRIGger:PULSe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:PULSe:LEVel?"))
