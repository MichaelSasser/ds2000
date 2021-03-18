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

import re

from logging import debug
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Pattern
from typing import Tuple


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

remove_value: Pattern = re.compile("[a-z]")


class Command(NamedTuple):
    path: Tuple[str, ...]
    value: Optional[Tuple[str, ...]]
    is_question: bool


def parse_msg(msg: str) -> Command:  # TODO: parse types
    """Parse a message and generate an Command."""
    t: List[str] = msg.split(" ")
    path: List[str] = t[0].split(":")[1:]  # First is empty
    is_question: bool = path[-1].endswith("?")
    if is_question:
        path[-1] = path[-1].replace("?", "")
    # Reassemble and split by
    value: Tuple[str, ...] = tuple(" ".join(t[1:]).split(","))
    command = Command(tuple(path), value, is_question)
    debug(f"Command: {command}")
    return command


def parse_values(values: Tuple[str, ...]) -> str:  # TODO: parse types
    """Parse a value and return a str."""
    global remove_value
    if len(values) == 1:
        debug("parse_values: found single string inside values: List[str]")
        try:
            value: float = float(values[0])
            debug(f"parse_values: string is numeric: {values[0]}")
            return str(value)
        except ValueError:
            pass
        return remove_value.sub("", values[0])

    return ",".join([remove_value.sub("", val) for val in values])


# vim: set ft=python :
