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
from ds2000.controller import Acquire, Bus, Display, IEEE, Timebase, Trigger, \
    Waveform, Channel


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

import vxi11

from collections import namedtuple
from logging import DEBUG, WARN, error, debug
from logging import basicConfig as loggingBasicConfig

Instrument = namedtuple("Instrument", "company model serial software_version")


class DS2000(object):
    def __init__(self, device_address: str):
        self.device_address: str = device_address
        self.__inst: vxi11 = None
        self.id: Instrument = Instrument(None, None, None, None)

        # Subclasses
        self.acquire = Acquire(self)
        self.display = Display(self)
        self.timebase = Timebase(self)
        self.ieee = IEEE(self)
        self.bus1 = Bus(self, 1)
        self.bus2 = Bus(self, 2)
        self.trigger = Trigger(self)
        self.waveform = Waveform(self)
        self.channel1 = Channel(self, 1)
        self.channel2 = Channel(self, 2)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def ask(self, msg: str):
        """This is a Wrapper for the ask method of vxi11.
        With a wrapper it makes it possible to change the underlying
        package behaviour, vxi11 itself.

        """
        answer: str = None
        try:  # Probably just for development
            answer = self.__inst.ask(msg)
        except vxi11.vxi11.Vxi11Exception as e:
            error(f"Error while asking: {e}")
        finally:
            if DEBUGGING:
                debug(f"asked: \"{msg}\", answered: \"{answer}\"")
        return answer

    def write(self, msg: str):
        """This is a Wrapper for the write method of vxi11.
        With a wrapper it makes it possible to change the underlying
        package behaviour, vxi11 itself.

        """
        try:  # Probably just for development
            self.__inst.write(msg)
        except vxi11.vxi11.Vxi11Exception as e:
            error(f"Error while writing: {e}")
        finally:
            if DEBUGGING:
                debug(f"written (raw): \"{msg}\"")

    def read_raw(self, num: int=-1):
        """This is a Wrapper for the read_raw method of vxi11.
        With a wrapper it makes it possible to change the underlying
        package behaviour, vxi11 itself.

        """
        msg: bytes = None
        try:  # Probably just for development
            msg = self.__inst.read_raw(num)
        except vxi11.vxi11.Vxi11Exception as e:
            error(f"Error while writing: {e}")
        return msg

    def connect(self):
        self.__inst = vxi11.Instrument(self.device_address)
        self.id = Instrument(*self.ieee.idn().split(","))

    # SYSTem Commands
    def info(self):
        return Instrument(*self.ieee.idn().split(","))

    def autoscale(self):
        """
        Rigol Programming Guide:

        Syntax
        :AUToscale
        Description
        Enable the auto setting function.
        Explanation
        This command is not available when the current state of the Pass/Fail
        function is “Enable Test”. For details, refer to the :MASK:ENABle
        command.
        The oscilloscope will adjust the vertical scale, horizontal time base
        and trigger mode for optimum display of the waveform. Note that to use
        the auto setting, the frequency of the signal under test should be no
        lower than 50 Hz, the duty cycle be greater than 1% and the amplitude
        be at least 20 mVpp.

        :return:
        """
        self.ask(":AUToscale")

    def clear(self):
        """
        Rigol Programming Guide:

        Syntax
        :CLEar
        Description
        Clear all the waveforms on the screen.
        Explanation
        Waveform will still be displayed if the oscilloscope is in RUN state.

        :return:
        """
        self.ask(":AUToscale")

    def run(self):
        """
        Rigol Programming Guide:

        Syntax
        :RUN
        Description
        Start the oscilloscope.
        Explanation
        You can use the :STOP command to set the oscilloscope to STOP.

        :return:
        """
        self.ask(":RUN")

    def single(self):
        """
        Rigol Programming Guide:

        Syntax
        :SINGle
        Description
        Set the oscilloscope to single trigger mode.
        Explanation
        In single trigger mode, the oscilloscope triggers once the trigger
        conditions are met and then stops.
        In single trigger mode, using the :TFORce command can generate a
        trigger signal forcefully.
        You can use the :RUN and :STOP command to set the oscilloscope to
        Auto trigger mode or STOP state respectively.

        :return:
        """
        self.ask(":SINGle")

    def stop(self):
        """
        Rigol Programming Guide:

        Syntax
        :STOP
        Description
        Stop the oscilloscope.
        Explanation
        You can use the :RUN command to set the oscilloscope to Run.

        :return:
        """
        self.write(":STOP")

    def t_force(self):  # ToDo: Prob. to Trigger Menu
        """
        Rigol Programming Guide:

        Syntax
        :TFORce
        Description
        Generate a trigger signal forcefully.
        Explanation
        Force trigger is applicable to normal and single trigger modes.

        :return:
        """
        self.ask(":TFORce")

    def t_half(self):  # ToDo: Prob. to Trigger Menu
        """
        Rigol Programming Guide:

        Syntax
        :TLHAlf
        Description
        Set the trigger level to the vertical midpoint of the trigger signal amplitude.

        :return:
        """
        self.ask(":TLHAlf")

    def reset(self):
        self.ieee.rst()

    def disconnect(self):
        self.__inst.close()

    def __str__(self) -> str:
        return f"DS2000Object.{self.id.serial}"

    def __repr__(self) -> str:
        return f"DS2000Object.{self.id.serial}"

    def __del__(self):
        self.disconnect()

def main(*args, **kwargs):
    ip = "192.168.30.186"
    #r = DS2000(ip)
    #r.connect()
    with DS2000(ip) as r:
        print("info:", r.info())
        from ds2000.func import simple_plot
        r.waveform.start(1)
        simple_plot(r, recorded=False)

        #print(f'df={df}\n')
        #print(df)

        #plt.plot(df)
    #r.disconnect()


#   r.reset()


if __name__ == '__main__':
    DEBUGGING: bool = True
    loggingBasicConfig(level=DEBUG if DEBUGGING else WARN,
                       format='%(asctime)s - %(levelname)s - %(message)s')

    main()
