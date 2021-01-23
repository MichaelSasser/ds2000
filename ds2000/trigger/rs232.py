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

from typing import Dict

from ds2000.common import SFunc
from ds2000.common import SSFunc
from ds2000.common import check_input
from ds2000.common import check_level


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class RS232When(SSFunc):
    def set_start_frame_position(self) -> None:
        """Set the trigger condition of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WHEN <when>
        :TRIGger:RS232:WHEN?

        **Description**

        Set the trigger condition of RS232 trigger to Start, Error, Check
        Error or Data.
        Query the current trigger condition of RS232 trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {STARt|ERRor|PARity|DATA}  STARt
        ======= ========= ========================== =======

        **Explanation**

        STARt: trigger on the start frame position.

        ERRor: trigger when error frame is detected.

        PARity: trigger when check error is detected.

        DATA: trigger on the last bit of the preset data bits and even-odd
        check bits.

        **Return Format**

        The query returns STAR, ERR, PAR or DATA.

        **Example**

        :TRIGger:RS232:WHEN ERRor
        The query returns ERR.
        """
        self.instrument.ask(":TRIGger:RS232:WHEN STARt")

    def set_error_detected(self) -> None:
        """Set the trigger condition of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WHEN <when>
        :TRIGger:RS232:WHEN?

        **Description**

        Set the trigger condition of RS232 trigger to Start, Error, Check
        Error or Data.
        Query the current trigger condition of RS232 trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {STARt|ERRor|PARity|DATA}  STARt
        ======= ========= ========================== =======

        **Explanation**

        STARt: trigger on the start frame position.

        ERRor: trigger when error frame is detected.

        PARity: trigger when check error is detected.

        DATA: trigger on the last bit of the preset data bits and even-odd
        check bits.

        **Return Format**

        The query returns STAR, ERR, PAR or DATA.

        **Example**

        :TRIGger:RS232:WHEN ERRor
        The query returns ERR.
        """
        self.instrument.ask(":TRIGger:RS232:WHEN ERRor")

    def set_parity_error_detected(self) -> None:
        """Set the trigger condition of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WHEN <when>
        :TRIGger:RS232:WHEN?

        **Description**

        Set the trigger condition of RS232 trigger to Start, Error, Check
        Error or Data.
        Query the current trigger condition of RS232 trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {STARt|ERRor|PARity|DATA}  STARt
        ======= ========= ========================== =======

        **Explanation**

        STARt: trigger on the start frame position.

        ERRor: trigger when error frame is detected.

        PARity: trigger when check error is detected.

        DATA: trigger on the last bit of the preset data bits and even-odd
        check bits.

        **Return Format**

        The query returns STAR, ERR, PAR or DATA.

        **Example**

        :TRIGger:RS232:WHEN ERRor
        The query returns ERR.
        """
        self.instrument.ask(":TRIGger:RS232:WHEN PARity")

    def set_data(self) -> None:
        """Set the trigger condition of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WHEN <when>
        :TRIGger:RS232:WHEN?

        **Description**

        Set the trigger condition of RS232 trigger to Start, Error, Check
        Error or Data.
        Query the current trigger condition of RS232 trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {STARt|ERRor|PARity|DATA}  STARt
        ======= ========= ========================== =======

        **Explanation**

        STARt: trigger on the start frame position.

        ERRor: trigger when error frame is detected.

        PARity: trigger when check error is detected.

        DATA: trigger on the last bit of the preset data bits and even-odd
        check bits.

        **Return Format**

        The query returns STAR, ERR, PAR or DATA.

        **Example**

        :TRIGger:RS232:WHEN ERRor
        The query returns ERR.
        """
        self.instrument.ask(":TRIGger:RS232:WHEN DATA")

    def status(self) -> str:
        """Query the current trigger condition of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WHEN <when>
        :TRIGger:RS232:WHEN?

        **Description**

        Set the trigger condition of RS232 trigger to Start, Error, Check
        Error or Data.
        Query the current trigger condition of RS232 trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {STARt|ERRor|PARity|DATA}  STARt
        ======= ========= ========================== =======

        **Explanation**

        STARt: trigger on the start frame position.

        ERRor: trigger when error frame is detected.

        PARity: trigger when check error is detected.

        DATA: trigger on the last bit of the preset data bits and even-odd
        check bits.

        **Return Format**

        The query returns STAR, ERR, PAR or DATA.

        **Example**

        :TRIGger:RS232:WHEN ERRor
        The query returns ERR.
        """
        return self.instrument.ask(":TRIGger:RS232:WHEN?")


