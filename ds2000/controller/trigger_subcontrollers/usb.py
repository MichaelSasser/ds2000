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

from ds2000.controller import SubController, SubSubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Usb",
]


class UsbWhen(SubSubController):
    def sop(self):
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
        raise NotImplementedError()
    def eop(self):
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
        raise NotImplementedError()
    def rc(self):
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
        raise NotImplementedError()
    def suspend(self):
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
        raise NotImplementedError()
    def exit_suspend(self):
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
        raise NotImplementedError()


class Usb(SubController):
    def __init__(self, device):
        super(Usb, self).__init__(device)
        self.when: UsbWhen = UsbWhen(self)

    def data_plus_source(self):
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
        raise NotImplementedError()

    def data_minus_source(self):
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
        raise NotImplementedError()

    def speed(self, full: bool = False):
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
        raise NotImplementedError()

    def data_plus_trigger_level(self):
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
        raise NotImplementedError()

    def data_minus_trigger_level(self):
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
        raise NotImplementedError()
