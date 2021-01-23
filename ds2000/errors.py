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
from __future__ import annotations

from sys import version_info
from typing import Any
from typing import Callable
from typing import List
from typing import Optional

from .__version__ import __version__
from .visa.driver import VISADriver


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Error(Exception):
    """Base class for exceptions in this module."""


class DS2000InternalError(Error):
    BUGMSG = (
        "If you discover this message, please try updating the "
        "ds2000 package. If you see this message again, we would "
        'be glad, if you would hand in a "Bug report" at '
        "https://github.com/MichaelSasser/ds2000/issues "
        "with the complete traceback.\n"
        f"Python version: {version_info.major}.{version_info.minor}."
        f"{version_info.micro} {version_info.releaselevel}\n"
        f"ds2000 version: {__version__} \n"
    )

    def __init__(
        self, message: Optional[str] = None, payload: Any = None
    ) -> None:
        """Raise when an operation attempts a state, due to duck typing.

        This should be fixed asap.
        """
        self.payload: Any = payload
        msg: str = self.__class__.BUGMSG

        if message:
            msg += "\nFor developers: " + message

        super().__init__(msg)


class DS2000ExampleFoundBugError(DS2000InternalError):
    def __init__(
        self, msg: str, examples: Callable[[str, str, bool], None]
    ) -> None:
        message: str = f"DEBUG_DUMMY: {msg=}, {examples=}"
        super().__init__(message, None)


class DS2000Error(Error):
    pass


class DS2000StateError(DS2000InternalError):
    pass


class DS2000InternalSyntaxError(DS2000InternalError):
    pass


class DS2000DriverNotFoundError(Error):
    def __init__(
        self,
        driver: VISADriver,
        drivers_available: List[VISADriver],
    ) -> None:
        """Raise, when no Instrument driver was found."""
        # TODO: Better description
        self.drivers_available = drivers_available[:]  # deepcopy
        # Remove the alway available Debug driver.
        self.drivers_available.remove(VISADriver.DEBUG_DRIVER)
        if len(self.drivers_available) > 0:
            super().__init__(
                "The requested driver is not available. You need "
                f'to install the requested driver "{driver}" '
                "or choose another driver: "
                f"{self.drivers_available}."
            )
        else:
            super().__init__(
                "No compatible VISA driver is available on your"
                "system. Please read the documentation:"
                "https://bit.ly/3bMsjP9."
            )
