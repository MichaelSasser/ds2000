#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020-2021  Michael Sasser <Michael@MichaelSasser.org>

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

from typing import Dict

from ds2000.common import SFunc
from ds2000.common import SSFunc
from ds2000.common import channel_as_enum
from ds2000.common import check_input
from ds2000.common import check_level
from ds2000.enums import ChannelEnum
from ds2000.enums import TriggerVideoModeEnum
from ds2000.enums import TriggerVideoPolarityEnum
from ds2000.enums import TriggerVideoStandardEnum
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class VideoSource(SSFunc):
    def set_channel_1(self) -> None:
        """Select the trigger source of video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:SOURce <source>
        :TRIGger:VIDeo:SOURce?

        **Description**

        Select the trigger source of video trigger.
        Query the current trigger source of video trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:VIDeo:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:VIDeo:SOURce CHANnel1")

    def set_channel_2(self) -> None:
        """Select the trigger source of video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:SOURce <source>
        :TRIGger:VIDeo:SOURce?

        **Description**

        Select the trigger source of video trigger.
        Query the current trigger source of video trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:VIDeo:SOURce CHANnel2
        The query returns CHAN2.
        """
        self.instrument.ask(":TRIGger:VIDeo:SOURce CHANnel2")

    def status(self) -> ChannelEnum:
        """Query the current trigger source of video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:SOURce <source>
        :TRIGger:VIDeo:SOURce?

        **Description**

        Select the trigger source of video trigger.
        Query the current trigger source of video trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:VIDeo:SOURce CHANnel2
        The query returns CHAN2.
        """
        return channel_as_enum(self.instrument.ask(":TRIGger:VIDeo:SOURce?"))


class VideoPolarity(SSFunc):
    def set_positive(self) -> None:
        """Set the video polarity in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:POLarity <polarity>
        :TRIGger:VIDeo:POLarity?

        **Description**

        Set the video polarity in video trigger.
        Query the current video polarity in video trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:VIDeo:POLarity POSitive
        The query returns POS.
        """
        self.instrument.ask(":TRIGger:VIDeo:POLarity POSitive")

    def set_negative(self) -> None:
        """Set the video polarity in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:POLarity <polarity>
        :TRIGger:VIDeo:POLarity?

        **Description**

        Set the video polarity in video trigger.
        Query the current video polarity in video trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:VIDeo:POLarity POSitive
        The query returns POS.
        """
        self.instrument.ask(":TRIGger:VIDeo:POLarity NEGative")

    def status(self) -> TriggerVideoPolarityEnum:
        """Query the current video polarity in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:POLarity <polarity>
        :TRIGger:VIDeo:POLarity?

        **Description**

        Set the video polarity in video trigger.
        Query the current video polarity in video trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:VIDeo:POLarity POSitive
        The query returns POS.
        """
        answer: str = self.instrument.ask(":TRIGger:VIDeo:POLarity?")
        if answer == "POS":
            return TriggerVideoPolarityEnum.POSITIVE
        if answer == "NEG":
            return TriggerVideoPolarityEnum.NEGATIVE
        raise DS2000StateError()


class VideoMode(SSFunc):
    def set_odd_field(self) -> None:
        """Set the sync type in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:MODE <mode>
        :TRIGger:VIDeo:MODE?

        **Description**

        Set the sync type in video trigger to AllLine, Line Number, Odd Field
        or Even Field.
        Query the current sync type in video trigger.

        **Parameter**

        ======= ========= ================================= =======
        Name    Type      Range                             Default
        ======= ========= ================================= =======
        <mode>  Discrete  {ODDField|EVENfield|LINE|ALINes}  ALINes
        ======= ========= ================================= =======


        Note: when the video standard is HDTV, the sync type could only be set
        to AllLine or Line Number. For the video standard, refer to the
        :TRIGger:VIDeo:STANdard command.

        **Explanation**

        ODDField: trigger on the rising edge of the first ramp waveform pulse
        in the odd field.

        EVENfield: trigger on the rising edge of the first ramp waveform pulse
        in the even field.

        LINE for NTSC and PAL/SECAM video standards, trigger on the specified
        line in the odd or even field; for HDTV video standard, trigger on the
        specified line. Note that when this sync trigger mode is selected, you
        can modify the line number using in the “Line Num” menu with a step
        of 1. The range of the line number is from
        1 to 525 (NTSC),
        1 to 625 (PAL/SECAM),
        1 to 525 (480P),
        1 to 625 (576P),
        1 to 750 (720P),
        1 to 1125 (1080P) or
        1 to 1125 (1080I).

        ALINes: trigger on all the horizontal sync pulses.

        **Return Format**

        The query returns ODDF, EVEN, LINE or ALIN.

        **Example**

        :TRIGger:VIDeo:MODE ODDField
        The query returns ODDF.
        """
        self.instrument.ask(":TRIGger:VIDeo:MODE ODDField")

    def set_even_field(self) -> None:
        """Set the sync type in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:MODE <mode>
        :TRIGger:VIDeo:MODE?

        **Description**

        Set the sync type in video trigger to AllLine, Line Number, Odd Field
        or Even Field.
        Query the current sync type in video trigger.

        **Parameter**

        ======= ========= ================================= =======
        Name    Type      Range                             Default
        ======= ========= ================================= =======
        <mode>  Discrete  {ODDField|EVENfield|LINE|ALINes}  ALINes
        ======= ========= ================================= =======


        Note: when the video standard is HDTV, the sync type could only be set
        to AllLine or Line Number. For the video standard, refer to the
        :TRIGger:VIDeo:STANdard command.

        **Explanation**

        ODDField: trigger on the rising edge of the first ramp waveform pulse
        in the odd field.

        EVENfield: trigger on the rising edge of the first ramp waveform pulse
        in the even field.

        LINE for NTSC and PAL/SECAM video standards, trigger on the specified
        line in the odd or even field; for HDTV video standard, trigger on the
        specified line. Note that when this sync trigger mode is selected, you
        can modify the line number using in the “Line Num” menu with a step
        of 1. The range of the line number is from
        1 to 525 (NTSC),
        1 to 625 (PAL/SECAM),
        1 to 525 (480P),
        1 to 625 (576P),
        1 to 750 (720P),
        1 to 1125 (1080P) or
        1 to 1125 (1080I).

        ALINes: trigger on all the horizontal sync pulses.

        **Return Format**

        The query returns ODDF, EVEN, LINE or ALIN.

        **Example**

        :TRIGger:VIDeo:MODE ODDField
        The query returns ODDF.
        """
        self.instrument.ask(":TRIGger:VIDeo:MODE EVENfield")

    def set_specific_line(self) -> None:
        """Set the sync type in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:MODE <mode>
        :TRIGger:VIDeo:MODE?

        **Description**

        Set the sync type in video trigger to AllLine, Line Number, Odd Field
        or Even Field.
        Query the current sync type in video trigger.

        **Parameter**

        ======= ========= ================================= =======
        Name    Type      Range                             Default
        ======= ========= ================================= =======
        <mode>  Discrete  {ODDField|EVENfield|LINE|ALINes}  ALINes
        ======= ========= ================================= =======


        Note: when the video standard is HDTV, the sync type could only be set
        to AllLine or Line Number. For the video standard, refer to the
        :TRIGger:VIDeo:STANdard command.

        **Explanation**

        ODDField: trigger on the rising edge of the first ramp waveform pulse
        in the odd field.

        EVENfield: trigger on the rising edge of the first ramp waveform pulse
        in the even field.

        LINE for NTSC and PAL/SECAM video standards, trigger on the specified
        line in the odd or even field; for HDTV video standard, trigger on the
        specified line. Note that when this sync trigger mode is selected, you
        can modify the line number using in the “Line Num” menu with a step
        of 1. The range of the line number is from
        1 to 525 (NTSC),
        1 to 625 (PAL/SECAM),
        1 to 525 (480P),
        1 to 625 (576P),
        1 to 750 (720P),
        1 to 1125 (1080P) or
        1 to 1125 (1080I).

        ALINes: trigger on all the horizontal sync pulses.

        **Return Format**

        The query returns ODDF, EVEN, LINE or ALIN.

        **Example**

        :TRIGger:VIDeo:MODE ODDField
        The query returns ODDF.
        """
        self.instrument.ask(":TRIGger:VIDeo:MODE LINE")

    def set_all_lines(self) -> None:
        """Set the sync type in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:MODE <mode>
        :TRIGger:VIDeo:MODE?

        **Description**

        Set the sync type in video trigger to AllLine, Line Number, Odd Field
        or Even Field.
        Query the current sync type in video trigger.

        **Parameter**

        ======= ========= ================================= =======
        Name    Type      Range                             Default
        ======= ========= ================================= =======
        <mode>  Discrete  {ODDField|EVENfield|LINE|ALINes}  ALINes
        ======= ========= ================================= =======


        Note: when the video standard is HDTV, the sync type could only be set
        to AllLine or Line Number. For the video standard, refer to the
        :TRIGger:VIDeo:STANdard command.

        **Explanation**

        ODDField: trigger on the rising edge of the first ramp waveform pulse
        in the odd field.

        EVENfield: trigger on the rising edge of the first ramp waveform pulse
        in the even field.

        LINE for NTSC and PAL/SECAM video standards, trigger on the specified
        line in the odd or even field; for HDTV video standard, trigger on the
        specified line. Note that when this sync trigger mode is selected, you
        can modify the line number using in the “Line Num” menu with a step
        of 1. The range of the line number is from
        1 to 525 (NTSC),
        1 to 625 (PAL/SECAM),
        1 to 525 (480P),
        1 to 625 (576P),
        1 to 750 (720P),
        1 to 1125 (1080P) or
        1 to 1125 (1080I).

        ALINes: trigger on all the horizontal sync pulses.

        **Return Format**

        The query returns ODDF, EVEN, LINE or ALIN.

        **Example**

        :TRIGger:VIDeo:MODE ODDField
        The query returns ODDF.
        """
        self.instrument.ask(":TRIGger:VIDeo:MODE ALINes")

    def status(self) -> TriggerVideoModeEnum:
        """Query the current sync type in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:MODE <mode>
        :TRIGger:VIDeo:MODE?

        **Description**

        Set the sync type in video trigger to AllLine, Line Number, Odd Field
        or Even Field.
        Query the current sync type in video trigger.

        **Parameter**

        ======= ========= ================================= =======
        Name    Type      Range                             Default
        ======= ========= ================================= =======
        <mode>  Discrete  {ODDField|EVENfield|LINE|ALINes}  ALINes
        ======= ========= ================================= =======


        Note: when the video standard is HDTV, the sync type could only be set
        to AllLine or Line Number. For the video standard, refer to the
        :TRIGger:VIDeo:STANdard command.

        **Explanation**

        ODDField: trigger on the rising edge of the first ramp waveform pulse
        in the odd field.

        EVENfield: trigger on the rising edge of the first ramp waveform pulse
        in the even field.

        LINE for NTSC and PAL/SECAM video standards, trigger on the specified
        line in the odd or even field; for HDTV video standard, trigger on the
        specified line. Note that when this sync trigger mode is selected, you
        can modify the line number using in the “Line Num” menu with a step
        of 1. The range of the line number is from
        1 to 525 (NTSC),
        1 to 625 (PAL/SECAM),
        1 to 525 (480P),
        1 to 625 (576P),
        1 to 750 (720P),
        1 to 1125 (1080P) or
        1 to 1125 (1080I).

        ALINes: trigger on all the horizontal sync pulses.

        **Return Format**

        The query returns ODDF, EVEN, LINE or ALIN.

        **Example**

        :TRIGger:VIDeo:MODE ODDField
        The query returns ODDF.
        """
        answer: str = self.instrument.ask(":TRIGger:VIDeo:MODE?")
        if answer == "ODDF":
            return TriggerVideoModeEnum.ODD_FIELD
        if answer == "EVEN":
            return TriggerVideoModeEnum.EVEN_FIELD
        if answer == "LINE":
            return TriggerVideoModeEnum.SPECIFIC_LINE
        if answer == "ALIN":
            return TriggerVideoModeEnum.ALL_LINES
        raise DS2000StateError()


class VideoStandard(SSFunc):

    VIDEO_STANDARD: Dict[str, TriggerVideoStandardEnum] = {
        "PALSecam": TriggerVideoStandardEnum.VideoPALSecam,
        "NTSC": TriggerVideoStandardEnum.VideoNTSC,
        "480P": TriggerVideoStandardEnum.Video480P,
        "576P": TriggerVideoStandardEnum.Video576P,
        "720P60HZ": TriggerVideoStandardEnum.Video720P60HZ,
        "720P50HZ": TriggerVideoStandardEnum.Video720P50HZ,
        "720P30HZ": TriggerVideoStandardEnum.Video720P30HZ,
        "720P25HZ": TriggerVideoStandardEnum.Video720P25HZ,
        "720P24HZ": TriggerVideoStandardEnum.Video720P24HZ,
        "1080P60HZ": TriggerVideoStandardEnum.Video1080P60HZ,
        "1080P50HZ": TriggerVideoStandardEnum.Video1080P50HZ,
        "1080P30HZ": TriggerVideoStandardEnum.Video1080P30HZ,
        "1080P25HZ": TriggerVideoStandardEnum.Video1080P25HZ,
        "1080P24HZ": TriggerVideoStandardEnum.Video1080P24HZ,
        "1080I30HZ": TriggerVideoStandardEnum.Video1080I30HZ,
        "1080I25HZ": TriggerVideoStandardEnum.Video1080I25HZ,
        "1080I24HZ": TriggerVideoStandardEnum.Video1080I24HZ,
    }

    def set_pal_secam(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard PALSecam")

    def set_ntsc(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard NTSC")

    def set_480p(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 480P")

    def set_576p(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 576P")

    def set_720p60hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 720P60HZ")

    def set_720p50hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 720P50HZ")

    def set_720p30hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 720P30HZ")

    def set_720p25hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 720P25HZ")

    def set_720p24hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 720P24HZ")

    def set_1080p60hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080P60HZ")

    def set_1080p50hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080P50HZ")

    def set_1080p30hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080P30HZ")

    def set_1080p25hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080P25HZ")

    def set_1080p24hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080P24HZ")

    def set_1080i30hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080I30HZ")

    def set_1080i25hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080I25HZ")

    def set_1080i24hz(self) -> None:
        """Select the video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        self.instrument.ask(":TRIGger:VIDeo:STANdard 1080I24HZ")

    def status(self) -> TriggerVideoStandardEnum:
        """Query the current video standard in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:STANdard <standard>
        :TRIGger:VIDeo:STANdard?

        **Description**

        Select the video standard in video trigger.
        Query the current video standard in video trigger.

        **Parameter**

        =========== ========= ==================================== =======
        Name        Type      Range                                Default
        =========== ========= ==================================== =======
        <standard>  Discrete  {PALSecam|NTSC|480P|576P|720P60HZ|   NTSC
                              720P50HZ|720P30HZ|720P25HZ|
                              720P24HZ|1080P60HZ|1080P50HZ|
                              1080P30HZ|1080P25HZ|1080P24HZ|
                              1080I30HZ|1080I25HZ|1080I24HZ}
        =========== ========= ==================================== =======

        **Return Format**

        The query returns the video standard selected.

        **Example**

        :TRIGger:VIDeo:STANdard NTSC
        The query returns NTSC.
        """
        try:
            return self.__class__.VIDEO_STANDARD[
                self.instrument.ask(":TRIGger:VIDeo:STANdard?")
            ]
        except IndexError:
            raise DS2000StateError(
                f"Got: {self.instrument.ask(':TRIGger:VIDeo:STANdard?')}"
            )


