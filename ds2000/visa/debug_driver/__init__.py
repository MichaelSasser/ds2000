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

from inspect import currentframe
from inspect import getattr_static
from inspect import getframeinfo
from logging import debug
from logging import error
from types import FrameType
from typing import Any, List
from typing import Optional

import coloredlogs  # TODO: Delete before first release

from .state import State
from .state import StorageDBType
from .parser import parse_msg, parse_values
from .parser import Command
from ds2000.visa.driver import InstrumentInfo
from ds2000.visa.driver import VISABase
from ds2000.errors import DS2000ExampleFoundBugError
from ds2000.common import Example
from ds2000.common import get_examples

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# TODO: Delete before first release
def setup_logging(debug_mode: bool) -> None:
    coloredlogs.DEFAULT_LOG_FORMAT = (
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    coloredlogs.DEFAULT_LOG_LEVEL = 0 if debug_mode else 21
    coloredlogs.install()


class DebugDriver(VISABase):

    # TODO: When testing this driver is will be choosen and replaced afterwards
    #       by a special testing version? Or should this driver get the testing
    #       version?
    def __init__(self, address: str):
        setup_logging(True)  # TODO: Delete before first release
        # if True: raise error on missmatch between msg and examples
        self.check_questions: bool = True
        self.state: State = State()

        super(self.__class__, self).__init__(address)

    def connect(self):
        """Connect to the instrument."""
        self.info = InstrumentInfo(
            "Dunder Mifflin Paper Company, Inc",
            "Dummy",
            "1234567890",
            "1.0.0",
        )
        print("This is the DEBUG_DRIVER driver. Please keep in mind to "
              "Enable debug level logging to see the output.")
        debug("Connected to DEBUG_DRIVER")

    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        debug("Disconnected from DEBUG_DRIVER")

    def ask(self, msg: str) -> Optional[str]:
        """Write and read afterwards from a instrument."""
        # Extract the examples from the function that has called this one
        # To give at least a plausible output, even, if it is fixed.
        # If this fails, give a "1.0" back, which should work with
        # str, int, list, tuple, sets, float.

        answer: Optional[str] = None
        command: Command = parse_msg(msg)
        examples: List[Example] = []

        try:
            examples = get_examples(self.__get_callers_doc())
        except Exception as e:
            debug("Exception occured while attempting to get an "
                  f"Example:\n{e}")

        # Check if the path of the question is the same as in the examples
        if self.check_questions:
            self.__check_questions(msg, examples)

        self.__mark_questions(msg, examples)

        # Devide, if this is a question -> get entry or not -> set entry
        if command.is_question:
            answer = parse_values(self.state.get(command, examples))
        else:
            self.state.set(command)
            answer = None

        debug(f'Asked: "{msg}", Answered: "{answer}"')
        return answer

    def write(self, msg: str) -> None:
        """Write to the instrument but don't wait for a response."""
        debug(f'Written: "{msg}"')

    def read_raw(self) -> bytes:
        """Read binary data from the instrument."""
        debug("Written b'1.0' (Fixed dummy value)")
        return b"1.0"  # Should work for str, int, list, float

    @staticmethod
    def __mark_questions(
        msg: str,
        examples: List[Example],
    ) -> None:
        """Mark a `Example`, if it's path matches the path in the `msg`."""
        for path, example in zip(
                DebugDriver.__get_paths_from_examples(examples),
                examples):
            # remove tailing "?"
            if msg.endswith("?"):
                msg = msg[:-1]

            # compare paths
            if msg.split(" ")[0] == path:
                example.marked = True

    @staticmethod
    def __get_paths_from_examples(examples: List[Example]) -> List[str]:
        """Extract path from question.

        **Example**

        "TRIGger:COUPling LFReject" -> TRIGger:COUPling.
        """
        return [example.question.split(" ", 1)[0] for example in examples]

    @staticmethod
    def __check_questions(
            msg: str,
            examples: List[Example],
            fail_on_err: bool = False,
    ) -> None:
        if examples is None:
            debug("DEBUG_DRIVER.__check_question: the examples was None")
            return

        # TODO: Should'n match exactly?
        # check if there is at least one path of an examples, that matches the
        # msg given by the original function call (Func, SFunc SSFunc).
        # If there is `None` check if raise an error or just write an error
        # message.
        if not any(
                (True
                 for path
                 in DebugDriver.__get_paths_from_examples(examples)
                 if msg.startswith(path))
        ):
            if fail_on_err:
                raise DS2000ExampleFoundBugError(f"{msg} != {examples}")
            else:
                error(f"DEBUG_DRIVER.__check_question: {msg=} != {examples=}")

    @staticmethod
    def __get_callers_doc() -> Optional[str]:
        """Get the __doc__ of the last called method"""
        frame: Optional[FrameType] = currentframe().f_back.f_back
        try:
            methode_name: str = getframeinfo(frame).function
            last_class: Any = getattr_static(frame.f_locals["self"],
                                             methode_name,
                                             None)
            doc: str = last_class.__doc__
        finally:
            del last_class
            del frame
        return doc

# vim: set ft=python :
