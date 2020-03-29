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
from typing import Optional, Tuple, NamedTuple, List

from ds2000.controller import BaseController, SubController, Ds2000Exception
from ds2000.math import get_prefix, Prefixed

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = [
    "Channel",
]


class ChannelOffsetRange(NamedTuple):
    """
    A structure to get get a iterable to check a entered offset against
    the ranges defined below.
    """
    min_scl: float  # minimal scale
    max_scl: float  # maximal scale
    off: float  # minimal offset: -off; maximal offset: off


class ChannelCoupling(SubController):
    def ac(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:COUPling AC")

    def dc(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:COUPling DC")

    def gnd(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:COUPling GND")

    def status(self) -> str:
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
        return self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:COUPling?").lower()


class ChannelUnits(SubController):
    def voltage(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}::UNITs VOLTage")

    def power(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}::UNITs WATT")

    def current(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}::UNITs AMPere")

    def unknown(self) -> None:
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}::UNITs UNKNown")

    def status(self) -> str:
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
        unit: str = self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}::UNITs?")
        if unit == "VOLT":
            return "voltage"
        if unit == "WATT":
            return "power"
        if unit == "AMP":
            return "current"
        if unit == "UNKN":
            return "unknown"
        Ds2000Exception("The channel unit couldn't be recognized.")


class ChannelBandwidthLimit(SubController):
    def off(self):
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:BWLimit OFF")

    def bw_20m(self):
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:BWLimit 20M")

    def bw_100m(self):  # ToDo: not for DS2072 & DS2012
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:BWLimit 100M")

    def status(self):
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
        self.subdevice.device.ask(
                f":CHANnel{self.subdevice.__channel}:BWLimit?")


class Channel(BaseController):
    OFFSET_RANGES: Tuple[ChannelOffsetRange, ...] = (
        ChannelOffsetRange(500.E-6, 50.E-3, 2),
        ChannelOffsetRange(51.E-3, 200.E-3, 10),
        ChannelOffsetRange(205.E-3, 2, 50),
        ChannelOffsetRange(2.05, 10, 100),
    )
    PROBE_ATTENUATION_RATIOS: Tuple[float, ...] = (
        0.01,
        0.02,
        0.05,
        0.1,
        0.2,
        0.5,
        1.0,
        2.0,
        5.0,
        1.0,
        10.0,
        20.0,
        50.0,
        100.0,
        200.0,
        500.0,
        1000.0,
    )

    def __init__(self, device, channel):
        super(Channel, self).__init__(device)

        self.__channel = channel

        self.coupling: ChannelCoupling = ChannelCoupling(self)
        self.units: ChannelUnits = ChannelUnits(self)
        self.bandwidth_limit: ChannelBandwidthLimit = ChannelBandwidthLimit(
                self)

    def get_invert(self) -> bool:
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
        return bool(int(self.device.ask(f":CHANnel{self.__channel}:INVert?")))

    def set_invert(self, enable: bool = False) -> None:
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
        if not isinstance(enable, bool):
            raise ValueError("\"enable\" must be of type \"bool\". You entered"
                             f"{type(enable)}.")
        self.device.ask(f":CHANnel{self.__channel}:INVert {int(enable)}")

    @staticmethod
    def __offset_check_range(rge: ChannelOffsetRange,
                             scale: float,
                             offset: float,
                             ratio: float) -> bool:
        """This function checks if the entered offset was within the possible
        scale range. If not, a detailed error will show the user, What the
        limits are.

        scl means scale
        off means offset

        The "Prefixed" object gives a output like 100mV insted of 0.1V.
        Note: The offset range is always ± nV, so the minumum is -nV
        and the maximum is +nV.

        :param rge: one of the  __class__.OFFSET_RANGES objects
        :param scale: The current channel scale
        :param offset: The requested offset.
        :return: - True, if the scale range was correct and the offset was
                   valid.
                 - False, if the scale range was incorrect.

        """
        min_scl_p: Prefixed = get_prefix(rge.min_scl*ratio)
        scl_p: Prefixed = get_prefix(scale)  # ratio comes from scope
        max_scl_p: Prefixed = get_prefix(rge.max_scl*ratio)
        off_p: Prefixed = get_prefix(rge.off*ratio)
        offset_p: Prefixed = get_prefix(offset)

        if rge.min_scl*ratio <= scale <= rge.max_scl*ratio:
            if -rge.off*ratio <= offset <= rge.off*ratio:
                return True  # The range and requested offset is correct.
            else:
                ValueError(f"If your scale is between "
                           f"{min_scl_p.value}{min_scl_p.prefix}V/div and "
                           f"{max_scl_p.value}{max_scl_p.prefix}V/div "
                           f"the offset must be between "
                           f"-{off_p.value}{off_p.prefix}V and "
                           f"{off_p.value}{off_p.prefix}V.\n"
                           f"Your scale is currently set to "
                           f"{scl_p.value}{scl_p.prefix}V/div.\n"
                           f"Your requestet offset is "
                           f"{offset_p.value}{offset_p.prefix}V.\n"
                           f"Make sure your offset is between "
                           f"-{off_p.value}{off_p.prefix}V "
                           f"and {off_p.value}{off_p.prefix}V or change your "
                           f"scale.\n"
                           "Keep in mind, the range of the vertical scale "
                           "is related to the probe attenuation ratio "
                           "currently set.")
        return False  # This was not the correct range

    def get_offset(self) -> float:
        """

        :offset: - Set to None to get the default value. (Default)
                 - Enter a floating point value to set the offset by yourselt.

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
        return float(self.device.ask(f":CHANnel{self.__channel}:OFFSet?"))

    def set_offset(self, offset: Optional[float] = None) -> None:
        """

        :offset: - Set to None to get the default value. (Default)
                 - Enter a floating point value to set the offset by yourselt.

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
        ratio: float = self.get_probe_attenuation_ratio()  # Probe att. ratio
        if offset is None:
            default: float = 2.0*ratio if self.__channel == 1 else -2.0*ratio
            self.device.ask(f":CHANnel{self.__channel}:OFFSet {default}")
            return

        # if offset is of type float, generate the boundaries
        if isinstance(offset, float):
            scale: float = self.get_scale()  # the channel scale in V/DIV

            # Check ranges and set the offset, if offset is in the boundaries
            # of scale.
            for r in self.__class__.OFFSET_RANGES:
                if self.__offset_check_range(r, scale, offset, ratio):
                    self.device.ask(f":CHANnel{self.__channel}:OFFSet {offset}")
                    return

            # Anything between or none of that. Generate and throw an error.
            err = ["The offset depends on the \"scale\" range:"]
            for r in self.__class__.OFFSET_RANGES:
                min_scl_p: Prefixed = get_prefix(r.min_scl*ratio)
                max_scl_p: Prefixed = get_prefix(r.max_scl*ratio)
                off_p: Prefixed = get_prefix(r.off*ratio)
                err.append(f"A scale from {min_scl_p.value}{min_scl_p.prefix}"
                           f"V/div to {max_scl_p.value}{max_scl_p.prefix}V/div "
                           f"results in an offset range of "
                           f"-{off_p.value}{off_p.prefix}V to "
                           f"{off_p.value}{off_p.prefix}V.")
            err.append("Please make sure, your are in this boundaries.")
            raise ValueError("\n".join(err))

        else:
            raise ValueError("\"offset\" must be of type float. You enterd "
                             f"{type(offset)}.")

    def get_scale(self) -> float:
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

    def set_scale(self, scale: float = 1) -> None:
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
        ratio: float = self.get_probe_attenuation_ratio()
        if (not isinstance(scale, float)
                or not (500.E-6*ratio <= scale <= 10*ratio)):
            ValueError(f"The scale must be within {500*ratio}μV..{10*ratio}V "
                       f"and of type float. You entered the type: "
                       f"{type(scale)}. Remember, this values depend on the"
                       f"probe attenuation ratio.")
        float(self.device.ask(f":CHANnel{self.__channel}:SCALe {scale}"))

    def get_probe_attenuation_ratio(self) -> float:
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
        return float(self.device.ask(f":CHANnel{self.__channel}:PROBe?"))

    def set_probe_attenuation_ratio(self, ratio: float = 1) -> None:
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
        if (not isinstance(ratio, float)
           or ratio not in self.__class__.PROBE_ATTENUATION_RATIOS):
            lst: List[str, ...]
            lst = [str(s) for s in self.__class__.PROBE_ATTENUATION_RATIOS]
            ValueError(f"\"ratio\" must be one of: "
                       f"{', '.join(lst)} and of type float. You entered "
                       f"{type(ratio)}.")
        self.device.ask(f":CHANnel{self.__channel}:PROBe {ratio}")

    def get_fine_adjust(self) -> bool:
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
        return bool(int(self.device.ask(f":CHANnel{self.__channel}:VERNier?")))

    def set_fine_adjust(self, enabled: bool = False) -> None:
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
        self.device.ask(f":CHANnel{self.__channel}:VERNier {int(enabled)}")
