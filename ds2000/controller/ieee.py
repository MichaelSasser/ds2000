#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ds2000.controller import BaseController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "IEEE",
]


class IEEE(BaseController):
    def __init__(self, device):
        """The "low level" functions barely untouched.

        :param device:
        """
        super(IEEE, self).__init__(device)

    def cls(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        \*CLS

        **Description**

        Clear all the event registers in the register set and clear the error
        queue.
        """
        NotImplementedError()

    def ese(self):  # ToDo: P. 29-31 -> ESR
        """
        **Rigol Programming Guide**

        **Syntax**

        \*ESE <mask>

        \*ESE?

        **Description**

        Set enable register for the standard event register set.
        Query the current value of the enable register of the standard event
        register set.

        **Parameter**

        ========  ========= ========== =======
        Name      Type      Range      Default
        ========  ========= ========== =======
        <mask>    Integer   0 to 255   0
        ========  ========= ========== =======

        **Explanation**

        <mask> is the sum of the weights of all the bits between
        bit 0 and bit 7 that have already been set. If the bit has already been
        set, the corresponding binary bit is 1; otherwise, it is 0.

        Definitions of the bits in ESE register:

        ======== ========= ======= ====================
        Bit      Weights   Name    Enable
        ======== ========= ======= ====================
        7        128       PON     Power On
        6        64        URQ     User Request
        5        32        CME     Command Error
        4        16        EXE     Execution Error
        3        8         DDE     Dev. Dependent Error
        2        4         QYE     Query Error
        1        2         RQL     Request Control
        0        1         OPC     Operation Complete
        ======== ========= ======= ====================

        **Return Format**

        The query returns an integer between 0 and 255 which equals the sum of
        the weights of all the bits that have already been set in the register.
        For example, the query returns 144 if bit 4 (16 in decimal) and
        bit 7 (128 in decimal) are enabled.

        **Example**

        \*ESE 16

        The query returns 16 (bit 4 is enabled).
        """
        NotImplementedError()

    def idn(self) -> str:
        """ This method returns the ID character string of the device_address
        as a Instrument Tuple.

        **Rigol Programming Guide**

        **Syntax**

        \*IDN?

        **Description**

        Query the current device information.

        **Return Format**

        Rigol Technologies,<model>,<serial number>,X.XX.XX
        <model>: the model number of the instrument.
        <serial number>: the serial number of the instrument.
        X.XX.XX: the software version of the instrument.

        **Example**

        \*IDN?

        The query returns RIGOL TECHNOLOGIES,DS2202,DS2A0000000001,00.00.01. Instrument
        """
        return self.device.ask("*IDN?")

    def opc(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        \*OPC

        \*OPC?

        **Description**

        Set the Operation Complete bit (bit 0) in the standard event status
        register to 1 after the current operation is finished.
        Query whether the current operation is finished.

        **Return Format**

        The query returns 1 if the current operation is finished; otherwise,
        returns 0
        """
        NotImplementedError()

    def rst(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        \*RST

        **Description**

        Restore the instrument to the default values.
        """
        self.device.ask("*RST")

    def sre(self):  # P. 35-37 -> STB
        """
        **Rigol Programming Guide**

        **Syntax**

        \*SRE <mask>

        \*SRE?

        **Description**

        Set the enable register for the state byte register set.
        Query the current value of the enable register of the state byte
        register set.

        **Parameter**

        ======== ========== =========== =======
        Name     Type       Range       Default
        ======== ========== =========== =======
        <mask>   Integer    0 to 255    0
        ======== ========== =========== =======

        **Explanation**

        <mask> is the sum of the weights of all the bits between
        bit 0 and bit 7 that have already been set. If the bit has already been
        set, the corresponding binary bit is 1; otherwise, it is 0.

        Definitions of the bits of SRE register:

        ===== ========= ====== ====================
        Bit   Weights   Name   Enable
        ===== ========= ====== ====================
        7     128       OPER   Operation Status Reg
        6     64        --     Not used
        5     32        ESB    Event Status Bit
        4     16        MAV    Message Available
        3     8         --     Not used
        2     4         MSG    Message
        1     2         USR    User
        0     1         TRG    Trigger
        ===== ========= ====== ====================

        **Return Format**

        The query returns an integer between 0 and 255 which equals the sum of
        the weights of all the bits that have already been set in the register.
        For example, the query returns 144 if bit 4 (16 in decimal) and
        bit 7 (128 in decimal) are enabled.

        **Example**

        \*SRE 16
        The query returns 16 (bit 4 is enabled).
        """
        NotImplementedError()

    def tst(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        \*TST?

        **Description**

        Perform a self-test.

        **Explanation**

        The self-test result is denoted by a 32-bit binary number.
        If the corresponding binary bit is 0, the self-test item passes the
        test; while 1 indicates a failure. The return value is the decimal
        integer corresponding to the binary number.

        The self-test item represented by each bit is as shown in the
        figure below. The bit that is not used is always 0.

        ====== ==================
        Bit    Description
        ====== ==================
        bit0   system voltage
        bit1   analog voltage
        bit2   storage system
        bit3   digital core
        bit4   digital IO
        bit8   battery
        bit9   fan 1
        bit10  fan 2
        bit12  inlet temperature
        bit13  outlet temperature
        bit16  real-time clock
        ====== ==================

        **Return Format**

        The query returns a decimal integer.

        **Example**

        \*TST?

        The query returns 0.
        """
        NotImplementedError()
