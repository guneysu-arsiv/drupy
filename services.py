#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
drupal_services is a module to call Drupal Services.
you must install https://www.drupal.org/project/services_token_access
module.

Because authenticating users with drupal requires
- Take X-CSRF-Token
- Login with user/password by giving X-CSRF-Token in the headers
- Take <session_name> and <session_id>
- Always send a Cookie header "Cookie: <session_name> = <session_id>
But be ware of that services_token is sent with url_parameter and
Use the module "AT YOUR OWN RISK!!!"

Go to user page and generate token.
Put this token into config.py
If your authenticated users will generate content, give your users to
use and manage tokens permission.

"""

import requests
import json
import logging

import datetime


def formatted_date(date_object, format='%m/%d/%Y - %H:%M:%S'):
    # TODO give ability to custom date/time formatting
    """
    Parameters:
        date  : datetime.date() item
        format      : string used for formatting
    """

    return date_object.strftime(format)


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

    def publish(self):
        pass

    def unpublish(self):
        pass

    def lookup(self):
        pass

    def autocomplete(self):
        pass

    def files(self):
        pass

    def attach_file(self):
        pass


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

    def __call__(self, method, url, data=None, accept='json'):
        """docstring for __call__"""
        resp = requests.request(method=method,
                                url=url,
                                params=self.params,
                                data=json.dumps(data),
                                headers={'Accept': 'application/%s' % accept,
                                         'Content-Type': 'application/json'})
        return resp.json()


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

    def create(self, Type, **kwargs):
        """
        Type parameter only used for Nodes.
        You can derive a custom NodeType class from Node() class.
        And pass it as an argument.
        See NodeService.new() method
        """

        # Method POST
        url = self.full_path
        data = self.new(Type, **kwargs)
        return self.request(
            method='POST',
            url=url,
            data=data)
        # FIXME No need to pass Type parameter if self is not instance of
        # NodeService

    def update(self, id, data):
        # Method PUT
        url = self.id_path(id)
        return self.request(
            method='PUT',
            url=url,
            data=data)  # FIXME data or json.dumps(data) ?

    def retrieve(self, id):
        # Method  GET
        # TODO normalize
        # node[body][und][value] -> node[body]
        # node[summary][und][value] -> node[summary]
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

    def create_raw(self):
        pass


class NodeService(Crud):

    """docstring for NodeService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'node'
        self.args = args
        self.kwargs = kwargs
        super(NodeService, self).__init__(*args, **kwargs)
        return

    def new(self, Type, **kwargs):
        # TODO May take Node type as argument
        """
        :param kargs:
        :return: Node(dict)
        Essential kwargs for node creations are
        type and title
        body not essential but should be exists
        summary is optional
        For nodes that contain different types of fields
        create your class that derived from Node class.
        Not implemented yet.
        NodeCls is a derived class from Node.
        You can derive a class and pass it as argument like
        self.node.new( MyCustomNodeType, **kwargs)
        """
        return Type(**kwargs)

    def last_updated(self):
        """
        Extra   : Retrieve the last updated node
        """
        if self.index() != []:
            nid = self.index()[0]['nid']
            node = self.retrieve(nid)
            title, path, body = node['title'], \
                node['path'], \
                node['body']['und'][0]['value']
            return dict(title=title, path=path, body=body)
        else:
            return dict()

    def custom(self):
        """
        Views data export Page
        Manually faked path for services path
        api/node/latest.json
        """
        data = self.request(method='GET',
                            url='%s/latest.json' % self.full_path)
        if data != [] and data[0].has_key('title'):
            return data
        else:
            return dict()


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
        :param kwargs:
        vid, name, description, format
        :vid           Required
        :name          Human readable term name (title)
        :description   like summary in nodes
        :format        Text format (machine readable)

        :return:
        dict(**kwargs)

        Unfortunately, you can not assign parents via REST api. But you can
        Retrieve parents of taxonomy terms in list format via
            <URL>/rest_end_point/taxonomy_vocabulary/getTree
            Method POST
            Payload {vid:<vocabulary_id>}
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
        :param kwargs:
        name, description, machine_name, format, hierarchy
        :name   Human readable vocabulary name (title)
        :description   like summary in nodes
        :machine_name   Machine readable ascii-set name. Not required.
        :format         Text format (machine readable)
        :hierarchy      Do not know, in integer

        :return:
        dict(**kwargs)
        """
        return super(VocabularyService, self).new(**kwargs)


class UserService(Crud):

    """docstring for UserService"""

    def __init__(self, *args, **kwargs):
        self.base_url = 'user'
        self.args = args
        self.kwargs = kwargs
        super(UserService, self).__init__(*args, **kwargs)

    def new(self, **kwargs):
        """
        Required keywords
            name, mail, pass
        Optional
            status,
        """
        return super(UserService, self).new(**kwargs)

    def register(self, **kwargs):
        """
        For compatibility
        """
        return self.create(**kwargs)

    def create(self, **kwargs):
        """
        Method  :   POST
        URL     :   register
        """
        return super(UserService, self).create(
            url='%s/%s' % (self.full_path, url),
            **kwargs)

    def login(self, *args, **kwargs):
        """docstring for login"""
        pass

    def logout(self, *args, **kwargs):
        """docstring for logout"""
        pass

    def token(self, *args, **kwargs):
        """docstring for token"""
        pass

    def request_new_password(self, *args, **kwargs):
        """docstring for request_new_password"""
        pass

    def cancel(self, *args, **kwargs):
        """docstring for cancel"""
        pass

    def password_reset(self, *args, **kwargs):
        """docstring for password_reset"""
        pass


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

    def set_variable(self, *args, **kwargs):
        """docstring for set_variable"""
        pass

    def resend_welcome_mail(self, *args, **kwargs):
        """docstring for resend_welcome_mail"""
        pass


class DrupalServices:

    """Drupal services class.
    config is a nice way to deal with configuration files."""
    # TODO Think that config  is property
    # Anytime it can replaced other config like
    # config_remote, config_other
    # get_attr, set_attr
    # Can be implemented by __call__ method

    def __init__(self, config):
        self.node = NodeService(config=config)
        self.term = TermService(config=config)
        self.file = FileService(config=config)
        self.user = UserService(config=config)
        self.vocabulary = VocabularyService(config=config)

    def __call__(self, config):
        return self.__init__(config)


if __name__ == '__main__':
    import config
    drupal = DrupalServices(config.config_local)
    # drupal(config.config_remote)
    # print drupal.node.create( Type=Takvim, title='__TEST', body='BOOO',
    # summary='**Foo**' )
    print drupal.node.last_updated().get('path')
    print drupal.node.custom()[0].get('path')
    # print drupal.node.full_path
    print formatted_date(datetime.date(2014, 1, 1), '%F')
