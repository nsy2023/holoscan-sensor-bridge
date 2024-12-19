"""
SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from collections import namedtuple
from enum import Enum

import hololink

# values are on hex number system to be consistent with rest of the list
IMX715_TABLE_WAIT_MS = "imx715-table-wait-ms"
IMX715_WAIT_MS = 0x01
IMX715_WAIT_MS_START = 0x0F

# Register addresses for camera properties. They only accept 8bits of value.

# Exposure
REG_EXP_MSB = 0x3051
REG_EXP_LSB = 0x3050

# (Analog + Digital) Gain
REG_G = 0x3090

imx715_start = [
        (0x3000, 0x00),  # mode select streaming on
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS_START),
        (0x3002, 0x00),
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS_START),
    ]

imx715_stop = [
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS),
        (0x3000, 0x01),  # mode select streaming off
        (0x3002, 0x01),
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS),
    ]

# IMX415-AAQR Window cropping 3840x2176  CSI-2_4lane 37.125Mhz AD:12bit Output:12bit 1485Mbps Master Mode 30fps
# value pairs use hex number system
imx715_mode_3840X2176_30fps = [
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS),
        (0x3008,0x7F),
        (0x300A,0x5B),
        (0x301C,0x04),
        (0x3024,0x94),
        (0x3025,0x11),
        (0x3031,0x00),
        (0x3032,0x00),
        (0x3033,0x08),
        (0x3040,0x0c),
        (0x3042,0x00),
        (0x3044,0x10),
        (0x3046,0x00),
        (0x3050,0x08),
        (0x30C1,0x00),
        (0x3116,0x24),
        (0x3118,0xA0),
        (0x311E,0x24),
        (0x32D4,0x21),
        (0x32EC,0xA1),
        (0x344C,0x2B),
        (0x344D,0x01),
        (0x344E,0xED),
        (0x344F,0x01),
        (0x3450,0xF6),
        (0x3451,0x02),
        (0x3452,0x7F),
        (0x3453,0x03),
        (0x358A,0x04),
        (0x35A1,0x02),
        (0x35EC,0x27),
        (0x35EE,0x8D),
        (0x35F0,0x8D),
        (0x35F2,0x29),
        (0x36BC,0x0C),
        (0x36CC,0x53),
        (0x36CD,0x00),
        (0x36CE,0x3C),
        (0x36D0,0x8C),
        (0x36D1,0x00),
        (0x36D2,0x71),
        (0x36D4,0x3C),
        (0x36D6,0x53),
        (0x36D7,0x00),
        (0x36D8,0x71),
        (0x36DA,0x8C),
        (0x36DB,0x00),
        (0x3701,0x00),
        (0x3720,0x00),
        (0x3724,0x02),
        (0x3726,0x02),
        (0x3732,0x02),
        (0x3734,0x03),
        (0x3736,0x03),
        (0x3742,0x03),
        (0x3862,0xE0),
        (0x38CC,0x30),
        (0x38CD,0x2F),
        (0x395C,0x0C),
        (0x39A4,0x07),
        (0x39A8,0x32),
        (0x39AA,0x32),
        (0x39AC,0x32),
        (0x39AE,0x32),
        (0x39B0,0x32),
        (0x39B2,0x2F),
        (0x39B4,0x2D),
        (0x39B6,0x28),
        (0x39B8,0x30),
        (0x39BA,0x30),
        (0x39BC,0x30),
        (0x39BE,0x30),
        (0x39C0,0x30),
        (0x39C2,0x2E),
        (0x39C4,0x2B),
        (0x39C6,0x25),
        (0x3A42,0xD1),
        (0x3A4C,0x77),
        (0x3AE0,0x02),
        (0x3AEC,0x0C),
        (0x3B00,0x2E),
        (0x3B06,0x29),
        (0x3B98,0x25),
        (0x3B99,0x21),
        (0x3B9B,0x13),
        (0x3B9C,0x13),
        (0x3B9D,0x13),
        (0x3B9E,0x13),
        (0x3BA1,0x00),
        (0x3BA2,0x06),
        (0x3BA3,0x0B),
        (0x3BA4,0x10),
        (0x3BA5,0x14),
        (0x3BA6,0x18),
        (0x3BA7,0x1A),
        (0x3BA8,0x1A),
        (0x3BA9,0x1A),
        (0x3BAC,0xED),
        (0x3BAD,0x01),
        (0x3BAE,0xF6),
        (0x3BAF,0x02),
        (0x3BB0,0xA2),
        (0x3BB1,0x03),
        (0x3BB2,0xE0),
        (0x3BB3,0x03),
        (0x3BB4,0xE0),
        (0x3BB5,0x03),
        (0x3BB6,0xE0),
        (0x3BB7,0x03),
        (0x3BB8,0xE0),
        (0x3BBA,0xE0),
        (0x3BBC,0xDA),
        (0x3BBE,0x88),
        (0x3BC0,0x44),
        (0x3BC2,0x7B),
        (0x3BC4,0xA2),
        (0x3BC8,0xBD),
        (0x3BCA,0xBD),
        (0x4004,0x48),
        (0x4005,0x09),
        (0x4018,0xA7),
        (0x401A,0x57),
        (0x401C,0x5F),
        (0x401E,0x97),
        (0x4020,0x5F),
        (0x4022,0xAF),
        (0x4024,0x5F),
        (0x4026,0x9F),
        (0x4028,0x4F),
        (IMX715_TABLE_WAIT_MS, IMX715_WAIT_MS),
    ]

class Imx715_Mode(Enum):
    IMX715_MODE_3840X2176_30FPS = 0
    Unknown = 1


frame_format = namedtuple(
    "FrameFormat", ["width", "height", "framerate", "pixel_format"]
)


imx_frame_format = []
imx_frame_format.insert(
    Imx715_Mode.IMX715_MODE_3840X2176_30FPS.value,
    frame_format(3840, 2176, 30, hololink.sensors.csi.PixelFormat.RAW_10),
)