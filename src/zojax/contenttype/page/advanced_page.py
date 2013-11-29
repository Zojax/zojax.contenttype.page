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
""" document implementation

$Id$
"""
from z3c.form.object import registerFactoryAdapter
from zojax.content.draft.browser.adding import AddContentWizard
from zojax.content.draft.browser.interfaces import IAddContentWizard
from zojax.content.forms.content import ContentStep
from zojax.content.forms.interfaces import IEditContentWizard, IContentStep
from zojax.content.forms.wizardedit import EditContentWizard
from zojax.content.type.interfaces import IItem
from zojax.layoutform import Fields
from zojax.resourcepackage.library import include
from zojax.wizard import WizardStepForm
from zojax.wizard.interfaces import ISaveable
from zope import interface
from zojax.richtext.field import RichTextProperty
from zope.cachedescriptors.property import Lazy
from zope.dublincore.interfaces import ICMFDublinCore
from zope.i18nmessageid import MessageFactory
from zope.schema.fieldproperty import FieldProperty
from interfaces import IAdvancedPage, IPageTab
from page import Page
from rwproperty import setproperty, getproperty
from zope.security.checker import canWrite


class AdvancedPage(Page):
    interface.implements(IAdvancedPage)

    @getproperty
    def tabs(self):
        return self.__dict__.get('tabs', [])

    @setproperty
    def tabs(self, value):
        old = self.tabs
        if value is not None:
            if len(value) > len(old):
                old.extend(value[len(old):])
            else:
                old = old[:len(value)]
        else:
            self.__data__['tabs'] = []
            return
        for k, v in enumerate(value):
            ov = old[k]
            ov.title = getattr(v, 'title', '')
            ov.text = getattr(v, 'text', '')
            ov.position = v.position

        # NOTE: sort by position
        old = sorted(old, key=lambda x: x.position)
        self.__dict__['tabs'] = old

    @property
    def text(self):
        return ''.join([getattr(tab.text, 'cooked', '') for tab in self.tabs])


class PageTab(object):
    interface.implements(IPageTab)

    title = None
    text = RichTextProperty(IPageTab['text'])
    position = FieldProperty(IPageTab['position'])

registerFactoryAdapter(IPageTab, PageTab)


class AdvancedPageView(object):
    """
    Advanced post view
    """
    def __init__(self, *args, **kw):
        include('advanced-page')
        super(AdvancedPageView, self).__init__(*args, **kw)


class AdvancedPageEditForm(EditContentWizard):
    interface.implements(ISaveable, IEditContentWizard)

    def __init__(self, *args, **kw):
        include('advanced-page')
        super(AdvancedPageEditForm, self).__init__(*args, **kw)

    @Lazy
    def fields(self):
        return Fields(IItem).omit('description')


class AdvancedPageAddForm(ContentStep):
    interface.implements(ISaveable)

    def __init__(self, *args, **kw):
        include('advanced-page')
        super(AdvancedPageAddForm, self).__init__(*args, **kw)

    @Lazy
    def fields(self):
        return Fields(IItem).omit('description')

    def isAvailable(self):
        if not (self.groups or self.subforms or self.forms or self.views):
            return bool(self.fields)

        return super(AdvancedPageAddForm, self).isAvailable()

