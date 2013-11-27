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
from zope.schema import ValidationError
from zope.schema.interfaces import WrongContainedType


class IPage(interface.Interface):
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Page title.'),
        required=True)

    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of the content.'),
        required=False)

    text = RichText(
        title=_(u'Body'),
        description=_(u'Page body text.'),
        required=True)


class IPageTab(interface.Interface):
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'document title.'),
        default=u'',
        missing_value=u'',
        required=True)

    text = RichText(
        title=_(u'Text'),
        description=_(u'Blog post body text.'),
        required=False)

    position = schema.TextLine(
        title=_(u'Position'),
        required=False)


class WrongTabsError(ValidationError):
    __doc__ = _("""Some have has an errors""")


class WrongTabError(ValidationError):
    __doc__ = _("""This tab has an error""")


class TabsField(schema.List):
    def _validate(self, value):
        try:
            super(TabsField, self)._validate(value)
        except WrongContainedType:
            raise WrongTabsError()


class TabSchema(schema.Object):
    def _validate(self, value):
        try:
            super(TabSchema, self)._validate(value)
        except WrongContainedType:
            raise WrongTabError()


class IAdvancedPage(IPage):
    text = interface.Attribute("Object's Text")

    tabs = TabsField(
        title=_(u"Tabs"),
        value_type=TabSchema(
            title=_(u'Tab'),
            schema=IPageTab),
        default=[],
        required=True)


class IPageType(interface.Interface):
    """ page type """


class IAdvancedPageType(IPageType):
    """ page content type """