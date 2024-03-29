#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018-2021  Michael Sasser <Michael@MichaelSasser.org>
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

from .common import Func
from .common import SFunc
from .common import SSFunc
from .common import check_input


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class TimebaseHorizontalRefMode(SSFunc):
    def set_center(self) -> None:
        """Set the horizontal reference mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:HREF:MODE <href>
        :TIMebase:HREF:MODE?

        **Description**

        Set the horizontal reference mode namely the reference position
        according to which the waveform expands and compresses horizontally.
        Query the current horizontal reference mode.

        **Parameter**

        ======= ========= ======================== =======
        Name    Type      Range                    Default
        ======= ========= ======================== =======
        <href>  Discrete  {CENTer,TPOSition,USER}  CENTer
        ======= ========= ======================== =======

        **Explanation**

        CENTer: the waveform expands or compresses horizontally around the
        center of the screen.
        TPOSition: the waveform expands or compresses horizontally around the
        trigger position.
        USER: the waveform expands or compresses horizontally around the
        user-defined reference position. Refer to the :TIMebase:HREF:POSition
        command.

        **Return Format**

        The query returns CENT, TPOS or USER.

        **Example**

        :TIMebase:HREF:MODE TPOSition
        The query returns TPOS.
        """
        self.instrument.say(":TIMebase:HREF:MODE CENTer")

    def set_trigger_position(self) -> None:
        """Set the horizontal reference mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:HREF:MODE <href>
        :TIMebase:HREF:MODE?

        **Description**

        Set the horizontal reference mode namely the reference position
        according to which the waveform expands and compresses horizontally.
        Query the current horizontal reference mode.

        **Parameter**

        ======= ========= ======================== =======
        Name    Type      Range                    Default
        ======= ========= ======================== =======
        <href>  Discrete  {CENTer,TPOSition,USER}  CENTer
        ======= ========= ======================== =======

        **Explanation**

        CENTer: the waveform expands or compresses horizontally around the
        center of the screen.
        TPOSition: the waveform expands or compresses horizontally around the
        trigger position.
        USER: the waveform expands or compresses horizontally around the
        user-defined reference position. Refer to the :TIMebase:HREF:POSition
        command.

        **Return Format**

        The query returns CENT, TPOS or USER.

        **Example**

        :TIMebase:HREF:MODE TPOSition
        The query returns TPOS.
        """

        self.instrument.say(":TIMebase:HREF:MODE CENTer")

    def status(self) -> str:
        """Query the current horizontal reference mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:HREF:MODE <href>
        :TIMebase:HREF:MODE?

        **Description**

        Set the horizontal reference mode namely the reference position
        according to which the waveform expands and compresses horizontally.
        Query the current horizontal reference mode.

        **Parameter**

        ======= ========= ======================== =======
        Name    Type      Range                    Default
        ======= ========= ======================== =======
        <href>  Discrete  {CENTer,TPOSition,USER}  CENTer
        ======= ========= ======================== =======

        **Explanation**

        CENTer: the waveform expands or compresses horizontally around the
        center of the screen.
        TPOSition: the waveform expands or compresses horizontally around the
        trigger position.
        USER: the waveform expands or compresses horizontally around the
        user-defined reference position. Refer to the :TIMebase:HREF:POSition
        command.

        **Return Format**

        The query returns CENT, TPOS or USER.

        **Example**

        :TIMebase:HREF:MODE TPOSition
        The query returns TPOS.
        """

        return self.instrument.ask(":TIMebase:HREF:MODE?")


