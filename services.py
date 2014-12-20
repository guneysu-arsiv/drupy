#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
drupal_services is a module to call Drupal Services.
"""

import requests
from pprint import pprint

class ServicesSessionInfo:

    """docstring for ServicesSessionInfo"""

    def __init__(self, url, username, password):
        # TODO
        # https://groups.drupal.org/node/358308
        # POST url/user/token.json
        #  Save CSRF = data['token']
        # POST url/user/login.json username/password
        #   Save session_name and session_id
        # POST url/system/get_variable.json
        #   Headers
        #       Cookie :    <session_name> = <session_id>
        #       X-CSRF-Token  = <CSRF Token>
        pass


class Crud(object):

    """docstring for Crud"""
    # TODO
    # Create/Retrieve/Update/Delete/Index

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        pass

    def index(self):
        full_url = '%s/%s.json' % (self.kwargs['config']['url'],
                              self.base_url)
        return requests.get(full_url,
                params = self.kwargs['config'].fromkeys( ['services_token'],
                    self.kwargs['config']['services_token'])
                ).json()

    def create(self):
        pass

    def update(self):
        pass

    def retrieve(self):
        pass

    def delete(self):
        pass


class FileServices(Crud):

    """docstring for FileServices"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'file'
        super(FileService, self).__init__(*args, **kwargs)
        return


class NodeService(Crud):

    """docstring for NodeService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'node'
        super(NodeService, self).__init__(*args, **kwargs)
        return


class TermService(Crud):

    """docstring for TermService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'taxonomy_term'
        super(TermService, self).__init__(*args, **kwargs)
        return

    def select_nodes(self):
        """docstring for select_nodes"""
        url = '%s/%s' % (self.base_url, 'selectNodes')
        # Method POST
        # Content-Type: application/x-www-form-urlencoded
        # Payload tid=<TID>
        return


class VocabularyService(Crud):

    """docstring for VocabularyService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'taxonomy_vocabulary'
        super(VocabularyService, self).__init__(*args, **kwargs)
        return

    def getTree(self):
        """docstring for getTree"""
        # Method POST
        # Content-Type: application/x-www-form-urlencoded
        # Payload vid=1
        #
        url = '%s/%s' % (self.base_url, 'getTree')
        return


class SystemService(object):

    """docstring for SystemService"""

    def __init__(self, *args, **kwargs):
        pass

    def connect(self, *args, **kwargs):
        """docstring for connect"""
        pass

    def get_variable(self, *args, **kwargs):
        """docstring for get_variable"""
        pass


class DrupalServices:

    """Drupal services class.
    config is a nice way to deal with configuration files."""

    def __init__(self, config):
        self.config = config
        self.node = NodeService(config=config)
        self.term = TermService(config=config)
        self.file = FileService(config=config)
        self.vocabulary = VocabularyService(config=config)

        if (config.has_key('username') and config.has_key('key')):
            pass
            # NotImplemented
        elif (config.has_key('services_token')):
            # TODO define new class for session
            # Get X-CSRF-Token
            pass


if __name__ == '__main__':
    import config
    import interface
    NODE = interface.node(title=u'BAŞLIK',
                          summary=u'ÖZET',
                          body=u'GÖVDE GÖSTERİSİ')

    drupal = DrupalServices(config.config_local)
    pprint ( drupal.node.index() )
    pprint ( drupal.file.index() )
    pprint ( drupal.term.index() )
    pprint ( drupal.vocabulary.index() )
