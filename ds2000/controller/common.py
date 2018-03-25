#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
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

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

__all__ = ['BaseController']


class BaseController(object):
    def __init__(self, device):
        self.device = device


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())
