#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>

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

from ds2000.controller import BaseController, SubController, SubSubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Trigger",
]


class Mode(SubController):
    def edge(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def pulse(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def runt(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def wind(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def nedge(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def video(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def pattern(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def delay(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def timeout(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def duration(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def shold(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def rs232(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def iic(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def spi(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()

    def usb(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE|PULSe|RUNT|WIND|NEDG|  EDGE
                          SLOPe|VIDeo|PATTern|DELay|
                          TIMeout|DURATion|SHOLd|
                          RS232|IIC|SPI|USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        raise NotImplementedError()


class Coupling(SubController):
    def ac(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:COUPling <couple>
        :TRIGger:COUPling?

        **Description**

        Select the desired trigger coupling mode.
        Query the current trigger coupling mode.

        **Parameter**

        ========= ========= ========================== =======
        Name      Type      Range                      Default
        ========= ========= ========================== =======
        <couple>  Discrete  {AC|DC|LFReject|HFReject}  DC
        ========= ========= ========================== =======

        **Explanation**

        It is only available in edge trigger.

        **Return Format**

        The query returns AC, DC, LFR or HFR.

        **Example**

        :TRIGger:COUPling LFReject
        The query returns LFR.
        """
        raise NotImplementedError()

    def dc(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:COUPling <couple>
        :TRIGger:COUPling?

        **Description**

        Select the desired trigger coupling mode.
        Query the current trigger coupling mode.

        **Parameter**

        ========= ========= ========================== =======
        Name      Type      Range                      Default
        ========= ========= ========================== =======
        <couple>  Discrete  {AC|DC|LFReject|HFReject}  DC
        ========= ========= ========================== =======

        **Explanation**

        It is only available in edge trigger.

        **Return Format**

        The query returns AC, DC, LFR or HFR.

        **Example**

        :TRIGger:COUPling LFReject
        The query returns LFR.
        """
        raise NotImplementedError()

    def low_frequency_reject(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:COUPling <couple>
        :TRIGger:COUPling?

        **Description**

        Select the desired trigger coupling mode.
        Query the current trigger coupling mode.

        **Parameter**

        ========= ========= ========================== =======
        Name      Type      Range                      Default
        ========= ========= ========================== =======
        <couple>  Discrete  {AC|DC|LFReject|HFReject}  DC
        ========= ========= ========================== =======

        **Explanation**

        It is only available in edge trigger.

        **Return Format**

        The query returns AC, DC, LFR or HFR.

        **Example**

        :TRIGger:COUPling LFReject
        The query returns LFR.
        """
        raise NotImplementedError()

    def high_frequency_reject(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:COUPling <couple>
        :TRIGger:COUPling?

        **Description**

        Select the desired trigger coupling mode.
        Query the current trigger coupling mode.

        **Parameter**

        ========= ========= ========================== =======
        Name      Type      Range                      Default
        ========= ========= ========================== =======
        <couple>  Discrete  {AC|DC|LFReject|HFReject}  DC
        ========= ========= ========================== =======

        **Explanation**

        It is only available in edge trigger.

        **Return Format**

        The query returns AC, DC, LFR or HFR.

        **Example**

        :TRIGger:COUPling LFReject
        The query returns LFR.
        """
        raise NotImplementedError()


class Sweep(SubController):
    def auto(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()

    def normal(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()

    def single(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:SWEep <sweep>
        :TRIGger:SWEep?

        **Description**

        Set the trigger mode to auto, normal or single.
        Query the current trigger mode.

        **Parameter**

        ======== ========= ===================== =======
        Name     Type      Range                 Default
        ======== ========= ===================== =======
        <sweep>  Discrete  {AUTO|NORMal|SINGle}  AUTO
        ======== ========= ===================== =======

        **Return Format**

        The query returns AUTO, NORM or SING.

        **Example**

        :TRIGger:SWEep SINGle
        The query returns SING.
        """
        raise NotImplementedError()


class Edge(SubController):
    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SOURce <source>
        :TRIGger:EDGe:SOURce?

        **Description**

        Select the trigger source of edge trigger.
        Query the current trigger source of edge trigger.

        **Parameter**

        ========= ========= =============================== ========
        Name      Type      Range                           Default
        ========= ========= =============================== ========
        <source>  Discrete  {CHANnel1|CHANnel2|EXT|ACLine}  CHANnel1
        ========= ========= =============================== ========

        **Return Format**

        The query returns CHAN1, CHAN2, EXT or ACL.

        **Example**

        :TRIGger:EDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:SLOPe <slope>
        :TRIGger:EDGe:SLOPe?

        **Description**

        Select the edge type of edge trigger.
        Query the current edge type of edge trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:EDGe:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:EDGe:LEVel <level>
        :TRIGger:EDGe:LEVel?

        **Description**

        Set the trigger level of edge trigger and the unit is the same with the
        current amplitude unit.
        Query the current trigger level of edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:EDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        raise NotImplementedError()


# ToDo: Shorter function names!!!
class PulseWhen(SubSubController):
    def pos_pulse_width_greater_than_specified_lower_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()

    def pos_pulse_width_lower_than_specified_upper_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()

    def neg_pulse_width_greater_than_specified_lower_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()

    def neg_pulse_width_lower_than_specified_upper_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()

    def pos_pulse_width_between_specified_upper_and_lower_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()

    def neg_pulse_width_between_specified_upper_and_lower_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:WHEN <when>
        :TRIGger:PULSe:WHEN?

        **Description**

        Select the trigger condition of pulse trigger.
        Query the current trigger condition of pulse trigger.

        **Parameter**

        ======= ========= ========================= =======
        Name    Type      Range                     Default
        ======= ========= ========================= =======
        <when>  Discrete  {PGReater|PLESs|NGReater  GReater
                          |NLESs|PGLess|NGLess}
        ======= ========= ========================= =======

        **Explanation**

        **PGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is greater than the specified
        Pulse Width.

        **PLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        positive pulse width of the input signal is lower than the specified
        Pulse Width.

        **NGReater**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:LWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is greater than the specified
        Pulse Width.

        **NLESs**: you need to specify a pulse width (refer to the
        :TRIGger:PULSe:UWIDth command). The oscilloscope triggers when the
        negative pulse width of the input signal is lower than the specified
        Pulse Width.

        **PGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the positive pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **NGLess**: you need to specify an upper (refer to the
        :TRIGger:PULSe:UWIDth command) and a lower (refer to the
        :TRIGger:PULSe:LWIDth command) pulse width. The oscilloscope triggers
        when the negative pulse width of the input signal is greater than the
        specified lower pulse width and lower than the upper pulse width.

        **Return Format**

        The query returns PGR, PLES, NGR, NLES, PGL or NGL.

        **Example**

        :TRIGger:PULSe:WHEN PGReater
        The query returns PGR.
        """
        raise NotImplementedError()


class Pulse(SubController):
    def __init__(self, device):
        super(Pulse, self).__init__(device)
        self.when: PulseWhen = PulseWhen(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:SOURce <source>
        :TRIGger:PULSe:SOURce?

        **Description**

        Select the trigger source in pulse trigger.
        Query the current trigger source in pulse trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**
        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:PULSe:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def upper_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:UWIDth <width>
        :TRIGger:PULSe:UWIDth?

        **Description**

        Set the upper limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current upper limit of the pulse width in pulse trigger.

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  2μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 10ns to 4s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PLESs, NLESs, PGLess or NGLess.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:UWIDth 0.000003
        The query returns 3.000000e-06.
        """
        raise NotImplementedError()

    def lower_pulse_width(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LWIDth <width>
        :TRIGger:PULSe:LWIDth?

        **Description**

        Set the lower limit of the pulse width in pulse trigger and the unit
        is s.
        Query the current lower limit of the pulse width in pulse trigger

        **Parameter**

        ======== ===== ========== =======
        Name     Type  Range      Default
        ======== ===== ========== =======
        <width>  Real  2ns to 4s  1μs
        ======== ===== ========== =======

        Note: when the trigger condition is PGLess or NGLess, the range is
        from 2ns to 3.99s.

        **Explanation**

        This command is available when the trigger condition (refer to the
        :TRIGger:PULSe:WHEN command) is PGReater, NGReater, PGLess or NGLess.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:PULSe:LWIDth 0.000003
        The query returns 3.000000e-06.
        """
        raise NotImplementedError()

    def level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:PULSe:LEVel <level>
        :TRIGger:PULSe:LEVel?

        **Description**

        Set the trigger level in pulse trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in pulse trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:PULSe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        raise NotImplementedError()


# ToDo: Shorter function names!!!
class RuntWhen(SubSubController):
    def none(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_greater_than_lower_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_lower_than_upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_between_lower_and_upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()


class Runt(SubController):
    def __init__(self, device):
        super(Runt, self).__init__(device)
        self.when: RuntWhen = RuntWhen(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:SOURce <source>
        :TRIGger:RUNT:SOURce?

        **Description**

        Select the trigger source of runt trigger.
        Query the current trigger source of runt trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RUNT:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def polarity(self, positive: bool = True):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:POLarity <polarity>
        :TRIGger:RUNT:POLarity?

        **Description**

        Select the pulse polarity of runt trigger.
        Query the current pulse polarity of runt trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:RUNT:POLarity NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def lower_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WLOWer <NR3>
        :TRIGger:RUNT:WLOWer?

        **Description**

        Set the lower limit of the pulse width in runt trigger.
        Query the current lower limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  1μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the lower limit of the
        pulse width is from 2ns to 3.99s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to GREater or GLESs.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WLOWer 0.02
        The query returns 2.000000e-02.
        """
        raise NotImplementedError()

    def upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WUPPer <NR3>
        :TRIGger:RUNT:WUPPer?

        **Description**

        Set the upper limit of the pulse width in runt trigger.
        Query the current upper limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  2μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the upper limit of the
        pulse width is from 10ns to 4s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WUPPer 0.02
        The query returns 2.000000e-02.
        """
        raise NotImplementedError()

    def upper_limit_trigger_level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:ALEVel <level>
        :TRIGger:RUNT:ALEVel?

        **Description**

        Set the upper limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current upper limit of the trigger level in runt trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:ALEVel 0.16
        The query returns 1.600000e-01.
         """
        raise NotImplementedError()

    def lower_limit_trigger_level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:BLEVel <level>
        :TRIGger:RUNT:BLEVel?

        **Description**

        Set the lower limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current lower limit of the trigger level in runt trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        raise NotImplementedError()


class WindowsSlope(SubSubController):
    def positive(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def negative(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def rfali(self):  # ToDo: what is rfali?
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SLOPe <type>
        :TRIGger:RUNT:SLOPe?

        **Description**

        Select the windows type of windows trigger.
        Query the current windows type of windows trigger.

        **Parameter**

        ======= ========= ========================== ========
        Name    Type      Range                      Default
        ======= ========= ========================== ========
        <type>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======= ========= ========================== ========

        **Return Format**

        The query returns POSitive, NEGative or RFALl.

        **Example**
        :TRIGger:WINDows:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()


class WindowsPosition(SubSubController):
    def exit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()

    def enter(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:POSition <pos>
        :TRIGger:RUNT:POSition?

        **Description**

        Select the trigger position of windows trigger.
        Query the current trigger position of windows trigger.

        **Parameter**

        ======= ========= ================== =======
        Name    Type      Range              Default
        ======= ========= ================== =======
        <type>  Discrete  {EXIT|ENTER|TIMe}  ENTER
        ======= ========= ================== =======

        **Return Format**

        The query returns EXIT, ENTER or TIM.

        **Example**

        :TRIGger:WINDows:POSition ENTER
        The query returns ENTER.
        """
        raise NotImplementedError()


class Windows(SubController):
    def __init__(self, device):
        super(Windows, self).__init__(device)
        self.slope: WindowsSlope = WindowsSlope(self)
        self.position: WindowsPosition = WindowsPosition(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:SOURce <source>
        :TRIGger:WINDows:SOURce?

        **Description**

        Select the trigger source of windows trigger.
        Query the current trigger source of windows trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:WINDows:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:WINDows:TIMe <NR3>
        :TRIGger:RUNT:TIMe?

        **Description**

        Select the windows time of windows trigger.
        Query the current windows time of windows trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Explanation**

        This command is only available when the trigger position of windows
        trigger (refer to the :TRIGger:Windows:POSition command) is set to
        TIMe.

        **Return Format**

        The query returns the windows time in scientific notation.

        **Example**

        :TRIGger:WINDows:TIMe 0.002
        The query returns 2.000000e-03.
        """
        raise NotImplementedError()


class NthEdge(SubController):
    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SOURce <source>
        :TRIGger:NEDGe:SOURce?

        **Description**

        Select the trigger source of Nth egde trigger.
        Query the current trigger source of Nth edge trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:NEDGe:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def slope(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:SLOPe <slope>
        :TRIGger:NEDGe:SLOPe?

        **Description**

        Select the edge type of Nth edge trigger.
        Query the current edge type of Nth edge trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POSitive or NEGative.

        **Example**

        :TRIGger:NEDGe:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def idle(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:IDLE <NR3>
        :TRIGger:NEDGe:IDLE?

        **Description**

        Set the idle time of Nth edge trigger.
        Query the current idle time of Nth edge trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the idle time value in scientific notation.

        **Example**

        :TRIGger:NEDGe:IDLE 0.002
        The query returns 2.000000e-03.
        """
        raise NotImplementedError()

    def edge(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:EDGE <NR1>
        :TRIGger:NEDGe:EDGE?

        **Description**

        Set the edge number of Nth edge trigger.
        Query the current edge number of Nth edge trigger.

        **Parameter**

        ====== ======== =========== =======
        Name   Type     Range       Default
        ====== ======== =========== =======
        <NR1>  Integer  1 to 65535  2
        ====== ======== =========== =======

        **Return Format**

        The query returns an integer between 1 and 65535.

        **Example**

        :TRIGger:NEDGe:EDGE
        """
        raise NotImplementedError()

    def level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NEDGe:LEVel <level>
        :TRIGger:NEDGe:LEVel?

        **Description**

        Set the trigger level in Nth edge trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in Nth edge trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:NEDGe:LEVel 0.16
        The query returns 1.600000e-01.
        """
        raise NotImplementedError()


class Trigger(BaseController):
    def __init__(self, device):
        super(Trigger, self).__init__(device)
        self.mode: Mode = Mode(self)
        self.coupling: Coupling = Coupling(self)
        self.sweep: Sweep = Sweep(self)
        self.pulse: Pulse = Pulse(self)
        self.runt: Runt = Runt(self)
        self.nth_edge: NthEdge = NthEdge(self)

    def status(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        TRIGger:STATus?

        **Description**

        Query the current trigger status.

        **Return Format**

        The query returns TD, WAIT, RUN, AUTO or STOP.
        """
        raise NotImplementedError()

    def holdoff(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:HOLDoff <value>
        :TRIGger:HOLDoff?

        **Description**

        Set the trigger holdoff time and the unit is s.
        Query the current trigger holdoff time.

        **Parameter**

        ======== ===== ============= =======
        Name     Type  Range         Default
        ======== ===== ============= =======
        <value>  Real  100ns to 10s  100ns
        ======== ===== ============= =======

        **Explanation**

        This setting is not available for the Nth edge trigger, video trigger,
        RS232 trigger, IIC trigger, SPI trigger and USB trigger.

        **Return Format**

        The query returns the trigger holdoff time in scientific notation.

        Example

        :TRIGger:HOLDoff 0.0000002
        The query returns 2.000000e-07.
        """
        raise NotImplementedError()

    def noise_reject(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NREJect <bool>
        :TRIGger:NREJect?

        **Description**

        Enable or disable noise reject.
        Query the current status of noise reject.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        ++Example**

        :TRIGger:NREJect ON
        The query returns 1.
        """
        raise NotImplementedError()

# ToDo: From HERE
    def level(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()

    def level50(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()

    def force(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()
