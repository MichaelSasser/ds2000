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
from ds2000.common import check_level
from ds2000.enums import ChannelEnum
from ds2000.enums import TrigerUSBSpeedEnum
from ds2000.enums import TriggerUSBWhenEnum
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


# TODO: Maybe rename to start, end etc.


class USBSource(SSFunc):
    def __init__(self, device, source: str):
        super(USBSource, self).__init__(device)
        self.src: str = source

    def set_channel_1(self) -> None:
        """Select the channel source in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DPLus <source>
        :TRIGger:USB:DPLus?

        :TRIGger:USB:DMINus <source>
        :TRIGger:USB:DMINus?

        **Description**

        Select the D+ data channel source in USB trigger.
        Query the current D+ data channel source in USB trigger.

        Select the D- data channel source in USB trigger.
        Query the current D- data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1,CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DPLus CHANnel2
        The query returns CHAN2.

        :TRIGger:USB:DMINus CHANnel2
        The query returns CHAN2.
        """
        self.instrument.say(f":TRIGger:USB:{self.src} CHANnel1")

    def status(self) -> ChannelEnum:
        """Select the channel source in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DPLus <source>
        :TRIGger:USB:DPLus?

        :TRIGger:USB:DMINus <source>
        :TRIGger:USB:DMINus?

        **Description**

        Select the D+ data channel source in USB trigger.
        Query the current D+ data channel source in USB trigger.

        Select the D- data channel source in USB trigger.
        Query the current D- data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1,CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DPLus CHANnel2
        The query returns CHAN2.

        :TRIGger:USB:DMINus CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(
            self.instrument.ask(f":TRIGger:USB:{self.src}?")
        )


class USBWhen(SSFunc):
    def set_sop(self) -> None:
        """Set the trigger condition of USB trigger to start of packet.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        self.instrument.say(":TRIGger:USB:WHEN SOP")

    def set_eop(self) -> None:
        """Set the trigger condition of USB trigger to end of packet.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        self.instrument.say(":TRIGger:USB:WHEN EOP")

    def set_rc(self) -> None:
        """Set the trigger condition of USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        self.instrument.say(":TRIGger:USB:WHEN RC")

    def set_suspend(self) -> None:
        """Set the trigger condition of USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        self.instrument.say(":TRIGger:USB:WHEN SUSPend")

    def set_suspend_exit(self) -> None:
        """Set the trigger condition of USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        self.instrument.say(":TRIGger:USB:WHEN EXITsuspend")

    def status(self) -> TriggerUSBWhenEnum:
        """Query the current trigger condition of USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:WHEN <condition>
        :TRIGger:USB:WHEN?

        **Description**

        Set the trigger condition of USB trigger.
        Query the current trigger condition of USB trigger.

        **Parameter**

        ============ ========= ================================= =======
        Name         Type      Range                             Default
        ============ ========= ================================= =======
        <condition>  Discrete  {SOP,EOP,RC,SUSPend,EXITsuspend}  SOP
        ============ ========= ================================= =======

        **Explanation**

        SOP: trigger at the sync bit at the start of the data packet (SOP).

        EOP: trigger at the end of the SEO portion of the EOP of the data
        packet.

        RC: trigger when SEO is greater than 10 ms.

        SUSPend: trigger when the idle time of the bus is greater than 3 ms.

        EXITsuspend: trigger when the bus exits from idle state for more
        than 10 ms.

        **Return Format**

        The query returns SOP, EOP, RC, SUSP or EXIT.

        **Example**

        :TRIGger:USB:WHEN RC
        The query returns RC.
        """
        answer: str = self.instrument.ask(":TRIGger:USB:WHEN?")
        if answer == "SOP":
            return TriggerUSBWhenEnum.SOP
        if answer == "EOP":
            return TriggerUSBWhenEnum.EOP
        if answer == "RC":
            return TriggerUSBWhenEnum.RC
        if answer == "SUSP":
            return TriggerUSBWhenEnum.SUSPEND
        if answer == "EXIT":
            return TriggerUSBWhenEnum.SUSPEND_EXIT
        raise DS2000StateError()


