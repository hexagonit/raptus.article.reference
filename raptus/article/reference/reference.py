from zope import interface, component

from Products.CMFCore.utils import getToolByName

from raptus.article.core.interfaces import IArticle
from raptus.article.reference.interfaces import IReference

class Reference(object):
    """ Provider for internal and external references on an article
    """
    interface.implements(IReference)
    component.adapts(IArticle)
    
    def __init__(self, context):
        self.context = context
        
    def getReferenceURL(self):
        """ Returns the URL or path of the reference
        """
        external = self.context.Schema()['external-reference'].get(self.context)
        if external:
            return external
        internal = self.getReference()
        if internal:
            return internal.absolute_url()
        
    def getReference(self):
        """ Returns the referenced object, if available
        """
        if not self.context.Schema()['external-reference'].get(self.context):
            return self.context.Schema()['internal-reference'].get(self.context)
