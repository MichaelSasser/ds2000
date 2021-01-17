#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2019-2021  Michael Sasser <Michael@MichaelSasser.org>

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
from __future__ import annotations

from logging import debug
from typing import NamedTuple

import numpy as np

from .common import Func, check_input
from .common import SFunc
from .errors import DS2000Error


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class WaveformStatus(NamedTuple):
    status: bool
    points: int


class Preamble(NamedTuple):
    format: str
    type: str
    points: int
    count: int
    x_inc: float
    x_origin: float
    x_ref: float
    y_inc: float
    y_origin: float
    y_ref: float


class Mode(SFunc):
    def normal(self):
        """
        **Rigol Programming Guide:**

        :WAVeform:MODE

        **Syntax**

        :WAVeform:MODE <mode>
        :WAVeform:MODE?

        **Description**

        Set the reading mode of waveform.
        Query the current reading mode of waveform.

        **Parameter**

        ======= ========== ====================== =======
        Name    Type       Range                  Default
        ======= ========== ====================== =======
        <type>  Discrete   {NORMal|MAXimum|RAW}   NORMal
        ======= ========== ====================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.

        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state. You
        can use the :WAVeform:POINts command to set the desired number of
        data points in the internal memory.

        **Return Format**

        The query returns NORM, MAX or RAW.

        **Example**

        :WAVeform:MODE RAW

        The query returns RAW.
        """
        self.sdev.dev.write(":WAVeform:MODE NORMal")

    def maximum(self):
        """
        **Rigol Programming Guide**

        :WAVeform:MODE

        **Syntax**

        :WAVeform:MODE <mode>

        :WAVeform:MODE?

        **Description**

        Set the reading mode of waveform.
        Query the current reading mode of waveform.

        **Parameter**

        ======= ========== ====================== =======
        Name    Type       Range                  Default
        ======= ========== ====================== =======
        <type>  Discrete   {NORMal|MAXimum|RAW}   NORMal
        ======= ========== ====================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.

        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state.
        You can use the :WAVeform:POINts command to set the desired number
        of data points in the internal memory.

        **Return Format**

        The query returns NORM, MAX or RAW.

        **Example**

        :WAVeform:MODE RAW

        The query returns RAW.
        """
        self.sdev.dev.write(":WAVeform:MODE MAXimum")

    def raw(self):
        """
        **Rigol Programming Guide**

        :WAVeform:MODE

        **Syntax**

        :WAVeform:MODE <mode>

        :WAVeform:MODE?

        **Description**

        Set the reading mode of waveform.
        Query the current reading mode of waveform.

        **Parameter**

        ======= ========== ====================== =======
        Name    Type       Range                  Default
        ======= ========== ====================== =======
        <type>  Discrete   {NORMal|MAXimum|RAW}   NORMal
        ======= ========== ====================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.

        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state. You
        can use the :WAVeform:POINts command to set the desired number of
        data points in the internal memory.

        **Return Format**

        The query returns NORM, MAX or RAW.

        **Example**

        :WAVeform:MODE RAW

        The query returns RAW.
        """
        self.sdev.dev.write(":WAVeform:MODE RAW")

    def get(self):
        answer: str = self.instrument.ask(":WAVeform:MODE?")
        if answer == "NORM":
            return "Normal"
        elif answer == "MAX":
            return "maximum"
        elif answer == "RAW":
            return "raw"
        else:
            raise DS2000Error("Unknown Return Value")

    def __str__(self) -> str:
        return self.get()

    def __repr__(self) -> str:
        return self.get()


