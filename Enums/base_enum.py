from enum import Enum


class BaseLedgerOperation(Enum):
     DAILY_REWARD = "DAILY_REWARD"
     SIGNUP_CREDIT = "SIGNUP_CREDIT"
     CREDIT_SPEND = "CREDIT_SPEND"
     CREDIT_ADD = "CREDIT_ADD"


class LedgerOperation(Enum):
     CONTENT_CREATION = "CONTENT_CREATION"
     CONTENT_ACCESS = "CONTENT_ACCESS"


def combined_enums(*enums):
    combined = {}
    for enum in enums:
        combined.update(enum.__members__)
    return Enum('CombinedLedgerOperation', combined)