#!/usr/bin/env python
# ds2000 
# Copyright (C) 2019  Michael Sasser <Michael@MichaelSasser.org>

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
from ds2000.controller import BaseController, SubController, Ds2000Exception

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

__all__ = ["Channel", ]

class Channel(BaseController):
    def __init__(self, device, channel):
        super(Channel, self).__init__(device)
        self.__channel = channel

    @property
    def scale(self) -> float:
        """

        Rigol Programming Guide:

        :CHANnel<n>:SCALe

        Syntax
        :CHANnel<n>:SCALe <scale>
        :CHANnel<n>:SCALe?

        Description
        Set the vertical scale of the waveform of CH1 or CH2.
        Query the current vertical scale of the waveform of CH1 or CH2.

        Parameter
        | Name     | Type     | Range         | Default |
        |----------+----------+---------------+---------|
        | <n>      | Discrete | {1|2}         | --      |
        | <scale>  | Real     | 500μV to 10V  | 1V      |
        Note: the range of the vertical scale is related to the probe ratio currently set. For the setting of the probe ratio, refer to the :CHANnel<n>:PROBe command.

        Return Format
        The query returns the vertical scale in scientific notation.

        Example
        :CHANnel1:SCALe 1
        The query returns 1.000000e+00.

        :return:
        """
        return float(self.device.ask(f":CHANnel{self.__channel}:SCALe?"))


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())

