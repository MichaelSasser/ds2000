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
    "Delay",
]


class DelayType(SubSubController):
    def greater(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        raise NotImplementedError()

    def less(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        raise NotImplementedError()

    def between(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        raise NotImplementedError()

    def outside(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TYPe <type>
        :TRIGger:DELay:TYPe?

        **Description**

        Set the delay type of delay trigger.
        Query the current delay type of delay trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
        ======= ========= ========================== =======

        **Explanation**

        GREater: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the preset time limit
        (refer to the :TRIGger:DELay:TLOWer command).

        LESS: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the preset time limit
        (refer to the :TRIGger:DELay:TUPPer command).

        GLESs: trigger when the time difference (△T) between the specified
        edges of source A and source B is greater than the lower limit of
        the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
        limit must be lower than the time upper limit.

        GOUT: trigger when the time difference (△T) between the specified
        edges of source A and source B is lower than the lower limit of the
        preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
        than the upper limit of the preset time
        (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
         limit must be lower than the time upper limit.

        **Return Format**

        The query returns GOUT, GRE, LESS or GLES.

        **Example**

        :TRIGger:DELay:TYPe GOUT
        The query returns GOUT.
        """
        raise NotImplementedError()


class Delay(SubController):
    def __init__(self, device):
        super(Delay, self).__init__(device)
        self.when: DelayType = DelayType(self)

    def signal(self, source, channel):  # SA/SB
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:SA <Source>
        :TRIGger:DELay:SA?

        :TRIGger:DELay:SB <Source>
        :TRIGger:DELay:SB?


        **Description**

        Select the trigger source of signal source A in delay trigger.
        Query the current trigger source of signal source A in delay trigger.

        Select the trigger source of signal source B in delay trigger.
        Query the current trigger source of signal source B in delay trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:DELay:SA CHANnel2
        The query returns CHAN2.

        :TRIGger:DELay:SB CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def slope(self, source, positive: bool = True):  # SLOPA/SLOPB
        """
        **Rigol Programming Guide**

        **Syntax**
        :TRIGger:DELay:SLOPA <slope>
        :TRIGger:DELay:SLOPA?

        :TRIGger:DELay:SLOPB <slope>
        :TRIGger:DELay:SLOPB?

        **Description**

        Set the edge type of edge A of delay trigger.
        Query the current edge type of edge A of delay trigger.

        Set the edge type of edge B of delay trigger.
        Query the current edge type of edge B of delay trigger.

        **Parameter**

        ======== ========= ==================== ========
        Name     Type      Range                Default
        ======== ========= ==================== ========
        <slope>  Discrete  {POSitive|NEGative}  POSitive
        ======== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:DELay:SLOPA NEGative
        The query returns NEG.

        :TRIGger:DELay:SLOPB NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TUPPer <NR3>
        :TRIGger:DELay:TUPPer?

        **Description**

        Set the upper limit of the delay time in delay trigger.
        Query the current upper limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ========== =======
        Name   Type  Range      Default
        ====== ===== ========== =======
        <NR3>  Real  2ns to 4s  2μs
        ====== ===== ========== =======

        Note: when the delay type is GLESs or GOUT, the range is
        from 12ns to 4s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the upper limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TUPPer 0.002
        The query returns 2.000000e-03.
        """
        raise NotImplementedError()

    def lower_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:DELay:TLOWer <NR3>
        :TRIGger:DELay:TLOWer?

        **Description**

        Set the lower limit of the delay time in delay trigger.
        Query the current lower limit of the delay time in delay trigger.

        **Parameter**

        ====== ===== ============= =======
        Name   Type  Range         Default
        ====== ===== ============= =======
        <NR3>  Real  2ns to 3.99s  1μs
        ====== ===== ============= =======

        Note: when the delay type is GLESs or GOUT, the range is from 2ns
        to 3.99s.

        **Explanation**

        This command is available when the delay type (refer to
        the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

        **Return Format**

        The query returns the lower limit of the delay time in scientific
        notation.

        **Example**

        :TRIGger:DELay:TLOWer 0.002
        The query returns 2.000000e-03.
        """
        raise NotImplementedError()
