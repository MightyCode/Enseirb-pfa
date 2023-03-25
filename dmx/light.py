"""Module for DMX light definitions."""

# BSD 3-Clause License
#
# Copyright (c) 2019-2022, Jacob Allen
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from abc import ABC, abstractmethod
from typing import List

from dmx.color import BLACK, Color
import config

DMX_MAX_ADDRESS = 512
DMX_MIN_ADDRESS = 1

light_map = config.light_map

def light_id(id):
    return light_map[id]
    
def light_coord(x, y):
    return light_map[x + y * config.row_number]


class DMXLight(ABC):
    """Represents a DMX light."""

    def __init__(self, address: int = 1):
        """Initialise the light. The base initialiser simply stores the address."""
        self._address = int(max(0, min(address, DMX_MAX_ADDRESS)))

    @abstractmethod
    def serialise(self) -> List[int]:
        """Serialise the DMX light to a sequence of bytes."""

    @property
    def start_address(self) -> int:
        """Start address (inclusive) of the light."""
        return self._address

    @property
    def end_address(self) -> int:
        """End address (inclusive) of the light."""
        end_address = self._address + self.slot_count - 1
        if end_address > DMX_MAX_ADDRESS or end_address < DMX_MIN_ADDRESS:
            return (end_address % DMX_MAX_ADDRESS) + DMX_MIN_ADDRESS
        return end_address

    @property
    def slot_count(self) -> int:
        """Get the number of slots used by this light."""
        return 0


class DMXLight4Slot(DMXLight):
    """Represents a DMX light with RGBW."""

    def __init__(self, address: int = 0):
        """Initialise the light."""
        super().__init__(address=address * 4)
        self._colour = BLACK

    @property
    def slot_count(self) -> int:
        """Get the number of slots used by this light."""
        return 4

    def set_colour(self, color: Color):
        """Set the color for the light."""
        self._colour = color

    def get_colour(self) -> Color:
        """Get the color for the light."""
        return self._colour
    
    def serialise(self) -> List[int]:
        """Serialise the DMX light to a sequence of bytes."""
        return self._colour.serialise()
