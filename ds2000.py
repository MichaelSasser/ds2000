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
from ds2000.controller import Acquire, Display, Timebase

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
        self.__inst: vxi11

        # Subclasses
        self.acquire = Acquire(self)
        self.display = Display(self)
        self.timebase = Timebase(self)

    def ask(self, msg: str):
        """This is a Wrapper for the ask method of vxi11.
        With a wrapper it makes it possible to change the underlaying
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

    def connect(self):
        self.__inst = vxi11.Instrument(self.device_address)
        return self.id

    def id(self) -> Instrument:
        """
        This method retruns the ID character string of the device_address as a
        Instrument Tuple.

        Rigol Programming Guide:

            *IDN?

        Command Format:

            *IDN?
        Function Explanation:

        The command queries the ID character string of the instrument,
        including a field separated by 4 commas:

        manufactory, model, serial number and the version number
        composed of numbers and separated by “.” .

        Returned Format:

            RIGOL TECHNOLOGIES,<model>, <serial number>,
            <software version number>.

        Example:

            RIGOL TECHNOLOGIES,DS1102E,DS1EB104702974,00.02.01.01.00

        :return: Instrument
        """
        return Instrument(*self.ask("*IDN?").split(","))

    def reset(self):
        """ This method resets system parameters.

        Note: The connection to the device_address will also reset. ds2000 will
        timeout, after that it will reconnect to the instrument.

        Rigol Programming Guide:

        *RST
        Command Format:
            *RST
        Function Explanation:
        The command resets the system parameters.

        :return: None
        """
        self.ask("*RST")

    # SYSTem Commands

    def run(self):
        """
        Rigol Programming Guide:

        :RUN
        Command Format:
        :RUN
        Function Explanation:
        The command initiates the oscilloscope to acquire waveform data
        according to its current settings. Acquisition runs continuously
        until the oscilloscope receives a :STOP command.

        :return:
        """
        self.ask(":RUN")

    def stop(self):
        """
        Rigol Programming Guide:

        Command Format:

        :STOP

        Function Explanation:

        The command controls the oscilloscope to stop acquiring data.
        To restart the acquisition, use the :RUN command.

        :return:
        """
        self.ask(":STOP")

    def auto(self):
        """
        Rigol Programming Guide:

        Command Format:

        :AUTO

        Function Explanation:

        The command controls the oscilloscope to evaluate all input
        waveforms characteristics and set the optimum conditions to
        display the waveforms.

        :return:
        """
        self.ask(":AUTO")

    def hardcopy(self):
        """
        Rigol Programming Guide:

        :HARDcopy

        Function Explanation:

        The command is to extract the current information on the screen
        and save the bitmap into the U disc in the form of “HardCopyxxx.bmp”.
        (Note: this command is unavailable in file system)

        :return:
        """
        self.ask(":HARDcopy")


def main(*args, **kwargs):
    ip = "192.168.30.201"
    r = DS2000(ip)
    r.connect()
    print(r.id())
    print(r.acquire)
    print(r.id())


#   r.reset()


if __name__ == '__main__':
    DEBUGGING: bool = True
    loggingBasicConfig(level=DEBUG if DEBUGGING else WARN,
                       format='%(asctime)s - %(levelname)s - %(message)s')

    main()
