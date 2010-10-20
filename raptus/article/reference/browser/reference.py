from Acquisition import aq_inner
from zope import interface, component

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from raptus.article.reference.interfaces import IReference

class Reference(ViewletBase):
    """ Viewlet information about internal or external references
    """
    index = ViewPageTemplateFile('reference.pt')
    
    @property
    @memoize
    def reference(self):
        provider = IReference(self.context)
        return provider.getReference()
    
    @property
    @memoize
    def reference_url(self):
        provider = IReference(self.context)
        return provider.getReferenceURL()
