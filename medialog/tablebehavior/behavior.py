from zope import schema
from zope.interface import implements
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from zope.schema.interfaces import IFromUnicode

from medialog.tablebehavior.widgets.widget import TableFieldWidget

_ = MessageFactory('medialog.tablebehavior')
from zope.interface import implementer

@implementer(IFromUnicode)
class ITableBehavior(form.Schema):
    """ A field for a table (to and from)"""

       
    form.fieldset(
        'plotly',
        label = 'Table',
        fields=[
              'table',
        ],
     )  
    
    table = schema.List(
        title=u'Table',
        default=[["A", "B"], ["A1", "B1"]],
        required=False,
    )  
    
    form.widget(
            table=TableFieldWidget
    )

alsoProvides(ITableBehavior, IFormFieldProvider)

