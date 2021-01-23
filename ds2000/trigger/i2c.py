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
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class I2CWhen(SSFunc):
    def set_start(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN STARt")

    def set_restart(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN RESTart")

    def set_stop(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN STOP")

    def set_nack(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN NACKnowledge")

    def set_address(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN ADDRess")

    def set_data(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN DATA")

    def set_address_and_data(self) -> None:
        """Set the trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        self.instrument.ask(":TRIGger:IIC:WHEN ADATa")

    def status(self) -> str:
        """Query the current trigger condition of IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:WHEN <trig_type>
        :TRIGger:IIC:WHEN?

        **Description**

        Set the trigger condition of IIC trigger.
        Query the current trigger condition of IIC trigger.

        **Parameter**

        ============ ========= ================================== =======
        Name         Type      Range                              Default
        ============ ========= ================================== =======
        <trig_type>  Discrete  {STARt|RESTart|STOP|NACKnowledge|  STARt
                               ADDRess|DATA|ADATa}
        ============ ========= ================================== =======

        **Explanation**

        STARt: trigger when SDA data transitions from high to low while SCL
        is high.

        RESTart: trigger when another start condition occurs before a stop
        condition.

        STOP: trigger when SDA data transitions from low to high while SCL
        is high.

        NACKnowledge: trigger when the SDA data is high during any
        acknowledgement of SCL clock position.

        ADDRess: trigger on the clock (SCL) edge corresponding to the byte
        of data (SDA) behind the preset address (Write, Read or R/W direction).

        DATA: the trigger searches for the control byte value on the data
        line (SDA) following which there is a reading bit and an
        acknowledgement bit and then searches for the specified data value.

        ADATa: trigger when the “Address” and “Data” conditions are met at the
         same time.

        **Return Format**

        The query returns STAR, STOP, NACK, REST, ADDR, DATA or ADAT.

        **Example**

        :TRIGger:IIC:WHEN RESTart
        The query returns REST.
        """
        return self.instrument.ask(":TRIGger:IIC:WHEN?")


class I2CDirection(SSFunc):
    def set_read(self) -> None:
        """Set the data direction in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DIRection <dir>
        :TRIGger:IIC:DIRection?

        **Description**

        Set the data direction in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current data direction in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ========= ==================== =======
        Name   Type      Range                Default
        ====== ========= ==================== =======
        <dir>  Discrete  {READ|WRITe|RWRite}  READ
        ====== ========= ==================== =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        self.instrument.ask(":TRIGger:IIC:DIRection READ")

    def set_write(self) -> None:
        """Set the data direction in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DIRection <dir>
        :TRIGger:IIC:DIRection?

        **Description**

        Set the data direction in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current data direction in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ========= ==================== =======
        Name   Type      Range                Default
        ====== ========= ==================== =======
        <dir>  Discrete  {READ|WRITe|RWRite}  READ
        ====== ========= ==================== =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        self.instrument.ask(":TRIGger:IIC:DIRection WRITe")

    def set_read_write(self) -> None:
        """Set the data direction in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DIRection <dir>
        :TRIGger:IIC:DIRection?

        **Description**

        Set the data direction in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current data direction in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ========= ==================== =======
        Name   Type      Range                Default
        ====== ========= ==================== =======
        <dir>  Discrete  {READ|WRITe|RWRite}  READ
        ====== ========= ==================== =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        self.instrument.ask(":TRIGger:IIC:DIRection RWRite")

    def status(self) -> str:
        """Query the current data direction in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DIRection <dir>
        :TRIGger:IIC:DIRection?

        **Description**

        Set the data direction in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current data direction in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ========= ==================== =======
        Name   Type      Range                Default
        ====== ========= ==================== =======
        <dir>  Discrete  {READ|WRITe|RWRite}  READ
        ====== ========= ==================== =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        return self.instrument.ask(":TRIGger:IIC:DIRection?")


class I2C(SFunc):
    def __init__(self, device):
        super(I2C, self).__init__(device)
        self.when: I2CWhen = I2CWhen(self)
        self.direction: I2CDirection = I2CDirection(self)

    def set_scl_source(self, channel: int = 1) -> None:
        """Select the SCL channel source in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:SCL <source>
        :TRIGger:IIC:SCL?

        **Description**

        Select the SCL channel source in IIC trigger.
        Query the current SCL channel source in IIC trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:IIC:SCL CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:IIC:SCL CHANnel{channel}")

    def get_scl_source(self) -> str:
        """Query the current SCL channel source in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:SCL <source>
        :TRIGger:IIC:SCL?

        **Description**

        Select the SCL channel source in IIC trigger.
        Query the current SCL channel source in IIC trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:IIC:SCL CHANnel2
        The query returns CHAN2.
        """
        scl: str = self.instrument.ask(":TRIGger:IIC:SCL?").lower()
        if scl == "chan1":
            return "channel 1"
        if scl == "chan2":
            return "channel 2"
        raise RuntimeError("The oscilloscope returned an unknown channel")

    def set_sda_source(self, channel: int = 2) -> None:
        """Select the SDA channel source in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:SDA <source>
        :TRIGger:IIC:SDA?

        **Description**

        Select the SDA channel source in IIC trigger.
        Query the current SDA channel source in IIC trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:IIC:SDA CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(f":TRIGger:IIC:SDA CHANnel{channel}")

    def get_sda_source(self) -> str:
        """Query the current SDA channel source in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:SDA <source>
        :TRIGger:IIC:SDA?

        **Description**

        Select the SDA channel source in IIC trigger.
        Query the current SDA channel source in IIC trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel2
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:IIC:SDA CHANnel2
        The query returns CHAN2.
        """
        sda: str = self.instrument.ask("TRIGger:IIC:SDA?").lower()
        if sda == "chan1":
            return "channel 1"
        if sda == "chan2":
            return "channel 2"
        raise RuntimeError("The oscilloscope returned an unknown channel")

    def set_address_bits_width(self, address_width: int = 7) -> None:
        """Set the address bits in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:AWIDth <bits>
        :TRIGger:IIC:AWIDth?

        **Description**

        Set the address bits in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current address bits in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ======= ========= ========= =======
        Name    Type      Range     Default
        ======= ========= ========= =======
        <bits>  Discrete  {7|8|10}  7
        ======= ========= ========= =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns 7, 8 or 10.

        **Example**

        :TRIGger:IIC:AWIDth 10
        The query returns 10.
        """
        if address_width not in (7, 8, 10):
            raise ValueError("You can only have 7, 8 or 10 address bits.")
        self.instrument.ask(f":TRIGger:IIC:AWIDth {address_width}")

    def get_address_bits_width(self) -> int:
        """Query the current address bits in IIC.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:AWIDth <bits>
        :TRIGger:IIC:AWIDth?

        **Description**

        Set the address bits in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current address bits in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ======= ========= ========= =======
        Name    Type      Range     Default
        ======= ========= ========= =======
        <bits>  Discrete  {7|8|10}  7
        ======= ========= ========= =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns 7, 8 or 10.

        **Example**

        :TRIGger:IIC:AWIDth 10
        The query returns 10.
        """
        return int(self.instrument.ask(":TRIGger:IIC:AWIDth?"))

    def set_address(self, address: int = 0x01) -> None:
        """Set the address value in IIC trigger

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:ADDRess <adr>
        :TRIGger:IIC:ADDRess?

        **Description**

        Set the address value in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current address value in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ======== ============================== =======
        Name   Type     Range                          Default
        ====== ======== ============================== =======
        <adr>  Integer  0 to $ 2^{n} – 1 $: 0 to 127,  1
                        0 to 255 or 0 to 1023
        ====== ======== ============================== =======

        Note: in the expression 2n - 1, n is the current address bits
        (refer to the :TRIGger:IIC:AWIDth command).

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:IIC:ADDRess 100
        The query returns 100.
        """
        check_input(
            address,
            "address",
            int,
            0,
            2 ** self.get_address_bits_width() - 1,
            "",
        )
        self.instrument.ask(f":TRIGger:IIC:ADDRess {address}")

    def get_address(self) -> int:
        """Query the current address value in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:ADDRess <adr>
        :TRIGger:IIC:ADDRess?

        **Description**

        Set the address value in IIC trigger when the trigger condition is
        Address or A&D.
        Query the current address value in IIC trigger when the trigger
        condition is Address or A&D.

        **Parameter**

        ====== ======== ============================== =======
        Name   Type     Range                          Default
        ====== ======== ============================== =======
        <adr>  Integer  0 to $ 2^{n} – 1 $: 0 to 127,  1
                        0 to 255 or 0 to 1023
        ====== ======== ============================== =======

        Note: in the expression 2n - 1, n is the current address bits
        (refer to the :TRIGger:IIC:AWIDth command).

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:IIC:ADDRess 100
        The query returns 100.
        """
        return int(self.instrument.ask(":TRIGger:IIC:ADDRess?"))

    def set_data(self, data_value: int = 0x00) -> None:
        """Set the data value in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DATA <dat>
        :TRIGger:IIC:DATA?

        **Description**

        Set the data value in IIC trigger when the trigger condition is Data
        or A&D.
        Query the current data value in IIC trigger when the trigger condition
        is Data or A&D.

        **Parameter**

        ====== ======== ============= =======
        Name   Type     Range         Default
        ====== ======== ============= =======
        <dat>  Integer  0 to 240 - 1  0
        ====== ======== ============= =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:IIC:DATA 64
        The query returns 64.
        """
        # TODO ... -1 check prog manual
        check_input(data_value, "data_value", int, 0, 239, "")
        self.instrument.ask(f":TRIGger:IIC:DATA {data_value}")

    def get_data(self) -> int:
        """Query the current data value in IIC.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DATA <dat>
        :TRIGger:IIC:DATA?

        **Description**

        Set the data value in IIC trigger when the trigger condition is Data
        or A&D.
        Query the current data value in IIC trigger when the trigger condition
        is Data or A&D.

        **Parameter**

        ====== ======== ============= =======
        Name   Type     Range         Default
        ====== ======== ============= =======
        <dat>  Integer  0 to 240 - 1  0
        ====== ======== ============= =======

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:IIC:DATA 64
        The query returns 64.
        """
        return int(self.instrument.ask(":TRIGger:IIC:DATA?"))

    def set_scl_trigger_level(self, level: float = 0) -> None:
        """Set the trigger level of SCL in IIC.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:CLEVel <level>
        :TRIGger:IIC:CLEVel?

        **Description**

        Set the trigger level of SCL in IIC trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SCL in IIC trigger.

        **Parameter**

        ======== ===== ================================= ========
        Name     Type  Range                             Default
        ======== ===== ================================= ========
        <level>  Real  ± 5 × VerticalScale from          0
                             the screen center - OFFSet
        ======== ===== ================================= ========

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:IIC:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        source = self.get_scl_source()
        if source == "channel 1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif source == "channel 2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??

        min_rng = -5 * scale - offset
        max_rng = 5 * scale - offset

        if not isinstance(level, float) or not min_rng <= level <= max_rng:
            ValueError(
                f'"level" must be of type float and between '
                f"{min_rng}..{max_rng}. You entered type {type(level)}."
            )

        self.instrument.ask(f":TRIGger:IIC:CLEVel {level}")

    def get_scl_trigger_level(self) -> float:
        """Query the current trigger level of SCL in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:CLEVel <level>
        :TRIGger:IIC:CLEVel?

        **Description**

        Set the trigger level of SCL in IIC trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SCL in IIC trigger.

        **Parameter**

        ======== ===== ================================= ========
        Name     Type  Range                             Default
        ======== ===== ================================= ========
        <level>  Real  ± 5 × VerticalScale from          0
                             the screen center - OFFSet
        ======== ===== ================================= ========

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:IIC:CLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:IIC:CLEVel?"))

    def set_sda_trigger_level(self, level: float = 0) -> None:
        """Set the trigger level of SDA in IIC trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DLEVel <level>
        :TRIGger:IIC:DLEVel?

        **Description**

        Set the trigger level of SDA in IIC trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SDA in IIC trigger.

        **Parameter**

        ======== ===== =========================== ========
        Name     Type  Range                       Default
        ======== ===== =========================== ========
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== ========

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:IIC:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        scale: float = -1.0
        offset: float = -1.0
        source = self.get_sda_source()
        if source == "channel 1":
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif source == "channel 2":
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??

        min_rng = -5 * scale - offset
        max_rng = 5 * scale - offset

        if not isinstance(level, float) or not min_rng <= level <= max_rng:
            ValueError(
                f'"level" must be of type float and between '
                f"{min_rng}..{max_rng}. You entered type {type(level)}."
            )

        self.instrument.ask(f":TRIGger:IIC:DLEVel {level}")

    def get_sda_trigger_level(self) -> float:
        """Query the current trigger level of SDA.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:IIC:DLEVel <level>
        :TRIGger:IIC:DLEVel?

        **Description**

        Set the trigger level of SDA in IIC trigger and the unit is the same
        with the current amplitude unit.
        Query the current trigger level of SDA in IIC trigger.

        **Parameter**

        ======== ===== =========================== ========
        Name     Type  Range                       Default
        ======== ===== =========================== ========
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== ========

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:IIC:DLEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:IIC:DLEVel?"))
