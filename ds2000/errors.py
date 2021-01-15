#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>
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
from typing import Any
from typing import Optional

from sys import version_info

from . import __version__

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
        """Raised when an operation attempts a state, due to duck typing.

        This should be fixed asap.
        """
        self.payload: Any = payload
        msg: str = self.__class__.BUGMSG

        if message:
            msg += "\nFor developers: " + message

        super().__init__(msg)


class DS2000Error(Error):
    pass


class DS2000StateError(Error):
    pass


class DS2000InternalSyntaxError(DS2000InternalError):
    pass
