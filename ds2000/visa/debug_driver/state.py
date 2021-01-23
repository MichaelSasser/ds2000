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
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from ds2000.common import Example
from .parser import Command

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

# It is basicly StorageDBType = Dict[str, Union[Command, StorageDBType]]
StorageDBType = Union[Optional[Union[Dict[str, Any], List[str]]], List[str]]


class State:
    """Store and recall the internal state of the instrument.

    **Why is self.db not flat?**
    During debuging it is useful to get an overview of a specific
    subfunction/subsystem of the instrument (e.g. trigger->coupling)
    to get an idea, what's the state of it.

    """

    DUMMY_VALUE: List[str] = [
        "1.0",
    ]

    def __init__(self):

        self.db: StorageDBType = {}

    def set(self, command: Command) -> None:
        """Set a new value to the db."""
        self.__set_nested(command.path, command.value)
        debug(f"CURRENT DB: {self.db}")  # TODO: Remove

    def get(self, command: Command, examples: List[Example]) -> StorageDBType:
        """Get a already stored or a fallback value from the db."""
        answer: StorageDBType = self.__get_nested(command.path)
        try:
            if answer is not None:
                debug(
                    f"State.get: Key {command.path} found in storage db: "
                    f"{answer}"
                )
                return answer
        except KeyError:
            pass
        debug(f"State.get: Key {command.path} not found in storage db.")

        if examples:
            answers: List[str] = [
                example.answer for example in examples if example.marked
            ]
            if answers:
                debug(f'State.get: Example found. Returning "{answers[0]}"')
                return [
                    answers[0],
                ]
        debug(
            "State.get: Example not found. Returning default dummy value "
            '"1.0"'
        )
        return self.__class__.DUMMY_VALUE

    def __get_nested(self, keys: Tuple[str, ...]) -> StorageDBType:
        """Use a list of keys to get a nested value from the self.db dict.

        **Example**

        You want to get :python: `['u', 'v']` from
        :python: `self.db = {'a': {'b': {'c': ['u', 'v']}}` you would use this
        methode like :python: `self.__get_nested(["a", "b", "c"]`
        """
        nxt: Union[StorageDBType] = self.db
        for key in keys:
            if (nxt := nxt.get(key, None)) is None:
                return None
        return nxt

    def __set_nested(self, keys: Tuple[str, ...], values: List[str]):
        """Use a list of keys to set a nested value inside the self.db dict.

        **Example**

        You want to set :python:`["u", "v"]` inside
        :python:`self.db = {}` you would use this
        methode like :python:`self.__set_nested(["a", "b", "c"], ["u", "v"]`.
        Now the condition :python:`self.db == {'a': {'b': {'c': ['u', 'v']}}`
        is :python:`True`.
        """
        tree = {}
        first: bool = True
        for key in reversed(keys):
            if first:
                first = False
                tree = {key: values}
            else:
                tree = {key: tree}
        self.db.update(tree)

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