class TimebaseHorizontalRef(SFunc):
    def __init__(self, device):
        super(TimebaseHorizontalRef, self).__init__(device)
        self.mode: TimebaseHorizontalRefMode = TimebaseHorizontalRefMode(self)

    # TODO: set_position() ?
    def get_position(self) -> int:
        """Query the current user-defined reference position.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:HREF:POSition <pos>
        :TIMebase:HREF:POSition?

        **Description**

        Set the user-defined reference position around which the waveform
        expands or compresses horizontally.
        Query the current user-defined reference position around which the
        waveform expands or compresses horizontally.

        **Parameter**

        ====== ======== ============ =======
        Name   Type     Range        Default
        ====== ======== ============ =======
        <pos>  Integer  -350 to 350  0
        ====== ======== ============ =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TIMebase:HREF:POSition 150
        The query returns 150.
        """
        return int(self.instrument.ask(":TIMebase:HREF:POSition?"))


class TimebaseDelay(SFunc):
    def set_enable(self) -> None:
        """Enable the delayed sweep.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:ENABle <bool>
        :TIMebase:DELay:ENABle?

        **Description**

        Enable or disable the delayed sweep.
        Query the current status of the delayed sweep.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:DELay:ENABle ON
        The query returns 1.

        """
        self.instrument.say(":TIMebase:DELay:ENABle 1")

    def set_disable(self) -> None:
        """Disable the delayed sweep.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:ENABle <bool>
        :TIMebase:DELay:ENABle?

        **Description**

        Enable or disable the delayed sweep.
        Query the current status of the delayed sweep.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:DELay:ENABle ON
        The query returns 1.

        """
        self.instrument.say(":TIMebase:DELay:ENABle 0")

    def status(self) -> bool:
        """Query the current status of the delayed sweep.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:ENABle <bool>
        :TIMebase:DELay:ENABle?

        **Description**

        Enable or disable the delayed sweep.
        Query the current status of the delayed sweep.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:DELay:ENABle ON
        The query returns 1.

        """
        return bool(int(self.instrument.ask(":TIMebase:DELay:ENABle?")))

    def set_offset(self, offset: float = 0) -> None:
        """Set the offset of the delayed time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:OFFSet <offset>
        :TIMebase:DELay:OFFSet?

        Description

        Set the offset of the delayed time base and the unit is s.
        Query the current offset of the delayed time base.

        Parameter

        ========= ===== ============================== =======
        Name      Type  Range                          Default
        ========= ===== ============================== =======
        <offset>  Real  -(LeftTime - DelayRange/2) to  0
                        (RightTime - DelayRange/2)
        ========= ===== ============================== =======

        .. note::
           LeftTime = 7×MainScale – MainOffset.
           For the MainScale, refer to the :TIMebase[:MAIN]:SCALe command.

           RightTime = 7×MainScale + MainOffset.
           For the MainOffset, refer to the :TIMebase[:MAIN]:OFFSet command.

           DelayRange = 14×DelayScale.
           For the DelayScale, refer to the :TIMebase:DELay:SCALe command.

        **Return Format**

        The query returns the offset in scientific notation.

        **Example**

        :TIMebase:DELay:OFFSet 0.000002
        The query returns 2.000000e-06.
        """
        main_scale: float = self.sdev.get_scale()
        main_offset: float = self.sdev.get_offset()
        delay_scale: float = self.get_scale()
        left_time: float = 7.0 * main_scale - main_offset
        right_time: float = 7.0 * main_scale + main_offset
        delay_range: float = 14.0 * delay_scale
        min_off: float = -(left_time - delay_range / 2)
        max_off: float = right_time - delay_range / 2
        if not isinstance(offset, float) or not min_off <= offset <= max_off:
            raise ValueError(
                f'In this configuration "offset" have to be '
                f"between: {min_off}..{max_off}. It also needs"
                f"to be of type float. You used: {type(offset)}."
            )
        self.instrument.say(f":TIMebase:DELay:OFFSet {offset}")

    def get_offset(self) -> float:
        """Query the current offset of the delayed time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:OFFSet <offset>
        :TIMebase:DELay:OFFSet?

        Description

        Set the offset of the delayed time base and the unit is s.
        Query the current offset of the delayed time base.

        Parameter

        ========= ===== ============================== =======
        Name      Type  Range                          Default
        ========= ===== ============================== =======
        <offset>  Real  -(LeftTime - DelayRange/2) to  0
                        (RightTime - DelayRange/2)
        ========= ===== ============================== =======

        .. note::
           LeftTime = 7×MainScale – MainOffset.
           For the MainScale, refer to the :TIMebase[:MAIN]:SCALe command.

           RightTime = 7×MainScale + MainOffset.
           For the MainOffset, refer to the :TIMebase[:MAIN]:OFFSet command.

           DelayRange = 14×DelayScale.
           For the DelayScale, refer to the :TIMebase:DELay:SCALe command.

        **Return Format**

        The query returns the offset in scientific notation.

        **Example**

        :TIMebase:DELay:OFFSet 0.000002
        The query returns 2.000000e-06.
        """
        return float(self.instrument.ask(":TIMebase:DELay:OFFSet?"))

    def set_scale(self, scale: float = 500.0e-9) -> None:
        """Set the scale of the delayed time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:SCALe <scale_value>
        :TIMebase:DELay:SCALe?

        **Description**

        Set the scale of the delayed time base and the unit is s/div.
        Query the current scale of the delayed time base.

        **Parameter**

        ============== ===== ================================== =======
        Name           Type  Range                              Default
        ============== ===== ================================== =======
        <scale_value>  Real  (1×50/real-time sample rate)×1/40  500ns
                             to the current MAIN SCALe
        ============== ===== ================================== =======

        Note: for the MAIN SCALe, refer to the :TIMebase[:MAIN]:SCALe command.

        **Return Format**

        The query returns the horizontal scale in scientific notation.

        **Example**

        :TIMebase:DELay:SCALe 0.00000005
        The query returns 5.000000e-08.
        """
        # ToDo: is this my unterstanding correct?
        sampl_rate: float = float(self.sdev.dev.acquire.get_samplerate())
        max_scale: float = self.sdev.get_scale()
        min_scale: float = 5 / (4 * sampl_rate)
        if (
            not isinstance(scale, float)
            and not min_scale >= scale >= max_scale
        ):
            ValueError(
                f"scale must be of type float and between the main "
                f"scale and (1×50/real-time sample rate)×1/40:"
                f"{min_scale}..{max_scale}."
            )
        self.instrument.say(f":TIMebase:DELay:SCALe {scale}")

    def get_scale(self) -> float:
        """Query the current scale of the delayed time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:DELay:SCALe <scale_value>
        :TIMebase:DELay:SCALe?

        **Description**

        Set the scale of the delayed time base and the unit is s/div.
        Query the current scale of the delayed time base.

        **Parameter**

        ============== ===== ================================== =======
        Name           Type  Range                              Default
        ============== ===== ================================== =======
        <scale_value>  Real  (1×50/real-time sample rate)×1/40  500ns
                             to the current MAIN SCALe
        ============== ===== ================================== =======

        Note: for the MAIN SCALe, refer to the :TIMebase[:MAIN]:SCALe command.

        **Return Format**

        The query returns the horizontal scale in scientific notation.

        **Example**

        :TIMebase:DELay:SCALe 0.00000005
        The query returns 5.000000e-08.
        """
        return float(self.instrument.ask(":TIMebase:DELay:SCALe?"))

    def set_position(self, pos: int = 0) -> None:
        """Set the user-defined reference position.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:HREF:POSition <pos>
        :TIMebase:HREF:POSition?

        **Description**

        Set the user-defined reference position around which the waveform
        expands or compresses horizontally.
        Query the current user-defined reference position around which the
        waveform expands or compresses horizontally.

        **Parameter**

        ====== ======== ============ =======
        Name   Type     Range        Default
        ====== ======== ============ =======
        <pos>  Integer  -350 to 350  0
        ====== ======== ============ =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TIMebase:HREF:POSition 150
        The query returns 150.
        """
        check_input(pos, "pos", int, -350, 350)
        self.instrument.say(":TIMebase:HREF:MODE USER")
        self.instrument.say(f":TIMebase:HREF:POSition {pos}")


