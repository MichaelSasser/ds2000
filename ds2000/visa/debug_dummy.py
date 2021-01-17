#!/usr/bin/env python
# ds2000
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
from logging import error
from logging import debug

from .driver import VISABase
from .driver import InstrumentInfo


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class DebugDummy(VISABase):

    # TODO: When testing this driver is will be choosen and replaced afterwards
    #       by a special testing version? Or should this driver get the testing
    #       version?
    def connect(self):
        """Connect to the instrument."""
        self.info = InstrumentInfo(
            "Dunder Mifflin Paper Company, Inc",
            "Dummy",
            "1234567890",
            "1.0.0",
        )
        print("This is the DEBUG_DUMMY driver. Please keep in mind to"
              "Enable debug level logging to see the output.")
        debug("Connected to DEBUG_DUMMY")

    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        debug("Disconnected from DEBUG_DUMMY")

    def ask(self, msg: str) -> str:
        """Write and read afterwards from a instrument."""
        debug(f'Asked: "{msg}", Answered: "1.0" (Fixed dummy value)')
        return "1.0"  # Should work for str, int, list, float

    def write(self, msg: str) -> None:
        """Write to the instrument but don't wait for a response."""
        debug(f'Written: "{msg}"')

    def read_raw(self) -> bytes:
        """Read binary data from the instrument."""
        debug("Written b'1.0' (Fixed dummy value)")
        return b"1.0"  # Should work for str, int, list, float

# vim: set ft=python :
