#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
drupal_services is a module to call Drupal Services.
"""

import requests

from datetime import date

TODAY = date.today().strftime('%d/%m/%Y')
# TODO give ability to custom date/time formatting


class Node(dict):
    """docstring for Node
        Placeholder for base Node type
        This class will be used for custom nodes
        that have different field types
        Like date, long, list, taxonomy_reference, etc.
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        body = {'body': {'und':
                             [{'summary': kwargs.get('summary'),
                               'value': kwargs.get('body')}]}}
        super(Node, self).__init__(**kwargs)
        self.update(body)


class Takvim(Node):
    """docstring for Takvim"""

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        field_date = {'field_date':
                          {'und': [{'value': {'date': TODAY}}]}}
        super(Takvim, self).__init__(type='takvim', **kwargs)
        self.update(field_date)


class BlogPost(Node):
    """docstring for Takvim"""

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        return super(BlogPost, self).__init__(type='blog_post', **kwargs)


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
        self.params = self.config.fromkeys(['services_token'],
                                           self.config['services_token'])
        self.headers = dict(Accept='application/json')

    # @classmethod
    def __call__(self, method, url, payload=None, accept='json'):
        """docstring for __call__"""
        sess = requests.Session()
        req = requests.Request(method=method,
                               url=url,
                               params=self.params,
                               data=payload,
                               headers={'Accept': 'application/%s' % accept})
        prepped = req.prepare()
        return sess.send(prepped).json()

    def get(self, url, accept='json', params=None, payload=None, *args, **kwargs):
        """docstring for get"""
        url_parameters = self.config.fromkeys(['services_token'],
                                              self.config['services_token'])
        return requests.get(url,
                            params=url_parameters,
                            headers={'Accept': 'application/%s' % accept},
                            data=payload,
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

    def id_path(self, id):
        return '%s/%s' % (self.full_path, id)

    def new(self, **kwargs):
        return dict(kwargs)

    def index(self):
        # Method GET
        return self.request('GET', self.full_path)

    def create(self, **kwargs):
        # Method POST
        return self.request(
            method='POST',
            url=self.full_path,
            data=self.new(**kwargs))

    def update(self, id, node):
        # Method PUT
        url = self.id_path(id)
        return self.request(
            method='PUT',
            url=self.full_path,
            data=self.new(**kwargs))

    def retrieve(self, id):
        # Method  GET
        return self.request('GET', self.id_path(id))

    def delete(self, id):
        # Method DELETE
        return self.request('DELETE', self.id_path(id))


class FileService(Crud):
    """docstring for FileServices"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'file'
        self.args = args
        self.kwargs = kwargs
        super(FileService, self).__init__(*args, **kwargs)
        return


class NodeService(Crud):
    """docstring for NodeService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'node'
        self.args = args
        self.kwargs = kwargs
        super(NodeService, self).__init__(*args, **kwargs)
        return

    def new(self, **kargs):
        return Node(**kwargs)


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

    def new(self, **kwargs):
        """
        Parameters
            vid         :   <vid>
            name        :   <name>
            description :   <description>
            format      :   None|markdown|plain_text|etc
        """
        return super(TermService, self).new(**kwargs)


class VocabularyService(Crud):
    """docstring for VocabularyService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'taxonomy_vocabulary'
        self.args = args
        self.kwargs = kwargs
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

    def new(self, **kwargs):
        """
        Parameters
            name        :   <name>
            description :   <description>
            machine_name:  <transliterate_this>
            format      :   None|markdown|plain_text|etc
            hierarchy   :   0 Dont know what is it
        """
        return super(VocabularyService, self).new(**kwargs)


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

    drupal = DrupalServices(config.config_local)
