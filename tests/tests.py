#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ahmedseref'

import sys
sys.path.append('..')
import services
import config
from pprint import pprint

test_drupal = services.DrupalServices(config=config.config_local)


# CRUID Tests


# 1/5 Index
def test_index_node():
    index = test_drupal.node.index()
    assert (index == [] or
            index[0].has_key('nid'))


def test_index_vocabulary():
    index = test_drupal.term.index()
    assert (index == [] or
            index[0].has_key('vid'))


def test_index_term():
    index = test_drupal.term.index()
    assert (index == [] or
            index[0].has_key('tid'))


def test_index_file():
    index = test_drupal.file.index()
    assert (index == [] or
            index[0].has_key('fid'))
# 2/5 Create


def test_create_node():
    resp = test_drupal.node.create(
        title='__TITLE',
        type='blog_post',
        body='**BOO YEAH!**',
        summary='_Summary_')
    assert (resp.has_key('nid'))


def test_create_vocabulary():
    resp = test_drupal.vocabulary.create(
        name='Voccaaa!',
        description='Description',
        machine_name='test_voca',
        format='markdown')
    assert (resp == [1])


def test_create_term():
    # TODO Check if there a vocabulary with vid
    # TODO Or pick first vid from vocabulary_index
    resp = test_drupal.term.create(
        vid=2,
        name='Example Term!',
        description='Description',
        machine_name='test_voca',
        format='markdown')
    assert (resp == [1])


def test_create_file():
    # Coming soon ;)
    pass

# 3/5 Retrieve


def test_retrieve_node():
    # TODO Fetch node index and pass a arbitrary id
    index = test_drupal.node.retrieve(313)
    assert (index.has_key('nid'))


def test_retrieve_vocabulary():
    # TODO Fetch vocabulary index and pass a arbitrary id
    index = test_drupal.vocabulary.retrieve(2)
    pprint(index)
    assert (index.has_key('vid'))


def test_retrieve_term():
    # TODO Fetch term index and pass a arbitrary id
    index = test_drupal.term.retrieve(2)
    pprint(index)
    assert (index.has_key('tid'))


if __name__ == '__main__':
    test_node_index()
