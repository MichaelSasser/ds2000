#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

from typing import NamedTuple

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class Prefixed(NamedTuple):
    value: float
    prefix: str
    divisor: float
    formatted: str


def get_prefix(value: float) -> Prefixed:
    prefixes = {
        -24: "y",  # yocto
        -21: "z",  # zepto
        -18: "a",  # atto
        -15: "f",  # femto
        -12: "p",  # pico
        -9: "n",  # nano
        -6: "µ",  # micro
        -3: "m",  # milli
        # -2 : 'c',  # centi (Not used in eletronics)
        # -1 : 'd',  # deci (Not used in eletronics)
        0: "",  # None
        # 1  : 'da',  # deca (Not used in eletronics)
        # 2  : 'h',  # hecto (Not used in eletronics)
        3: "k",  # kilo
        6: "M",  # mega
        9: "G",  # giga
        12: "T",  # tera
        15: "P",  # peta
        18: "E",  # exa
        21: "Z",  # zetta
        24: "Y",  # yotta
    }

    negative = False
    if value < 0:
        value *= -1.0
        negative = True

    power = 0
    if value != 0:
        while value < 1:
            value *= 1000.0
            power -= 3

    while value >= 1000.0:
        value /= 1000.0
        power += 3

    return Prefixed(
        value=float((-value) if negative else value),
        prefix=prefixes[power],
        divisor=float(power),
        formatted=f"{value}{prefixes[power]}",
    )
