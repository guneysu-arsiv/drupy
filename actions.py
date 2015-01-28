#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class NodeActions(object):
    """docstring for NodeActions"""
    def __init__(self, *args, **kwargs):
        super(NodeActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def publish(self):
        pass

    def unpublish(self):
        pass

class VocabularyActions(object):
    """docstring for VocabularyActions"""
    def __init__(self, *args, **kwargs):
        super(VocabularyActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

class TermActions(object):
    """docstring for TermActions"""
    def __init__(self, *args, **kwargs):
        super(TermActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def selectNodes(self, *args, **kwargs):
        """docstring for selectNodes"""
        pass

class FileActions(object):
    """docstring for FileActions"""
    def __init__(self, *args, **kwargs):
        super(FileActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def create_raw(self, *args, **kwargs):
        """docstring for create_raw"""
        pass



class UserActions(object):
    """docstring for UserActions"""
    def __init__(self, *args, **kwargs):
        super(UserActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

class SystemActions(object):
    """docstring for SystemActions"""
    def __init__(self, *args, **kwargs):
        super(SystemActions, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def connect(self, *args, **kwargs):
        """docstring for connect"""
        pass

    def get_variable(self, *args, **kwargs):
        """docstring for get_variable"""
        pass

    def set_variable(self, *args, **kwargs):
        """docstring for set_variable"""
        pass

    def del_variable(self, *args, **kwargs):
        """docstring for del_variable"""
        pass