class TimebaseMode(SFunc):
    def set_main(self) -> None:
        """Set the horizontal time base mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:MODE <mode>
        :TIMebase:MODE?

        **Description**

        Set the horizontal time base mode.
        Query the current horizontal time base mode.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <mode>  Discrete  {MAIN,XY,ROLL}  MAIN
        ======= ========= =============== =======

        **Return Format**

        The query returns MAIN, XY or ROLL.

        **Example**

        :TIMebase:MODE MAIN
        The query returns MAIN.
        """
        self.instrument.say(":TIMebase:MODE MAIN")

    def set_xy(self) -> None:
        """Set the horizontal time base mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:MODE <mode>
        :TIMebase:MODE?

        **Description**

        Set the horizontal time base mode.
        Query the current horizontal time base mode.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <mode>  Discrete  {MAIN,XY,ROLL}  MAIN
        ======= ========= =============== =======

        **Return Format**

        The query returns MAIN, XY or ROLL.

        **Example**

        :TIMebase:MODE MAIN
        The query returns MAIN.
        """
        self.instrument.say(":TIMebase:MODE XY")

    def set_roll(self) -> None:
        """Set the horizontal time base mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:MODE <mode>
        :TIMebase:MODE?

        **Description**

        Set the horizontal time base mode.
        Query the current horizontal time base mode.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <mode>  Discrete  {MAIN,XY,ROLL}  MAIN
        ======= ========= =============== =======

        **Return Format**

        The query returns MAIN, XY or ROLL.

        **Example**

        :TIMebase:MODE MAIN
        The query returns MAIN.
        """
        self.instrument.say(":TIMebase:MODE ROLL")

    def status(self) -> str:
        """Query the current horizontal time base mode.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:MODE <mode>
        :TIMebase:MODE?

        **Description**

        Set the horizontal time base mode.
        Query the current horizontal time base mode.

        **Parameter**

        ======= ========= =============== =======
        Name    Type      Range           Default
        ======= ========= =============== =======
        <mode>  Discrete  {MAIN,XY,ROLL}  MAIN
        ======= ========= =============== =======

        **Return Format**

        The query returns MAIN, XY or ROLL.

        **Example**

        :TIMebase:MODE MAIN
        The query returns MAIN.
        """
        return self.instrument.ask(":TIMebase:MODE?").lower()


