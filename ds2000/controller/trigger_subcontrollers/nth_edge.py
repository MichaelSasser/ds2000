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

from ds2000.controller import SubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "NthEdge",
]


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