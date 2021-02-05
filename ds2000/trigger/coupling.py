#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020-2021  Michael Sasser <Michael@MichaelSasser.org>

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
from __future__ import annotations

from ds2000.common import SFunc
from ds2000.errors import DS2000StateError
from ds2000.enums import TriggerCouplingEnum


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Coupling(SFunc):
    def set_ac(self) -> None:
        """Select the desired trigger coupling mode.

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
        self.instrument.ask(":TRIGger:COUPling AC")

    def set_dc(self) -> None:
        """Select the desired trigger coupling mode.

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
        self.instrument.ask(":TRIGger:COUPling DC")

    def set_lf_reject(self) -> None:
        """Select the desired trigger coupling mode.

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
        self.instrument.ask(":TRIGger:COUPling LFReject")

    def set_hf_reject(self) -> None:
        """Select the desired trigger coupling mode.

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
        self.instrument.ask(":TRIGger:COUPling HFReject")

    def status(self) -> TriggerCouplingEnum:
        """Query the current trigger coupling mode.

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
        answer: str = self.instrument.ask(":TRIGger:COUPling?")
        if answer == "AC":
            return TriggerCouplingEnum.AC
        if answer == "DC":
            return TriggerCouplingEnum.DC
        if answer == "LFR":
            return TriggerCouplingEnum.LF_REJECT
        if answer == "HFR":
            return TriggerCouplingEnum.HF_REJECT
        raise DS2000StateError()
