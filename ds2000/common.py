#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018-2021  Michael Sasser <Michael@MichaelSasser.org>
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
from typing import Any
from typing import Optional
from typing import Union
from typing import NamedTuple
from typing import List
from logging import debug
from logging import error

from .errors import DS2000InternalSyntaxError
from .visa.driver import VISABase
from .math.format import get_prefix


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Example(NamedTuple):
    question: str
    answer: str


class Func:  # pylint: disable=R0903
    def __init__(self, dev) -> None:
        self.dev = dev
        self.instrument: VISABase = dev.instrument


class SFunc:  # pylint: disable=R0903
    def __init__(self, dev) -> None:
        self.sdev = dev
        self.instrument: VISABase = dev.instrument


class SSFunc:  # pylint: disable=R0903
    def __init__(self, dev) -> None:
        self.ssdev = dev
        self.instrument: VISABase = dev.instrument


def check_input(
    arg: Any,
    arg_name: str,
    arg_type: Optional[Any] = None,
    mini: Union[None, int, float] = None,
    maxi: Union[None, int, float] = None,
    unit: Optional[str] = None,
    ext_type_err: Optional[str] = None,
    ext_range_err: Optional[str] = None,
) -> None:
    """Validating input type and input value is a oftten done thing here.
    To not repeate it the whole time, this should help quite a bit.

    Type and range checks are optional. If you only want to check for one, leave
    the other arguments of this function as None. One of both is needed.

    To format the error message nicely, use the unit argument. Use "s" for
    example, if you want to format 10.E-6 as 10µs. If disabled it will fill the
    placeholder with 0.00001 without "s".

    mini and maxi need to be the same type.

    :param arg: The argument, to validate.
    :param arg_name: The name of the argument as string.
    :param arg_type: The type the argument should be.
    :param mini: The min value of the argument range.
    :param maxi: The max value of the argument range.
    :param unit: The unit of the argument, if it should be formated.
    :param ext_type_err: Some extended error msg, if a type error will occure.
    :param ext_range_err: Some extended error msg, if a Value will occure.
    :return: None
    """

    # Check, if this function is used as intended: One or both checks are
    # active.
    if (arg_type is None) and (mini is None or maxi is None):
        raise DS2000InternalSyntaxError(
            "This check does nothing. If this is "
            "intended, remove this check. "
            "otherwhise make sure it checks for "
            "the argument type and/or the argument "
            "value range."
        )
    # Check, if this function is used as intended: mini and maxi have the same
    # type.
    if (mini is None or maxi is None) and type(mini) != type(maxi):
        raise DS2000InternalSyntaxError(
            "The arguments mini and maxi have"
            "a different type. Make sure you"
            "always compare same types.\n"
            f"mini: {type(mini)}\n"
            f"maxi: {type(maxi)}\n"
            f"Keep in mind. 1 is an integer and "
            f"1.0 is a float type."
        )

    # Check for the argument type.
    if (arg_type is not None) and not isinstance(arg, arg_type):
        raise TypeError(
            f'The argument "{arg_name}" needs to be of type '
            f"{type(arg)}. You entered {arg} ({type(arg)})"
            f"{'. ' if ext_type_err else '.'}"
            f"{ext_type_err if ext_type_err else ''}"
        )

    # Check for the argument range.
    if (mini is not None) and (maxi is not None) and not (mini <= arg <= maxi):
        raise ValueError(
            f'The argument "{arg_name}" needs to be in between '
            f"{get_prefix(mini).formatted+unit if unit else mini}"
            f" and "
            f"{get_prefix(maxi).formatted+unit if unit else maxi}."
            f" You entered "
            f"{get_prefix(arg).formatted+unit if unit else arg}"
            f"{'. ' if ext_range_err else '.'}"
            f"{ext_range_err if ext_range_err else ''}"
        )


def check_level(level: float, scale: float, offset: float):
    min_rng = -5.0 * scale - offset
    max_rng = 5.0 * scale - offset

    if not isinstance(level, float) or not min_rng <= level <= max_rng:
        ValueError(
            f'"level" must be of type float and between '
            f"{min_rng}..{max_rng}. You entered type {type(level)}."
        )


def get_example(doc: str) -> Optional[Example]:
    """Extract the example of a docstring."""
    if doc is None:
        error("DEBUG_DRIVER.__get_example -> doc is None")
        return None
    lines: List[str] = [s.strip()
                        for s in doc.split("**Example**")[1].splitlines()
                        if s.strip()
                        ]
    # Remove lines at the end that are not part of the example
    while not lines[-1].startswith("The query returns"):
        lines.pop()

    # Check if there are only two lines left
    if not len(lines) == 2:
        error("DEBUG_DRIVER.__get_example -> More then two lines detected")
        return None

    if not lines[0].startswith(":"):
        error("DEBUG_DRIVER.__get_example -> Question dosn't start with \".\"")
        return None

    # Remove "The query returns " and "." of the answer
    lines[1] = lines[1].replace("The query returns ", "")[:-1]

    debug(f"DEBUG_DRIVER.__get_example -> Example Q&A: {lines}")

    return Example(*lines)
