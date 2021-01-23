#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
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

import pytest

from ds2000 import DS2000
from ds2000.visa.driver import VISADriver


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


@pytest.fixture(scope="session", autouse=True)
def dev():
    """Use "dev" fixture to initialize the debug instrument."""
    # Setup
    # print("setting up", item)
    dev: DS2000 = DS2000("1.1.1.1", VISADriver.DEBUG_DRIVER)

    # Exercise - None

    # Verify - None

    # Cleanup -None
    return dev


# vim: set ft=python :
