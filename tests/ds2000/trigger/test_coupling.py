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
    # Setup
    dev.trigger.coupling.set_ac()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == CouplingEnum.AC

    # Cleanup - None


def test_coupling_set_dc(dev) -> None:
    # Setup
    dev.trigger.coupling.set_dc()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == CouplingEnum.DC

    # Cleanup - None


def test_coupling_set_lf_reject(dev) -> None:
    # Setup
    dev.trigger.coupling.set_lf_reject()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == CouplingEnum.LF_REJECT

    # Cleanup - None


def test_coupling_set_hf_reject(dev) -> None:
    # Setup
    dev.trigger.coupling.set_hf_reject()

    # Exercise
    actual: CouplingEnum = dev.trigger.coupling.status()

    # Verify
    assert actual == CouplingEnum.HF_REJECT

    # Cleanup - None


# vim: set ft=python :
