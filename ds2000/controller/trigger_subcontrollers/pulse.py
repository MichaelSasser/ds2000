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
    "Pulse",
]


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

