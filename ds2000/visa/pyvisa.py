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

from logging import debug
from logging import error
from logging import info
from typing import Optional

# from .driver import InstrumentInfo
from .driver import VISABase


import pyvisa


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class DummyError(Exception):
    pass


class PYVISA(VISABase):
    def connect(self) -> None:
        """Connect to the instrument."""
        # arch: aur/librevisa-git
        # TCPIP::192.168.30.193::INSTR
        try:
            rm = pyvisa.ResourceManager()
            info(f"Available Devices: {rm.list_resources()}")
            # ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
            self.__instrument = rm.open_resource(self.address)
            # self.__instrument = vxi11.Instrument(self.address)
            # self.info = InstrumentInfo(*self.ask("*IDN?").split(","))
        except OSError as e:
            raise OSError(
                "Your backend seems not to be configured correctly. "
                "Make sure to follow the gude: "
                "https://pyvisa.readthedocs.io/en/latest/introduction/"
                "configuring.html"
            ) from e
        except AttributeError as e:
            raise AttributeError(
                "To use PyVISA Correctly, you need to use a correct ressource "
                "name. Please check the PyVISA Docs:"
                "https://pyvisa.readthedocs.io/en/latest/introduction/"
                "names.html ."
            ) from e

    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        # self.__instrument.close()

    def communicate(self, msg: str) -> Optional[str]:
        """Write and read afterwards from a instrument."""
        answer: Optional[str] = None
        try:
            answer = self.__instrument.query(msg)
        except DummyError as e:
            # TODO: Raise before first release.
            error(f"Error while asking: {e}")
        finally:
            debug(f'Asked: "{msg}", Answered: "{answer}"')
        return answer

    def write(self, msg: str) -> None:
        """Write to the instrument but don't wait for a response."""
        try:  # Probably just for development
            self.__instrument.write(msg)
        except DummyError as e:
            # TODO: Raise before first release.
            error(f"Error while writing: {e}")
        finally:
            debug(f'Written: "{msg}"')

    def read_raw(self) -> Optional[bytes]:
        """Read binary data from the instrument."""
        msg: Optional[bytes] = None
        try:
            msg = self.__instrument.read_raw()
        except DummyError as e:
            # TODO: Raise before first release.
            error(f"Error while writing: {e}")
        return msg


# vim: set ft=python :
