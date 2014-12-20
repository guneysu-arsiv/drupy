#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
TODAY = date.today().strftime('%d/%m/%Y')

__all__ = ['node']


def node(title, summary, body, date=None, type='takvim'):
    """docstring for node"""
    node = {'type': type,
            'title': title,
            'body': {'und': [{'summary': summary,
                              'value': body}]},
            'field_date': {'und': [{'value': {'date': TODAY}}]}
            }
    return node


def taxonomy():
    pass


def vocabulary():
    pass


def file():
    pass

if __name__ == '__main__':
    print node(title=u'BAŞLIK',
               summary='Summary',
               body=u'*BODY*')
