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

from abc import ABC
from abc import abstractmethod
from enum import Enum
from enum import auto
from types import TracebackType
from typing import Any
from typing import NamedTuple
from typing import Optional
from typing import Type


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class VISADriver(Enum):
    VXI11 = (auto(),)  # python-vxi11 - pure python
    PYVISA = (auto(),)  # pyvisa - uses NI VISA
    PYVISA_PY = (auto(),)  # pyvisa-py - limited subset of pyvisa, pure python
    DEBUG_DRIVER = (auto(),)  # a dummy to debug, mimics a instrument


class InstrumentInfo(NamedTuple):
    company: Optional[str]
    model: Optional[str]
    serial: Optional[str]
    software_version: Optional[str]


class VISABase(ABC):
    def __init__(self, address: str):
        self.__instrument: Any = None
        self.address: str = address
        self.info: InstrumentInfo = InstrumentInfo(None, None, None, None)

    @abstractmethod
    def connect(self) -> None:
        """Connect to the instrument."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from the instrument."""
        pass

    @abstractmethod
    def communicate(self, msg: str) -> Optional[str]:
        """Write and read afterwards from a instrument."""
        pass

    def ask(self, msg: str) -> str:
        """Write and read afterwards from a instrument."""
        answer: Optional[str] = self.communicate(msg)
        if answer is None:  # Report if answer is None -> str
            raise TypeError("BUG: The answer is None, but should be str")
        return answer

    def say(self, msg: str) -> None:
        """Do the same as ``ask`` but consume the answer."""
        answer: Optional[str] = self.communicate(msg)
        if answer is not None:  # Report if answer is not None -> None
            raise TypeError("Bug: The answer is not None, but should be None.")

    @abstractmethod
    def write(self, msg: str) -> None:
        """Write to the instrument but don't wait for a response."""
        pass

    @abstractmethod
    def read_raw(self):
        """Read binary data from the instrument."""
        pass

    def __enter__(self) -> VISABase:
        """Connect to the Instrument with the `with` statement."""
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Connect to the Instrument with the `with` statement."""
        self.disconnect()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__}({self.info.serial})"


# vim: set ft=python :
