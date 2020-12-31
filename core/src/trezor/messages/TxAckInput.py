# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TxAckInputWrapper import TxAckInputWrapper

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckInput(p.MessageType):
    MESSAGE_WIRE_TYPE = 22

    def __init__(
        self,
        *,
        tx: TxAckInputWrapper,
    ) -> None:
        self.tx = tx

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tx', TxAckInputWrapper, p.FLAG_REQUIRED),
        }