class USBSpeed(SSFunc):
    def set_full(self) -> None:
        """Set the signal speed in USB trigger to Full Speed.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:SPEed <value>
        :TRIGger:USB:SPEed?

        **Description**

        Set the signal speed in USB trigger to Low Speed or Full Speed.
        Query the current signal speed in USB trigger.

        **Parameter**

        ======== ========= =========== ========
        Name     Type      Range       Default
        ======== ========= =========== ========
        <value>  Discrete  {LOW,FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        self.instrument.say(":TRIGger:USB:SPEed FULL")

    def set_low(self) -> None:
        """Set the signal speed in USB trigger to Low Speed.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:SPEed <value>
        :TRIGger:USB:SPEed?

        **Description**

        Set the signal speed in USB trigger to Low Speed or Full Speed.
        Query the current signal speed in USB trigger.

        **Parameter**

        ======== ========= =========== ========
        Name     Type      Range       Default
        ======== ========= =========== ========
        <value>  Discrete  {LOW,FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        self.instrument.say(":TRIGger:USB:SPEed LOW")

    def status(self) -> TrigerUSBSpeedEnum:
        """Query the current signal speed in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:SPEed <value>
        :TRIGger:USB:SPEed?

        **Description**

        Set the signal speed in USB trigger to Low Speed or Full Speed.
        Query the current signal speed in USB trigger.

        **Parameter**

        ======== ========= =========== ========
        Name     Type      Range       Default
        ======== ========= =========== ========
        <value>  Discrete  {LOW,FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        answer: str = self.instrument.ask(":TRIGger:USB:SPEed?")
        if answer == "FULL":
            return TrigerUSBSpeedEnum.FULL
        if answer == "LOW":
            return TrigerUSBSpeedEnum.LOW
        raise DS2000StateError()


class USB(SFunc):
    def __init__(self, device):
        super(USB, self).__init__(device)
        self.source_data_plus: USBSource = USBSource(self, "DPLus")
        self.source_data_minus: USBSource = USBSource(self, "DMINus")
        self.when: USBWhen = USBWhen(self)
        self.speed: USBSpeed = USBSpeed(self)

    def set_data_plus_trigger_level(self, level: float = 0.0) -> None:
        """Set the trigger level of the D+ data line in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:PLEVel <level>
        :TRIGger:USB:PLEVel?

        **Description**

        Set the trigger level of the D+ data line in USB trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of the D+ data line in USB trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5× VerticalScale from     0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:USB:PLEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source_data_plus.status()
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
        self.instrument.say(f":TRIGger:USB:PLEVel {level}")

    def get_data_plus_trigger_level(self) -> float:
        """Query the current trigger level of the D+ data line in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:PLEVel <level>
        :TRIGger:USB:PLEVel?

        **Description**

        Set the trigger level of the D+ data line in USB trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of the D+ data line in USB trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5× VerticalScale from     0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:USB:PLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:USB:PLEVel?"))

    def set_data_minus_trigger_level(self, level: float = 0.0) -> None:
        """Set the trigger level of the D- data line in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:MLEVel <level>
        :TRIGger:USB:MLEVel?

        **Description**

        Set the trigger level of the D- data line in USB trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of the D- data line in USB trigger.

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

        :TRIGger:USB:MLEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source_data_minus.status()
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
        self.instrument.say(f":TRIGger:USB:MLEVel {level}")

    def get_data_minus_trigger_level(self) -> float:
        """Query the current trigger level of the D- data line in USB trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:MLEVel <level>
        :TRIGger:USB:MLEVel?

        **Description**

        Set the trigger level of the D- data line in USB trigger and the unit
        is the same with the current amplitude unit.
        Query the current trigger level of the D- data line in USB trigger.

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

        :TRIGger:USB:MLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:USB:MLEVel?"))
