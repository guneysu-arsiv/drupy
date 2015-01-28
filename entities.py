#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Vocabulary(dict):
    pass

class Term(dict):
    pass

class File(dict):
    pass

class Node(dict):

    """docstring for Node
        Placeholder for base Node type
        This class will be used for custom nodes
        that have different field types
        Like date, long, list, taxonomy_reference, etc.
    """

    def __init__(self,
                 type=None,
                 log='Published via Drupal Services',
                 status=None,
                 comment=None,
                 sticky=None,
                 language="und",
                 promote=None,
                 frontpage=None,
                 **kwargs):

        kwargs.update(dict(
            type=type,
            log=log,
            status=status,
            comment=comment,
            sticky=sticky,
            language=language,
            promote=promote,
            frontpage=frontpage))
        body = dict(body=dict(und=[dict(
            summary=kwargs.get('summary'),
            value=kwargs.get('body')
        )]))
        # body = {'body': {'und':
        #                  [{'summary': kwargs.get('summary'),
        #                    'value': kwargs.get('body')}]}}
        super(Node, self).__init__(**kwargs)
        self.update(dict(
            self.items() +
            body.items() +
            dict(status=status).items())
        )



class System(object):
    """docstring for System"""
    def __init__(self, *args, **kwargs):
        super(System, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

