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

from dmx.colour import BLACK, Colour

DMX_MAX_ADDRESS = 512
DMX_MIN_ADDRESS = 1

ligh_map = [0, 1, 2, 27, 28, 29, 3, 4, 5, 30, 31, 32, 6, 7, 8, 33, 34, 35, 9, 10, 11, 36, 37, 38, 12, 13, 14, 39, 40,
            41, 15, 16, 17, 42, 43, 44, 18, 19, 20, 45, 46, 47, 21, 22, 23, 48, 49, 50, 24, 25, 26, 51, 52, 53]


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

    def set_colour(self, colour: Colour):
        """Set the colour for the light."""
        self._colour = colour

    def serialise(self) -> List[int]:
        """Serialise the DMX light to a sequence of bytes."""
        return self._colour.serialise()
