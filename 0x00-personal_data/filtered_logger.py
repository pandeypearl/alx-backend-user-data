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
