from dataclasses import dataclass


# here, fronzen makes it hashable, otherwise it will crash
@dataclass(frozen=True)
class Subject:
    name: str