class Video(SFunc):
    MAX_LINES_OF_VIDEO_STANDATD: Dict[TriggerVideoStandardEnum, int] = {
        TriggerVideoStandardEnum.VideoNTSC: 525,
        TriggerVideoStandardEnum.VideoPALSecam: 625,
        TriggerVideoStandardEnum.Video480P: 525,
        TriggerVideoStandardEnum.Video576P: 625,
        TriggerVideoStandardEnum.Video720P60HZ: 750,
        TriggerVideoStandardEnum.Video720P50HZ: 750,
        TriggerVideoStandardEnum.Video720P30HZ: 750,
        TriggerVideoStandardEnum.Video720P25HZ: 750,
        TriggerVideoStandardEnum.Video720P24HZ: 750,
        TriggerVideoStandardEnum.Video1080P60HZ: 1125,
        TriggerVideoStandardEnum.Video1080P50HZ: 1125,
        TriggerVideoStandardEnum.Video1080P30HZ: 1125,
        TriggerVideoStandardEnum.Video1080P25HZ: 1125,
        TriggerVideoStandardEnum.Video1080P24HZ: 1125,
        TriggerVideoStandardEnum.Video1080I30HZ: 1125,
        TriggerVideoStandardEnum.Video1080I25HZ: 1125,
        TriggerVideoStandardEnum.Video1080I24HZ: 1125,
    }

    def __init__(self, device):
        super(Video, self).__init__(device)
        self.source: VideoSource = VideoSource(self)
        self.polarity: VideoPolarity = VideoPolarity(self)
        self.mode: VideoMode = VideoMode(self)
        self.standard: VideoStandard = VideoStandard(self)

    def set_line(self, line: int = 1) -> None:
        """Set the line number in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:LINE <line>
        :TRIGger:VIDeo:LINE?

        **Description**

        Set the line number in video trigger when the sync type is Line Number
        (refer to the :TRIGger:VIDeo:MODE command).
        Query the current line number of the specified line.

        **Parameter**

        ======= ======== ===================== =======
        Name    Type     Range                 Default
        ======= ======== ===================== =======
        <line>  Integer  NTSC：1 to 525        1
                         PAL：1 to 625
                         480P：1 to 525
                         576P：1 to 625
                         720P60HZ：1 to 750
                         720P50HZ：1 to 750
                         720P30HZ：1 to 750
                         720P25HZ：1 to 750
                         720P24HZ：1 to 750
                         1080P60HZ：1 to 1125
                         1080P50HZ：1 to 1125
                         1080P30HZ：1 to 1125
                         1080P25HZ：1 to 1125
                         1080P24HZ：1 to 1125
                         1080I30HZ：1 to 1125
                         1080I25HZ：1 to 1125
                         1080I24HZ：1 to 1125
        ======= ======== ===================== =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:VIDeo:LINE 100
        The query returns 100.
        """
        check_input(
            line,
            "line",
            int,
            1,
            self.__class__.MAX_LINES_OF_VIDEO_STANDATD[self.standard.status()],
        )
        self.instrument.ask(f":TRIGger:VIDeo:LINE {line}")

    def get_line(self) -> int:
        """Query the current line number of the specified line.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:LINE <line>
        :TRIGger:VIDeo:LINE?

        **Description**

        Set the line number in video trigger when the sync type is Line Number
        (refer to the :TRIGger:VIDeo:MODE command).
        Query the current line number of the specified line.

        **Parameter**

        ======= ======== ===================== =======
        Name    Type     Range                 Default
        ======= ======== ===================== =======
        <line>  Integer  NTSC：1 to 525        1
                         PAL：1 to 625
                         480P：1 to 525
                         576P：1 to 625
                         720P60HZ：1 to 750
                         720P50HZ：1 to 750
                         720P30HZ：1 to 750
                         720P25HZ：1 to 750
                         720P24HZ：1 to 750
                         1080P60HZ：1 to 1125
                         1080P50HZ：1 to 1125
                         1080P30HZ：1 to 1125
                         1080P25HZ：1 to 1125
                         1080P24HZ：1 to 1125
                         1080I30HZ：1 to 1125
                         1080I25HZ：1 to 1125
                         1080I24HZ：1 to 1125
        ======= ======== ===================== =======

        **Return Format**

        The query returns an integer.

        **Example**

        :TRIGger:VIDeo:LINE 100
        The query returns 100.
        """
        return int(self.instrument.ask(":TRIGger:VIDeo:LINE?"))

    def set_level(self, level: float = 0.0) -> None:
        """Set the trigger level in video trigge.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:LEVel <level>
        :TRIGger:VIDeo:LEVel?

        **Description**

        Set the trigger level in video trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in video trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:VIDeo:LEVel 0.16
        The query returns 1.600000e-01.
        """
        channel: ChannelEnum = self.source.status()
        if channel == ChannelEnum.CHANNEL_1:
            scale = self.sdev.dev.channel1.get_scale()
            offset = self.sdev.dev.channel1.get_offset()
        elif channel == ChannelEnum.CHANNEL_2:
            scale = self.sdev.dev.channel2.scale()
            offset = self.sdev.dev.channel2.get_offset()
        else:
            raise DS2000StateError(
                "The level coul'd only be set, if the source is"
                "Channel 1 or Channel 2."
            )  # TODO: Right??
        check_level(level, scale, offset)
        self.instrument.ask(f":TRIGger:VIDeo:LEVel {level}")

    def get_level(self) -> float:
        """Query the current trigger level in video trigger.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:VIDeo:LEVel <level>
        :TRIGger:VIDeo:LEVel?

        **Description**

        Set the trigger level in video trigger and the unit is the same with
        the current amplitude unit.
        Query the current trigger level in video trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        .. note::
           For the VerticalScale, refer to the :CHANnel<n>:SCALe command.

           For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the trigger level in scientific notation.

        **Example**

        :TRIGger:VIDeo:LEVel 0.16
        The query returns 1.600000e-01.
        """
        return float(self.instrument.ask(":TRIGger:VIDeo:LEVel?"))
