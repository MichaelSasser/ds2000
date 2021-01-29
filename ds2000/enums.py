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

from enum import Enum

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# Common

class ChannelEnum(Enum):
    CHANNEL_1 = "channel_1"
    CHANNEL_2 = "channel_2"
    EXT = "ext"
    AC_LINE = "ac_line"

# Trigger -> Coupling


class TriggerCouplingEnum(Enum):
    AC = "ac"
    DC = "dc"
    LF_REJECT = "lf_reject"
    HF_REJECT = "hf_reject"


# Trigger -> Delay


class TriggerDelayTypeEnum(Enum):
    GREATER = "greater"  # GREater
    LESS = "less"  # LESS
    INSIDE = "inside"  # GLESs  # TODO: Maybe use between
    OUTSIDE = "outside"  # GOUT


class TriggerDelaySlopeEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


# Trigger -> Duration


class TriggerDurationWhenEnum(Enum):  # TODO: most of TriggerDelayTypeEnum
    GREATER = "greater"
    LESS = "less"
    BETWEEN = "between"


# Trigger -> Edge


class TriggerEdgeSlopeEnum(Enum):
    RISING = "rising"
    FALLING = "falling"
    BOTH = "both"


# Trigger -> I2C

class TriggerI2CWhenEnum(Enum):
    START = "start"
    RESTART = "restart"
    STOP = "stop"
    NACK = "nack"
    ADDRESS = "address"
    DATA = "data"
    ADDRESS_AND_DATA = "address_and_data"


class TriggerI2CDirectionEnum(Enum):
    READ = "read"
    WRITE = "write"
    READ_AND_WRITE = "read_and_write"


# Trigger -> Mode

class TriggerModeEnum(Enum):
    EDGE = "edge"
    PULSE = "pulse"
    RUNT = "runt"
    WINDOW = "window"
    NTH_EDGE = "nth_edge"
    SLOPE = "slope"
    VIDEO = "video"
    PATTERN = "pattern"
    DELAY = "delay"
    TIMEOUT = "timeout"
    DURATION = "duration"
    SETUP_HOLD = "setup_hold"
    RS232 = "rs232"
    I2C = "i2c"
    SPI = "spi"
    USB = "usb"

# vim: set ft=python :
