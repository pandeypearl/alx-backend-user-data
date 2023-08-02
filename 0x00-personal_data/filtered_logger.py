#!/usr/bin/env python3
"""
Defines Logger With Custom Log Formatter
"""

import os
import re
import logging
from typing import List, Tuple


def filter_datum(
    fields: List[str], redaction: str,
    message: str, separator: str
) -> str:
    """
    Filtering message by replacing each value
    with a redaction
    """
    for key in fields:
        pattern = r'({0}=)[^{1}]*({1})'.format(key, separator)
        message = re.sub(pattern, r'\1{}\2'.format(redaction), message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Instantiation method.
        Sets fileds for each instance.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formatting the LogRecord instance.
        """
        log = super(RedactingFormatter, self).format(record=record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
