#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019-2021  Michael Sasser <Michael@MichaelSasser.org>
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
from __future__ import annotations

from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Tuple

from .common import Func
from .common import SFunc
from .common import check_input
from .errors import DS2000Error
from .math.format import Prefixed
from .math.format import get_prefix


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class ChannelOffsetRange(NamedTuple):
    """
    A structure to get get a iterable to check a entered offset against
    the ranges defined below.
    """

    min_scl: float  # minimal scale
    max_scl: float  # maximal scale
    off: float  # minimal offset: -off; maximal offset: off


class ChannelCoupling(SFunc):
    def set_ac(self) -> None:
        """Set the coupling mode.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:COUPling AC")

    def set_dc(self) -> None:
        """Set the coupling mode.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:COUPling DC")

    def set_gnd(self) -> None:
        """Set the coupling mode.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:COUPling GND")

    def status(self) -> str:
        """Query the current coupling mode of CH1 or CH2.

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
        return self.instrument.ask(
            f":CHANnel{self.sdev._channel}:COUPling?"
        ).lower()


class ChannelUnits(SFunc):
    def set_voltage(self) -> None:
        """Set the amplitude display.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}::UNITs VOLTage")

    def set_power(self) -> None:
        """Set the amplitude display.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}::UNITs WATT")

    def set_current(self) -> None:
        """Set the amplitude display.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}::UNITs AMPere")

    def set_unknown(self) -> None:
        """Set the amplitude display.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}::UNITs UNKNown")

    def status(self) -> str:
        """Query the current amplitude display unit.

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
        unit: str = self.instrument.ask(
            f":CHANnel{self.sdev._channel}::UNITs?"
        )
        if unit == "VOLT":
            return "voltage"
        if unit == "WATT":
            return "power"
        if unit == "AMP":
            return "current"
        if unit == "UNKN":
            return "unknown"
        DS2000Error("The channel unit couldn't be recognized.")


class ChannelBandwidthLimit(SFunc):
    def set_off(self):
        """Set the bandwidth limit.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:BWLimit OFF")

    def set_bw_20m(self):
        """Set the bandwidth limit.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:BWLimit 20M")

    def set_bw_100m(self):  # ToDo: not for DS2072 & DS2012
        """Set the bandwidth limit.

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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:BWLimit 100M")

    def status(self):
        """Query the current bandwidth limit.
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
        self.instrument.ask(f":CHANnel{self.sdev._channel}:BWLimit?")


class Channel(Func):
    OFFSET_RANGES: Tuple[ChannelOffsetRange, ...] = (
        ChannelOffsetRange(500.0e-6, 50.0e-3, 2),
        ChannelOffsetRange(51.0e-3, 200.0e-3, 10),
        ChannelOffsetRange(205.0e-3, 2, 50),
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

    def __init__(self, dev, channel):
        super(Channel, self).__init__(dev)

        self._channel = channel

        self.coupling: ChannelCoupling = ChannelCoupling(self)
        self.units: ChannelUnits = ChannelUnits(self)
        self.bandwidth_limit: ChannelBandwidthLimit = ChannelBandwidthLimit(
            self
        )

    def set_enable_invert(self) -> None:
        """Enable the inverted display.

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
        self.instrument.ask(f":CHANnel{self._channel}:INVert 1")

    def set_disable_invert(self) -> None:
        """Disable the inverted display.

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
        self.instrument.ask(f":CHANnel{self._channel}:INVert 0")

    def get_invert(self) -> bool:
        """Query the current status of the inverted display.

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
        return bool(
            int(self.instrument.ask(f":CHANnel{self._channel}:INVert?"))
        )

    @staticmethod
    def __offset_check_range(
        rge: ChannelOffsetRange, scale: float, offset: float, ratio: float
    ) -> bool:
        """Checks if the entered offset was within the possible scale range.

        If not, a detailed error will show the user, What the limits are.

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
        min_scl_p: Prefixed = get_prefix(rge.min_scl * ratio)
        scl_p: Prefixed = get_prefix(scale)  # ratio comes from scope
        max_scl_p: Prefixed = get_prefix(rge.max_scl * ratio)
        off_p: Prefixed = get_prefix(rge.off * ratio)
        offset_p: Prefixed = get_prefix(offset)

        if rge.min_scl * ratio <= scale <= rge.max_scl * ratio:
            if -rge.off * ratio <= offset <= rge.off * ratio:
                return True  # The range and requested offset is correct.
            else:
                ValueError(
                    "If your scale is between "
                    f"{min_scl_p.formatted}V/div and "
                    f"{max_scl_p.formatted}V/div "
                    "the offset must be between "
                    f"-{off_p.formatted}V and "
                    f"{off_p.formatted}V.\n"
                    "Your scale is currently set to "
                    f"{scl_p.formatted}V/div.\n"
                    "Your requestet offset is "
                    f"{offset_p.formatted}V.\n"
                    "Make sure your offset is between "
                    f"-{off_p.formatted}V "
                    f"and {off_p.formatted}V or change your "
                    "scale.\n"
                    "Keep in mind, the range of the vertical scale "
                    "is related to the probe attenuation ratio "
                    "currently set."
                )
        return False  # This was not the correct range

    def set_offset(self, offset: Optional[float] = None) -> None:
        """Set the vertical offset of the waveform.

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
            default: float = (
                2.0 * ratio if self._channel == 1 else -2.0 * ratio
            )
            self.instrument.ask(f":CHANnel{self._channel}:OFFSet {default}")
            return

        # if offset is of type float, generate the boundaries
        if isinstance(offset, float):
            scale: float = self.get_scale()  # the channel scale in V/DIV

            # Check ranges and set the offset, if offset is in the boundaries
            # of scale.
            for r in self.__class__.OFFSET_RANGES:
                if self.__offset_check_range(r, scale, offset, ratio):
                    self.instrument.ask(
                        f":CHANnel{self._channel}:OFFSet {offset}"
                    )
                    return

            # Anything between or none of that. Generate and throw an error.
            err = ['The offset depends on the "scale" range:']
            for r in self.__class__.OFFSET_RANGES:
                min_scl_p: Prefixed = get_prefix(r.min_scl * ratio)
                max_scl_p: Prefixed = get_prefix(r.max_scl * ratio)
                off_p: Prefixed = get_prefix(r.off * ratio)
                err.append(
                    f"A scale from {min_scl_p.formatted}"
                    f"V/div to {max_scl_p.formatted}V/div "
                    f"results in an offset range of "
                    f"-{off_p.formatted}V to "
                    f"{off_p.formatted}V."
                )
            err.append("Please make sure, your are in this boundaries.")
            raise ValueError("\n".join(err))

        else:
            raise ValueError(
                '"offset" must be of type float. You enterd '
                f"{type(offset)}."
            )

    def get_offset(self) -> float:
        """Query the current vertical offset of the waveform.

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
        return float(self.instrument.ask(f":CHANnel{self._channel}:OFFSet?"))

    def set_scale(self, scale: float = 1.0) -> None:
        """Set the vertical scale of the waveform.

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
        check_input(
            scale,
            "scale",
            float,
            500.0e-6 * ratio,
            10.0 * ratio,
            "V",
            ext_range_err=(
                "Remember, this values depend on the "
                "probe attenuation ratio."
            ),
            )
        float(self.instrument.ask(f":CHANnel{self._channel}:SCALe {scale}"))

    def get_scale(self) -> float:
        """Query the current vertical scale of the waveform.

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
        return float(self.instrument.ask(f":CHANnel{self._channel}:SCALe?"))

    def set_probe_attenuation_ratio(self, ratio: float = 1) -> None:
        """Set the probe attenuation ratio.

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
        if (
                not isinstance(ratio, float)
                or ratio not in self.__class__.PROBE_ATTENUATION_RATIOS
        ):
            lst: List[str, ...]
            lst = [str(s) for s in self.__class__.PROBE_ATTENUATION_RATIOS]
            ValueError(
                f'"ratio" must be one of: '
                f"{', '.join(lst)} and of type float. You entered "
                f"{type(ratio)}."
            )
        self.instrument.ask(f":CHANnel{self._channel}:PROBe {ratio}")

    def get_probe_attenuation_ratio(self) -> float:
        """Query the probe attenuation ratio.

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
        return float(self.instrument.ask(f":CHANnel{self._channel}:PROBe?"))

    def set_fine_adjust(self, enabled: bool = False) -> None:
        """Set the current status of the fine adjustment function (vertival).
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:VERNier <bool>
        :CHANnel<n>:VERNier?

        **Description**

        Enable or disable the fine adjustment function of the vertical scale
        of CH1 or CH2.
        Query the current status of the fine adjustment function of the
        vertical scale of CH1 or CH2.

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
        self.instrument.ask(f":CHANnel{self._channel}:VERNier {int(enabled)}")

    def get_fine_adjust(self) -> bool:
        """Query the current status of the fine adjustment function (vertival).
        **Rigol Programming Guide**

        **Syntax**

        :CHANnel<n>:VERNier <bool>
        :CHANnel<n>:VERNier?

        **Description**

        Enable or disable the fine adjustment function of the vertical scale
        of CH1 or CH2.
        Query the current status of the fine adjustment function of the
        vertical scale of CH1 or CH2.

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
        return bool(
            int(self.instrument.ask(f":CHANnel{self._channel}:VERNier?"))
        )