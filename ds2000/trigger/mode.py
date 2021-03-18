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

from ds2000.common import SFunc
from ds2000.enums import TriggerModeEnum
from ds2000.errors import DS2000StateError


__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"


class Mode(SFunc):
    def set_edge(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE EDGE")

    def set_pulse(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE PULSe")

    def set_runt(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE RUNT")

    def set_windows(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE WIND")

    def set_nth_edge(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE NEDG")

    def set_slope(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE SLOPe")

    def set_video(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE VIDeo")

    def set_pattern(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE PATTern")

    def set_delay(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE DELay")

    def set_timeout(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE TIMeout")

    def set_duration(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE DURATion")

    def set_setup_hold(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE SHOLd")

    def set_rs232(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE RS232")

    def set_i2c(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE IIC")

    def set_spi(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE SPI")

    def set_usb(self) -> None:
        """Select the trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        self.instrument.say(":TRIGger:MODE USB")

    def status(self) -> TriggerModeEnum:
        """Query the current trigger type.

        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:MODE <mode>
        :TRIGger:MODE?

        **Description**

        Select the trigger type.
        Query the current trigger type.

        **Parameter**

        ======= ========= ============================ =======
        Name    Type      Range                        Default
        ======= ========= ============================ =======
        <mode>  Discrete  {EDGE,PULSe,RUNT,WIND,NEDG,  EDGE
                          SLOPe,VIDeo,PATTern,DELay,
                          TIMeout,DURATion,SHOLd,
                          RS232,IIC,SPI,USB}
        ======= ========= ============================ =======

        **Return Format**

        The query returns the current trigger type.

        **Example**

        :TRIGger:MODE SLOPe
        The query returns SLOP.
        """
        answer: str = self.instrument.ask(":TRIGger:MODE?")
        if answer == "EDGE":
            return TriggerModeEnum.EDGE
        if answer == "PULS":
            return TriggerModeEnum.PULSE
        if answer == "RUNT":
            return TriggerModeEnum.RUNT
        if answer == "WIND":
            return TriggerModeEnum.WINDOW
        if answer == "NEDG":
            return TriggerModeEnum.NTH_EDGE
        if answer == "SLOP":
            return TriggerModeEnum.SLOPE
        if answer == "VID":
            return TriggerModeEnum.VIDEO
        if answer == "PATT":
            return TriggerModeEnum.PATTERN
        if answer == "DEL":
            return TriggerModeEnum.DELAY
        if answer == "TIM":
            return TriggerModeEnum.TIMEOUT
        if answer == "DURAT":
            return TriggerModeEnum.DURATION
        if answer == "SHOL":
            return TriggerModeEnum.SETUP_HOLD
        if answer == "RS232":
            return TriggerModeEnum.RS232
        if answer == "IIC":
            return TriggerModeEnum.I2C
        if answer == "SPI":
            return TriggerModeEnum.SPI
        if answer == "USB":
            return TriggerModeEnum.USB
        raise DS2000StateError()
