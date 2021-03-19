#!/usr/bin/env python
# ds2000
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
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Union

from ds2000.common import Example
from ds2000.errors import DS2000InternalSyntaxError

from .parser import Command


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

# It is basicly StorageDBType = Dict[str, Union[Command, StorageDBType]]
# StorageDBType = Union[Optional[Union[Dict[str, Any], List[str]]], List[str]]
StorageDBKeyType = str
StorageDBValueType = Union[str, Tuple[str, ...], "StorageDBType"]  # type: ignore
StorageDBType = Dict[str, Union[str, Tuple[str, ...], "StorageDBType"]]  # type: ignore


class State:

    """Store and recall the internal state of the instrument.

    **Why is self.db not flat?**
    During debuging it is useful to get an overview of a specific
    subfunction/subsystem of the instrument (e.g. trigger->coupling)
    to get an idea, what's the state of it.

    """

    DUMMY_VALUE: Tuple[str, ...] = tuple(
        "1.0",
    )

    def __init__(self):

        self.db: StorageDBType = {}

    def set(self, command: Command) -> None:
        """Set a new value to the db."""
        if command.value is None:
            raise DS2000InternalSyntaxError(
                f"Setting the db with an Value None. {command=}"
            )
        self.__set_nested(command.path, command.value)
        debug(f"CURRENT DB: {self.db}")  # TODO: Remove

    # ToDo: Currently only supports string as return.
    def get(
        self, command: Command, examples: Optional[Tuple[Example, ...]]
    ) -> Tuple[str, ...]:
        """Get a already stored or a fallback value from the db."""
        answer: Tuple[str, ...] = self.__class__.DUMMY_VALUE
        try:  # Try to find entry in self.db
            entry: StorageDBValueType = self.__get_nested(command.path)
            if isinstance(entry, tuple):
                return entry
            raise AttributeError()  # Todo: Reorder function code
        except AttributeError:  # No entry found in self.db
            debug(f"Key {command.path} found in storage db")

            if examples:  # Example found in docs.
                answers: Tuple[str, ...] = tuple(
                    example.answer for example in examples if example.marked
                )
                if answers:
                    debug(f'Example found. Returning "{answers[0]}"')
                    return tuple(
                        answers[0],
                    )
                debug('No Example found. Returning default dummy value "1.0"')
        return answer

    def __get_nested(self, keys: Tuple[str, ...]) -> StorageDBValueType:
        """Use a list of keys to get a nested value from the self.db dict.

        **Example**

        You want to get :python: `['u', 'v']` from
        :python: `self.db = {'a': {'b': {'c': ['u', 'v']}}` you would use this
        methode like :python: `self.__get_nested(["a", "b", "c"]`
        """
        db: StorageDBType = self.db  # ref
        for key in keys:
            db = db.get(key, None)  # type: ignore
        return db

    def __set_nested(self, keys: Tuple[str, ...], values: Tuple[str, ...]):
        """Use a list of keys to set a nested value inside the self.db dict.

        **Example**

        You want to set :python:`["u", "v"]` inside
        :python:`self.db = {}` you would use this
        methode like :python:`self.__set_nested(('a', 'b', 'c'), ('u', 'v'))`.
        Now the condition :python:`self.db == {'a': {'b': {'c': ('u', 'v')}}}`
        is :python:`True`.
        """
        db: StorageDBType = self.db  # create ref.
        for key in keys[:-1]:
            db = db.setdefault(key, {})  # type: ignore
        db[keys[-1]] = values

    # TODO:
    # def __getitem__(self, key: str) -> Any:
    #     pass
    #
    # def __setitem__(self, key, value):
    #     pass
    #
    # def to_json() -> JSONType:
    #     pass

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__}()"


# vim: set ft=python :
