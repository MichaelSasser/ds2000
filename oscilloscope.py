#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.org>
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
from __future__ import annotations

from logging import DEBUG, WARN, getLogger
from logging import basicConfig as loggingBasicConfig

from ds2000.oscilloscope import DS2000


from ds2000.func import simple_plot

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


def main():
    ip = "192.168.30.196"
    # r = DS2000(ip)
    # r.connect()
    with DS2000(ip) as r:
        print("info:", r.info())

        print(f"{r.channel1.coupling.status()=}")
        r.waveform.start(1)
        simple_plot(r, recorded=False)

        # print(f'df={df}\n')
        # print(df)
        # plt.plot(df)
    # r.disconnect()


#   r.reset()


if __name__ == "__main__":
    DEBUGGING: bool = True
    loggingBasicConfig(
        level=DEBUG if DEBUGGING else WARN,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    getLogger("matplotlib.font_manager").disabled = True
    main()
