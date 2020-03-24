#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019-2020  Michael Sasser <Michael@MichaelSasser.org>

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
from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = [
    "Calculate",
]


class Addition(SubController):
    def sa(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADD:SA <source>
        
        :CALCulate:ADD:SA?
        
        **Description**
        
        Select the channel source of signal source A of the addition operation.
        
        Query the current channel source of signal source A of the addition
        operation.
        
        **Parameter**

        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <source>   Discrete   {CHANnel1|CHANnel2}   CHANnel1
        ========== ========== ===================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:ADD:SA CHANnel2
        """
        raise NotImplementedError()

    def sb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADD:SB <source>
        
        :CALCulate:ADD:SB?
        
        **Description**
        
        Select the channel source of signal source B of the addition operation.
        
        Query the current channel source of signal source B of the addition
        operation.
        
        **Parameter**
        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <source>   Discrete   {CHANnel1|CHANnel2}   CHANnel1
        ========== ========== ===================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:ADD:SB CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADD:INVert <bool>
        
        :CALCulate:ADD:INVert?
        
        **Description**
        
        Enable or disable the inverted display of the addition operation result.
        
        Query the current status of the inverted display of the addition
        operation result.
        
        **Parameter**

        ======== ======= ================== =======
        Name     Type    Range              Default
        ======== ======= ================== =======
        <bool>   Bool    {{0|OFF}|{1|ON}}   0|OFF
        ======== ======= ================== =======

        **Return Format**
        
        The query returns 0 or 1.
        
        **Example**
        
        :CALCulate:ADD:INVert ON
        
        The query returns 1.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADD:VSCale <scale>
        
        :CALCulate:ADD:VSCale?
        
        **Description**
        
        Set the vertical scale of the addition operation result.
        
        Query the current vertical scale of the addition operation result.
        
        **Parameter**

        ========= ======= ============================ =======
        Name      Type    Range                        Default
        ========= ======= ============================ =======
        <scale>   Real    0.02V to 500V Related to     2V
                          the current channel scale
        ========= ======= ============================ =======

        Note: for the channel scale, refer to the :CHANnel<n>:SCALe command.
        
        **Return Format**
        
        The query returns the vertical scale in scientifc notation.
        
        **Example**
        
        :CALCulate:ADD:VSCale 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADD:VOFFset <offs>
        
        :CALCulate:ADD:VOFFset?
        
        **Description**
        
        Set the vertical offset of the addition operation result.
        
        Query the current vertical offset of the addition operation result.
        
        **Parameter**

        ========= ====== ============================== =======
        Name      Type   Range                          Default
        ========= ====== ============================== =======
        <offs>    Real   -40 × VScale to 40 × VScale    0
        ========= ====== ============================== =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:ADD:VSCale command.
        
        **Return Format**
        
        The query returns the vertical offset in scientific notation.
        
        **Example**
        
        :CALCulate:ADD:VOFFset 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Subtraction(SubController):
    def sa(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:SUB:SA <source>
        
        :CALCulate:SUB:SA?
        
        **Description**
        
        Select the channel source of signal source A of subtraction operation.
        
        Query the current channel source of signal source A of subtraction
        operation.
        
        **Parameter**

        =========== =========== ==================== =========
        Name        Type        Range                 Default
        =========== =========== ==================== =========
        <source>    Discrete    {CHANnel1|CHANnel2}   CHANnel1
        =========== =========== ==================== =========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:SUB:SA CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:SUB:SB <source>
        
        :CALCulate:SUB:SB?
        
        **Description**
        
        Select the channel source of signal source B of subtraction operation.
        
        Query the current channel source of signal source B of subtraction
        operation.
        
        **Parameter**

        =========== =========== ====================== ========
        Name        Type        Range                  Default
        =========== =========== ====================== ========
        <source>    Discrete    {CHANnel1|CHANnel2}    CHANnel1
        =========== =========== ====================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:SUB:SB CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:SUB:INVert <bool>
        
        :CALCulate:SUB:INVert?
        
        **Description**
        
        Enable or disable the inverted display of the subtraction operation
        result.
        
        Query the current status of the inverted display of the subtraction
        operation result.
        
        **Parameter**

        ========= ======= ================== =======
        Name      Type    Range              Default
        ========= ======= ================== =======
        <bool>    Bool    {{0|OFF}|{1|ON}}   0|OFF
        ========= ======= ================== =======

        **Return Format**
        
        The query returns 0 or 1.
        
        **Example**
        
        :CALCulate:SUB:INVert ON
        
        The query returns 1.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:SUB:VSCale <scale>
        
        :CALCulate:SUB:VSCale?
        
        **Description**
        
        Set the vertical scale of the subtraction operation result.
        
        Query the current vertical scale of the subtraction operation result.
        
        **Parameter**

        ========= ======= =========================== =======
        Name      Type    Range                       Default
        ========= ======= =========================== =======
        <scale>   Real    0.02V to 500V Related to    2V
                          the current channel scale
        ========= ======= =========================== =======

        Note: for the channel scale, refer to the :CHANnel<n>:SCALe command.
        
        **Return Format**
        
        The query returns the vertical scale in scientific notation.
        
        **Example**
        
        :CALCulate:SUB:VSCale 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:SUB:VOFFset <offs>
        
        :CALCulate:SUB:VOFFset?
        
        **Description**
        
        Set the vertical offset of the subtraction operation result.
        
        Query the current vertical offset of the subtraction operation result.
        
        **Parameter**

        ========= ======= ============================== =======
        Name      Type    Range                          Default
        ========= ======= ============================== =======
        <offs>    Real    -40 × VScale to 40 × VScale    0
        ========= ======= ============================== =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:SUB:VSCale command.
        
        **Return Format**
        
        The query returns the vertical offset in scientific notation.
        
        **Example**
        
        :CALCulate:SUB:VOFFset 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Multiplication(SubController):
    def sa(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MULTiply:SA <source>
        
        :CALCulate:MULTiply:SA?
        
        **Description**
        
        Select the channel source of signal source A of multiplication
        operation.
        
        Query the current channel source of signal source A of multiplication
        operation.
        
        **Parameter**

        =========== =========== ====================== ========
        Name        Type        Range                  Default
        =========== =========== ====================== ========
        <source>    Discrete    {CHANnel1|CHANnel2}    CHANnel1
        =========== =========== ====================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:MULTiply:SA CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MULTiply:SB <source>
        
        :CALCulate:MULTiply:SB?
        
        **Description**
        
        Select the channel source of signal source B of multiplication
        operation.
        
        Query the current channel source of signal source B of multiplication
        operation.
        
        **Parameter**

        =========== =========== ======================= ========
        Name        Type        Range                   Default
        =========== =========== ======================= ========
        <source>    Discrete    {CHANnel1|CHANnel2}     CHANnel1
        =========== =========== ======================= ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:MULTiply:SB CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MULTiply:INVert <bool>
        
        :CALCulate:MULTiply:INVert?
        
        **Description**
        
        Enable or disable the inverted display of the multiplication operation
        result.
        
        Query the current status of the inverted display of the multiplication
        operation result.
        
        **Parameter**

        ======== ======= ================= ========
        Name     Type    Range              Default
        ======== ======= ================= ========
        <bool>   Bool    {{0|OFF}|{1|ON}}   0|OFF
        ======== ======= ================= ========

        **Return Format**
        
        The query returns 0 or 1.
        
        **Example**
        
        :CALCulate:MULTiply:INVert ON
        
        The query returns 1.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MULTiply:VSCale <scale>
        
        :CALCulate:MULTiply:VSCale?
        
        **Description**
        
        Set the vertical scale of the multiplication operation result.
        
        Query the current vertical scale of the multiplication operation result.
        
        **Parameter**

        ========= ======= ================================ =======
        Name      Type    Range                            Default
        ========= ======= ================================ =======
        <scale>   Real    5.0e-08U to 1.0e+07U Related     2V
                          to the current channel scale
        ========= ======= ================================ =======

        Note: for the channel scale, refer to the :CHANnel<n>:SCALe command.
        
        **Return Format**
        
        The query returns the vertical scale in scientific notation.
        
        **Example**
        
        :CALCulate:MULTiply:VSCale 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MULTiply:VOFFset <offs>
        
        :CALCulate:MULTiply:VOFFset?
        
        **Description**
        
        Set the vertical offset of the multiplication operation result.
        
        Query the current vertical offset of the multiplication operation
        result.
        
        **Parameter**

        ======= ====== ================================ =======
        Name    Type   Range                            Default
        ======= ====== ================================ =======
        <offs>  Real   -40 × VScale to 40 × VScale      0
        ======= ====== ================================ =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:MULTiply:VSCale command.
        
        **Return Format**
        
        The query returns the vertical offset in scientific notation.
        
        **Example**
        
        :CALCulate:MULTiply:VOFFset 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Division(SubController):
    def sa(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:DIVision:SA <source>
        
        :CALCulate:DIVision:SA?
        
        **Description**
        
        Select the channel source of signal source A of division operation.
        
        Query the current channel source of signal source A of division
        operation.
        
        **Parameter**

        ========== =========== ====================== ========
        Name       Type        Range                  Default
        ========== =========== ====================== ========
        <source>   Discrete    {CHANnel1|CHANnel2}    CHANnel1
        ========== =========== ====================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:DIVision:SA CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:DIVision:SB <source>
        
        :CALCulate:DIVision:SB?
        
        **Description**
        
        Select the channel source of signal source B of division operation.
        
        Query the current channel source of signal source B of division
        operation.
        
        **Parameter**

        =========== =========== ===================== ========
        Name        Type        Range                 Default
        =========== =========== ===================== ========
        <source>    Discrete    {CHANnel1|CHANnel2}   CHANnel1
        =========== =========== ===================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        :CALCulate:DIVision:SB CHANnel2
        
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:DIVision:INVert <bool>
        
        :CALCulate:DIVision:INVert?
        
        Decsription
        
        Enable or disable the inverted display of the division operation result.
        
        Query the current status of the inverted display of the division
        operation result.
        
        **Parameter**

        ========= ====== ================== =======
        Name      Type   Range              Default
        ========= ====== ================== =======
        <bool>    Bool   {{0|OFF}|{1|ON}}   0|OFF
        ========= ====== ================== =======

        **Return Format**
        
        The query returns 0 or 1.
        
        **Example**
        
        :CALCulate:DIVision:INVert ON
        
        The query returns 1.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:DIVision:VSCale <scale>
        
        :CALCulate:DIVision:VSCale?
        
        **Description**
        
        Set the vertical scale of the division operation result.
        Query the current vertical scale of the division operation result.
        
        **Parameter**

        ========== ======= ======================= =======
        Name       Type    Range                   Default
        ========== ======= ======================= =======
        <scale>    Real    5.0e-07U to 5.0e+08U    2V
                                 Related to the current channel scale
        ========== ======= ======================= =======

        
        Note: for the channel scale, refer to the :CHANnel<n>:SCALe command.
        
        **Return Format**
        
        The query returns the vertical scale in scientific notation.
        
        **Example**
        
        :CALCulate:DIVision:VSCale 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:DIVision:VOFFset <offs>
        
        :CALCulate:DIVision:VOFFset?
        
        **Description**
        
        Set the vertical offset of the division operation result.
        
        Query the current vertical offset of the division operation result.
        
        **Parameter**

        ======== ======= ============================== =======
        Name     Type    Range                          Default
        ======== ======= ============================== =======
        <offs>   Real    -40 × VScale to 40 × VScale    0
        ======== ======= ============================== =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:DIVision:VSCale command.
        
        **Return Format**
        
        The query returns the vertical offset in scientific notation.
        
        **Example**
        
        :CALCulate:DIVision:VOFFset 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Fft(SubController):
    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:SOURce <source>
        
        :CALCulate:FFT:SOURce?
        
        **Description**
        
        Select the signal source of FFT operation.
        
        Query the current signal source of FFT operation.
        
        **Parameter**

        ========== =========== ===================== ========
        Name       Type        Range                 Default
        ========== =========== ===================== ========
        <source>   Discrete    {CHANnel1|CHANnel2}   CHANnel1
        ========== =========== ===================== ========

        **Return Format**
        
        The query returns CHAN1 or CHAN2.
        
        **Example**
        
        :CALCulate:FFT:SOURce CHANnel2
        """
        raise NotImplementedError()

    def window(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:WINDow <window>
        
        :CALCulate:FFT:WINDow?
        
        **Description**
        
        Select the window function of the FFT operation.
        
        Query the current window function of the FFT operation.
        
        **Parameter**

        ========== ========== ====================================== =========
        Name       Type       Range                                  Default
        ========== ========== ====================================== =========
        <window>   Discrete   {RECTangle|HANNing|HAMMing|BLACkman}   RECTangle
        ========== ========== ====================================== =========

        **Return Format**
        
        The query returns RECT, HANN, HAMM or BLAC.
        
        **Example**
        
        :CALCulate:FFT:WINDow HANNing
        """
        raise NotImplementedError()

    def split(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:SPLit <bool>
        
        :CALCulate:FFT:SPLit?
        
        **Description**
        
        Enable or disable the split display of the FFT operation.
        
        Query the current status of the split display of the FFT operation.
        
        **Parameter**

        ======== ======= ================== =======
        Name     Type    Range              Default
        ======== ======= ================== =======
        <bool>   Bool    {{0|OFF}|{1|ON}}   1|ON
        ======== ======= ================== =======

        **Return Format**
        
        The query returns 0 or 1.
        
        **Example**
        
        :CALCulate:FFT:SPLit OFF
        
        The query returns 0.
        """
        raise NotImplementedError()

    def vsmode(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:VSMode <vmode>
        
        :CALCulate:FFT:VSMode?
        
        **Description**
        
        Set the vertical scale of the FFT operation result to linear or log.
        
        Query the current vertical scale of the FFT operation result.
        
        **Parameter**

        ========= =========== =============== =======
        Name      Type        Range           Default
        ========= =========== =============== =======
        <vmode>   Discrete    {VRMS|DBVRms}   VRMS
        ========= =========== =============== =======

        **Return Format**
        
        The query returns VRMS or DBVR.
        
        **Example**
        
        :CALCulate:FFT:VSMode DBVRms
        
        The query returns DBVR.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:VSCale <vscale>
        
        :CALCulate:FFT:VSCale?
        
        **Description**
        
        Set the vertical scale of the FFT operation result.
        
        Query the current vertical scale of the FFT operation result.
        
        **Parameter**

        ========== ====== =============================== ============
        Name       Type   Range                           Default
        ========== ====== =============================== ============
        <vscale>   Real   Related to the current FFT      10dBVrms/div
                          display mode:
                          **dBVrms**: 1 to 100
                          **Vrms**: 0.01 to 200,
                          related to the current
                          channel scale (from
                          channel scale/128 to channel
                          scale*128)
        ========== ====== =============================== ============

        Note:
        For the FFT display mode, refer to the :CALCulate:FFT:VSMode command.
        
        For the channel scale, refer to the :CHANnel<n>:SCALe command. Once
        you change the channel scale, the range of <vscale> will be changed
        only after the MATH channel is re-activated.
        
        **Return Format**
        
        The query returns the vertical scale in scientific notation.
        
        **Example**
        
        :CALCulate:FFT:VSCale 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:VOFFset <offs>
        
        :CALCulate:FFT:VOFFset?
        
        **Description**
        
        Set the vertical offset of the FFT operation result.
        
        Query the current vertical offset of the FFT operation result.
        
        **Parameter**

        ======== ======= ============================= ========
        Name     Type    Range                          Default
        ======== ======= ============================= ========
        <offs>   Real    -40 × VScale to 40 × VScale    0
        ======== ======= ============================= ========

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:FFT:VSCale command.
        
        **Return Format**
        
        The query returns the vertical offset in scientifc notation.
        
        **Example**
        
        :CALCulate:FFT:VOFFset 2
        
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def hscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:HSCale <hscale>
        
        :CALCulate:FFT:HSCale?
        
        **Description**
        
        Set the horizontal coefficient in FFT operation. This command
        indirectly sets the FFT horizontal scale.
        
        Query the current horizontal coefficient in FFT operation.
        
        **Parameter**

        ========== =========== ============ =======
        Name       Type        Range        Default
        ========== =========== ============ =======
        <hscale>   Discrete    {1|2|3|4}    1
        ========== =========== ============ =======

        Note: you can use the :CALCulate:FFT:HSPan command to set the
        horizontal scale of FFT directly.
        
        **Explanation**
        
        1: Horizontal Scale=the current FFT sample rate of the screen/20.
        
        2: Horizontal Scale=the current FFT sample rate of the screen/40.
        
        3: Horizontal Scale=the current FFT sample rate of the screen/100.
        
        4: Horizontal Scale=the current FFT sample rate of the screen/200.
        
        **Return Format**
        
        The query returns 1, 2, 3 or 4.
        
        **Example**
        
        :CALCulate:FFT:HSCale 2
        """
        raise NotImplementedError()

    def hoffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        
        :CALCulate:FFT:HOFFset <offs>
        
        :CALCulate:FFT:HOFFset?
        
        **Description**
        
        Set the horizontal offset of the FFT operation result and the unit
        is Hz.
        
        Query the current horizontal offset of the FFT operation result.
        
        **Parameter**

        ======== ======= ===================================== =======
        Name     Type    Range                                 Default
        ======== ======= ===================================== =======
        <offs>   Real    -0.4*the current FFT sample rate of   0
                         the screen to +0.4*the current FFT
                         sample rate of the screen
        ======== ======= ===================================== =======

        Note: the current FFT sample rate of the screen = number of points per
        grid horizontally/horizontal time base. For the horizontal time base,
        refer to the :TIMebase[:MAIN]:SCALe command.
        
        **Return Format**
        
        The query returns the horizontal offset in scientific notation.
        
        **Example**
        
        :CALCulate:FFT:HOFFset 10000000
        """
        raise NotImplementedError()

    def hspan(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:HSPan <span>
        
        :CALCulate:FFT:HSPan?
        
        **Description**
        
        Set the horizontal scale of the FFT operation result.
        
        Query the current horizontal scale of the FFT operation result.
        
        **Parameter**

        ======== ====== ======================================== ========
        Name     Type   Range                                    Default
        ======== ====== ======================================== ========
        <span>   Real   The current FFT sample rate of the       5MHz/div
                        screen/200 to the current FFT sample
                        rate of the screen/20
        ======== ====== ======================================== ========

        Note:
        The step is 1X-2X-5X-10X within the range.
        
        The current FFT sample rate of the screen =the number of points per
        grid horizontally/horizontal time base. For the horizontal time base,
        refer to the :TIMebase[:MAIN]:SCALe command.
        
        You can use the :CALCulate:FFT:HSCale command to set the horizontal
        scale of FFT operation indirectly.
        
        **Return Format**
        
        The query returns the current horizontal scale in scientific notation
        and the unit is Hz/div.
        
        **Example**
        
        :CALCulate:FFT:HSPan 2500000
        
        The query returns 2.500000e+06.
        """
        raise NotImplementedError()

    def hcenter(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:FFT:HCENter <center>

        :CALCulate:FFT:HCENter?

        **Description**

        Set the center frequency of the FFT operation result and the unit is Hz.

        Query the current center frequency of the current FFT operation result.

        **Parameter**

        =========== ====== =================================== ========
        Name        Type   Range                                Default
        =========== ====== =================================== ========
        <center>    Real   Horizontal offset of the             35MHz
                           operation result +7*the current
                           horizontal scale
        =========== ====== =================================== ========

        Note: for the horizontal offset, refer to the :CALCulate:FFT:HOFFset
        command; for the horizontal scale, refer to the :CALCulate:FFT:HSCale
        and :CALCulate:FFT:HSPan commands.

        **Return Format**

        The query returns the frequency value in scientific notation.

        **Example**

        :CALCulate:FFT:HCENter 10000000

        The query returns 1.000000e+07.
        """
        raise NotImplementedError()


class Logic(SubController):
    def sa(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:SA <source>

        :CALCulate:LOGic:SA?

        **Description**

        Select the channel source of signal source A of logic operation.

        Query the current channel source of signal source A of logic operation.

        **Parameter**

        ========== ========== ===================== ========
        Name       Type       Range                 Default
        ========== ========== ===================== ========
        <source>   Discrete   {CHANnel1|CHANnel2}   CHANnel1
        ========== ========== ===================== ========

        **Explanation**

        The signal source specified by this command is used instead of the
        signal source specified by the :CALCulate:LOGic:SB command if the
        current logic operation type is NOT.

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :CALCulate:LOGic:SA CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def sb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:SB <source>

        :CALCulate:LOGic:SB?

        **Description**

        Select the channel source of signal source B of logic operation.

        Query the current channel source of signal source B of logic operation.

        **Parameter**

        =========== =========== ===================== ========
        Name        Type        Range                 Default
        =========== =========== ===================== ========
        <source>    Discrete    {CHANnel1|CHANnel2}   CHANnel1
        =========== =========== ===================== ========

        **Explanation**

        The signal source specified by the :CALCulate:LOGic:SA command is
        used instead of the signal source specified by this command if the
        current logic operation type is NOT.

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :CALCulate:LOGic:SB CHANnel2

        The query returns CHAN2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:INVert <bool>
     
        :CALCulate:LOGic:INVert?
     
        **Description**
     
        Enable or disable the inverted display of the logic operation result.
     
        Query the current status of the inverted display of the logic operation
        result.
     
        **Parameter**

        ======== ====== =================== =======
        Name     Type   Range               Default
        ======== ====== =================== =======
        <bool>   Bool   {{0|OFF}|{1|ON}}    0|OFF
        ======== ====== =================== =======

        **Return Format**
     
        The query returns 0 or 1.
     
        **Example**
     
        :CALCulate:LOGic:INVert ON
     
        The query returns 1.
        """
        raise NotImplementedError()

    def vscale(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:VSCale <scale>
     
        :CALCulate:LOGic:VSCale?
     
        **Description**
     
        Set the vertical scale of the logic operation result.
     
        Query the current vertical scale of the logic operation result.
     
        **Parameter**

        ========= ====== ================ =======
        Name      Type   Range            Default
        ========= ====== ================ =======
        <scale>   Real   0.05U to 100U    1U
        ========= ====== ================ =======

        **Return Format**
     
        The query returns the vertical scale in scientific notation.
     
        **Example**
     
        :CALCulate:LOGic:VSCale 2
     
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:VOFFset <offs>
     
        :CALCulate:LOGic:VOFFset?
     
        **Description**
     
        Set the vertical offset of the logic operation result.
     
        Query the current vertical offset of the logic operation result.
     
        **Parameter**

        ======== ====== ============================= =======
        Name     Type   Range                         Default
        ======== ====== ============================= =======
        <offs>   Real   -40 × VScale to 40 × VScale   0
        ======== ====== ============================= =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:LOGic:VSCale command.
     
        **Return Format**
     
        The query returns the vertical offset in scientific notation.
     
        **Example**
     
        :CALCulate:LOGic:VOFFset 2
     
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def operator(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:OPERator <oper>
     
        :CALCulate:LOGic:OPERator?
     
        **Description**
     
        Select the operator of logic operation.
     
        Query the operator of the current logic operation.
     
        **Parameter**

        ======== ========== ================== =======
        Name     Type       Range              Default
        ======== ========== ================== =======
        <oper>   Discrete   {AND|OR|NOT|XOR}   AND
        ======== ========== ================== =======

        **Return Format**
     
        The query returns AND, OR, NOT or XOR.
     
        **Example**
     
        :CALCulate:LOGic:OPERator XOR
     
        The query returns XOR.
     
        """
        raise NotImplementedError()

    def athreshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:ATHReshold <thre>
       
        :CALCulate:LOGic:ATHReshold?
       
        **Description**
       
        Set the threshold of logic channel A.
       
        Query the current threshold of logic channel A.
       
        **Parameter**

        ======== ====== =========================== =======
        Name     Type   Range                       Default
        ======== ====== =========================== =======
        <thre>   Real   Screen Range (the offset    0
                        changes with the scale)
        ======== ====== =========================== =======

        **Return Format**
       
        The query returns the current threshold in scientific notation.
       
        **Example**
       
        :CALCulate:LOGic:ATHReshold 2
       
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def bthreshold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:LOGic:BTHReshold <thre>
       
        :CALCulate:LOGic:BTHReshold?
       
        **Description**
       
        Set the threshold of logic channel B.
       
        Query the current threshold of logic channel B.
       
        **Parameter**

        ======= ====== ========================== =======
        Name    Type   Range                      Default
        ======= ====== ========================== =======
        <thre>  Real   Screen Range (the offset   0
                       changes with the scale)
        ======= ====== ========================== =======

        **Return Format**
       
        The query returns the current threshold in scientific notation.
       
        **Example**
       
        :CALCulate:LOGic:BTHReshold 2
       
        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Advanced(SubController):
    def expression(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:EXPRession <expression>
        
        :CALCulate:ADVanced:EXPRession?
        
        **Description**
        
        Set the expression of advanced operation.
        
        Query the current expression of advanced operation.
        
        **Parameter**

        ============== ======================== ======================= =======
        Name           Type                     Range                   Default
        ============== ======================== ======================= =======
        <expression>   ASCII character string   Refer to Explanation    CH1+CH2
        ============== ======================== ======================= =======

        **Explanation**

        Input the valid expression using the characters as shown in the figure
        below. Note that the length of the expression should be no greater
        than 64 bytes.

        =========== =========================================================
        Type        Value
        =========== =========================================================
        Channel     CH1, CH2, CH3, CH4
        Function    Intg(), Diff(), Log(), Exp(), Sqrt(), Cosine(), Tangent()
        Variable    Variable1, Variable2
        Operator    +, -, \*, /, (, ), !(), <, >, <=, >=, ==, !=, ||, &&
        Figure      0,1,2,3,4,5,6,7,8,9, E
        =========== =========================================================

        **Return Format**

        The query returns the current expression in character string.

        **Example**

        :CALCulate:ADVanced:EXPRession CH1+2

        The query returns CH1+2.
        """
        raise NotImplementedError()

    def invert(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:INVert <bool>

        :CALCulate:ADVanced:INVert?

        **Description**

        Enable or disable the inverted display of the advanced operation result.

        Query the current status of the inverted display of the advanced
        operation result.

        **Parameter**

        ======== ====== =================== =======
        Name     Type   Range               Default
        ======== ====== =================== =======
        <bool>   Bool   {{0|OFF}|{1|ON}}    0|OFF
        ======== ====== =================== =======

        **Return Format**

        The query returns 0 or 1.

        **Example**

        :CALCulate:ADVanced:INVert ON

        The query returns 1.
        """
        raise NotImplementedError()

    def variable1(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:VARiable1 <numeric_value>

        :CALCulate:ADVanced:VARiable1?

        **Description**

        Set the variable1 in the advanced operation expression.

        Query the current value variable1 in the advanced operation expression.

        **Parameter**

        ================= ====== =========================== =======
        Name              Type   Range                       Default
        ================= ====== =========================== =======
        <numeric_value>   Real   -9.9999e-09 to 9.9999e+09   0
        ================= ====== =========================== =======

        **Explanation**

        This command determines the value of variable1 that the
        :CALCulate:ADVanced:EXPRession command might refer to.

        **Return Format**

        The query returns the current value of variable1 in scientific
        notation.

        **Example**

        :CALCulate:ADVanced:VARiable1 606

        The query returns 6.060000e+02.
        """
        raise NotImplementedError()

    def variable2(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:VARiable2 <numeric_value>

        :CALCulate:ADVanced:VARiable2?

        **Description**

        Set the variable2 in the advanced operation expression.

        Query the current value of variable2 in the advanced operation
        expression.

        **Parameter**

        ================= ====== =========================== =======
        Name              Type   Range                       Default
        ================= ====== =========================== =======
        <numeric_value>   Real   -9.9999e-09 to 9.9999e+09   0
        ================= ====== =========================== =======

        **Explanation**

        This command determines the value of variable2 that the
        :CALCulate:ADVanced:EXPRession command might refer to.

        **Return Format**

        The query returns the current value of variable2 in scientific notation.

        **Example**

        :CALCulate:ADVanced:VARiable2 606

        The query returns 6.060000e+02.
        """
        raise NotImplementedError()

    def vscalc(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:VSCale <numeric_value>

        :CALCulate:ADVanced:VSCale?

        **Description**

        Set the vertical scale of the advanced operation result.

        Query the current vertical scale of the advanced operation result.

       ** Parameter**

        ================== ======= ============================= ========
        Name               Type    Range                          Default
        ================== ======= ============================= ========
        <numeric_value>    Real    2.0e-02V to 5.0e+02V Related   2V
                                   to the current channel scale
        ================== ======= ============================= ========

        Note: for the channel scale, refer to the :CHANnel<n>:SCALe command.

        **Return Format**

        The query returns the vertical scale in scientific notation.

        **Example**

        :CALCulate:ADVanced:VSCale 2

        The query returns 2.000000e+00.
        """
        raise NotImplementedError()

    def voffset(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:ADVanced:VOFFset?

        **Description**

        Set the vertical offset of the advanced operation result.

        Query the current vertical offset of the advanced operation result.

        **Parameter**

        ======== ====== ============================== =======
        Name     Type   Range                          Default
        ======== ====== ============================== =======
        <offs>   Real   -40 × VScale to 40 × VScale    0
        ======== ====== ============================== =======

        Note: for the VScale (the vertical scale of MATH), refer to the
        :CALCulate:ADVanced:VSCale command.

        **Return Format**

        The query returns the vertical offset in scientific notation.

        **Example**

        :CALCulate:ADVanced:VOFFset 2

        The query returns 2.000000e+00.
        """
        raise NotImplementedError()


class Calculate(BaseController):
    def __init__(self, device):
        super(Calculate, self).__init__(device)
        self.add: Addition = Addition(self)
        self.sub: Subtraction = Subtraction(self)
        self.mul: Multiplication = Multiplication(self)
        self.div: Division = Division(self)
        self.fft: Fft = Fft(self)
        self.logic: Logic = Logic(self)
        self.adv: Advanced = Advanced(self)

    def mode(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :CALCulate:MODE <mod>

        :CALCulate:MODE?

        **Description**

        Select the type of the math operation or disable the math operation
        function.

        Query the type of the current math operation.

        **Parameter**

        ====== ========= ============================= =======
        Name   Type      Range                         Default
        ====== ========= ============================= =======
        <mod>  Discrete  {ADD|SUB|MULTiply|DIVision    Off
                         |FFT|LOGic|ADVanced|OFF}
        ====== ========= ============================= =======

        **Return Format**

        The query returns ADD, SUB, MULT, DIV, FFT, LOG, ADV or OFF.

        **Example**

        :CALCulate:MODE FFT

        The query returns FFT.
        """
        raise NotImplementedError()
