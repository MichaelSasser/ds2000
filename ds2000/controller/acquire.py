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

from collections import namedtuple
from logging import warning

from ds2000.controller import BaseController, Ds2000Exception

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

__all__ = ["Acquire", ]

AcquireType = namedtuple("AcquireType", "type average_count")


class Acquire(BaseController):
    def type_normal(self):
        """

        :ACQuire:TYPE
        Command Format:
        :ACQuire:TYPE <type>
        :ACQuire:TYPE?
        Function Explanation:
        The commands set and query the current acquire type of the oscilloscope.
        <type> could be NORMal, AVERage or PEAKdetect.
        Returned Format:
        The query returns NORMAL, AVERAGE or PEAKDETECT.
        Example:
        :ACQ:TYPE AVER Setup the acquire type as Average.
        :ACQ:TYPE? The query returns AVERAGE
        :return:
        """
        self.device.ask(":ACQuire:TYPE NORMal")

    def type_average(self, count: int = 0):
        """

        :ACQuire:TYPE
        Command Format:
        :ACQuire:TYPE <type>
        :ACQuire:TYPE?
        Function Explanation:
        The commands set and query the current acquire type of the
        oscilloscope. <type> could be NORMal, AVERage or PEAKdetect.
        Returned Format:
        The query returns NORMAL, AVERAGE or PEAKDETECT.
        Example:
        :ACQ:TYPE AVER Setup the acquire type as Average.
        :ACQ:TYPE? The query returns AVERAGE
        :return:
        """
        self.device.ask(":ACQuire:TYPE AVERage")
        if count == 0:
            return
        elif count in (2, 4, 8, 16, 32, 64, 128, 256):
            self.device.ask(f":ACQuire:AVERages {count}")
        else:
            raise ValueError("The \"count\" must be 0, to leave the count"
                             "untouched or 2, 4, 8, 16, 32, 64, 128 or 256.")

    def type_peakdetect(self):
        """

        :ACQuire:TYPE
        Command Format:
        :ACQuire:TYPE <type>
        :ACQuire:TYPE?
        Function Explanation:
        The commands set and query the current acquire type of the
        oscilloscope. <type> could be NORMal, AVERage or PEAKdetect.
        Returned Format:
        The query returns NORMAL, AVERAGE or PEAKDETECT.
        Example:
        :ACQ:TYPE AVER Setup the acquire type as Average.
        :ACQ:TYPE? The query returns AVERAGE
        :return:
        """
        self.device.ask(":ACQuire:TYPE PEAKdetect")

    def type(self) -> AcquireType:
        """

        :ACQuire:TYPE
        Command Format:
        :ACQuire:TYPE <type>
        :ACQuire:TYPE?
        Function Explanation:
        The commands set and query the current acquire type of the
        oscilloscope. <type> could be NORMal, AVERage or PEAKdetect.
        Returned Format:
        The query returns NORMAL, AVERAGE or PEAKDETECT.
        Example:
        :ACQ:TYPE AVER Setup the acquire type as Average.
        :ACQ:TYPE? The query returns AVERAGE

        :return:
        """
        acquire_type: str = self.device.ask(":ACQuire:TYPE?")
        if acquire_type == "NORM":
            return AcquireType("Normal", 0)
        elif acquire_type == "AVER":
            count = int(self.device.ask(":ACQuire:AVERages?"))
            return AcquireType("Average", count)
        elif acquire_type == "PEAK":
            return AcquireType("Peakdetect", 0)
        else:
            raise Ds2000Exception(f"Unknown acquire type: \"{acquire_type}\"")

    def mode_realtime(self):
        """

        :ACQuire:MODE
        Command Format:
        :ACQuire:MODE <mode>
        :ACQuire:MODE?
        Function Explanation:
        The commands set and query the current acquire mode of the
        oscilloscope. <mode> could be RTIMe (Real time Sampling) or ETIMe
        (Equivalent Sampling).
        Returned Format:
        The query returns REAL_TIME or EQUAL_TIME.
        Example:
        :ACQ:MODE ETIM Setup the acquire mode as ETIMe.
        :ACQ:MODE? The query returns EQUAL_TIME.

        :return:
        """
        self.device.ask(":ACQuire:MODE RTIMe")

    def mode_equivalent(self):
        """

        :ACQuire:MODE
        Command Format:
        :ACQuire:MODE <mode>
        :ACQuire:MODE?
        Function Explanation:
        The commands set and query the current acquire mode of the
        oscilloscope. <mode> could be RTIMe (Real time Sampling) or ETIMe
        (Equivalent Sampling).
        Returned Format:
        The query returns REAL_TIME or EQUAL_TIME.
        Example:
        :ACQ:MODE ETIM Setup the acquire mode as ETIMe.
        :ACQ:MODE? The query returns EQUAL_TIME.

        :return:
        """
        self.device.ask(":ACQuire:MODE ETIMe")

    def mode(self) -> str:
        """

        :ACQuire:MODE
        Command Format:
        :ACQuire:MODE <mode>
        :ACQuire:MODE?
        Function Explanation:
        The commands set and query the current acquire mode of the
        oscilloscope. <mode> could be RTIMe (Real time Sampling) or ETIMe
        (Equivalent Sampling).
        Returned Format:
        The query returns REAL_TIME or EQUAL_TIME.
        Example:
        :ACQ:MODE ETIM Setup the acquire mode as ETIMe.
        :ACQ:MODE? The query returns EQUAL_TIME.

        :return:
        """
        acquire_mode: str = self.device.ask(":ACQuire:MODE?")
        if acquire_mode == "REAL_TIME":
            return "Realtime"
        elif acquire_mode == "EQUAL_TIME":
            return "Equivalent"
        else:
            raise Ds2000Exception("Unknown acquire mode.")

    def samplerate(self, channel: int) -> float:
        """

        ToDo: Add digital for DS1000?

        :ACQuire:SAMPlingrate?
        Command Format:
        :ACQuire:SAMPlingrate? {CHANnel<n>|DIGITAL}
        Function Explanation:
        The command queries the current sampling rate of the analog channel
        or digital channel (only for DS1000D series). <n> is 1 or 2 means
        channel 1 or channel 2.
        Returned Format:
        The query returns the setting value of the sampling rate.
        Example:
        :ACQ:SAMP? CHANnel2 Query the sampling rate for channel 2.
        100000000.000000 The query returns 100M.

        :return:
        """
        if channel <= 0 or channel > 4:
            raise ValueError("You have to enter a correct channel")
        elif channel in (3, 4):
            warning("It is possible, that you choose a wrong channel."
                    "If your oscilloscope has 4 channels, ignore this"
                    "warning.")
        return float(self.device.ask(
                f":ACQuire:SAMPlingrate? CHANnel{channel}"))

    def memorydepth_normal(self):
        """

        :ACQuire:MEMDepth <depth>
        Command Format:
        :ACQuire:MEMDepth <depth>
        :ACQuire:MEMDepth?
        Function Explanation:

        The commands set and query the memory depth of the oscilloscope.
        <depth> could be LONG (long memory) or NORMal (normal memory)
        Returned Format:
        The query returns LONG or NORMAL.
        Example:
        :ACQ:MEMD LONG Set the memory type as LONG.
        :ACQ:MEMD? The query returns LONG.

        :return:
        """
        self.device.ask(":ACQuire:MEMDepth NORMal")

    def memorydepth_long(self):
        """

        :ACQuire:MEMDepth <depth>
        Command Format:
        :ACQuire:MEMDepth <depth>
        :ACQuire:MEMDepth?
        Function Explanation:

        The commands set and query the memory depth of the oscilloscope.
        <depth> could be LONG (long memory) or NORMal (normal memory)
        Returned Format:
        The query returns LONG or NORMAL.
        Example:
        :ACQ:MEMD LONG Set the memory type as LONG.
        :ACQ:MEMD? The query returns LONG.

        :return:
        """
        self.device.ask(":ACQuire:MEMDepth LONG")

    def memorydepth(self):
        """

        ToDo: What is normal/long? Change to nice return value
        :ACQuire:MEMDepth <depth>
        Command Format:
        :ACQuire:MEMDepth <depth>
        :ACQuire:MEMDepth?
        Function Explanation:

        The commands set and query the memory depth of the oscilloscope.
        <depth> could be LONG (long memory) or NORMal (normal memory)
        Returned Format:
        The query returns LONG or NORMAL.
        Example:
        :ACQ:MEMD LONG Set the memory type as LONG.
        :ACQ:MEMD? The query returns LONG.

        :return:
        """
        return self.device.ask(":ACQuire:MEMDepth?")


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())
