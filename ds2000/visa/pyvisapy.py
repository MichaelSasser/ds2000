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


# from logging import debug
# from logging import error
# from typing import Optional
#
# from .driver import InstrumentInfo
# from .driver import VISABase


# import pyvisa-py


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

raise NotImplementedError()


class PYVISAPY(VISABase):
    pass


#     def connect(self):
#         """Connect to the instrument."""
#         self.__instrument = vxi11.Instrument(self.address)
#         self.info = InstrumentInfo(*self.ask("*IDN?").split(","))
#
#     def disconnect(self):
#         """Disconnect from the instrument."""
#         self.__instrument.close()
#
#     def ask(self, msg: str) -> str:
#         """Write and read afterwards from a instrument."""
#         answer: Optional[str] = None
#         try:
#             answer = self.__instrument.ask(msg)
#         except vxi11.vxi11.Vxi11Exception as e:
#             # TODO: Raise before first release.
#             error(f"Error while asking: {e}")
#         finally:
#             debug(f'Asked: "{msg}", Answered: "{answer}"')
#         return answer
#
#     def write(self, msg: str) -> None:
#         """Write to the instrument but don't wait for a response."""
#         try:  # Probably just for development
#             self.__instrument.write(msg)
#         except vxi11.vxi11.Vxi11Exception as e:
#             # TODO: Raise before first release.
#             error(f"Error while writing: {e}")
#         finally:
#             debug(f'Written: "{msg}"')
#
#     def read_raw(self) -> bytes:
#         """Read binary data from the instrument."""
#         msg: Optional[bytes] = None
#         try:
#             msg = self.__instrument.read_raw()
#         except vxi11.vxi11.Vxi11Exception as e:
#             # TODO: Raise before first release.
#             error(f"Error while writing: {e}")
#         return msg

# vim: set ft=python :
