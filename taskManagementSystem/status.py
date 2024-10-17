from enum import Enum

class Status(Enum):
    CREATED  = 1
    ASSIGNED = 2
    IN_PROGRESS = 3
    COMPLETED = 4