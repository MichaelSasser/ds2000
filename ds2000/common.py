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
from dataclasses import dataclass
from logging import debug
from logging import error
from typing import Any
from typing import List
from typing import Optional
from typing import Union

from .errors import DS2000InternalSyntaxError
from .math.format import get_prefix
from .visa.driver import VISABase


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


@dataclass
class Example:
    question: str
    answer: str
    marked: bool = False  # Marked as the one which has been asked.


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
    min_: Union[None, int, float] = None,
    max_: Union[None, int, float] = None,
    unit: Optional[str] = None,
    ext_type_err: Optional[str] = None,
    ext_range_err: Optional[str] = None,
) -> None:
    """Validate input type and input value.

    Validate input type and input value is a oftten done thing here.
    To not repeate it the whole time, this should help quite a bit.

    Type and range checks are optional. If you only want to check for one,
    leave the other arguments of this function as None. One of both is needed.

    To format the error message nicely, use the unit argument. Use "s" for
    examples, if you want to format 10.E-6 as 10µs. If disabled it will fill
    the placeholder with 0.00001 without "s".

    mini and maxi need to be the same type.

    :param arg: The argument, to validate.
    :param arg_name: The name of the argument as string.
    :param arg_type: The type the argument should be.
    :param min_: The min value of the argument range.
    :param max_: The max value of the argument range.
    :param unit: The unit of the argument, if it should be formated.
    :param ext_type_err: Some extended error msg, if a type error will occure.
    :param ext_range_err: Some extended error msg, if a Value will occure.
    :return: None
    """

    # Check, if this function is used as intended: One or both checks are
    # active.
    if (arg_type is None) and (min_ is None or max_ is None):
        raise DS2000InternalSyntaxError(
            "This check does nothing. If this is "
            "intended, remove this check. "
            "otherwhise make sure it checks for "
            "the argument type and/or the argument "
            "value range."
        )
    # Check, if this function is used as intended: min_ and max_ have the same
    # type.
    if (min_ is None or max_ is None) and type(min_) != type(max_):
        raise DS2000InternalSyntaxError(
            "The arguments min_ and max_ have"
            "a different type. Make sure you"
            "always compare same types.\n"
            f"min_: {type(min_)}\n"
            f"max_: {type(max_)}\n"
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
    if (min_ is not None) and (max_ is not None) and not (min_ <= arg <= max_):
        raise ValueError(
            f'The argument "{arg_name}" needs to be in between '
            f"{get_prefix(min_).formatted + unit if unit else min_}"
            f" and "
            f"{get_prefix(max_).formatted + unit if unit else max_}."
            f" You entered "
            f"{get_prefix(arg).formatted + unit if unit else arg}"
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


def get_examples(doc: str) -> List[Example]:
    """Extract the examples of a docstring."""
    # If ther is no "doc", return an empty list
    if doc is None:
        error("DEBUG_DRIVER.__get_example -> doc is None")
        return []

    # Get the lines that are not empy from "doc"
    lines: List[str] = [
        s.strip()
        for s in doc.split("**Example**")[1].splitlines()
        if s.strip()
    ]

    # Remove lines at the end that are not part of the examples
    # e.g. There can be followup documentation after **Example**,
    # but ther shouldn't be a line starting with "The query returns",
    # except the last answer
    while not lines[-1].startswith("The query returns"):
        lines.pop()

    # Return with an empty list if the lines don't have an even number.
    # There should always be a question and an answer.
    if not len(lines) % 2 == 0:
        error(
            "DEBUG_DRIVER.__get_example -> More then two/four lines "
            "detected"
        )
        return []

    examples: List[Example] = []
    question: Optional[str] = None
    answer: Optional[str] = None
    line_must_be_answer: bool = False
    for line in lines:
        if line.startswith(":"):  # Qusetion line
            if question is not None:
                raise DS2000InternalSyntaxError(
                    "There where two questions "
                    "next to each other. Check "
                    "docs"
                )
            question = line
            line_must_be_answer = True
            continue  # an answer can only be in the next iteration

        if line.startswith("The query returns "):  # Answer line
            if answer is not None:
                raise DS2000InternalSyntaxError(
                    "There where two answers "
                    "next to each other. Check "
                    "docs"
                )
            # Remove "The query returns " and "." (last char) of the answer
            answer = line.replace("The query returns ", "")[:-1]

        if question is not None and answer is not None:
            examples.append(Example(question, answer))
            debug(f"DEBUG_DRIVER.__get_example -> New Example: {lines}")
            question = None
            answer = None
            line_must_be_answer = False
            continue

        # Ther is no answer after a question -> err
        if line_must_be_answer:
            raise DS2000InternalSyntaxError(
                "Missing answer line after " "question line. Check docs."
            )

    return examples


def channel_as_int(channel_msg: str) -> int:
    return int(channel_msg[-1])
