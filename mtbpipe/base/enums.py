from enum import Enum


class StrAutoEnum(str, Enum):

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name