class Format(SFunc):
    def word(self):
        """
        **Rigol Programming Guide**

        :WAVeform:FORMat

        **Syntax**

        :WAVeform:FORMat <format>

        :WAVeform:FORMat?

        **Description**

        Set the return format of the waveform data.
        Query the current return format of the waveform data.

        **Parameter**

        ========= ========== =================== =======
        Name      Type       Range               Default
        ========= ========== =================== =======
        <format>  Discrete   {WORD|BYTE|ASCii}   BYTE
        ========= ========== =================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.

        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state. You
        can use the :WAVeform:POINts command to set the desired number of
        data points in the internal memory.

        **Return Format**

        The query returns WORD, BYTE or ASC.

        **Example**

        :WAVeform:FORMat WORD

        The query returns WORD.
        """
        self.sdev.dev.write(":WAVeform:FORMat WORD")

    def byte(self):
        """
        **Rigol Programming Guide**

        :WAVeform:FORMat

        **Syntax**

        :WAVeform:FORMat <format>
        :WAVeform:FORMat?

        **Description**

        Set the return format of the waveform data.
        Query the current return format of the waveform data.

        **Parameter**

        ========= ========== =================== =======
        Name      Type       Range               Default
        ========= ========== =================== =======
        <format>  Discrete   {WORD|BYTE|ASCii}   BYTE
        ========= ========== =================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.
        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state. You
        can use the :WAVeform:POINts command to set the desired number of
        data points in the internal memory.

        **Return Format**

        The query returns WORD, BYTE or ASC.

        **Example**

        :WAVeform:FORMat WORD

        The query returns WORD.
        """
        self.sdev.dev.write(":WAVeform:FORMat BYTE")

    def ascii(self):
        """
        Rigol Programming Guide:

        :WAVeform:FORMat

        Syntax
        :WAVeform:FORMat <format>
        :WAVeform:FORMat?

        Description
        Set the return format of the waveform data.
        Query the current return format of the waveform data.

        **Parameter**

        ========= ========== =================== =======
        Name      Type       Range               Default
        ========= ========== =================== =======
        <format>  Discrete   {WORD|BYTE|ASCii}   BYTE
        ========= ========== =================== =======

        **Explanation**

        In different modes, the :WAVeform:POINts command returns different
        numbers of waveform points.

        **NORMal** : return the number of waveform points currently displayed.

        **MAXimum** : return the maximum number of effective data points under
        the current state. Return the number of data points displayed on the
        screen when the instrument is in run state and the number of data
        points in the internal memory in stop state.

        **RAW** : It is only available when the instrument is in stop state. You
        can use the :WAVeform:POINts command to set the desired number of
        data points in the internal memory.

        **Return Format**

        The query returns WORD, BYTE or ASC.

        **Example**

        :WAVeform:FORMat WORD

        The query returns WORD.
        """
        self.sdev.dev.write(":WAVeform:FORMat ASCii")

    def get(self):
        answer: str = self.instrument.ask(":WAVeform:FORMAT?")
        if answer == "WORD":
            return "word"
        elif answer == "BYTE":
            return "byte"
        elif answer == "ASC":
            return "ascii"
        else:
            raise DS2000Error("Unknown Return Value")

    def __str__(self) -> str:
        return self.get()

    def __repr__(self) -> str:
        return self.get()