class Timebase(Func):
    def __init__(self, dev):
        super(Timebase, self).__init__(dev)
        self.delay: TimebaseDelay = TimebaseDelay(self)
        self.horizontal_ref: TimebaseHorizontalRef = TimebaseHorizontalRef(
            self
        )
        self.mode: TimebaseMode = TimebaseMode(self)

    def set_offset(self, seconds: int = 0) -> None:
        """Set the offset of the main time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase[:MAIN]:OFFSet <offset>
        :TIMebase[:MAIN]:OFFSet?

        **Description**

        Set the offset of the main time base and the unit is s.
        Query the current offset of the main time base.

        **Parameter**

        ========= ===== ======================================= =======
        Name      Type  Range                                   Default
        ========= ===== ======================================= =======
        <offset>  Real  **RUN**: -MemDepth/SamplingRate to 1s   0
                        (when the TimeScale is less than 20ms)
                        -MemDepth/SamplingRate to 10×TimeScale
                        (when the TimeScale is greater than or
                        equal to 20ms)
                        **STOP**: -7000s to 7000s
                        **ROLL RUN**: not avaliable
                        **ROLL STOP**: -7000s to 0
        ========= ===== ======================================= =======

        .. note::
           For the MemDepth, refer to the :ACQuire:MDEPth command.

           For the SamplingRate, refer to the :ACQuire:SRATe? command.

           For the TimeScale, refer to the :TIMebase[:MAIN]:SCALe command.

        **Return Format**

        The query returns the offset in the scientific notation.

        **Example**

        :TIMebase:MAIN:OFFSet 0.0002
        The query returns 2.000000e-04.
        """
        check_input(seconds, "seconds", int)

        trigger: str = self.dev.trigger.status()
        mode: str = self.mode.status()

        # Checks, if the entered value is legal.
        if trigger == "run":
            if mode == "ROLL":
                raise RuntimeError(
                    "You need to be in STOP mode. to perform " "this action!"
                )
            mem_depth: float = float(self.dev.acquire.get_memorydepth())
            sampl_rate: float = float(self.dev.acquire.get_samplerate())
            time_scale: float = self.get_scale()
            min_offset: float = -mem_depth / sampl_rate
            if time_scale < 20.0e-3 and not (min_offset <= seconds <= 1.0):
                raise ValueError(
                    f'"seconds" in "{trigger.upper()}" '
                    f"mode must be between "
                    f"-MemDepth/SamplingRate .. 1.0.\n "
                    f"MemDepth := {mem_depth}\n"
                    f"SamplingRate := {sampl_rate}\n"
                    f"-MemDepth/SamplingRate = {min_offset}\n"
                    f"This means your limits are "
                    f"{min_offset}..1"
                )
            elif time_scale >= 20.0e-3 and not (
                min_offset <= seconds <= 10.0 * time_scale
            ):
                raise ValueError(
                    f'"seconds" in "{trigger.upper()}" '
                    f"mode must be between "
                    f"-MemDepth/SamplingRate .. 10.0*TimeScale.\n "
                    f"MemDepth := {mem_depth}\n"
                    f"SamplingRate := {sampl_rate}\n"
                    f"-MemDepth/SamplingRate = {min_offset}\n"
                    f"TimeScale := {time_scale}\n"
                    f"TimeScale * 10 = {10 * time_scale}\n"
                    f"This means your limits are "
                    f"{min_offset}..{10 * time_scale}"
                )

        elif trigger == "stop":
            if mode == "ROLL" and not (-7000.0 <= seconds <= 0):
                raise ValueError(
                    f'"seconds" in "{trigger.upper()}" '
                    f"+ {mode.upper()} mode must be between "
                    "-7000.0 .. 0.0."
                )

            elif not (-7000.0 <= seconds <= 7000):
                raise ValueError(
                    f'"seconds" in "{trigger.upper()}" '
                    f"mode must be between -7000.0 .. 7000.0."
                )

        self.instrument.say(f":TIMebase:MAIN:OFFSet {seconds}")

    def get_offset(self) -> int:
        """Query the current offset of the main time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase[:MAIN]:OFFSet <offset>
        :TIMebase[:MAIN]:OFFSet?

        **Description**

        Set the offset of the main time base and the unit is s.
        Query the current offset of the main time base.

        **Parameter**

        ========= ===== ======================================= =======
        Name      Type  Range                                   Default
        ========= ===== ======================================= =======
        <offset>  Real  **RUN**: -MemDepth/SamplingRate to 1s   0
                        (when the TimeScale is less than 20ms)
                        -MemDepth/SamplingRate to 10×TimeScale
                        (when the TimeScale is greater than or
                        equal to 20ms)
                        **STOP**: -7000s to 7000s
                        **ROLL RUN**: not avaliable
                        **ROLL STOP**: -7000s to 0
        ========= ===== ======================================= =======

        .. note::
           For the MemDepth, refer to the :ACQuire:MDEPth command.

           For the SamplingRate, refer to the :ACQuire:SRATe? command.

           For the TimeScale, refer to the :TIMebase[:MAIN]:SCALe command.

        **Return Format**

        The query returns the offset in the scientific notation.

        **Example**

        :TIMebase:MAIN:OFFSet 0.0002
        The query returns 2.000000e-04.
        """
        return int(self.instrument.ask(":TIMebase[:MAIN]:OFFSet?"))

    def set_scale(self, seconds: float = 1.0e-6) -> float:
        """Set the scale of the main time base and the unit is s/div.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase[:MAIN]:SCALe <scale_value>

        :TIMebase[:MAIN]:SCALe?

        **Description**

        Set the scale of the main time base and the unit is s/div.
        Query the current scale of the main time base.

        =============== ======= ======================= =======
        Name            Type    Range                   Default
        =============== ======= ======================= =======
        <scale_value>   Real    Depend on the time      1μs
                                base mode [1]:
                                **Normal**: 2ns[2] to
                                1ks
                                **ROLL**: 200ms to
                                1ks
        =============== ======= ======================= =======

        .. note::
           [1]: refer to the :TIMebase:MODE command.

           [2]: this value is different for different model. For DS2072 and
           DS2012, the value is 5 ns.

        **Return Format**

        The query returns the current scale of the main time base in
        scientific notation.

        **Example**

        :TIMebase:MAIN:SCALe 0.0002

        The query returns 2.000000e-04.
        """
        # ToDo: MinMax dependend on model
        # TODO: Need to enable fine_adjustment before?
        check_input(seconds, "seconds", int, 2.0e-9, 1000.0, "s")
        return float(self.instrument.ask(f":TIMebase:MAIN:SCALe {seconds}"))

    def get_scale(self) -> float:
        """Query the current scale of the main time base.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase[:MAIN]:SCALe <scale_value>

        :TIMebase[:MAIN]:SCALe?

        **Description**

        Set the scale of the main time base and the unit is s/div.
        Query the current scale of the main time base.

        =============== ======= ======================= =======
        Name            Type    Range                   Default
        =============== ======= ======================= =======
        <scale_value>   Real    Depend on the time      1μs
                                base mode [1]:
                                **Normal**: 2ns[2] to
                                1ks
                                **ROLL**: 200ms to
                                1ks
        =============== ======= ======================= =======

        Note[1]: refer to the :TIMebase:MODE command.

        Note[2]: this value is different for different model. For DS2072 and
        DS2012, the value is 5 ns.

        **Return Format**

        The query returns the current scale of the main time base in
        scientific notation.

        **Example**

        :TIMebase:MAIN:SCALe 0.0002

        The query returns 2.000000e-04.
        """
        return float(self.instrument.ask(":TIMebase:MAIN:SCALe?"))

    def enable_fine_adjustment(self) -> None:
        """Enable the fine adjustment of the horizontal scale.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:VERNier <bool>
        :TIMebase:VERNier?

        **Description**

        Enable or disable the fine adjustment of the horizontal scale.
        Query the current status of the fine adjustment of the horizontal
        scale.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:VERNier ON
        The query returns 1.
        """
        self.instrument.say(":TIMebase:VERNier 1")

    def disable_fine_adjustment(self) -> None:
        """Disable the fine adjustment of the horizontal scale.

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:VERNier <bool>
        :TIMebase:VERNier?

        **Description**

        Enable or disable the fine adjustment of the horizontal scale.
        Query the current status of the fine adjustment of the horizontal
        scale.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:VERNier ON
        The query returns 1.
        """
        self.instrument.say(":TIMebase:VERNier 0")

    def is_fine_adjustment_enabled(self) -> bool:
        """Query the current status of the fine adjustment (horizontal).

        **Rigol Programming Guide**

        **Syntax**

        :TIMebase:VERNier <bool>
        :TIMebase:VERNier?

        **Description**

        Enable or disable the fine adjustment of the horizontal scale.
        Query the current status of the fine adjustment of the horizontal
        scale.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0,OFF},{1,ON}}  0,OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:VERNier ON
        The query returns 1.
        """
        return bool(int(self.instrument.ask(":TIMebase:VERNier 1")))
