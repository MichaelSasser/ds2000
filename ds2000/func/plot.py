#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019-2021  Michael Sasser <Michael@MichaelSasser.org>
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
from logging import debug

from ds2000.math.format import get_prefix

try:
    import matplotlib.pyplot as plt
    import numpy as np

    from matplotlib.ticker import FormatStrFormatter
    from matplotlib.ticker import MultipleLocator
except ImportError:
    raise ImportError(
        'To use this functionality you need the extras: "func".'
        'Install them with pip install "ds2000[func]".'
    )

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def simple_plot(inst, title: str = "", recorded: bool = False) -> None:
    """

    :type title: The title of the plot
    :param inst: The instrument class.
    :param recorded: If recorded is False, the plot will be only the current
                     waveform on the screen. None
    """
    # TODO: Add offset
    p = inst.waveform.preamble()
    t_scale = inst.timebase.get_scale()
    c_scale = inst.channel1.get_scale()
    inst.waveform.channel(1)  # TODO: Check for active channels; make argument.
    inst.waveform.format.byte()
    inst.waveform.mode.raw()

    # Create Subplots
    fig, ax = plt.subplots(figsize=(10, 6))

    # Get data for x-/y-Axis
    df = (
        (inst.waveform.data(recorded) - p.y_ref - p.y_origin)
        * p.y_inc
        * 10.0 ** (-get_prefix(c_scale).divisor)
    )  # y
    time = np.linspace(0.0, get_prefix(t_scale).value * 14, num=df.size)  # x

    ax.plot(time, df)
    plt.title(f'{inst.id.company.split(" ")[0]} {inst.id.model}', loc="left")
    plt.title(
        f"V={get_prefix(t_scale).value} {get_prefix(t_scale).prefix}s, "
        f"H={get_prefix(c_scale).value} {get_prefix(c_scale).prefix}V",
        loc="right",
    )

    ax.set(
        xlabel=f"Time ({get_prefix(t_scale).prefix}s)",
        ylabel=f"Voltage ({get_prefix(c_scale).prefix}V)",
        title=title,
    )

    ax.xaxis.set_major_locator(MultipleLocator(get_prefix(t_scale).value))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%d"))
    ax.xaxis.set_minor_locator(MultipleLocator(get_prefix(t_scale).value * 2))

    ax.yaxis.set_major_locator(MultipleLocator(get_prefix(c_scale).value))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%d"))
    ax.yaxis.set_minor_locator(MultipleLocator(get_prefix(c_scale).value / 2))

    ax.grid()

    # fig.savefig("test.png")

    plt.xlim(0, get_prefix(inst.timebase.get_scale()).value * 14)
    plt.ylim(
        -get_prefix(inst.channel1.get_scale()).value * 8 / 2,
        get_prefix(inst.channel1.get_scale()).value * 8 / 2,
    )
    plt.show()

    a = -inst.waveform.y_origin - inst.waveform.y_reference  # debug
    debug(f"lower: {a * 10 ** get_prefix(inst.channel1.get_scale()).divisor}")

    debug(f"r.channel1.get_scale()={inst.channel1.get_scale()}\n")

    debug(f"r.waveform.x_increment={inst.waveform.x_increment}")
    debug(f"r.waveform.x_origin={inst.waveform.x_origin}")
    debug(f"r.waveform.x_reference={inst.waveform.x_reference}\n")

    debug(
        f"r.waveform.y_increment={inst.waveform.y_increment}"
    )  # voltage value per unit
    debug(f"r.waveform.y_origin={inst.waveform.y_origin}")  # vertical offset
    debug(
        f"r.waveform.y_reference={inst.waveform.y_reference}"
    )  # vertical ref

    debug(get_prefix(inst.timebase.get_scale()))
