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
    "Rs232",
]


class Rs232When(SubSubController):
    def start_frame_position(self):
        """
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
        raise NotImplementedError()

    def error_detected(self):
        """
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
        raise NotImplementedError()

    def parity_error_detected(self):
        """
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
        raise NotImplementedError()

    def data(self):
        """
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
        raise NotImplementedError()


class Rs232Parity(SubSubController):
    def even(self):
        """
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
        raise NotImplementedError()

    def odd(self):
        """
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
        raise NotImplementedError()

    def none(self):
        """
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
        raise NotImplementedError()


class Rs232(SubController):
    def __init__(self, device):
        super(Rs232, self).__init__(device)
        self.when: Rs232When = Rs232When(self)
        self.parity: Rs232Parity = Rs232Parity(self)

    def source(self):
        """
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
        raise NotImplementedError()

    def stop_bits(self):
        """
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
        raise NotImplementedError()

    def data(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RS232:DATA <data>
        :TRIGger:RS232:DATA?

        **Description**

        Set the data value in RS232 trigger when the trigger condition is Data.
        Query the current data value in RS232 trigger when the trigger
        condition is Data.

        **Parameter**

        ======= ======== ========== =======
        Name    Type     Range      Default
        ======= ======== ========== =======
        <data>  Integer  0 to 2n-1  70
        ======= ======== ========== =======

        Note: in the expression 2n - 1, n is the current data bits
        (refer to the :TRIGger:RS232:WIDTh command).

        **Explanation**

        To set the trigger condition, refer to the :TRIGger:RS232:WHEN command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:RS232:DATA 10
        The query returns 10.
        """
        raise NotImplementedError()

    def data_bit_width(self):
        """
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
        raise NotImplementedError()

    def baud(self):  # BAUD and BUSer
        """
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
        raise NotImplementedError()

    def level(self):
        """
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
        raise NotImplementedError()