class RS232Parity(SSFunc):
    def set_even(self) -> None:
        """Set the even-odd check mode in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:PARity <parity>
        :TRIGger:RS232:PARity?

        **Description**

        Set the even-odd check mode in RS232 trigger when the trigger condition
        is Error or Check Error.
        Query the current even-odd check mode in RS232 trigger when the trigger
        condition is Error or Check Error.

        **Parameter**

        ========= ========= =============== ========
        Name      Type      Range            Default
        ========= ========= =============== ========
        <parity>  Discrete  {EVEN|ODD|NONE}  NONE
        ========= ========= =============== ========

        Note: the even-odd check mode can not be set to NONE when the trigger
        condition is Check Error.

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns EVEN, ODD or NONE.

        **Example**

        :TRIGger:RS232:PARity EVEN
        The query returns EVEN.
        """
        self.instrument.ask(":TRIGger:RS232:PARity EVEN")

    def set_odd(self) -> None:
        """Set the even-odd check mode in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:PARity <parity>
        :TRIGger:RS232:PARity?

        **Description**

        Set the even-odd check mode in RS232 trigger when the trigger condition
        is Error or Check Error.
        Query the current even-odd check mode in RS232 trigger when the trigger
        condition is Error or Check Error.

        **Parameter**

        ========= ========= =============== ========
        Name      Type      Range            Default
        ========= ========= =============== ========
        <parity>  Discrete  {EVEN|ODD|NONE}  NONE
        ========= ========= =============== ========

        Note: the even-odd check mode can not be set to NONE when the trigger
        condition is Check Error.

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns EVEN, ODD or NONE.

        **Example**

        :TRIGger:RS232:PARity EVEN
        The query returns EVEN.
        """
        self.instrument.ask(":TRIGger:RS232:PARity ODD")

    def set_none(self) -> None:
        """Set the even-odd check mode in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:PARity <parity>
        :TRIGger:RS232:PARity?

        **Description**

        Set the even-odd check mode in RS232 trigger when the trigger condition
        is Error or Check Error.
        Query the current even-odd check mode in RS232 trigger when the trigger
        condition is Error or Check Error.

        **Parameter**

        ========= ========= =============== ========
        Name      Type      Range            Default
        ========= ========= =============== ========
        <parity>  Discrete  {EVEN|ODD|NONE}  NONE
        ========= ========= =============== ========

        Note: the even-odd check mode can not be set to NONE when the trigger
        condition is Check Error.

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns EVEN, ODD or NONE.

        **Example**

        :TRIGger:RS232:PARity EVEN
        The query returns EVEN.
        """
        self.instrument.ask(":TRIGger:RS232:PARity NONE")

    def status(self) -> str:
        """Query the current even-odd check mode in RS232 trigger.
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:PARity <parity>
        :TRIGger:RS232:PARity?

        **Description**

        Set the even-odd check mode in RS232 trigger when the trigger condition
        is Error or Check Error.
        Query the current even-odd check mode in RS232 trigger when the trigger
        condition is Error or Check Error.

        **Parameter**

        ========= ========= =============== ========
        Name      Type      Range            Default
        ========= ========= =============== ========
        <parity>  Discrete  {EVEN|ODD|NONE}  NONE
        ========= ========= =============== ========

        Note: the even-odd check mode can not be set to NONE when the trigger
        condition is Check Error.

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns EVEN, ODD or NONE.

        **Example**

        :TRIGger:RS232:PARity EVEN
        The query returns EVEN.
        """
        return self.instrument.ask(":TRIGger:RS232:PARity?")


