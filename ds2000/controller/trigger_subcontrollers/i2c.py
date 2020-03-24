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
    "I2c",
]


class I2cWhen(SubSubController):
    def start(self):
        """
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
        raise NotImplementedError()

    def restart(self):
        """
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
        raise NotImplementedError()

    def stop(self):
        """
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
        raise NotImplementedError()

    def nack(self):
        """
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
        raise NotImplementedError()

    def address(self):
        """
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
        raise NotImplementedError()

    def data(self):
        """
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
        raise NotImplementedError()

    def address_and_data(self):
        """
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
        raise NotImplementedError()


class I2cDirection(SubSubController):
    def read(self):
        """
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
        <dir>  Discrete  {READ|WRITe|RWRite}  READ

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        raise NotImplementedError()

    def write(self):
        """
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
        <dir>  Discrete  {READ|WRITe|RWRite}  READ

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        raise NotImplementedError()

    def read_write(self):
        """
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
        <dir>  Discrete  {READ|WRITe|RWRite}  READ

        **Explanation**

        To set the IIC trigger condition, refer to the :TRIGger:IIC:WHEN
        command.

        **Return Format**

        The query returns READ, WRIT or RWR.

        **Example**

        :TRIGger:IIC:DIRection RWRite
        The query returns RWR.
        """
        raise NotImplementedError()


class I2c(SubController):
    def __init__(self, device):
        super(I2c, self).__init__(device)
        self.when: I2cWhen = I2cWhen(self)
        self.direction: I2cDirection = I2cDirection(self)

    def scl_source(self):
        """
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
        raise NotImplementedError()

    def sda_source(self):
        """
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
        raise NotImplementedError()

    def address_bits_width(self):
        """
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
        raise NotImplementedError()

    def address(self):
        """
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
        raise NotImplementedError()

    def data(self):
        """
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
        raise NotImplementedError()

    def scl_trigger_level(self):
        """
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
        raise NotImplementedError()

    def sda_trigger_level(self):
        """
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
        raise NotImplementedError()
