##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" page interfaces

$Id$
"""
from zope import schema, interface
from zojax.richtext.field import RichText
from zojax.contenttypes.interfaces import _


class IPage(interface.Interface):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Page title.'),
        required = True)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'A short summary of the content.'),
        required = False)

    text = RichText(
        title = _(u'Body'),
        description = _(u'Page body text.'),
        required = True)


class IPageType(interface.Interface):
    """ page content type """