# TODO: Check selected trigger before settitng values
class RS232(SFunc):
    def __init__(self, device) -> None:
        super(RS232, self).__init__(device)
        self.when: RS232When = RS232When(self)
        self.parity: RS232Parity = RS232Parity(self)

    def set_source(self, channel: int = 1) -> None:
        """Select the trigger source of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:SOURce <source>
        :TRIGger:RS232:SOURce?

        **Description**

        Select the trigger source of RS232 trigger.
        Query the current trigger source of RS232 trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        Reuturn Format
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RS232:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:RS232:SOURce CHANnel{channel}")

    def get_source(self) -> str:
        """Query the current trigger source of RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:SOURce <source>
        :TRIGger:RS232:SOURce?

        **Description**

        Select the trigger source of RS232 trigger.
        Query the current trigger source of RS232 trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        Reuturn Format
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RS232:SOURce CHANnel2
        The query returns CHAN2.
        """
        return self.instrument.ask(":TRIGger:RS232:SOURce?")

    def set_stop_bits(self, stop_bits: int = 1) -> None:
        """Set the stop bit in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:STOP <bit>
        :TRIGger:RS232:STOP?

        **Description**

        Set the stop bit in RS232 trigger when the trigger condition is Error.
        Query the current stop bit in RS232 trigger when the trigger condition
        is Error.

        **Parameter**

        ====== ========= ====== =======
        Name   Type      Range  Default
        ====== ========= ====== =======
        <bit>  Discrete  {1|2}  1
        ====== ========= ====== =======

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns 1 or 2.

        **Example**

        :TRIGger:RS232:STOP 2
        The query returns 2.
        """
        check_input(stop_bits, "stop_bits", int, 1, 2, "stop bits")
        self.instrument.ask(f":TRIGger:RS232:STOP {stop_bits}")

    def get_stop_bits(self) -> int:
        """Query the current stop bit in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:STOP <bit>
        :TRIGger:RS232:STOP?

        **Description**

        Set the stop bit in RS232 trigger when the trigger condition is Error.
        Query the current stop bit in RS232 trigger when the trigger condition
        is Error.

        **Parameter**

        ====== ========= ====== =======
        Name   Type      Range  Default
        ====== ========= ====== =======
        <bit>  Discrete  {1|2}  1
        ====== ========= ====== =======

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns 1 or 2.

        **Example**

        :TRIGger:RS232:STOP 2
        The query returns 2.
        """
        return int(self.instrument.ask(":TRIGger:RS232:STOP?"))

    def set_data(self, data_bits: int = 70) -> None:
        """Set the data value in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:DATA <data>
        :TRIGger:RS232:DATA?

        **Description**

        Set the data value in RS232 trigger when the trigger condition is Data.
        Query the current data value in RS232 trigger when the trigger
        condition is Data.

        **Parameter**

        ======= ======== ================= =======
        Name    Type     Range             Default
        ======= ======== ================= =======
        <data>  Integer  0 to $ 2^{n}-1 $  70
        ======= ======== ================= =======

        Note: in the expression $ 2^{n} - 1 $, n is the current data bits
        (refer to the :TRIGger:RS232:WIDTh command).

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:RS232:DATA 10
        The query returns 10.
        """
        check_input(
            data_bits,
            "data_bits",
            int,
            0,
            2 * self.get_data_bit_width() - 1,
            "data bits",
        )
        self.instrument.ask(f":TRIGger:RS232:WIDTh {data_bits}")

    def get_data(self) -> int:
        """Query the current data value in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:DATA <data>
        :TRIGger:RS232:DATA?

        **Description**

        Set the data value in RS232 trigger when the trigger condition is Data.
        Query the current data value in RS232 trigger when the trigger
        condition is Data.

        **Parameter**

        ======= ======== ================= =======
        Name    Type     Range             Default
        ======= ======== ================= =======
        <data>  Integer  0 to $ 2^{n}-1 $  70
        ======= ======== ================= =======

        Note: in the expression $ 2^{n} - 1 $, n is the current data bits
        (refer to the :TRIGger:RS232:WIDTh command).

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:RS232:DATA 10
        The query returns 10.
        """
        return int(self.instrument.ask(":TRIGger:RS232:WIDTh?"))

    def set_data_bit_width(self, data_bit_width: int = 70) -> None:
        """Set the data bits in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WIDTh <width>
        :TRIGger:RS232:WIDTh?

        **Description**

        Set the data bits in RS232 trigger when the trigger condition is Data.
        Query the current data bits in RS232 trigger when the trigger condition
        is Data.

        **Parameter**

        ======== ========= ========== =======
        Name     Type      Range      Default
        ======== ========= ========== =======
        <width>  Discrete  {5|6|7|8}  8
        ======== ========= ========== =======

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns 5, 6, 7 or 8.

        **Example**

        :TRIGger:RS232:WIDTh 6
        The query returns 6.
        """
        check_input(
            data_bit_width, "data_bit_width", int, 5, 8, "data bit width"
        )
        self.instrument.ask(f":TRIGger:RS232:WIDTh {data_bit_width}")

    def get_data_bit_width(self) -> int:
        """Query the current data bits in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:WIDTh <width>
        :TRIGger:RS232:WIDTh?

        **Description**

        Set the data bits in RS232 trigger when the trigger condition is Data.
        Query the current data bits in RS232 trigger when the trigger condition
        is Data.

        **Parameter**

        ======== ========= ========== =======
        Name     Type      Range      Default
        ======== ========= ========== =======
        <width>  Discrete  {5|6|7|8}  8
        ======== ========= ========== =======

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns 5, 6, 7 or 8.

        **Example**

        :TRIGger:RS232:WIDTh 6
        The query returns 6.
        """
        return int(self.instrument.ask(":TRIGger:RS232:WIDTh?"))

    def set_baud(self, baud: int = 9600) -> None:  # BAUD and BUSer
        """Set the baud rate in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:BAUD <baud_rate>
        :TRIGger:RS232:BAUD?

        **Description**

        Set the baud rate in RS232 trigger and the unit is bps.
        Query the current baud rate in RS232 trigger.

        **Parameter**

        ============ ========= ============================= =======
        Name         Type      Range                         Default
        ============ ========= ============================= =======
        <baud_rate>  Discrete  {2400|4800|9600|19200|38400|  9600
                               57600|115200|USER}
        ============ ========= ============================= =======

        Note: for USER, refer to the :TRIGger:RS232:BUSer command.

        **Return Format**

        The query returns the baud rate currently set.

        **Example**

        :TRIGger:RS232:BAUD 4800
        The query returns 4800.

        **AND**

        :TRIGger:RS232:BUSer <user baud>
        :TRIGger:RS232:BUSer?

        **Description**

        Set the user-defined baud rate in RS232 trigger and the unit is bps.
        Query the current user-defined baud rate in RS232 trigger.

        **Parameter**

        ============ ======== ============ =======
        Name         Type     Range        Default
        ============ ======== ============ =======
        <user baud>  Integer  1 to 900000  9600
        ============ ======== ============ =======

        **Return Format**

        The query returns the current baud rate.

        **Example**

        :TRIGger:RS232:BUSer 50000
        The query returns 50000.
        """
        if baud in (2400, 4800, 9600, 19200, 38400, 9600, 57600, 115200):
            self.instrument.ask(f":TRIGger:RS232:BAUD {baud}")
            return
        check_input(baud, "baud", int, 1, 900000, "Baud")
        self.instrument.ask(f":TRIGger:RS232:BUSer {baud}")

    def get_baud(self) -> Dict[str, int]:  # BAUD and BUSer
        """Query the current baud rate in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:BAUD <baud_rate>
        :TRIGger:RS232:BAUD?

        **Description**

        Set the baud rate in RS232 trigger and the unit is bps.
        Query the current baud rate in RS232 trigger.

        **Parameter**

        ============ ========= ============================= =======
        Name         Type      Range                         Default
        ============ ========= ============================= =======
        <baud_rate>  Discrete  {2400|4800|9600|19200|38400|  9600
                               57600|115200|USER}
        ============ ========= ============================= =======

        Note: for USER, refer to the :TRIGger:RS232:BUSer command.

        **Return Format**

        The query returns the baud rate currently set.

        **Example**

        :TRIGger:RS232:BAUD 4800
        The query returns 4800.

        **AND**

        :TRIGger:RS232:BUSer <user baud>
        :TRIGger:RS232:BUSer?

        **Description**

        Set the user-defined baud rate in RS232 trigger and the unit is bps.
        Query the current user-defined baud rate in RS232 trigger.

        **Parameter**

        ============ ======== ============ =======
        Name         Type     Range        Default
        ============ ======== ============ =======
        <user baud>  Integer  1 to 900000  9600
        ============ ======== ============ =======

        **Return Format**

        The query returns the current baud rate.

        **Example**

        :TRIGger:RS232:BUSer 50000
        The query returns 50000.
        """
        return {
            "built-in": int(self.instrument.ask(":TRIGger:RS232:BAUD?")),
            "user": int(self.instrument.ask(":TRIGger:RS232:BUSer?")),
        }

    def set_level(self, level: float = 0) -> None:
        """Set the trigger level in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:LEVel <level>
        :TRIGger:RS232:LEVel?

        **Description**

        Set the trigger level in RS232 trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in RS232 trigger.

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

        :TRIGger:RS232:LEVel 0.16
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
        self.instrument.ask(f":TRIGger:RS232:LEVel {level}")

    def get_level(self) -> float:
        """Query the current trigger level in RS232 trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:LEVel <level>
        :TRIGger:RS232:LEVel?

        **Description**

        Set the trigger level in RS232 trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in RS232 trigger.

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

        :TRIGger:RS232:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:RS232:LEVel?"))
