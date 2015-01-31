#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fields


class Title(str):

    """docstring for Title"""

    def __init__(self, *args, **kwargs):
        super(Title, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs


class Log(str):

    """docstring for Log"""

    def __init__(self, *args, **kwargs):
        super(Log, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs


def Bool(function,  val=None):
    """
    Decorator function for Boolean properties of Node.
    Pass val parameter for
    Comment/Status/Promote-Frontpage/Sticky properties
    """
    def decorated(val=None):
        return None if not val else True
    return decorated


@Bool
def Status():
    """
    Emulates behaviour of Drupal Services
    status/sticky/frontpage-promote
    But you can pass False/0/None value.
    """
    pass


@Bool
def Comment():
    """docstring for Comment"""
    pass


@Bool
def Promote():
    """docstring for Promote"""
    pass


@Bool
def Sticky():
    """docstring for Sticky"""
    pass


@Bool
def Translate():
    """docstring for Sticky"""
    pass


def Language(val=None):
    """docstring for Language"""
    return "und" if not val else val


def Name(val=None):
    """docstring for Name
    Not sure what is it
    """
    return "" if not val else val


def Picture(val=None):
    """docstring for Picture
    Not sure what is it
    """
    return 0 if not val else val


def Data(val=None):
    """docstring for Data
    Not sure what is it
    """
    return None if not val else val

if __name__ == '__main__':
    print Title("foo")
    print Log("log")

    print Status(val=1)
    print Sticky(val=1)
    print Comment(val=1)
    print Promote(val=1)

    print Status(val=0)
    print Sticky(val=0)
    print Comment(val=0)
    print Promote(val=0)

    print Status(val=False)
    print Sticky(val=False)
    print Comment(val=False)
    print Promote(val=False)

    print Status(val=None)
    print Sticky(val=None)
    print Comment(val=None)
    print Promote(val=None)
