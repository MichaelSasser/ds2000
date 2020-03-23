#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019-2020  Michael Sasser <Michael@MichaelSasser.org>
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
    "Channel",
]


class Coupling(SubController):
    def ac(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:COUPling <coupling>
        :CHANnel<n>:COUPling?

        **Description**

        Set the coupling mode of CH1 or CH2 to AC, DC or GND.
        Query the current coupling mode of CH1 or CH2.

        **Parameter**

        =========== ========= ============= =======
        Name        Type      Range         Default
        =========== ========= ============= =======
        <n>         Discrete  {1|2}         --
        <coupling>  Discrete  {AC|DC|GND}   DC
        =========== ========= ============= =======

        **Return Format**

        The query returns AC, DC or GND.

        **Example**

        :CHANnel1:COUPling AC
        The query returns AC.

        """
        raise NotImplementedError()

    def dc(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:COUPling <coupling>
        :CHANnel<n>:COUPling?

        **Description**

        Set the coupling mode of CH1 or CH2 to AC, DC or GND.
        Query the current coupling mode of CH1 or CH2.

        **Parameter**

        =========== ========= ============= =======
        Name        Type      Range         Default
        =========== ========= ============= =======
        <n>         Discrete  {1|2}         --
        <coupling>  Discrete  {AC|DC|GND}   DC
        =========== ========= ============= =======

        **Return Format**

        The query returns AC, DC or GND.

        **Example**

        :CHANnel1:COUPling AC
        The query returns AC.

        """
        raise NotImplementedError()

    def gnd(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:COUPling <coupling>
        :CHANnel<n>:COUPling?

        **Description**

        Set the coupling mode of CH1 or CH2 to AC, DC or GND.
        Query the current coupling mode of CH1 or CH2.

        **Parameter**

        =========== ========= ============= =======
        Name        Type      Range         Default
        =========== ========= ============= =======
        <n>         Discrete  {1|2}         --
        <coupling>  Discrete  {AC|DC|GND}   DC
        =========== ========= ============= =======

        **Return Format**

        The query returns AC, DC or GND.

        **Example**

        :CHANnel1:COUPling AC
        The query returns AC.

        """
        raise NotImplementedError()


class Units(SubController):
    def voltage(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:UNITs <units>
        :CHANnel<n>:UNITs?

        **Description**

        Set the amplitude display unit of CH1 or CH2.
        Query the current amplitude display unit of the CH1 or CH2.

        **Parameter**

        ======== ========= ============================== =======
        Name     Type      Range                          Default
        ======== ========= ============================== =======
        <n>      Discrete  {1|2}                          --
        <units>  Discrete  {VOLTage|WATT|AMPere|UNKNown}  VOLTage
        ======== ========= ============================== =======

        **Return Format**

        The query returns VOLT, WATT, AMP or UNKN.

        **Example**

        :CHANnel1:UNITs VOLTage
        The query returns VOLT.

        """
        raise NotImplementedError()

    def power(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:UNITs <units>
        :CHANnel<n>:UNITs?

        **Description**

        Set the amplitude display unit of CH1 or CH2.
        Query the current amplitude display unit of the CH1 or CH2.

        **Parameter**

        ======== ========= ============================== =======
        Name     Type      Range                          Default
        ======== ========= ============================== =======
        <n>      Discrete  {1|2}                          --
        <units>  Discrete  {VOLTage|WATT|AMPere|UNKNown}  VOLTage
        ======== ========= ============================== =======

        **Return Format**

        The query returns VOLT, WATT, AMP or UNKN.

        **Example**

        :CHANnel1:UNITs VOLTage
        The query returns VOLT.

        """
        raise NotImplementedError()

    def current(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:UNITs <units>
        :CHANnel<n>:UNITs?

        **Description**

        Set the amplitude display unit of CH1 or CH2.
        Query the current amplitude display unit of the CH1 or CH2.

        **Parameter**

        ======== ========= ============================== =======
        Name     Type      Range                          Default
        ======== ========= ============================== =======
        <n>      Discrete  {1|2}                          --
        <units>  Discrete  {VOLTage|WATT|AMPere|UNKNown}  VOLTage
        ======== ========= ============================== =======

        **Return Format**

        The query returns VOLT, WATT, AMP or UNKN.

        **Example**

        :CHANnel1:UNITs VOLTage
        The query returns VOLT.

        """
        raise NotImplementedError()

    def unknown(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:UNITs <units>
        :CHANnel<n>:UNITs?

        **Description**

        Set the amplitude display unit of CH1 or CH2.
        Query the current amplitude display unit of the CH1 or CH2.

        **Parameter**

        ======== ========= ============================== =======
        Name     Type      Range                          Default
        ======== ========= ============================== =======
        <n>      Discrete  {1|2}                          --
        <units>  Discrete  {VOLTage|WATT|AMPere|UNKNown}  VOLTage
        ======== ========= ============================== =======

        **Return Format**

        The query returns VOLT, WATT, AMP or UNKN.

        **Example**

        :CHANnel1:UNITs VOLTage
        The query returns VOLT.

        """
        raise NotImplementedError()


class Channel(BaseController):
    def __init__(self, device, channel):
        super(Channel, self).__init__(device)
        self.__channel = channel
        self.coupling: Coupling = Coupling(self)
        self.units: Units = Units(self)

    def bandwidth_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:BWLimit <type>
        :CHANnel<n>:BWLimit?

        **Description**

        Set the bandwidth limit of CH1 or CH2 to 20M (20 MHz), 100M (100 MHz)
        or OFF (turn bandwidth limit off).
        Query the current bandwidth limit of CH1 or CH2.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <n>     Discrete  {1|2}           --
        <type>  Discrete  {20M|100M|OFF}  OFF
        ======= ========= =============== =======

        Note: for DS2072 and DS2012, the bandwidth limit can only be 20MHz.

        **Return Format**

        The query returns 20M, 100M or OFF.

        **Example**

        :CHANnel1:BWLimit 20M
        The query returns 20M.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:INVert <bool>
        :CHANnel<n>:INVert?

        **Description**

        Enable or disable the inverted display of CH1 or CH2.
        Query the current status of the inverted display of CH1 or CH2.

        **Parameter**

        ======= ========= ================= =======
        Name    Type      Range             Default
        ======= ========= ================= =======
        <n>     Discrete  {1|2}             --
        <bool>  Bool      {{0|OFF}|{1|ON}}  0|OFF
        ======= ========= ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :CHANnel1:INVert ON
        The query returns 1.
        """
        raise NotImplementedError()

    def offset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:OFFSet <offset>
        :CHANnel<n>:OFFSet?

        **Description**

        Set the vertical offset of the waveform of CH1 or CH2.
        Query the current vertical offset of the waveform of CH1 or CH2.

        **Parameter**

        ========= ========= ================================= =============
        Name      Type      Range                             Default
        ========= ========= ================================= =============
        <n>       Discrete  {1|2}                             --
        <offset>  Real      **500μV/div to 50mV/div**: ± 2V   CHANnel1: 2V
                            **51mV/div to 200mV/div**: ± 10V  CHANnel2: -2V
                            **205mV/div to 2V/div**: ± 50V
                            **2.05V/div to 10V/div**: ± 100V
        ========= ========= ================================= =============


        **Return Format**

        The query returns the vertical offset in scientific notation.

        **Example**

        :CHANnel1:OFFSet 0.01
        The query returns 1.000000e-02.
        """
        raise NotImplementedError()

    @property  # ToDo
    def scale(self) -> float:
        """
        **Rigol Programming Guide**

        :CHANnel<n>:SCALe

        **Syntax**

        :CHANnel<n>:SCALe <scale>

        :CHANnel<n>:SCALe?

        **Description**

        Set the vertical scale of the waveform of CH1 or CH2.
        Query the current vertical scale of the waveform of CH1 or CH2.

        **Parameter**

        ========= ========= ============== =======
        Name      Type      Range          Default
        ========= ========= ============== =======
        <n>       Discrete  {1|2}          --
        <scale>   Real      500μV to 10V   1V
        ========= ========= ============== =======

        Note: the range of the vertical scale is related to the probe ratio
        currently set. For the setting of the probe ratio, refer to the
        :CHANnel<n>:PROBe command.

        **Return Format**

        The query returns the vertical scale in scientific notation.

        **Example**

        :CHANnel1:SCALe 1

        The query returns 1.000000e+00.
        """
        return float(self.device.ask(f":CHANnel{self.__channel}:SCALe?"))

    def probe(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:PROBe

        **Syntax**

        :CHANnel<n>:PROBe <atten>
        :CHANnel<n>:PROBe?

        **Description**

        Set the probe attenuation ratio of CH1 or CH2.
        Query the probe attenuation ratio of CH1 or CH2.

        **Parameter**

        ======== ========= =================================== =======
        Name     Type      Range                               Default
        ======== ========= =================================== =======
        <n>      Discrete  {1|2}                               --
        <atten>  Discrete  {0.01|0.02|0.05|0.1|0.2|0.5|1|2|5|  1
                           10|20|50|100|200|500|1000}
        ======== ========= =================================== =======

        **Return Format**

        The query returns the attenuation ratio currently set.

        **Example**

        :CHANnel1:PROBe 10
        The query returns 10.

        """
        raise NotImplementedError()

    def fine_adjust(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:VERNier <bool>
        :CHANnel<n>:VERNier?

        **Description**

        Enable or disable the fine adjustment function of the vertical scale
        of CH1 or CH2.
        Query the current status of the fine adjustment function of the vertical
        scale of CH1 or CH2.

        **Parameter**

        ======= ========= ================ =======
        Name    Type      Range            Default
        ======= ========= ================ =======
        <n>     Discrete  {1|2}            --
        <bool>  Bool      {0|OFF}|{1|ON}}  0|OFF
        ======= ========= ================ =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :CHANnel1:VERNier ON
        The query returns 1.
        """
        raise NotImplementedError()
