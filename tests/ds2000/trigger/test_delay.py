#!/usr/bin/env python
# ds2000 - install and manage your MSFS2020 addons
# Copyright (C) 2021  Michael Sasser <Michael@MichaelSasser.org>

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

import pytest

from ds2000.trigger.delay import DelaySlopeEnum
from ds2000.trigger.delay import DelayTypeEnum


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def test_delay_type_greater(dev) -> None:
    """Test the delay type of delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TYPe <type>
    :TRIGger:DELay:TYPe?

    **Description**

    Set the delay type of delay trigger.
    Query the current delay type of delay trigger.

    **Parameter**

    ======= ========= ========================== =======
    Name    Type      Range                      Default
    ======= ========= ========================== =======
    <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
    ======= ========= ========================== =======

    **Explanation**

    GREater: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the preset time limit
    (refer to the :TRIGger:DELay:TLOWer command).

    LESS: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the preset time limit
    (refer to the :TRIGger:DELay:TUPPer command).

    GLESs: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the lower limit of
    the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
    limit must be lower than the time upper limit.

    GOUT: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the lower limit of the
    preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
     limit must be lower than the time upper limit.

    **Return Format**

    The query returns GOUT, GRE, LESS or GLES.

    **Example**

    :TRIGger:DELay:TYPe GOUT
    The query returns GOUT.
    """
    # Setup
    desired: DelayTypeEnum = DelayTypeEnum.GREATER
    dev.trigger.delay.type.greater()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.type.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_type_less(dev) -> None:
    """Test the delay type of delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TYPe <type>
    :TRIGger:DELay:TYPe?

    **Description**

    Set the delay type of delay trigger.
    Query the current delay type of delay trigger.

    **Parameter**

    ======= ========= ========================== =======
    Name    Type      Range                      Default
    ======= ========= ========================== =======
    <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
    ======= ========= ========================== =======

    **Explanation**

    GREater: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the preset time limit
    (refer to the :TRIGger:DELay:TLOWer command).

    LESS: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the preset time limit
    (refer to the :TRIGger:DELay:TUPPer command).

    GLESs: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the lower limit of
    the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
    limit must be lower than the time upper limit.

    GOUT: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the lower limit of the
    preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
     limit must be lower than the time upper limit.

    **Return Format**

    The query returns GOUT, GRE, LESS or GLES.

    **Example**

    :TRIGger:DELay:TYPe GOUT
    The query returns GOUT.
    """
    # Setup
    desired: DelayTypeEnum = DelayTypeEnum.LESS
    dev.trigger.delay.type.less()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.type.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_type_inside(dev) -> None:
    """Test the delay type of delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TYPe <type>
    :TRIGger:DELay:TYPe?

    **Description**

    Set the delay type of delay trigger.
    Query the current delay type of delay trigger.

    **Parameter**

    ======= ========= ========================== =======
    Name    Type      Range                      Default
    ======= ========= ========================== =======
    <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
    ======= ========= ========================== =======

    **Explanation**

    GREater: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the preset time limit
    (refer to the :TRIGger:DELay:TLOWer command).

    LESS: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the preset time limit
    (refer to the :TRIGger:DELay:TUPPer command).

    GLESs: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the lower limit of
    the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
    limit must be lower than the time upper limit.

    GOUT: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the lower limit of the
    preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
     limit must be lower than the time upper limit.

    **Return Format**

    The query returns GOUT, GRE, LESS or GLES.

    **Example**

    :TRIGger:DELay:TYPe GOUT
    The query returns GOUT.
    """
    # Setup
    desired: DelayTypeEnum = DelayTypeEnum.INSIDE
    dev.trigger.delay.type.inside()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.type.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_type_outside(dev) -> None:
    """Test the delay type of delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TYPe <type>
    :TRIGger:DELay:TYPe?

    **Description**

    Set the delay type of delay trigger.
    Query the current delay type of delay trigger.

    **Parameter**

    ======= ========= ========================== =======
    Name    Type      Range                      Default
    ======= ========= ========================== =======
    <type>  Discrete  {GREater|LESS|GLESs|GOUT}  GREater
    ======= ========= ========================== =======

    **Explanation**

    GREater: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the preset time limit
    (refer to the :TRIGger:DELay:TLOWer command).

    LESS: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the preset time limit
    (refer to the :TRIGger:DELay:TUPPer command).

    GLESs: trigger when the time difference (△T) between the specified
    edges of source A and source B is greater than the lower limit of
    the preset time (refer to the :TRIGger:DELay:TLOWer command) and lower
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
    limit must be lower than the time upper limit.

    GOUT: trigger when the time difference (△T) between the specified
    edges of source A and source B is lower than the lower limit of the
    preset time (refer to the :TRIGger:DELay:TLOWer command) or greater
    than the upper limit of the preset time
    (refer to the :TRIGger:DELay:TUPPer command). Note that the time lower
     limit must be lower than the time upper limit.

    **Return Format**

    The query returns GOUT, GRE, LESS or GLES.

    **Example**

    :TRIGger:DELay:TYPe GOUT
    The query returns GOUT.
    """
    # Setup
    desired: DelayTypeEnum = DelayTypeEnum.OUTSIDE
    dev.trigger.delay.type.outside()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.type.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_slope_a_set_positive(dev) -> None:
    """Test the type of edge A of delay trigger.

    **Rigol Programming Guide**

    **Syntax**
    :TRIGger:DELay:SLOPA <slope>
    :TRIGger:DELay:SLOPA?

    **Description**

    Set the edge type of edge A of delay trigger.
    Query the current edge type of edge A of delay trigger.

    Set the edge type of edge B of delay trigger.
    Query the current edge type of edge B of delay trigger.

    **Parameter**

    ======== ========= ==================== ========
    Name     Type      Range                Default
    ======== ========= ==================== ========
    <slope>  Discrete  {POSitive|NEGative}  POSitive
    ======== ========= ==================== ========

    **Return Format**

    The query returns POS or NEG.

    **Example**

    :TRIGger:DELay:SLOPA NEGative
    The query returns NEG.

    :TRIGger:DELay:SLOPB NEGative
    The query returns NEG.
    """
    # Setup
    desired: DelaySlopeEnum = DelaySlopeEnum.POSITIVE
    dev.trigger.delay.slope_a.set_positive()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.slope_a.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_slope_a_set_negative(dev) -> None:
    """Test the type of edge A of delay trigger.

    **Rigol Programming Guide**

    **Syntax**
    :TRIGger:DELay:SLOPA <slope>
    :TRIGger:DELay:SLOPA?

    **Description**

    Set the edge type of edge A of delay trigger.
    Query the current edge type of edge A of delay trigger.

    Set the edge type of edge B of delay trigger.
    Query the current edge type of edge B of delay trigger.

    **Parameter**

    ======== ========= ==================== ========
    Name     Type      Range                Default
    ======== ========= ==================== ========
    <slope>  Discrete  {POSitive|NEGative}  POSitive
    ======== ========= ==================== ========

    **Return Format**

    The query returns POS or NEG.

    **Example**

    :TRIGger:DELay:SLOPA NEGative
    The query returns NEG.

    :TRIGger:DELay:SLOPB NEGative
    The query returns NEG.
    """
    # Setup
    desired: DelaySlopeEnum = DelaySlopeEnum.NEGATIVE
    dev.trigger.delay.slope_a.set_negative()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.slope_a.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_slope_b_set_positive(dev) -> None:
    """Test the type of edge B of delay trigger.

    **Rigol Programming Guide**

    **Syntax**
    :TRIGger:DELay:SLOPA <slope>
    :TRIGger:DELay:SLOPA?

    **Description**

    Set the edge type of edge A of delay trigger.
    Query the current edge type of edge A of delay trigger.

    Set the edge type of edge B of delay trigger.
    Query the current edge type of edge B of delay trigger.

    **Parameter**

    ======== ========= ==================== ========
    Name     Type      Range                Default
    ======== ========= ==================== ========
    <slope>  Discrete  {POSitive|NEGative}  POSitive
    ======== ========= ==================== ========

    **Return Format**

    The query returns POS or NEG.

    **Example**

    :TRIGger:DELay:SLOPA NEGative
    The query returns NEG.

    :TRIGger:DELay:SLOPB NEGative
    The query returns NEG.
    """
    # Setup
    desired: DelaySlopeEnum = DelaySlopeEnum.POSITIVE
    dev.trigger.delay.slope_b.set_positive()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.slope_b.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_slope_b_set_negative(dev) -> None:
    """Test the type of edge B of delay trigger.

    **Rigol Programming Guide**

    **Syntax**
    :TRIGger:DELay:SLOPA <slope>
    :TRIGger:DELay:SLOPA?

    **Description**

    Set the edge type of edge A of delay trigger.
    Query the current edge type of edge A of delay trigger.

    Set the edge type of edge B of delay trigger.
    Query the current edge type of edge B of delay trigger.

    **Parameter**

    ======== ========= ==================== ========
    Name     Type      Range                Default
    ======== ========= ==================== ========
    <slope>  Discrete  {POSitive|NEGative}  POSitive
    ======== ========= ==================== ========

    **Return Format**

    The query returns POS or NEG.

    **Example**

    :TRIGger:DELay:SLOPA NEGative
    The query returns NEG.

    :TRIGger:DELay:SLOPB NEGative
    The query returns NEG.
    """
    # Setup
    desired: DelaySlopeEnum = DelaySlopeEnum.NEGATIVE
    dev.trigger.delay.slope_b.set_negative()

    # Exercise
    actual: DelayTypeEnum = dev.trigger.delay.slope_b.status()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_channel_signal_source_a_1(dev) -> None:
    """Test the trigger source of signal source A in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SA <Source>
    :TRIGger:DELay:SA?

    **Description**

    Select the trigger source of signal source A in delay trigger.
    Query the current trigger source of signal source A in delay trigger.


    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SA CHANnel2
    The query returns CHAN2.
    """
    # Setup
    desired: int = 1
    dev.trigger.delay.set_channel_signal_source_a(desired)

    # Exercise
    actual: int = dev.trigger.delay.get_channel_signal_source_a()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_channel_signal_source_a_2(dev) -> None:
    """Test the trigger source of signal source A in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SA <Source>
    :TRIGger:DELay:SA?

    **Description**

    Select the trigger source of signal source A in delay trigger.
    Query the current trigger source of signal source A in delay trigger.


    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SA CHANnel2
    The query returns CHAN2.
    """
    # Setup
    desired: int = 2
    dev.trigger.delay.set_channel_signal_source_a(desired)

    # Exercise
    actual: int = dev.trigger.delay.get_channel_signal_source_a()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_channel_signal_source_a_fail(dev) -> None:
    """Test the trigger source of signal source A in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SA <Source>
    :TRIGger:DELay:SA?

    **Description**

    Select the trigger source of signal source A in delay trigger.
    Query the current trigger source of signal source A in delay trigger.


    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SA CHANnel2
    The query returns CHAN2.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.set_channel_signal_source_a(3)

    with pytest.raises(ValueError):
        dev.trigger.delay.set_channel_signal_source_a(0)

    # Cleanup - None


def test_delay_channel_signal_source_b_1(dev) -> None:
    """Test the trigger source of signal source B in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SB <Source>
    :TRIGger:DELay:SB?

    **Description**

    Select the trigger source of signal source B in delay trigger.
    Query the current trigger source of signal source B in delay trigger.

    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SB CHANnel2
    The query returns CHAN2.
    """
    # Setup
    desired: int = 1
    dev.trigger.delay.set_channel_signal_source_b(desired)

    # Exercise
    actual: int = dev.trigger.delay.get_channel_signal_source_b()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_channel_signal_source_b_2(dev) -> None:
    """Test the trigger source of signal source B in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SB <Source>
    :TRIGger:DELay:SB?

    **Description**

    Select the trigger source of signal source B in delay trigger.
    Query the current trigger source of signal source B in delay trigger.

    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SB CHANnel2
    The query returns CHAN2.
    """
    # Setup
    desired: int = 2
    dev.trigger.delay.set_channel_signal_source_b(desired)

    # Exercise
    actual: int = dev.trigger.delay.get_channel_signal_source_b()

    # Verify
    assert actual == desired

    # Cleanup - None


def test_delay_channel_signal_source_b_fail(dev) -> None:
    """Test the trigger source of signal source B in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:SB <Source>
    :TRIGger:DELay:SB?

    **Description**

    Select the trigger source of signal source B in delay trigger.
    Query the current trigger source of signal source B in delay trigger.

    **Parameter**

    ========= ========= ==================== ========
    Name      Type      Range                Default
    ========= ========= ==================== ========
    <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
    ========= ========= ==================== ========

    **Return Format**

    The query returns CHAN1 or CHAN2.

    **Example**

    :TRIGger:DELay:SB CHANnel2
    The query returns CHAN2.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.set_channel_signal_source_b(3)

    with pytest.raises(ValueError):
        dev.trigger.delay.set_channel_signal_source_b(0)

    # Cleanup - None


