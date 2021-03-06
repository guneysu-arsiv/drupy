#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(dict):
    """
    Base class for Node types.
    Note that body (long text with summary) field is not required
    for a content type. It is highly recommended for a content type
    """
    def __init__(self, *args, **kwargs):
        super(Node, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

class Takvim(Node):

    """docstring for Takvim"""
    # FIXME get parameter for field_date
    # TODO getting field name from parameters

    def __init__(self, **kwargs):
        # FIXME FIXME FIXME here is very confusing
        self.kwargs = kwargs

        kwargs['field_date'] = dict(und=[dict(
            value=dict(date=formatted_date(kwargs.get('field_date'))),
            timezone='UTC'
        )])
        kwargs.update(dict(format='markdown', type='takvim'))
        kwargs['status'] = True
        super(Takvim, self).__init__(**kwargs)


class BlogPost(Node):

    """docstring for Takvim"""
    # FIXME FIXME FIXME !!!

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        return super(BlogPost, self).__init__(type='blog_post', **kwargs)


class Page(Node):

    """docstring for Simple Page"""
    # FIXME FIXME FIXME !!!

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        return super(Page, self).__init__(type='page', **kwargs)
