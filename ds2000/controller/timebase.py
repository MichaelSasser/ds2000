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

from ds2000.controller import BaseController, SubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Timebase",
]


class Delay(SubController):
    def enable(self):
        """
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
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:DELay:ENABle ON
        The query returns 1.

        """
        raise NotImplementedError()

    def offset(self):
        """
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

        Note:
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
        raise NotImplementedError()

    def scale(self):
        """
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
        raise NotImplementedError()


class HorizontalRef(SubController):
    def mode(self):
        """
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
        <href>  Discrete  {CENTer|TPOSition|USER}  CENTer
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
        raise NotImplementedError()

    def position(self):
        """
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
        raise NotImplementedError()


class Timebase(BaseController):
    def __init__(self, device, channel):
        super(Timebase, self).__init__(device)
        self.__channel = channel
        self.delay: Delay = Delay(self)
        self.horizontal_ref: HorizontalRef = HorizontalRef(self)

    def offset(self):
        """
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

        Note:
        For the MemDepth, refer to the :ACQuire:MDEPth command.
        For the SamplingRate, refer to the :ACQuire:SRATe? command.
        For the TimeScale, refer to the :TIMebase[:MAIN]:SCALe command.

        **Return Format**

        The query returns the offset in the scientific notation.

        **Example**

        :TIMebase:MAIN:OFFSet 0.0002
        The query returns 2.000000e-04.
        """
        raise NotImplementedError()

    @property
    def scale(self) -> float:  # ToDo
        """
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
        return float(self.device.ask(":TIMebase:MAIN:SCALe?"))

    def mode(self):
        """
        **Rigol Programming Guide**

        :TIMebase:MODE

        **Command Format**

        :TIMebase:MODE <mode>

        :TIMebase:MODE?

        **Function Explanation**

        The commands set and query the scan mode of horizontal timebase.
        <mode> could be MAIN (main timebase) or DELayed (delayed scan).

        **Returned Format**

        The query returns MAIN or DELAYED.

        **Example**

        :TIM:MODE MAIN Setup the horizontal timebase as MAIN.

        :TIM:MODE? The query returns MAIN.
        """
        raise NotImplementedError()

    def format(self):
        """
        **Rigol Programming Guide**

        :TIMebase:FORMat

        **Command Format**

        :TIMebase:FORMat <value>

        :TIMebase:FORMat?

        **Function Explanation**

        The commands set and query the horizontal timebase. <value> could be
        XY, YT or SCANning.

        **Returned Format**

        The query returns X-Y, Y-T or SCANNING.

        **Example**

        :TIM:FORM YT Setup the form of grid as YT.

        :TIM:FORM? The query returns Y-T.
        """
        raise NotImplementedError()

    def fine_adjustment(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        :TIMebase:VERNier <bool>
        :TIMebase:VERNier?

        **Description**

        Enable or disable the fine adjustment of the horizontal scale.
        Query the current status of the fine adjustment of the horizontal scale.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :TIMebase:VERNier ON
        The query returns 1.
        """
        raise NotImplementedError()
