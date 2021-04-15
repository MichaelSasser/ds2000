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

    """Use the Enum to get or set the channel status."""

    CHANNEL_1 = "channel_1"
    CHANNEL_2 = "channel_2"
    EXT = "ext"
    AC_LINE = "ac_line"


# TODO: Maybe TriggerSlopeEnum
class SlopeEnum(Enum):

    """Use the Enum to get or set the slope status."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    BOTH = "both"


# Acquire


class AcquireTypeEnum(Enum):

    """Use the Enum to get or set the acquire status."""

    NORMAL = "normal"
    AVERAGE = "average"
    PEAKDETECT = "peakdetect"
    HIGHRES = "highres"


# class AcquireMemoryDepth(Enum):
#     S14K
#     S140K
#     S1M4
#     S14M
#     S56M

# Trigger


class TriggerStatusEnum(Enum):

    """Use the Enum to get or set the trigger status."""

    TD = "td"
    WAIT = "wait"
    RUN = "run"
    AUTO = "auto"
    STOP = "stop"


# Trigger -> Coupling


class TriggerCouplingEnum(Enum):

    """Use the Enum to get or set the coupling status of the trigger."""

    AC = "ac"
    DC = "dc"
    LF_REJECT = "lf_reject"
    HF_REJECT = "hf_reject"


# Trigger -> Delay


class TriggerDelayTypeEnum(Enum):

    """Use the Enum to get or set the delay type of the trigger."""

    GREATER = "greater"  # GREater
    LESS = "less"  # LESS
    INSIDE = "inside"  # GLESs  # TODO: Maybe use between
    OUTSIDE = "outside"  # GOUT


# Trigger -> Duration


class TriggerDurationWhenEnum(Enum):  # TODO: most of TriggerDelayTypeEnum

    """Use the Enum to get or set the duration of the trigger."""

    GREATER = "greater"
    LESS = "less"
    BETWEEN = "between"


# Trigger -> Edge


# Trigger -> I2C


class TriggerI2CWhenEnum(Enum):

    """Use the Enum to get or set the I²C trigger."""

    START = "start"
    RESTART = "restart"
    STOP = "stop"
    NACK = "nack"
    ADDRESS = "address"
    DATA = "data"
    ADDRESS_AND_DATA = "address_and_data"


class TriggerI2CDirectionEnum(Enum):

    """Use the Enum to get or set the I²C direction to trigger."""

    READ = "read"
    WRITE = "write"
    READ_AND_WRITE = "read_and_write"


# Trigger -> Mode


class TriggerModeEnum(Enum):

    """Use the Enum to get or set the trigger mode."""

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


# Trigger -> Pulse


class TriggerPulseWhenEnum(Enum):

    """Use the Enum to get or set the pulse trigger."""

    POSIVE_GREATER = "positive_greater"
    POSITIVE_LESS = "positive_less"
    NEGATIVE_GREATER = "negative_greater"
    NEGATIVE_LESS = "negative_less"
    POSITIVE_BETWEEN = "positive_between"
    NEGATIVE_BETWEEN = "negative_between"


# Trigger -> RS232


class TriggerRS232WhenEnum(Enum):

    """Use the Enum to get or set the RS232 trigger."""

    START_FRAME = "start_frame"
    ERROR = "error"
    PARITY_ERROR = "parity_error"
    DATA = "data"


class TriggerRS232Parity(Enum):

    """Use the Enum to get or set the RS232 parity to trigger."""

    EVEN = "even"
    ODD = "odd"
    NONE = "none"


# Trigger -> Runt


class TriggerRuntWhenEnum(Enum):

    """Use the Enum to get or set the runt trigger."""

    NONE = "none"
    GREATER = "greater"
    LESS = "less"
    BETWEEN = "between"


class TriggerRuntPolarityEnum(Enum):

    """Use the Enum to get or set the runt polarity to trigger."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


# Trigger -> Setup/Hold


class TriggerSetupHoldTypeEnum(Enum):

    """Use the Enum to get or set the SETUP & HOLD trigger type."""

    SETUP = "setup"
    HOLD = "hold"
    SETUP_HOLD = "setup_hold"


class TriggerSetupHoldPatternEnum(Enum):

    """Use the Enum to get or set the SETUP & HOLD pattern to trigger."""

    HIGH = "high"
    LOW = "low"


# Trigger -> Slope


class TriggerSlopeWhenEnum(Enum):

    """Use the Enum to get or set the slope trigger."""

    POSIVE_GREATER = "positive_greater"
    POSITIVE_LESS = "positive_less"
    NEGATIVE_GREATER = "negative_greater"
    NEGATIVE_LESS = "negative_less"
    POSITIVE_BETWEEN = "positive_between"
    NEGATIVE_BETWEEN = "negative_between"


# Trigger -> SPI


# Trigger -> Sweep


class TriggerSweepEnum(Enum):

    """Use the Enum to get or set the sweep trigger."""

    AUTO = "auto"
    NORMAL = "normal"
    SINGLE = "single"


# Trigger -> Timeout


# Trigger -> USB

# TODO: Maybe rename to start, end etc.
class TriggerUSBWhenEnum(Enum):

    """Use the Enum to get or set the USB trigger."""

    SOP = "sop"
    EOP = "eop"
    RC = "rc"
    SUSPEND = "suspend"
    SUSPEND_EXIT = "suspend exit"


class TrigerUSBSpeedEnum(Enum):

    """Use the Enum to get or set the USB speed to trigger."""

    FULL = "full"
    LOW = "low"


# Trigger -> Video


class TriggerVideoPolarityEnum(Enum):

    """Use the Enum to get or set the video polarity to trigger."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


class TriggerVideoModeEnum(Enum):

    """Use the Enum to get or set the video mode to trigger."""

    ODD_FIELD = "odd_field"
    EVEN_FIELD = "even_line"
    SPECIFIC_LINE = "specific_line"
    ALL_LINES = "all_lines"


class TriggerVideoStandardEnum(Enum):

    """Use the Enum to get or set the video standard to trigger."""

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


class TriggerWindowsPositionEnum(Enum):

    """Use the Enum to get or set the window position to trigger."""

    EXIT = "exit"
    ENTER = "enter"
    TIME = "time"


# vim: set ft=python :
