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
from ds2000.common import check_input
from ds2000.common import check_level

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class USBWhen(SSFunc):
    def set_sop(self) -> None:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        self.instrument.ask(":TRIGger:USB:WHEN SOP")

    def set_eop(self) -> None:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        self.instrument.ask(":TRIGger:USB:WHEN EOP")

    def set_rc(self) -> None:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        self.instrument.ask(":TRIGger:USB:WHEN RC")

    def set_suspend(self) -> None:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        self.instrument.ask(":TRIGger:USB:WHEN SUSPend")

    def set_exit_suspend(self) -> None:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        self.instrument.ask(":TRIGger:USB:WHEN EXITsuspend")

    def status(self) -> str:
        """
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
        <condition>  Discrete  {SOP|EOP|RC|SUSPend|EXITsuspend}  SOP
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
        return self.instrument.ask(":TRIGger:USB:WHEN?")


class USB(SFunc):
    def __init__(self, device):
        super(USB, self).__init__(device)
        self.when: USBWhen = USBWhen(self)

    def set_data_plus_source(self, channel: int = 1) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DPLus <source>
        :TRIGger:USB:DPLus?

        **Description**

        Select the D+ data channel source in USB trigger.
        Query the current D+ data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DPLus CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.instrument.ask(f":TRIGger:USB:DPLus CHANnel{channel}")

    def get_data_plus_source(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DPLus <source>
        :TRIGger:USB:DPLus?

        **Description**

        Select the D+ data channel source in USB trigger.
        Query the current D+ data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DPLus CHANnel2
        The query returns CHAN2.
        """
        return self.instrument.ask(":TRIGger:USB:DPLus?")

    def set_data_minus_source(self, channel: int = 2) -> None:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DMINus <source>
        :TRIGger:USB:DMINus?

        **Description**

        Select the D- data channel source in USB trigger.
        Query the current D- data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DMINus CHANnel2
        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.instrument.ask(f":TRIGger:USB:DMINus CHANnel{channel}")

    def get_data_minus_source(self) -> str:
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:USB:DMINus <source>
        :TRIGger:USB:DMINus?

        **Description**

        Select the D- data channel source in USB trigger.
        Query the current D- data channel source in USB trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:USB:DMINus CHANnel2
        The query returns CHAN2.
        """
        return self.instrument.ask(":TRIGger:USB:DMINus?")

    def set_speed_full(self) -> None:
        """
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
        <value>  Discrete  {LOW|FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        self.instrument.ask(":TRIGger:USB:SPEed FULL")

    def set_speed_low(self) -> None:
        """
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
        <value>  Discrete  {LOW|FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        self.instrument.ask(":TRIGger:USB:SPEed LOW")

    def get_speed(self) -> str:
        """
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
        <value>  Discrete  {LOW|FULL}  LOW
        ======== ========= =========== ========

        **Return Format**

        The query returns LOW or FULL.

        **Example**

        :TRIGger:USB:SPEed FULL
        The query returns FULL.
        """
        return self.instrument.ask(":TRIGger:USB:SPEed?")

    def set_data_plus_trigger_level(self, level: float = 0.0) -> None:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:USB:PLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_data_plus_source()
        if channel == "CHANnel1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:USB:PLEVel {level}")

    def get_data_plus_trigger_level(self) -> float:
        """
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

        Note:
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
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:USB:MLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        channel: str = self.get_data_minus_source()
        if channel == "CHANnel1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == "CHANnel2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise RuntimeError("The oscilloscope returned an unknown channel")
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:USB:MLEVel {level}")

    def get_data_minus_trigger_level(self) -> float:
        """
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

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:USB:MLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:USB:MLEVel?"))
