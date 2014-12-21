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

class ServicesRequest(object):
    """docstring for ServicesRequest
        Headers
            Accept          : application/json
            Cookie          : <session_name> = <session_id>
            X-CSRF-Token    : <x-csrf-token>
            Session Info    : <username> <e-mail> etc.
        Payload
            services_token  : <token>
        """
        # TODO Implement HEAD method to fetch headers
    def __init__(self, config, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.config = config
        self.params = self.config.fromkeys( ['services_token'],
                    self.config['services_token'])
        self.headers  = dict ( Accept = 'application/json')

    def __call__(self, *args, **kwargs):
        """docstring for __call__"""
        # TODO return request data
        pass

    def get(self, url, accept='json',params=None, payload=None, *args, **kwargs):
        """docstring for get"""
        url_parameters = self.config.fromkeys( ['services_token'],
                    self.config['services_token'])
        return requests.get(url,
                params = url_parameters,
                headers = {'Accept': 'application/%s' % accept},
                data = payload,
                ).json()
        pass

    def post(self, *args, **kwargs):
        """docstring for post"""
        pass

    def put(self, *args, **kwargs):
        """docstring for put put"""
        pass

    def delete(self, *args, **kwargs):
        """docstring for delete"""
        pass



class Crud(object):

    """docstring for Crud"""
    # TODO
    # Add Accept: application/json to all requests
    # Or find a method that always add .json to end of url
    # Create/Retrieve/Update/Delete/Index

    def __init__(self, config, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.config = config
        self.request = ServicesRequest(config)
        self.full_path = '%s/%s' % (self.config['url'],
                              self.base_url)
        pass

    def index(self):
        return self.request.get(self.full_path)

    def create(self):
        pass

    def update(self):
        pass

    def retrieve(self, id):
        url = '%s/%s.json' % ( self.full_path,
                id)

        return self.request.get(url)

    def delete(self):
        pass


class FileService(Crud):

    """docstring for FileServices"""

    def __new__(self, *args, **kwargs):
        self.base_url = 'file'
        self.args = args
        self.kwargs = kwargs
        return


class NodeService(Crud):

    """docstring for NodeService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'node'
        self.args = args
        self.kwargs = kwargs
        super(NodeService, self).__init__(*args, **kwargs)
        return


class TermService(Crud):

    """docstring for TermService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'taxonomy_term'
        self.args = args
        self.kwargs = kwargs
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
        self.args = args
        self.kwargs = kwargs
        super(VocabularyService, self).__init__(*args, **kwargs)

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
        self.node = NodeService(config=config)
        self.term = TermService(config=config)
        self.file = FileService(config=config)
        self.vocabulary = VocabularyService(config=config)

if __name__ == '__main__':
    import config
    import interface
    NODE = interface.node(title=u'BAŞLIK',
                          summary=u'ÖZET',
                          body=u'GÖVDE GÖSTERİSİ')

    # import ipdb; ipdb.set_trace() # BREAKPOINT
    drupal = DrupalServices(config.config_local)
    # pprint ( drupal.node.index() )
    pprint ( drupal.node.retrieve(120) )
    # pprint ( drupal.file.index() )
    # pprint ( drupal.term.index() )
    # pprint ( drupal.vocabulary.index() )
    # pprint ( drupal.vocabulary.retrieve(2))
