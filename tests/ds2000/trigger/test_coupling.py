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

from typing import Optional

from ds2000.common import get_example
from ds2000.visa.debug_driver import Example

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# def test_coupling(dev) -> None:
#     # Setup
#     desired = "AC"
#
#     # Exercise
#     actual = dev.trigger.coupling.ac()
#
#     # Verify
#     assert desired == actual

    # Cleanup - None

# def test_coupling(dev) -> None:
#     # Setup
#     func = dev.trigger.coupling.ac
#     example: Optional[Example] = get_example(func.__doc__)
#     # Exercise
#     print(example.question)
#     actual = func(example.question) == example.answer
#     # Verify
#     assert actual
#
#     # Cleanup - None

def test_coupling(dev) -> None:
    # Setup
    dev.trigger.coupling.ac()

    # Exercise
    actual = dev.trigger.coupling.status()

    # Verify
    assert actual == "AC"

    # Cleanup - None

# vim: set ft=python :