class Waveform(Func):
    def __init__(self, dev):
        super(Waveform, self).__init__(dev)
        self.mode: Mode = Mode(self)
        self.format: Format = Format(self)

    def channel(self, channel: int = 1):
        """
        **Rigol Programming Guide**

        :WAVeform:SOURce

        **Syntax**

        :WAVeform:SOURce <source>

        :WAVeform:SOURce?

        **Description**

        Set the channel source of waveform reading.
        Query the current channel source of waveform reading.

        **Parameter**

        ========== ========= ==================== ========
         Name      Type      Range                Default
        ========== ========= ==================== ========
         <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========== ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2。

        **Example**

        :WAVeform:SOURce CHANnel2

        The query returns CHAN2.
        """
        check_input(channel, "channel", int, 1, 2)
        self.dev.write(f":WAVeform:SOURce CHANnel{channel}")

    def points(self, points: int):
        """
        **Rigol Programming Guide**

        :WAVeform:POINts

        **Syntax**

        :WAVeform:POINts <point>

        :WAVeform:POINts?

        **Description**

        Set the number of waveform points to be read.
        Query the current number of waveform points to be read.

        **Parameter**

        =========== =========== ======================= =======
        Name        Type        Range                   Default
        =========== =========== ======================= =======
        <point>     Integer     **NORMal**: 1 to 1400   --
                                **MAX**: 1 to the
                                number of effective
                                points currently
                                on the screen
                                **RAW**: 1 to the
                                current maximum memory
                                depth
        =========== =========== ======================= =======

        **Explanation**

        The number of waveform points is limited by the current reading mode
        of waveform (refer to the :WAVeform:MODE command).
        Return Format
        The query returns an integer.

        **Example**

        :WAVeform:POINts 600

        The query returns 600..
        """
        if not isinstance(points, int):
            raise TypeError("The parameter points must be of the type int.")
        current_format: str = str(self.format)
        if current_format == "normal" and 1 < points > 1400:
            raise ValueError(
                "The parameter points in normal mode must be"
                "between 1 and 1400."
            )
        elif current_format == "maximum" and 1 < points:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the number of effective points "
                "currently on the screen."
            )
        elif current_format == "raw" and 1 < points:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the current maximum memory depth."
            )
        points = self.instrument.ask(f"WAVeform:POINts {points}")
        return points

    def data(self, recorded: bool = False):
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:DATA?

        **Description**

        Read the waveform data.

        **Explanation**

        This command is affected by the :WAVeform:FORMat, :WAVeform:MODE,
        :WAVeform:POINts, :WAVeform:SOURce and related commands.

        Procedures of the screen waveform data reading:

        =========================== =================================
        Command                     Description
        =========================== =================================
        S1. :WAV:SOURce CHAN1       Set the channel source to be read
        S2. :WAV:MODE NORM          Set the waveform mode to NORM
        S3. :WAV:DATA?              Obtain data from buffer
        =========================== =================================

        Procedures of the internal memory waveform data reading:

        =========================== ==========================================
        Command                     Description
        =========================== ==========================================
        S1. :STOP                   The internal memory waveform data can only
                                    be read in STOP state
        S2. :WAV:SOURce CHAN1       Set the channel source to be read
        S3. :WAV:MODE RAW           Set the waveform mode to RAW
        S4. :WAV:RESet              Reset the waveform reading
        S5. :WAV:BEGin              Start the waveform reading
        S6. :WAV:STATus?            Get the state
            1) IDLE                 Waveform reading thread finishes
                :WAV:DATA?          Get data in buffer
                :WAV: END           Waveform reading finishes
            2) READ                 Waveform reading thread is running
                :WAV:DATA?          Get data in buffer
                Repeat S6           Continue to read waveform data
        =========================== ==========================================

        See the example below.

        .. code-block:: c

           visa32.viPrintf(viSession, ":STOP\\n");
           visa32.viPrintf(viSession, ":WAV:MODE RAW\\n");
           visa32.viPrintf(viSession, ":WAV:SOURce %s\\n", strChan );
           visa32.viPrintf(viSession, ":WAV:RESet\\n");
           visa32.viPrintf(viSession, ":WAV:BEGin\\n");
           while (true) {
               Thread.Sleep( 100 );
               visa32.viPrintf(viSession, ":WAV:STATus?\\n");
               visa32.viScanf(viSession, "%s", strBuild);
               if (strBuild[0] == 'I') {  //IDLE
                   visa32.viPrintf(viSession, ":WAV:DATA?\\n");
                   visa32.viRead(viSession, wfmBuf, wfmBuf.Length, out readCnt);
                   readSum += ( readCnt -12);
                   readTim++;
                   Console.WriteLine("{0}: Read {1} Sum {2}" ,
                                     readTim, readCnt, readSum);
                   return readSum;
               } else {
                   visa32.viPrintf(viSession, ":WAV:DATA?\\n");
                   visa32.viRead(viSession, wfmBuf, wfmBuf.Length, out readCnt);
                   readSum += (readCnt -12);
                   readTim++;
                   Console.WriteLine("{0}: Read {1} Sum {2}" ,
                                     readTim, readCnt, readSum);
                   Console.WriteLine("Press any key to read next data." );
                   //Console.ReadKey();
                   Console.WriteLine("Reading..." );
               }
           }


        **Return Format**

        The data returned contains 2 parts: the TMC data description header and
        the waveform data.

        #900000ddddXXXX...

        Wherein, dddd denotes the number of the effective waveform points in
        the data stream.
        When reading the internal memory data, the waveform data returned each
        time might be the data block in one area of the buffer. Each data
        block has a TMC description header similar to #9XXXXXXXXX, wherein
        XXXXXXXXX denotes the number of the waveform points in this data block.
        Waveform data in two adjacent data blocks are consecutive.

        The waveform data read can be converted to the voltage of each point
        of the waveform on the screen according to the method below.

        The figure below shows the waveform data read. First, select "View as
        hexadecimal only" from the dropdown list at the right of Buffer; at
        this point, the waveform data read is displayed in hexadecimal format;
        the first 11 figures denote the number of bytes that the "Denoter"
        holds in the internal memory; the figures following are the waveform
        data on the screen and users can convert the waveform data read to the
        voltage of each point of the waveform on the screen using the formula
        (ox63 - vertical reference position in Y direction) ×
        VerticalScale-OFFSet.
        For the vertical reference position in Y direction, refer to the
        **:WAVeform:YREFerence?** command, for the VerticalScale, refer to the
        **:CHANnel<n>:SCALe** command and for the OFFSet, refer to the
        **:CHANNel<n>:OFFSet** command.

        Note: when the return format of the waveform data is set to ASCii
        (refer to the :WAVeform:FORMat command), the query returns the actual
        voltage of each point of the waveform on the screen in scientific
        notation.

        **C# Test Program**


        .. code-block:: c#

           using System;
           using System.Collections.Generic;
           using System.Linq;
           using System.Text;
           using System.Diagnostics;
           using System.Threading;
           using System.IO;
           namespace FalconWavQuery
           {
           class Program
           {
                   static void Main(string[] args)
                   {
                           Int32 viDef = 0;
                           Int32 viSession = 0;
                           Int32 s32ReadByte;
                           if (args.Length < 2) {
                                   Console.WriteLine("Invalid Input!
                                            FalconWavQuery CHAN1 fileName");
                                   return;
                           }
                           Stopwatch stpWatch = new Stopwatch();
                           InitVisa(out viDef);
                           if (ConnectDevice(viDef, out viSession) == true) {}
                           else {
                                   Console.WriteLine("Connect fail!");
                                   return;
                           }
                           stpWatch.Start();
                           s32ReadByte = TestReadWfm(viSession,
                                                     args[0], args[1]);
                           stpWatch.Stop();
                           Console.WriteLine("Speed is {0} KB/s",
                                             s32ReadByte /
                                             stpWatch.ElapsedMilliseconds);
                           DeInitVisa(viDef, viSession);
                           Console.WriteLine("Press any key to continue.");
                           Console.ReadKey();
                   }
                   static Int32 TestReadWfm(Int32 viSession, string strChan,
                                            string strFile)
                   {
                           byte []wfmBuf;
                           Int32 readCnt = 0;
                           Int32 readSum = 0;
                           Int32 readTim = 0;
                           Int32 maxPacket = 0;
                           StringBuilder strBuild;
                           Stream streamOut;
                           BinaryWriter wfmStream;
                           wfmBuf = new byte[1024 * 1024 * 10];
                           strBuild = new StringBuilder(256);
                           visa32.viPrintf(viSession, ":STOP\\n");
                           visa32.viPrintf(viSession, ":WAV:MODE RAW\\n");
                           visa32.viPrintf(viSession, ":WAV:SOURce %s\\n",
                                           strChan);
                           visa32.viPrintf(viSession, ":WAV:RESet\\n");
                           visa32.viPrintf(viSession, ":WAV:BEGin\\n");
                           //read buffer to WFM
                           streamOut = File.Create(strFile, 10000000);
                           wfmStream = new BinaryWriter(streamOut);
                           while (true) {
                                   //Thread.Sleep( 10000 );
                                   visa32.viPrintf(viSession,
                                                   ":WAV:STATus?\\n");
                                   visa32.viScanf(viSession, "%s", strBuild);
                                    if (strBuild[0] == 'I') {  //IDLE
                                           visa32.viPrintf(viSession,
                                                           ":WAV:DATA?\\n");
                                           visa32.viRead(viSession, wfmBuf,
                                                    wfmBuf.Length, out readCnt);
                                           //data header #9XXXX...
                                           //plus end mark \\n
                                           readCnt -= 12;
                                           readSum += (readCnt);
                                           if (readCnt > maxPacket) {
                                                   maxPacket = readCnt;
                                           }
                                           //readTim++;
                                           //skip data header #9XXXX...
                                           if (readCnt > 0) {
                                                   wfmStream.Write(wfmBuf, 11,
                                                                   readCnt);
                                           }
                                           wfmStream.Close();
                                           Console.WriteLine("{0}: Read {1} Sum
                                                {2} Max {3}", readTim,
                                                readCnt, readSum,
                                                             maxPacket);
                                           return readSum;
                                   } else {
                                           //READ
                                           visa32.viPrintf(viSession,
                                                           ":WAV:DATA?\\n");
                                           visa32.viRead(viSession, wfmBuf,
                                                    wfmBuf.Length, out readCnt);
                                           //data header #9XXXX...
                                           //plus end mark \\n
                                           readCnt -= 12;
                                           readSum += (readCnt);
                                           if (readCnt > maxPacket) {
                                                   maxPacket = readCnt;
                                           }
                                           Console.WriteLine("{0}: Read {1} ",
                                                             readTim, readCnt);
                                           readTim++;
                                           //skip data header #9XXXX...
                                           if (readCnt > 0) {
                                                   wfmStream.Write(wfmBuf, 11,
                                                                   readCnt);
                                           }
                                   }
                           }
                           return readSum;
                   }
                   //initialize VISA
                   static bool InitVisa(out Int32 viDef)
                   {
                           Int32 viError;
                           viError = visa32.viOpenDefaultRM(out viDef);
                           if (viError != visa32.VI_SUCCESS) {
                                   return false;
                           } else {
                                   return true;
                           }
                   }
                   //to initialize VISA
                   static void DeInitVisa(Int32 viDef, Int32 viSession)
                   {
                           visa32.viClose(viSession);
                           visa32.viClose(viDef);
                   }
                   //connect devices
                   static bool ConnectDevice(Int32 viDef, out Int32 viSession)
                   {
                           Int32 viError;
                           Int32 viFindList;
                           Int32 viRetCount;
                           StringBuilder strRsrc = new StringBuilder(256);
                           viError = visa32.viFindRsrc(viDef, "USB?*", out
                                                       viFindList,
                                                       out viRetCount,
                                                       strRsrc);
                           if (viRetCount > 0) {
                                   viError = visa32.viOpen(viDef,
                                                           strRsrc.ToString(),
                                                           0, 0, out viSession);
                                   if (viError != visa32.VI_SUCCESS) {
                                           visa32.viClose(viDef);
                                           return false;
                                   }
                                   return true;
                           } else {
                                   viSession = 0;
                                   return false;
                           }
                   }
           }
           }
        """

        def get_data():
            try:
                self.dev.write(":WAVeform:DATA?")
            except Exception:
                raise DS2000Error("Write Operation was not successful.")

            # Read (RAW)
            try:
                dat = self.dev.read_raw()
            except Exception:
                raise DS2000Error("Raw read Operation was not successful.")
            return dat

        if recorded:
            self.dev.stop()
            self.mode.raw()
            self.reset()
            self.start(1)
            self.stop(self.dev.acquire.memorydepth)
            self.begin()
            data = []
            while True:
                if self.status().status:  # IDLE
                    data.append(get_data())
                    self.end()
                    break
                else:  # READ
                    data.append(get_data())
            data = b"".join(data)
        else:
            data = get_data()

        # print(data)

        debug(f"{data=}")
        # exit(0)
        if data[:7] == b"#900000":  # screen waveform data
            # #900000dddd -> dddd
            eff_waves: int = int(data[7:11])  # number of effective waveforms
        elif data[:2] == b"#9":  # internal memory data
            # #9XXXXXXXXX -> XXXXXXXXX
            eff_waves = int(data[2:11])
        else:
            raise DS2000Error("Could not identify the incoming data.")

        # print(f"eff_waves = {eff_waves}")

        try:
            raw_wave = data[11 : (11 + eff_waves)]
        except Exception:
            raise DS2000Error("The waveform was corrupted.")

        if eff_waves != len(raw_wave):
            raise DS2000Error(
                "The effective waves of the head do not match"
                " the number of received waves."
            )

        # print(f"raw_wave = {raw_wave}")
        # print(f"lan raw_wave: {len(raw_wave)}")
        return np.frombuffer(raw_wave, np.uint8)  # DataFrame

    @property
    def x_increment(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:XINCrement?

        **Description**

        Query the time difference between two neighboring points of the
        specified source (refer to the :WAVeform:SOURce command) in X direction
        and the unit is s.

        **Return Format**

        The query returns the time difference in scientific notation.

        **Example**

        :WAVeform:XINCrement?

        The query returns 1.000000e-08.
        """
        return float(self.instrument.ask(":WAVeform:XINCrement?"))

    @property
    def x_origin(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:XORigin?

        **Description**

        Query the time from the trigger point to the reference time (refer to
        the :WAVeform:SOURce command) of the specified source (refer to the
        :WAVeform:XREFerence? command) in X direction and the unit is s.

        **Return Format**

        The query returns the time value in scientific notation.

        **Example**

        :WAVeform:XORigin?

        The query returns -7.000000e-06.
        """
        return float(self.instrument.ask(":WAVeform:XORigin?"))

    @property
    def x_reference(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:XREFerence?

        **Description**

        Query the reference time of the specified source (refer to the
        :WAVeform:SOURce command) in X direction and the unit is s.

        **Return Format**

        The query returns the reference time in integer.

        **Example**


        :WAVeform:XREFerence?

        The query returns 0.
        """
        return float(self.instrument.ask(":WAVeform:XREFerence?"))

    @property
    def y_increment(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:YINCrement?

        **Description**

        Query the voltage value per unit of the specified source (refer to the
        :WAVeform:SOURce command) in Y direction and the unit is the same with
        the unit of the signal source.

        **Return Format**

        The query returns the voltage value in scientific notation.

        **Example**

        :WAVeform:YINCrement?

        The query returns 4.000000e-02.
        """
        return float(self.instrument.ask(":WAVeform:YINCrement?"))

    @property
    def y_origin(self) -> float:
        """
        Rigol Programming Guide

        **Syntax**

        :WAVeform:YORigin?

        **Description**

        Query the vertical offset relative to the vertical reference position
        (refer to the :WAVeform:SOURce command) of the specified source
        (refer to the :WAVeform:YREFerence? command) in Y direction and the
        unit is the same with the unit of the signal source.

        **Return Format**

        The query returns the offset value in scientific notation.

        **Example**

        :WAVeform:YORigin?

        The query returns 2.000000e+00.
        """
        return float(self.instrument.ask(":WAVeform:YORigin?"))

    @property
    def y_reference(self) -> float:
        """
        **Rigol Programming Guide**

        **Syntax**

        :WAVeform:YREFerence?

        **Description**

        Query the vertical reference position of the specified source (refer to
        the :WAVeform:SOURce command) in Y direction and the unit is the same
        with the unit of the signal source.

        **Return Format**

        The query returns the reference position in integer.

        **Example**

        :WAVeform:YREFerence?

        The query returns 127.
        """
        return float(self.instrument.ask(":WAVeform:YREFerence?"))

    def start(self, start: int = 1):
        """
        **Rigol Programming Guide**

        :WAVeform:STARt

        **Syntax**

        :WAVeform:STARt <sta>

        :WAVeform:STARt?

        **Description**

        Set the start position of internal memory waveform reading.
        Query the current start position of internal memory waveform reading.

        **Parameter**

        =========== =========== ====================== ========
        Name        Type        Range                   Default
        =========== =========== ====================== ========
        <sta>       Integer     **NORMal**: 1 to 1400       --
                                **MAX**: 1 to the
                                number of effective
                                points currently
                                on the screen
                                **RAW**: 1 to the
                                current maximum memory
                                depth
        =========== =========== ====================== ========

        **Explanation**

        For the memory depth, refer to the :ACQuire:MDEPth command.
        The setting of the start position is limited by the current reading
        mode of the waveform (refer to the :WAVeform:MODE command).

        **Return Format**

        The query returns an integer.

        **Example**

        :WAVeform:STARt 100

        The query returns 100.
        """
        current_format: str = str(self.format)
        if current_format == "normal" and 1 < start > 1400:
            raise ValueError(
                "The parameter points in normal mode must be"
                "between 1 and 1400."
            )
        elif current_format == "maximum" and 1 < start:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the number of effective points "
                "currently on the screen."
            )
        elif current_format == "raw" and 1 < start:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the current maximum memory depth."
            )
        self.dev.write(f":WAVeform:STARt {start}")

    def stop(self, stop: int):
        """
        **Rigol Programming Guide**

        :WAVeform:STOP

        **Syntax**

        :WAVeform:STOP <sta>

        :WAVeform:STOP?

        **Description**

        Set the stop position of internal memory waveform reading.
        Query the current stop position of internal memory waveform reading.

        **Parameter**

        =========== =========== ======================= =======
        Name        Type        Range                   Default
        =========== =========== ======================= =======
        <sta>       Integer     **NORMal**: 1 to 1400   --
                                **MAX**: 1 to the
                                number of effective
                                points currently
                                on the screen
                                **RAW**: 1 to the
                                current maximum memory
                                depth
        =========== =========== ======================= =======

        **Explanation**

        For the memory depth, refer to the :ACQuire:MDEPth command.
        The setting of the stop position is limited by the current reading
        mode of the waveform (refer to the :WAVeform:MODE command).

        **Return Format**

        The query returns an integer.

        **Example**

        :WAVeform:STOP 200

        The query returns 200.
        """
        current_format: str = str(self.format)
        if current_format == "normal" and 1 < stop > 1400:
            raise ValueError(
                "The parameter points in normal mode must be"
                "between 1 and 1400."
            )
        elif current_format == "maximum" and 1 < stop:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the number of effective points "
                "currently on the screen."
            )
        elif current_format == "raw" and 1 < stop:  # Todo: Check max
            raise ValueError(
                "The parameter points in maximal mode must be"
                "between 1 and the current maximum memory depth."
            )
        self.dev.write(f":WAVeform:STOP {stop}")

    def begin(self):
        """
        **Rigol Programming Guide**

        :WAVeform:BEGin

        **Syntax**

        :WAVeform:BEGin

        **Description**

        Enable the waveform reading.
        """
        self.dev.write(":WAVeform:BEGin")

    def end(self):
        """
        **Rigol Programming Guide**

        :WAVeform:END

        **Syntax**

        :WAVeform:END

        **Description**

        Stop the waveform reading.
        """
        self.dev.write(":WAVeform:END")

    def reset(self):
        """
        **Rigol Programming Guide**

        :WAVeform:RESet

        **Syntax**

        :WAVeform:RESet

        **Description**

        Reset the waveform reading.
        """
        self.dev.write(":WAVeform:RESet")

    def preamble(self) -> Preamble:
        """
        **Rigol Programming Guide**

        :WAVeform:PREamble?

        **Syntax**

        :WAVeform:PREamble?

        **Description**

        Query and return all the waveform parameters.

        **Return Format**

        The query returns 10 waveform parameters separated by ",":
        <format>,<type>,<points>,<count>,<xincrement>,<xorigin>,<xreference>,
        <yincrement>,<yorigin>,<yreference>

        ============= =========================================================
        <format>:     0 (WORD), 1 (BYTE) or 2 (ASC). Refer to the
                      :WAVeform:FORMat command.
        <type>:       0 (NORMal), 1 (MAXimum) or 2 (RAW). Refer to the
                      :WAVeform:MODE command.
        <points>:     integer between 1 and 56000000. Refer to the
                      :WAVeform:POINts command.
        <count>:      the number of averages in average sample mode (refer to
                      the :ACQuire:AVERages command) and 1 in other modes.
        <xincrement>: the time difference between two neighboring points in X
                      direction. Refer to the :WAVeform:XINCrement? command.
        <xorigin>:    the time from the trigger point to the "Reference Time"
                      in X direction. Refer to the :WAVeform:XORigin? command.
        <xreference>: the reference time of the data point in X direction.
                      Refer to the :WAVeform:XREFerence? command.
        <yincrement>: the voltage value per unit in Y direction. Refer to the
                      :WAVeform:YINCrement? command.
        <yorigin>     the vertical offset relative to the "Vertical Reference
                      Position" in Y direction. Refer to the :WAVeform:YORigin?
                      command.
        <yreference>: the vertical reference position in Y direction. Refer
                      to the :WAVeform:YREFerence? command.
        ============= =========================================================

        **Example**

        :WAVeform:PREamble?

        The query returns 0,0,1400,1,0.000000,-0.000007,0,0.040000,2.000000,127.
        """
        pre = self.instrument.ask(":WAVeform:PREamble?").split(",")
        if len(pre) != 10:
            raise DS2000Error("Unexpected waveform preamble length.")
        return Preamble(
            pre[0],  # ('format', str)
            pre[1],  # ('type', str),
            int(pre[2]),  # ('points', int),
            int(pre[3]),  # ('count', int),
            float(pre[4]),  # ('x_inc', float),
            float(pre[5]),  # ('x_origin', float),
            float(pre[6]),  # ('x_ref', float),
            float(pre[7]),  # ('y_inc', float),
            float(pre[8]),  # ('y_origin', float),
            float(pre[9]),
        )  # ('y_ref', float)

    def status(self) -> WaveformStatus:
        """
        **Rigol Programming Guide**

        :WAVeform:STATus?

        **Syntax**

        :WAV:STATus?

        **Description**

        Query and return the current waveform reading state.

        **Explanation**

        **IDLE**: the waveform reading thread finishes.

        **READ**: the waveform reading thread is running.

        **n**: the current number of waveform points to be read.

        **Return Format**

        The query returns IDLE,n or READ,n.
        """
        status = self.instrument.ask(":WAVeform:STATus?").split(",")
        print(status)
        if len(status) != 2:
            raise DS2000Error("Unexpected waveform status length.")
        if status[0] == "IDLE":
            return WaveformStatus(True, status[1])
        elif status[0] == "READ":
            return WaveformStatus(False, status[1])
        raise DS2000Error("Unexpected waveform status.")
