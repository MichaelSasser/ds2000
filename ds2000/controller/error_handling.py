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
from typing import Any
from sys import version_info
from pkg_resources import get_distribution

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Ds2000Exception",
    "Ds2000StateError",
    "Ds2000InternalSyntaxError",
]


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class Ds2000Exception(Error):  # ToDo: Change to Ds2000Error
    pass


class Ds2000StateError(Error):
    pass


class Ds2000InternalSyntaxError(Error):
    DBGMSG = "If you discover this message, please try updating the " \
             "ds2000 package. If you see this message again, we would " \
             "be glad, if you would hand in a \"Bug report\" at " \
             "https://github.com/MichaelSasser/ds2000/issues " \
             "with the complete traceback.\n" \
             f"Python version: {version_info.major}.{version_info.minor}." \
             f"{version_info.micro} {version_info.releaselevel}\n" \
             f"ds2000 version: {get_distribution('ds2000').version} \n"

    def __init__(self, message: Any = None, *args, **kwargs):
        """Raised when an operation attempts a state, due to duck typing, that's
        not allowed and should be fixed asap.
        """
        msg = self.__class__.DBGMSG
        if message:
            msg += '\nFor developers: ' + str(message)

        super().__init__(msg, *args, **kwargs)
