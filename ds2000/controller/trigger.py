#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018-2020  Michael Sasser <Michael@MichaelSasser.org>

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

from ds2000.controller import BaseController
from ds2000.controller.trigger_subcontrollers import (Mode,
                                                      Coupling,
                                                      Sweep,
                                                      Edge,
                                                      Pulse,
                                                      Windows,
                                                      Runt,
                                                      NthEdge,
                                                      Slope,
                                                      Video,
                                                      Pattern,
                                                      Delay,
                                                      Timeout,
                                                      Duration,
                                                      SetupHold,
                                                      Rs232,
                                                      I2c,
                                                      Spi, )


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Trigger",
]


class Trigger(BaseController):
    def __init__(self, device):
        super(Trigger, self).__init__(device)
        self.mode: Mode = Mode(self)
        self.coupling: Coupling = Coupling(self)
        self.sweep: Sweep = Sweep(self)
        self.edge: Edge = Edge(self)
        self.pulse: Pulse = Pulse(self)
        self.runt: Runt = Runt(self)
        self.window: Windows = Windows(self)
        self.nth_edge: NthEdge = NthEdge(self)
        self.slope: Slope = Slope(self)
        self.video: Video = Video(self)
        self.pattern: Pattern = Pattern(self)
        self.delay: Delay = Delay(self)
        self.timeout: Timeout = Timeout(self)
        self.duration: Duration = Duration(self)
        self.setup_hold: SetupHold = SetupHold(self)
        self.rs232: Rs232 = Rs232(self)
        self.iic: I2c = I2c(self)
        self.spi: Spi = Spi(self)

    def status(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        TRIGger:STATus?

        **Description**

        Query the current trigger status.

        **Return Format**

        The query returns TD, WAIT, RUN, AUTO or STOP.
        """
        raise NotImplementedError()

    def holdoff(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:HOLDoff <value>
        :TRIGger:HOLDoff?

        **Description**

        Set the trigger holdoff time and the unit is s.
        Query the current trigger holdoff time.

        **Parameter**

        ======== ===== ============= =======
        Name     Type  Range         Default
        ======== ===== ============= =======
        <value>  Real  100ns to 10s  100ns
        ======== ===== ============= =======

        **Explanation**

        This setting is not available for the Nth edge trigger, video trigger,
        RS232 trigger, IIC trigger, SPI trigger and USB trigger.

        **Return Format**

        The query returns the trigger holdoff time in scientific notation.

        Example

        :TRIGger:HOLDoff 0.0000002
        The query returns 2.000000e-07.
        """
        raise NotImplementedError()

    def noise_reject(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:NREJect <bool>
        :TRIGger:NREJect?

        **Description**

        Enable or disable noise reject.
        Query the current status of noise reject.

        **Parameter**

        ======= ===== ================= =======
        Name    Type  Range             Default
        ======= ===== ================= =======
        <bool>  Bool  {{0|OFF}|{1|ON}}  0|OFF
        ======= ===== ================= =======

        **Return Format**

        The query returns 0 or 1.

        ++Example**

        :TRIGger:NREJect ON
        The query returns 1.
        """
        raise NotImplementedError()

# ToDo: From HERE
    def level(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()

    def level50(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()

    def force(self):
        """
        **Rigol Programming Guide**

        **Syntax**
        """
        raise NotImplementedError()
