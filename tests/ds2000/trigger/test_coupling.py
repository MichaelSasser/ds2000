#!/usr/bin/env python
# ds2000 - install and manage your MSFS2020 addons
# Copyright (C) 2021  Michael Sasser <Michael@MichaelSasser.org>

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

from ds2000.trigger.coupling import CouplingEnum


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def test_coupling_set_ac(dev) -> None:
    """Test the trigger coupling mode.

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
    # Setup
    desired: CouplingEnum = CouplingEnum.AC
    dev.trigger.coupling.set_ac()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_coupling_set_dc(dev) -> None:
    """Test the trigger coupling mode.

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
    # Setup
    desired: CouplingEnum = CouplingEnum.DC
    dev.trigger.coupling.set_dc()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_coupling_set_lf_reject(dev) -> None:
    """Test the trigger coupling mode.

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
    # Setup
    desired: CouplingEnum = CouplingEnum.LF_REJECT
    dev.trigger.coupling.set_lf_reject()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_coupling_set_hf_reject(dev) -> None:
    """Test the trigger coupling mode.

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
    # Setup
    desired: CouplingEnum = CouplingEnum.HF_REJECT
    dev.trigger.coupling.set_hf_reject()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == desired

    # Cleanup - None


# vim: set ft=python :
