#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020  Michael Sasser <Michael@MichaelSasser.org>
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
from .mode import *
from .coupling import *
from .sweep import *
from .edge import *
from .pulse import *
from .windows import *
from .runt import *
from .nth_edge import *
from .slope import *
from .video import *
from .pattern import *
from .delay import *
from .timeout import *
from .duration import *
from .setup_hold import *
from .rs232 import *
from .i2c import *
from .spi import *
from .usb import *

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = (
    *mode.__all__,
    *coupling.__all__,
    *sweep.__all__,
    *edge.__all__,
    *pulse.__all__,
    *windows.__all__,
    *runt.__all__,
    *nth_edge.__all__,
    *slope.__all__,
    *video.__all__,
    *pattern.__all__,
    *delay.__all__,
    *timeout.__all__,
    *setup_hold.__all__,
    *rs232.__all__,
    *i2c.__all__,
    *spi.__all__,
    *usb.__all__,
)
