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


# TODO: Many are the same or part of another.

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


# Trigger -> Nth Edge


class TriggerNthEdgeSlopeEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


# Trigger -> Pulse


class TriggerPulseWhenEnum(Enum):
    POSIVE_GREATER = "positive_greater"
    POSITIVE_LESS = "positive_less"
    NEGATIVE_GREATER = "negative_greater"
    NEGATIVE_LESS = "negative_less"
    POSITIVE_BETWEEN = "positive_between"
    NEGATIVE_BETWEEN = "negative_between"


# Trigger -> RS232


class TriggerRS232WhenEnum(Enum):
    START_FRAME = "start_frame"
    ERROR = "error"
    PARITY_ERROR = "parity_error"
    DATA = "data"


class TriggerRS232Parity(Enum):
    EVEN = "even"
    ODD = "odd"
    NONE = "none"


# Trigger -> Runt


class TriggerRuntWhenEnum(Enum):
    NONE = "none"
    GREATER = "greater"
    LESS = "less"
    BETWEEN = "between"


class TriggerRuntPolarityEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


# Trigger -> Setup/Hold


class TriggerSetupHoldTypeEnum(Enum):
    SETUP = "setup"
    HOLD = "hold"
    SETUP_HOLD = "setup_hold"


class TriggerSetupHoldSlopeEnum(Enum):
    RISING = "rising"
    FALLING = "falling"


class TriggerSetupHoldPatternEnum(Enum):
    HIGH = "high"
    LOW = "low"


# Trigger -> Slope


class TriggerSlopeWhenEnum(Enum):
    POSIVE_GREATER = "positive_greater"
    POSITIVE_LESS = "positive_less"
    NEGATIVE_GREATER = "negative_greater"
    NEGATIVE_LESS = "negative_less"
    POSITIVE_BETWEEN = "positive_between"
    NEGATIVE_BETWEEN = "negative_between"


class TriggerSlopeWindowEnum(Enum):
    UPPER = "upper"
    LOWER = "lower"
    BOTH = "both"


# Trigger -> SPI


class TriggerSPISlopeEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


# Trigger -> Sweep


class TriggerSweepEnum(Enum):
    AUTO = "auto"
    NORMAL = "normal"
    SINGLE = "single"


# Trigger -> Timeout


class TriggerTimeoutSlopeEnum(Enum):
    RISING = "rising"
    FALLING = "falling"
    BOTH = "both"


# Trigger -> USB

# TODO: Maybe rename to start, end etc.
class TriggerUSBWhenEnum(Enum):
    SOP = "sop"
    EOP = "eop"
    RC = "rc"
    SUSPEND = "suspend"
    SUSPEND_EXIT = "suspend exit"


class TrigerUSBSppedEnum(Enum):
    FULL = "full"
    LOW = "low"


# Trigger -> Video


class TriggerVideoPolarityEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


class TriggerVideoModeEnum(Enum):
    ODD_FIELD = "odd_field"
    EVEN_FIELD = "even_line"
    SPECIFIC_LINE = "specific_line"
    ALL_LINES = "all_lines"


class TriggerVideoStandardEnum(Enum):
    VideoPALSecam = "VideoPALSecam"
    VideoNTSC = "VideoNTSC"
    Video480P = "Video480P"
    Video576P = "Video576P"
    Video720P60HZ = "Video720P60HZ"
    Video720P50HZ = "Video720P50HZ"
    Video720P30HZ = "Video720P30HZ"
    Video720P25HZ = "Video720P25HZ"
    Video720P24HZ = "Video720P24HZ"
    Video1080P60HZ = "Video1080P60HZ"
    Video1080P50HZ = "Video1080P50HZ"
    Video1080P30HZ = "Video1080P30HZ"
    Video1080P25HZ = "Video1080P25HZ"
    Video1080P24HZ = "Video1080P24HZ"
    Video1080I30HZ = "Video1080I30HZ"
    Video1080I25HZ = "Video1080I25HZ"
    Video1080I24HZ = "Video1080I24HZ"


# Trigger -> Windows


class TriggerWindowsSlopeEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    BOTH = "both"


class TriggerWindowsPositionEnum(Enum):
    EXIT = "exit"
    ENTER = "enter"
    TIME = "time"


# vim: set ft=python :
