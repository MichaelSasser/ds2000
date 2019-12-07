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

from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = [
    "Bus",
]


class Mode(SubController):
    def parallel(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:MODE <mode>

        :BUS<n>:MODE?

        **Description**

        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        **Parameter**

        ======== ========== ========================== =======
        Name     Type       Range                      Default
        ======== ========== ========================== =======
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel
        ======== ========== ========================== =======

        **Return Format**

        The query returns PAR, RS232, IIC or SPI.

        **Example**

        :BUS1:MODE SPI

        The query returns SPI.
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:MODE PARallel"
        )

    def rs232(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:MODE <mode>
        
        :BUS<n>:MODE?

        **Description**

        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        **Parameter**

        ======== ========== ========================== ========
        Name     Type       Range                      Default
        ======== ========== ========================== ========
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel
        ======== ========== ========================== ========

        **Return Format**

        The query returns PAR, RS232, IIC or SPI.

        **Example**

        :BUS1:MODE SPI

        The query returns SPI.
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE RS232")

    def i2c(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:MODE <mode>

        :BUS<n>:MODE?

        **Description**

        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        **Parameter**

        ======== ========== ========================== ========
        Name     Type       Range                      Default
        ======== ========== ========================== ========
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel
        ======== ========== ========================== ========

        **Return Format**

        The query returns PAR, RS232, IIC or SPI.

        **Example**

        :BUS1:MODE SPI

        The query returns SPI.
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE IIC")

    def spi(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:MODE <mode>

        :BUS<n>:MODE?

        **Description**

        Set the decoding mode of bus 1 or 2.
        Query the current decoding mode of bus 1 or 2.

        **Parameter**

        ======== ========== ========================== ========
        Name     Type       Range                      Default
        ======== ========== ========================== ========
        <n>      Discrete   {1|2}                      --
        <mode>   Discrete   {PARallel|RS232|IIC|SPI}   PARallel
        ======== ========== ========================== ========

        **Return Format**

        The query returns PAR, RS232, IIC or SPI.

        **Example**

        :BUS1:MODE SPI

        The query returns SPI.
        """
        self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:MODE SPI")

    def get(self) -> str:
        answer = self.subdevice.ask(f":BUS{self.subdevice.busnumber}:MODE?")
        if answer == "PAR":
            return "Parallel"
        elif answer == "RS232":
            return "RS232"
        elif answer == "IIC":
            return "I2C"
        elif answer == "SPI":
            return "SPI"
        raise Ds2000Exception("Unknown Bus Mode")

    def __str__(self) -> str:
        return str(self.get)

    def __repr__(self) -> str:
        return str(self.get())


class Format(SubController):
    def hex(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:FORMat <format>

        :BUS<n>:FORMat?

        **Description**

        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary
        or ASCII.
        Query the current display format of bus 1 or 2.

        **Parameter**

        ======== ========== ========================== ========
        Name       Type       Range                 Default
        ======== ========== ========================== ========
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX
        ======== ========== ========================== ========

        **Return Format**

        The query returns HEX, DEC, BIN or ASC.

        **Example**

        :BUS1:FORMat DEC

        The query returns DEC.
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:FORMAT HEX"
        )

    def dec(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:FORMat <format>

        :BUS<n>:FORMat?

        **Description**

        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary
        or ASCII.
        Query the current display format of bus 1 or 2.

        **Parameter**

        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX
        ========== ========== ===================== ========

        **Return Format**

        The query returns HEX, DEC, BIN or ASC.

        **Example**

        :BUS1:FORMat DEC

        The query returns DEC.
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:FORMAT DEC"
        )

    def bin(self):
        """
        **Rigol Programming Guide:**

        **Syntax**

        :BUS<n>:FORMat <format>

        :BUS<n>:FORMat?

        **Description**

        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary
        or ASCII.
        Query the current display format of bus 1 or 2.

        **Parameter**

        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX
        ========== ========== ===================== ========

        **Return Format**

        The query returns HEX, DEC, BIN or ASC.

        **Example**

        :BUS1:FORMat DEC

        The query returns DEC.
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:FORMAT BIN"
        )

    def ascii(self):
        """
        **Rigol Programming Guide:**

        **Syntax**

        :BUS<n>:FORMat <format>

        :BUS<n>:FORMat?

        **Description**

        Set the display format of bus 1 or 2 to hexadecimal, decimal, binary
        or ASCII.
        Query the current display format of bus 1 or 2.

        **Parameter**

        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <n>        Discrete   {1|2}                 --
        <format>   Discrete   {HEX|DEC|BIN|ASCii}   HEX
        ========== ========== ===================== ========

        **Return Format**

        The query returns HEX, DEC, BIN or ASC.

        **Example**

        :BUS1:FORMat DEC

        The query returns DEC.
        """
        self.subdevice.device.ask(
            f":BUS{self.subdevice.__busnumber}:FORMAT ASCii"
        )

    def get(self) -> str:
        answer = self.subdevice.ask(f":BUS{self.subdevice.__busnumber}:FORMAT?")
        if answer == "HEX":
            return "HEX"
        elif answer == "DEC":
            return "DEC"
        elif answer == "BIN":
            return "BIN"
        elif answer == "ASC":
            return "ASCII"
        else:
            raise Ds2000Exception("Unknown Bus Format")

    def __str__(self) -> str:
        return str(self.get)

    def __repr__(self) -> str:
        return str(self.get())


class Parallel(SubController):
    @property
    def clk(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:PARallel:CLK <sour>

        :BUS<n>:PARallel:CLK?

        **Description**

        Set the clock channel source of parallel decoding on bus 1 or 2.

        Query the current clock channel source of parallel decoding on bus 1
        or 2.

        **Parameter**

        ======== ========= ========================== =======
        Name     Type      Range                      Default
        ======== ========= ========================== =======
        <n>      Discrete  {1|2}                      --
        <sour>   Discrete  {CHANnel1|CHANnel2|OFF}    OFF
        ======== ========= ========================== =======

        **Explanation**

        When OFF is selected, no clock channel is set and the oscilloscope
        samples data once the channel data jumps. At this point, the edge set
        by the :BUS<n>:PARallel:SLOPe command can be ignored.

        **Return Format**

        The query returns CHAN1, CHAN2 or OFF.

        **Example**

        :BUS1:PARallel:CLK CHANnel2
        """
        raise NotImplementedError()

    def slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:PARallel:SLOPe <pos>

        :BUS<n>:PARallel:SLOPe?

        **Description**

        Set the oscilloscope to sample the channel data on the rising edge,
        falling edge or rising&falling edges of the clock.

        Query on which kind of edge of the clock the oscilloscope samples the
        data channel.

        **Parameter**

        ===== ========= ========================== ========
        Name  Type      Range                      Default
        ===== ========= ========================== ========
        <n>   Discrete  {1|2}                      --
        <pos> Discrete  {POSitive|NEGative|BOTH}   POSitive
        ===== ========= ========================== ========

        **Explanation**

        When no clock channel is set (refer to the
        :BUS<n>:PARallel:CLK command), the oscilloscope samples data once the
        channel data jumps and the edge set by this command can be ignored.

        **Return Format**

        The query returns POS, NEG or BOTH.

        **Example**

        :BUS1:PARallel:SLOPe NEGative

        The query returns NEG.
        """
        raise NotImplementedError()

    def bitset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:PARallel:BSET <b0>,<b1>,<b2>…<b19>

        :BUS<n>:PARallel:BSET?

        **Description**

        This command specifies channel source for each bit and sets the data
        width (up to 20bits: from bit 0 to bit 19).
        Query the current channel source of each bit.

        **Parameter**

        ====== ========= ===================== ========
        Name   Type      Range                 Default
        ====== ========= ===================== ========
        <n>    Discrete  {1|2}                 --
        <b0>   Discrete  {CHANnel1|CHANnel2}   CHANnel1
        <b1>   Discrete  {CHANnel1|CHANnel2}   CHANnel2
        <b2>   Discrete  {CHANnel1|CHANnel2}   CHANnel1
        ...    ...        ...                  ...
        <b19>  Discrete  {CHANnel1|CHANnel2}   CHANnel1
        ====== ========= ===================== ========

        **Explanation**

        The setting sequence of the bits is LSB. For **Example**, when setting
        CHAN2,CHAN1, bit 0 is CHAN2 and bit 1 is CHAN1.

        **Return Format**

        The query returns the channel sources (separated by commas) of all
        the bits in the current data channel. For **Example**, CHAN2,CHAN1.

        **Example**

        :BUS1:PARallel:BSET CHAN1,CHAN2

        The query returns CHAN1,CHAN2.
        """
        raise NotImplementedError()

    def threshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:PARallel:THReshold <sour>,<thre>

        :BUS<n>:PARallel:THReshold? <sour>

        **Description**

        Set the threshold of the channel of parallel decoding on bus 1 or 2.

        Query the current threshold of the channel of parallel decoding on
        bus 1 or 2.

        **Parameter**

        ======= ========= ============================== ========
        Name    Type      Range                          Default
        ======= ========= ============================== ========
        <n>     Discrete  {1|2}                          --
        <sour>  Discrete  {CHANnel1|CHANnel2}            CHANnel1
        <thre>  Real      ± 5 × VerticalScale from the   0
                          screen center - OFFSet
        ======= ========= ============================== ========

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the current threshold in scientific notation.

        **Example**

        :BUS1:PARallel:THReshold CHANnel2,2.4
        """
        raise NotImplementedError()

    def offset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:PARallel:OFFSet <val>

        :BUS<n>:PARallel:OFFSet?

        **Description**

        Set the vertical offset in parallel decoding on bus 1 or 2. Enable
        the display of the bus (refer to the :BUS<n>:DISPlay command), before
        using this command.

        Query the current vertical offset in parallel
        decoding on bus 1 or bus 2.

        **Parameter**

        ====== ========== ================================== =======
        Name   Type       Range                              Default
        ====== ========== ================================== =======
        <n>    Discrete   {1|2}                              --
        <val>  Integer    **Normal**[1]: -166 to 148         0
                          **Statistic**[2]: -163 to 143
                          **Half screen**[3]: -103 to 52
        ====== ========== ================================== =======

        Note[1]: the screen display is normal and the statistic function is not
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[2]: the screen display is normal and the statistic function is
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[3]: the screen is divided into two windows (refer to the
        :TIMebase:DELay:ENABle and :CALCulate:FFT:SPLit commands).

        **Return Format**

        The query returns the offset in integer.

        **Example**

        :BUS1:PARallel:OFFSet 2

        The query returns 2.
        """
        raise NotImplementedError()


class Rs232(SubController):
    def tx(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:TX <source>

        :BUS<n>:RS232:TX?

        **Description**

        Set the transmitting channel of RS232 decoding on bus 1 or 2 or do
        not set this channel.

        Query the current transmitting channel of RS232 decoding on bus 1 or 2.

        **Parameter**

        ========== ========== ========================= ========
        Name       Type       Range                     Default
        ========== ========== ========================= ========
        <n>        Discrete   {1|2}                     --
        <source>   Discrete   {CHANnel1|CHANnel2|OFF}   CHANnel1
        ========== ========== ========================= ========

        **Return Format**

        The query returns CHAN1, CHAN2 or OFF.
        **Example**

        :BUS1:RS232:TX CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def rx(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:RX <source>

        :BUS<n>:RS232:RX?

        **Description**

        Set the receiving channel of RS232 decoding on bus 1 or 2 or do not
        set this channel.

        Query the current receiving channel of RS232 decoding on bus 1 or 2.

        **Parameter**

        ========== ========== ==================================
        Name       Type       Range                     Default
        ========== ========== ==================================
        <n>        Discrete   {1|2}                     --
        <source>   Discrete   {CHANnel1|CHANnel2|OFF}   CHANnel2
        ========== ========== ==================================

        **Return Format**

        The query returns CHAN1, CHAN2 or OFF.
        **Example**

        :BUS1:RS232:RX CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def polarity(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:POLarity <pol>

        :BUS<n>:RS232:POLarity?

        **Description**

        Set the polarity of RS232 decoding on bus 1 or 2.

        Query the current polarity of RS232 decoding on bus 1 or 2.

        **Parameter**

        ======= =========== ===================== ========
        Name    Type        Range                 Default
        ======= =========== ===================== ========
        <n>     Discrete    {1|2}                 --
        <pol>   Discrete    {POSitive|NEGative}   NEGative
        ======= =========== ===================== ========

        **Return Format**

        The query returns POS or NEG.
        **Example**

        :BUS1:RS232:POLarity NEGative

        The query returns NEG.
        """
        raise NotImplementedError()

    def endian(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:ENDian <endian>

        :BUS<n>:RS232:ENDian?

        **Description**

        Set the endian of data transmission of RS232 decoding on bus 1 or 2.

        Query the current endian of data transmission of RS232 decoding on
        bus 1 or 2.

        **Parameter**

        ========== ========== =========== =======
        Name       Type       Range       Default
        ========== ========== =========== =======
        <n>        Discrete   {1|2}       --
        <endian>   Discrete   {MSB|LSB}   LSB
        ========== ========== =========== =======

        **Return Format**

        The query returns MSB or LSB.

        **Example**

        :BUS1:RS232:ENDian MSB
        The query returns MSB.
        """
        raise NotImplementedError()

    def baud(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:BAUD <baud>

        :BUS<n>:RS232:BAUD?

        **Description**

        Set the baud rate of data transmission of RS232 decoding on bus 1 or 2.

        Query the current baud rate of data transmission of RS232 decoding on
        bus 1 or 2.

        **Parameter**

        ======= ========== =========================== =======
        Name    Type       Range                       Default
        ======= ========== =========================== =======
        <n>     Discrete   {1|2}                       --
        <baud>  Discrete   {2400|4800|9600|19200|      9600
                           38400|57600|115200|USER}
        ======= ========== =========================== =======

        Note: when the baud rate is set to USER, you need to set a specific
        baud rate using the :BUS<n>:RS232:BUSer command.

        **Return Format**

        The query returns the baud rate currently set and the unit is bps.
        **Example**

        :BUS1:RS232:BAUD 4800

        The query returns 4800.
        """
        raise NotImplementedError()

    def buser(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:BUSer <baud>

        :BUS<n>:RS232:BUSer?

        **Description**

        Set the user-defined baud rate of data transmission in RS232 decoding
        on bus 1 or 2.

        Query the current user-defined baud rate of RS232 decoding on bus 1
        or 2.

        **Parameter**

        ======= ========== ============== =======
        Name    Type       Range          Default
        ======= ========== ============== =======
        <n>     Discrete   {1|2}           --
        <baud>  Integer    50 to 1000000   9600
        ======= ========== ============== =======

        **Return Format**

        The query returns the current baud rate and the unit is bps.

        **Example**

        :BUS1:RS232:BUSer 19200

        The query returns 19200.
        """
        raise NotImplementedError()

    def dbits(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:DBITs <bits>

        :BUS<n>:RS232:DBITs?

        **Description**

        Set the data width of RS232 decoding on bus 1 or 2.

        Query the current data width of RS232 decoding on bus 1 or 2.

        **Parameter**

        ========== =========== ================ =======
        Name       Type        Range            Default
        ========== =========== ================ =======
        <n>        Discrete    {1|2}            --
        <bits>     Discrete    {5|6|7|8|9}      8
        ========== =========== ================ =======

        **Return Format**

        The query returns 5, 6, 7, 8 or 9.
        **Example**

        :BUS1:RS232:DBITs 7

        The query returns 7.
        """
        raise NotImplementedError()

    def sbits(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:SBITs <stop bits>

        :BUS<n>:RS232:SBITs?

        **Description**

        Set the stop bit after each frame of data in RS232 decoding on bus 1
        or 2.

        Query the current stop bit after each frame of data in RS232 decoding
        on bus 1 or 2.

        **Parameter**

        ============== ============ ============ =======
        Name            Type        Range        Default
        ============== ============ ============ =======
        <n>             Discrete    {1|2}        --
        <stop bits>     Discrete    {1|1.5|2}    1
        ============== ============ ============ =======

        **Return Format**

        The query returns 1, 1.5 or 2.

        **Example**

        :BUS1:RS232:SBITs 2

        The query returns 2.
        """
        raise NotImplementedError()

    def parity(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:PARity <parity>

        :BUS<n>:RS232:PARity?

        **Description**

        Set the even-odd check mode of data transmission of RS232 decoding
        on bus 1 or 2.

        Query the current even-odd check mode of data transmission of RS232
        decoding on bus 1 or 2.

        **Parameter**

        =========== =========== =================== =======
        Name        Type        Range               Default
        =========== =========== =================== =======
        <n>         Discrete    {1|2}               --
        <parity>    Discrete    {NONE|ODD|EVEN}     NONE
        =========== =========== =================== =======

        **Return Format**

        The query returns NONE, ODD or EVEN.

        **Example**

        :BUS1:RS232:PARity NONE

        The query returns NONE.
        """
        raise NotImplementedError()

    def packet(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:PACKet <bool>

        :BUS<n>:RS232:PACKet?

        **Description**

        Enable or disable the packet end in data transmission.

        Query the current status of the packet end in data transmission.

        **Parameter**

        ============= ============= =================== =======
        Name          Type          Range               Default
        ============= ============= =================== =======
        <n>           Discrete      {1|2}               --
        <bool>        Bool          {{0|OFF}|{1|ON}}    0|OFF
        ============= ============= =================== =======

        **Explanation**

        When the packet end is enabled, several data blocks are combined
        according to the packet end.

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :BUS1:RS232:PACKet ON

        The query returns 1.
        """
        raise NotImplementedError()

    def pend(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:PEND <package end>

        :BUS<n>:RS232:PEND?

        **Description**

        Set the packet end of data transmission.

        Query the current packet end of data transmission.

        **Parameter**

        =============== ============ ====================== =======
        Name            Type         Range                  Default
        =============== ============ ====================== =======
        <n>             Discrete     {1|2}                  --
        <package end>   Discrete     {NULL|LF|CR|SP|FF}     NULL
        =============== ============ ====================== =======

        **Explanation**

        The hexadecimal numbers corresponding to the **Parameter**s are as follows.

        NULL: 00; LF: 0A; CR: 0D; SP: 20; FF: FF.

        **Return Format**

        The query returns NULL, LF, CR, SP or FF.

        **Example**

        :BUS1:RS232:PEND FF

        The query returns FF.
        """
        raise NotImplementedError()

    def threshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:TTHReshold <tthre>

        :BUS<n>:RS232:TTHReshold?

        **Description**

        Set the threshold of the transmitting channel of R232 decoding on
        bus 1 or 2.

        Query the current threshold of the transmitting channel of R232
        decoding on bus 1 or 2.

        **Parameter**

        ========== =========== =============================== =======
        Name       Type        Range                           Default
        ========== =========== =============================== =======
        <n>        Discrete    {1|2}                           --
        <tthre>    Real        ± 5 × VerticalScale from t      0
                               he screen center - OFFSet
        ========== =========== =============================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**

        :BUS1:RS232:TTHReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def rthreshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:RTHReshold <rthre>

        :BUS<n>:RS232:RTHReshold?

        **Description**

        Set the threshold of the receiving channel of R232 decoding on bus
        1 or 2.

        Query the current threshold of the receiving channel of R232 decoding
        on bus 1 or 2.

        **Parameter**

        ========== ============ =============================== =======
        Name       Type         Range                           Default
        ========== ============ =============================== =======
        <n>        Discrete     {1|2}                           --
        <rthre>    Real         ± 5 × VerticalScale from        0
                                the screen center - OFFSet
        ========== ============ =============================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**

        :BUS1:RS232:RTHReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def offset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:RS232:OFFSet <val>

        :BUS<n>:RS232:OFFSet?

        **Description**

        Set the vertical offset in RS232 decoding on bus 1 or 2. Before using
        this command, enable the bus display (refer to the :BUS<n>:DISPlay
        command).

        Query the current vertical offset in RS232 decoding on bus 1 or 2.

        **Parameter**

        ======= ========== ================================= =======
        Name    Type       Range                             Default
        ======= ========== ================================= =======
        <n>     Discrete   {1|2}                             --
        <val>   Integer    **Normal[1]**: -166 to 148        0
                           **Statistic[2]**: -163 to 143
                           **Half screen[3]**: -103 to 52
        ======= ========== ================================= =======

        Note[1]: the screen display is normal and the statistic function is not
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[2]: the screen display is normal and the statistic function is
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[3]: the screen is divided into two windows (refer to the
        :TIMebase:DELay:ENABle and :CALCulate:FFT:SPLit commands).

        **Return Format**

        The query returns the offset in integer.

        **Example**

        :BUS1:RS232:OFFSet 2

        The query returns 2.
        """
        raise NotImplementedError()

class I2c(SubController):
    def sclk_source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:IIC:SCLK:SOURce <sour>
        :BUS<n>:IIC:SCLK:SOURce?

        **Description**

        Set the clock channel source of IIC decoding on bus 1 or 2.

        Query the current clock channel source of IIC decoding on bus 1 or 2.

        **Parameter**

        ======= ========== ===================== ========
        Name    Type       Range                 Default
        ======= ========== ===================== ========
        <n>     Discrete   {1|2}                 --
        <sour>  Discrete   {CHANnel1|CHANnel2}   CHANnel1
        ======= ========== ===================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :BUS1:IIC:SCLK:SOURce CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sclk_threshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:IIC:SCLK:THReshold <thre>

        :BUS<n>:IIC:SCLK:THReshold?

        **Description**

        Set the threshold of the clock channel of IIC decoding on bus 1 or 2.

        Query the current threshold of the clock channel of IIC decoding on
        bus 1 or 2.

        **Parameter**

        ========= =========== ============================= =======
        Name      Type        Range                         Default
        ========= =========== ============================= =======
        <n>       Discrete    {1|2}                         --
        <thre>    Real        ± 5 × VerticalScale from      0
                              the screen center - OFFSet
        ========= =========== ============================= =======

        Note:

        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**
        :BUS1:IIC:SCLK:THReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def sda_source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:IIC:SDA:SOURce <sour>

        :BUS<n>:IIC:SDA:SOURce?

        **Description**

        Set the data channel source of IIC decoding on bus 1 or 2.

        Query the current data channel source of IIC decoding on bus 1 or 2.

        **Parameter**

        ========= =========== ======================= ========
        Name      Type        Range                   Default
        ========= =========== ======================= ========
        <n>       Discrete    {1|2}                   --
        <sour>    Discrete    {CHANnel1|CHANnel2}     CHANnel2
        ========= =========== ======================= ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :BUS1:IIC:SDA:SOURce CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sda_threshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:IIC:SDA:THReshold <thre>

        :BUS<n>:IIC:SDA:THReshold?

        **Description**

        Set the threshold of the data channel of IIC decoding on bus 1 or 2.

        Query the current threshold of the data channel of IIC decoding
        on bus 1 or 2.

        **Parameter**

        =========== =========== ============================== =======
        Name        Type        Range                          Default
        =========== =========== ============================== =======
        <n>         Discrete    {1|2}                          --
        <thre>      Real        ± 5 × VerticalScale from       0
                                the screen center - OFFSet
        =========== =========== ============================== =======

        Note:

        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**

        :BUS1:IIC:SDA:THReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def offset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:IIC:OFFSet <val>

        :BUS<n>:IIC:OFFSet?

        **Description**

        Set the vertical offset in IIC decoding on bus 1 or 2. Before using
        this command, enable the bus display (refer to the :BUS<n>:DISPlay
        command).

        Query the current vertical offset in IIC decoding on bus 1 or 2.

        **Parameter**

        ========== =========== ================================== =======
        ame        Type        Range                              Default
        ========== =========== ================================== =======
        <n>        Discrete    {1|2}                              --
        <val>      Integer     **Normal**[1]: -166 to 148         0
                               **Statistic**[2]: -163 to 143
                               **Half screen**[3]: -103 to 52
        ========== =========== ================================== =======

        Note[1]: the screen display is normal and the statistic function is
        not enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[2]: the screen display is normal and the statistic function is
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[3]: the screen is divided into two windows (refer to the
        :TIMebase:DELay:ENABle and :CALCulate:FFT:SPLit commands).

        **Return Format**

        The query returns the offset in integer.

        **Example**

        :BUS1:IIC:OFFSet 2

        The query returns 2.
        """
        raise NotImplementedError()

class Spi(SubController):
    def sclk_source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SCLK:SOURce <sour>

        :BUS<n>:SPI:SCLK:SOURce?

        **Description**

        Set the clock channel source of SPI decoding on bus 1 or 2.

        Query the current clock channel source of SPI decoding on bus 1 or 2.

        **Parameter**

        ======== ========== ====================== ========
        Name     Type       Range                  Default
        ======== ========== ====================== ========
        <n>      Discrete   {1|2}                  --
        <sour>   Discrete   {CHANnel1|CHANnel2}    CHANnel1
        ======== ========== ====================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :BUS1:SPI:SCLK:SOURce CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sclk_slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SCLK:SLOPe <pos>

        :BUS<n>:SPI:SCLK:SLOPe?

        **Description**

        Set the clock edge type in SPI decoding on bus 1 or 2.

        Query the current clock edge type in SPI decoding on bus 1 or 2.

        **Parameter**

        ======= =========== ======================= =========
        Name    Type        Range                   Default
        ======= =========== ======================= =========
        <n>     Discrete    {1|2}                   --
        <pos>   Discrete    {POSitive|NEGative}     POSitive
        ======= =========== ======================= =========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :BUS1:SPI:SCLK:SLOPe NEGative

        The query returns NEG.
        """
        raise NotImplementedError()

    def sclk_thrshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SCLK:THReshold <thre>

        :BUS<n>:SPI:SCLK:THReshold?

        **Description**

        Set the threshold of the clock channel of SPI decoding on bus 1 or 2.

        Query the current threshold of the clock channel of SPI decoding
        on bus 1 or 2.

        **Parameter**

        ======== =========== ============================== =======
        Name     Type        Range                          Default
        ======== =========== ============================== =======
        <n>      Discrete    {1|2}                          --
        <thre>   Real        ± 5 × VerticalScale from       0
                             the screen center - OFFSet
        ======== =========== ============================== =======

        Note:

        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**

        :BUS1:SPI:SCLK:THReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def sda_source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SDA:SOURce <sour>

        :BUS<n>:SPI:SDA:SOURce?

        **Description**

        Set the data channel source in SPI decoding on bus 1 or 2.

        Query the current data channel source in SPI decoding on bus 1 or 2.

        **Parameter**

        ========= =========== ===================== ========
        Name      Type        Range                 Default
        ========= =========== ===================== ========
        <n>       Discrete    {1|2}                 --
        <sour>    Discrete    {CHANnel1|CHANnel2}   CHANnel2
        ========= =========== ===================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :BUS1:SPI:SDA:SOURce CHANnel1

        The query returns CHAN1.
        """
        raise NotImplementedError()

    def sda_polarity(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SDA:POLarity <pos>

        :BUS<n>:SPI:SDA:POLarity?

        **Description**

        Set the polarity of the SDA data line in SPI decoding on bus 1 or 2.

        Query the current polarity of the SDA data line in SPI decoding on
        bus 1 or 2.

        **Parameter**

        ======= ========== ============ =======
        Name    Type       Range        Default
        ======= ========== ============ =======
        <n>     Discrete   {1|2}        --
        <pos>   Discrete   {HIGH|LOW}   LOW
        ======= ========== ============ =======

        **Return Format**

        The query returns HIGH or LOW.

        **Example**

        :BUS1:SPI:SDA:POLarity HIGH

        The query returns HIGH.
        """
        raise NotImplementedError()

    def sda_threshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:SDA:THReshold <thre>

        :BUS<n>:SPI:SDA:THReshold?

        **Description**

        Set the threshold of the data channel in SPI decoding on bus 1 or 2.

        Query the current threshold of the data channel in SPI decoding on
        bus 1 or 2.

        **Parameter**

        ========= =========== ============================ =========
        Name      Type        Range                         Default
        ========= =========== ============================ =========
        <n>       Discrete    {1|2}                         --
        <thre>    Real        ± 5 × VerticalScale from      0
                              the screen center - OFFSet
        ========= =========== ============================ =========

        Note:

        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the threshold set in scientific notation.

        **Example**

        :BUS1:SPI:SDA:THReshold 2.4

        The query returns 2.400000e+00.
        """
        raise NotImplementedError()

    def dbits(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:DBITs <width>

        :BUS<n>:SPI:DBITs?

        **Description**

        Set the data width in SPI decoding on bus 1 or 2.

        Query the current data width in SPI decoding on bus 1 or 2.

        **Parameter**

        ========== =========== ========== =======
        Name       Type        Range      Default
        ========== =========== ========== =======
        <n>        Discrete    {1|2}      --
        <width>    Integer     4 to 32    8
        ========== =========== ========== =======

        **Return Format**

        The query returns an integer between 4 and 32.

        **Example**

        :BUS1:SPI:DBITs 10

        The query returns 10.
        """
        raise NotImplementedError()

    def endian(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:ENDian <endian>

        :BUS<n>:SPI:ENDian?

        **Description**

        Set the endian of data transmission in SPI decoding on bus 1 or 2.

        Query the current endian of data transmission in SPI decoding on
        bus 1 or 2.

        **Parameter**

        =========== =========== =========== =======
        Name        Type        Range       Default
        =========== =========== =========== =======
        <n>         Discrete    {1|2}       --
        <endian>    Discrete    {MSB|LSB}   MSB
        =========== =========== =========== =======

        **Return Format**

        The query returns MSB or LSB.

        **Example**

        :BUS1:SPI:ENDian MSB

        The query returns MSB.
        """
        raise NotImplementedError()

    def offset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:SPI:OFFSet <val>

        :BUS<n>:SPI:OFFSet?

        **Description**

        Set the vertical offset in SPI decoding on bus 1 or 2. Before using
        this command, enable the bus display (refer to the :BUS<n>:DISPlay
        command).

        Query the vertical offset in SPI decoding on bus 1 or 2.

        **Parameter**

        ======= =========== ================================== =======
        Name    Type        Range                              Default
        ======= =========== ================================== =======
        <n>     Discrete    {1|2}                              --
        <val>   Integer     **Normal**[1]: -166 to 148         0
                            **Statistic**[2]: -163 to 143
                            **Half screen**[3]: -103 to 52
        ======= =========== ================================== =======

        Note[1]: the screen display is normal and the statistic function is not
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[2]: the screen display is normal and the statistic function is
        enabled (refer to the :MEASure:STATistic:DISPlay command).

        Note[3]: the screen is divided into two windows (refer to the
        :TIMebase:DELay:ENABle and :CALCulate:FFT:SPLit commands).

        **Return Format**

        The query returns the offset in integer.

        **Example**

        :BUS1:SPI:OFFSet 2

        The query returns 2.
        """
        raise NotImplementedError()

class Bus(BaseController):
    def __init__(self, device, busnumber):
        super(Bus, self).__init__(device)
        self.__busnumber = busnumber

        # Device Subclasses
        self.mode: Mode = Mode(self)
        self.format: Format = Format(self)
        self.parallel: Parallel = Parallel(self)
        self.rs232: Rs232 = Rs232(self)
        self.i2c: I2c = I2c(self)

    @property
    def display(self) -> bool:
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:DISPlay <bool>

        :BUS<n>:DISPlay?

        **Description**

        Enable or disable the display of bus 1 or 2.
        Query the current display status of bus 1 or 2.

        **Parameter**

        ======== ========== ================== ========
        Name     Type       Range              Default
        ======== ========== ================== ========
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF
        ======== ========== ================== ========

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :BUS1:DISPlay ON

        The query returns 1.
        """
        return (
            True
            if self.device.ask(f":BUS{self.__busnumber}:DISPlay?") == 1
            else False
        )

    @display.setter
    def display(self, enable: bool = True):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:DISPlay <bool>

        :BUS<n>:DISPlay?

        **Description**

        Enable or disable the display of bus 1 or 2.
        Query the current display status of bus 1 or 2.

        **Parameter**

        ======== ========== ================== ========
        Name     Type       Range              Default
        ======== ========== ================== ========
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF
        ======== ========== ================== ========

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :BUS1:DISPlay ON

        The query returns 1.
        """
        assert isinstance(enable, bool)
        self.device.ask(f":BUS{self.__busnumber}:DISPlay {1 if enable else 0}")

    @property
    def eventtable(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:EVENt <bool>

        :BUS<n>:EVENt?

        **Description**

        Enable or disable the event table of bus 1 or bus 2.
        Query the current status of the event table of bus 1 or bus 2.

        **Parameter**

        ======== ========== ================== ========
        Name     Type       Range              Default
        ======== ========== ================== ========
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF
        ======== ========== ================== ========

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :BUS1:EVENt ON

        The query returns 1.
        """
        return (
            True
            if self.device.ask(f":BUS{self.__busnumber}:EVENt?") == 1
            else False
        )

    @eventtable.setter
    def eventtable(self, enable: bool = True):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:EVENt <bool>

        :BUS<n>:EVENt?

        **Description**

        Enable or disable the event table of bus 1 or bus 2.
        Query the current status of the event table of bus 1 or bus 2.

        **Parameter**

        ======== ========== ================== ========
        Name     Type       Range              Default
        ======== ========== ================== ========
        <n>      Discrete   {1|2}              --
        <bool>   Bool       {{0|OFF}|{1|ON}}   0|OFF
        ======== ========== ================== ========

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :BUS1:EVENt ON

        The query returns 1.
        """
        assert isinstance(enable, bool)
        self.device.ask(f":BUS{self.__busnumber}:EVENt {1 if enable else 0}")

    def export_eventtable_to_usb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :BUS<n>:EEXPort

        **Description**

        Export the event table of bus 1 or 2.

        **Parameter**

        ====== ========== ======= =======
        Name   Type       Range   Default
        ====== ========== ======= =======
        <n>    Discrete   {1|2}   --
        ====== ========== ======= =======

        **Explanation**

        The data list can be exported to external USB storage device in CSV
        format if USB storage device is currently connected.
        """
        self.device.ask(f":BUS{self.__busnumber}:EEXPort")