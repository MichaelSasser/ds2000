# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.de>

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


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.de"

from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'maintenance', 'suffix'])

__version_info__: Version = Version(0, 0, 1, 'dev1')
__version__: str = '.'.join(map(str, __version_info__))