def test_delay_set_upper_limit_when_less1(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 2.0e-9
    dev.trigger.delay.type.less()
    dev.trigger.delay.set_upper_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_upper_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_upper_limit_when_less2(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 4.0
    dev.trigger.delay.type.less()
    dev.trigger.delay.set_upper_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_upper_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_upper_limit_when_less_fail1(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.inside()
        dev.trigger.delay.set_upper_limit(1.0e-9)

    # Cleanup - None


def test_delay_set_upper_limit_when_less_fail2(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.inside()
        dev.trigger.delay.set_upper_limit(4.1)

    # Cleanup - None


def test_delay_set_upper_limit_when_outside(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 12.0e-9
    dev.trigger.delay.type.outside()
    dev.trigger.delay.set_upper_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_upper_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_upper_limit_when_outside_fail(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.outside()
        dev.trigger.delay.set_upper_limit(2.0e-9)

    # Cleanup - None


def test_delay_set_upper_limit_when_inside(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 12.0e-9
    dev.trigger.delay.type.inside()
    dev.trigger.delay.set_upper_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_upper_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_upper_limit_when_inside_fail(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.inside()
        dev.trigger.delay.set_upper_limit(2.0e-9)

    # Cleanup - None


def test_delay_set_upper_limit_when_greater_fail(dev) -> None:
    """Test the upper limit of the delay time in delay trigger.

    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TUPPer <NR3>
    :TRIGger:DELay:TUPPer?

    **Description**

    Set the upper limit of the delay time in delay trigger.
    Query the current upper limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ========== =======
    Name   Type  Range      Default
    ====== ===== ========== =======
    <NR3>  Real  2ns to 4s  2μs
    ====== ===== ========== =======

    Note: when the delay type is GLESs or GOUT, the range is
    from 12ns to 4s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the upper limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TUPPer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify - None
    with pytest.raises(TypeError):
        dev.trigger.delay.type.greater()
        dev.trigger.delay.set_upper_limit(12.0e-9)

    # Cleanup - None


def test_delay_set_lower_limit_when_less(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 2.0e-9
    dev.trigger.delay.type.less()
    dev.trigger.delay.set_lower_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_lower_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_lower_limit_when_less_fail1(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.less()
        dev.trigger.delay.set_lower_limit(1.0e-9)

    # Cleanup - None


def test_delay_set_lower_limit_when_less_fail2(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(ValueError):
        dev.trigger.delay.type.less()
        dev.trigger.delay.set_lower_limit(4.0)

    # Cleanup - None


def test_delay_set_lower_limit_when_outside(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 2.0e-9
    dev.trigger.delay.type.outside()
    dev.trigger.delay.set_lower_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_lower_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_lower_limit_when_inside(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup
    desired: float = 2.0e-9
    dev.trigger.delay.type.inside()
    dev.trigger.delay.set_lower_limit(desired)

    # Exercise
    actual: float = dev.trigger.delay.get_lower_limit()

    # Verify
    assert pytest.approx(actual, 0.0001) == desired

    # Cleanup - None


def test_delay_set_lower_limit_when_greater_fail(dev) -> None:
    """Test the lower limit of the delay time in delay trigger.

    ToDo: The range in the note is the same as in the table?
    **Rigol Programming Guide**

    **Syntax**

    :TRIGger:DELay:TLOWer <NR3>
    :TRIGger:DELay:TLOWer?

    **Description**

    Set the lower limit of the delay time in delay trigger.
    Query the current lower limit of the delay time in delay trigger.

    **Parameter**

    ====== ===== ============= =======
    Name   Type  Range         Default
    ====== ===== ============= =======
    <NR3>  Real  2ns to 3.99s  1μs
    ====== ===== ============= =======

    Note: when the delay type is GLESs or GOUT, the range is from 2ns
    to 3.99s.

    **Explanation**

    This command is available when the delay type (refer to
    the :TRIGger:DELay:TYPe command) is LESS, GOUT or GLESs.

    **Return Format**

    The query returns the lower limit of the delay time in scientific
    notation.

    **Example**

    :TRIGger:DELay:TLOWer 0.002
    The query returns 2.000000e-03.
    """
    # Setup - None
    # Exercise - None
    # Verify
    with pytest.raises(TypeError):
        dev.trigger.delay.type.greater()
        dev.trigger.delay.set_lower_limit(2.0e-9)

    # Cleanup - None


# vim: set ft=python :
