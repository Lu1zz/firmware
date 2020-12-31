# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoPoolOwnerType(p.MessageType):

    def __init__(
        self,
        *,
        staking_key_path: List[int] = None,
        staking_key_hash: bytes = None,
    ) -> None:
        self.staking_key_path = staking_key_path if staking_key_path is not None else []
        self.staking_key_hash = staking_key_hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('staking_key_path', p.UVarintType, p.FLAG_REPEATED),
            2: ('staking_key_hash', p.BytesType, None),
        }
