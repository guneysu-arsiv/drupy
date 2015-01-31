#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = [
    'field_date',
    'long_text']

lass LongText(object):
    """docstring for LongText"""

    def __init__(self, *args, **kwargs):
        super(LongText, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs


class LongTextWithSummary(dict):

    """docstring for LongTextWithSummary"""

    def __init__(self, *args, **kwargs):
        super(LongTextWithSummary, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs


class Body(LongTextWithSummary):

    """docstring for Body"""

    def __init__(self, *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs
