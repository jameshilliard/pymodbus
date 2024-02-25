"""ModbusMessage layer.

is extending ModbusProtocol to handle receiving and sending of messsagees.

ModbusMessage provides a unified interface to send/receive Modbus requests/responses.
"""
from __future__ import annotations

from pymodbus.message.base import MessageBase


class MessageSocket(MessageBase):
    """Modbus Socket frame type.

    [         MBAP Header         ] [ Function Code] [ Data ]
    [ tid ][ pid ][ length ][ uid ]
      2b     2b     2b        1b           1b           Nb

    * length = uid + function code + data
    """

    def decode(self, _data: bytes) -> tuple[int, int, int, bytes]:
        """Decode message."""
        return 0, 0, 0, b''

    def encode(self, _data: bytes, _device_id: int, _tid: int) -> bytes:
        """Decode message."""
        return b''