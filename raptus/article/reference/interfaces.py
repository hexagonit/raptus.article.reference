from zope import interface

class IReference(interface.Interface):
    """ Provider for internal and external references on an article
    """
        
    def getReferenceURL():
        """ Returns the URL or path of the reference
        """
        
    def getReference():
        """ Returns the referenced object, if available
        """