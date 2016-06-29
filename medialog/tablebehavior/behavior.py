from zope import schema
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from medialog.tablebehavior.widgets.widget import TableFieldWidget

_ = MessageFactory('medialog.tablebehavior')


class ITableBehavior(form.Schema):
    """ A field for a table (to and from)"""
    
    form.fieldset(
        'plotly',
        label = 'Table',
        fields=[
              'table',
        ],
     )  
    
    table = schema.TextLine(
        title=u'Table',
        default=u'',
        required=False,
    )  
    
    form.widget(
            table=TableFieldWidget
    )

alsoProvides(ITableBehavior, IFormFieldProvider)

