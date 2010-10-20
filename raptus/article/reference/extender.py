from Acquisition import aq_parent
from AccessControl import ClassSecurityInfo

from zope.interface import implements
from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes import atapi

try: # Plone 4 and higher
    from archetypes.referencebrowserwidget import ReferenceBrowserWidget as BaseReferenceBrowserWidget
except: # BBB Plone 3
    from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget as BaseReferenceBrowserWidget

from raptus.article.core import RaptusArticleMessageFactory as _
from raptus.article.core.interfaces import IArticle

class ReferenceField(ExtensionField, atapi.ReferenceField):
    """ ReferenceField
    """

class StringField(ExtensionField, atapi.StringField):
    """ StringField
    """
    
class ReferenceBrowserWidget(BaseReferenceBrowserWidget):
    _properties = BaseReferenceBrowserWidget._properties.copy()
    security = ClassSecurityInfo()

    security.declarePublic('isVisible')
    def isVisible(self, instance, mode='view'):
        """ Check if we are contained in an Article
        """
        container = aq_parent(instance)
        if IArticle.providedBy(container):
            return 'visible'
        return 'invisible'
    
class StringWidget(atapi.StringWidget):
    _properties = atapi.StringWidget._properties.copy()
    security = ClassSecurityInfo()

    security.declarePublic('isVisible')
    def isVisible(self, instance, mode='view'):
        """ Check if we are contained in an Article
        """
        container = aq_parent(instance)
        if IArticle.providedBy(container):
            return 'visible'
        return 'invisible'
    
class ArticleExtender(object):
    """ Adds the reference fields to the article schema
    """
    implements(ISchemaExtender)
    adapts(IArticle)

    fields = [
        ReferenceField('internal-reference',
        relationship = 'referenceTo',
        multiValued = False,
        widget = ReferenceBrowserWidget(
            allow_search = True,
            allow_browse = True,
            show_indexes = False,
            force_close_on_insert = True,
            label = _(u'label_internal_reference', default=u'Internal reference'),
            description = '',
            visible = {'edit' : 'visible', 'view' : 'invisible' }
            )
        ),
        
        StringField('external-reference',
            validators = ('isURL',),
            widget = StringWidget(
                description = '',
                label = _(u'label_external_reference', default=u'External reference')
            )
        ),
    ]

    def __init__(self, context):
         self.context = context
         
    def getFields(self):
        return self.fields
