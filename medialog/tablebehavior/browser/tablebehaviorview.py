from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

#from medialog.tablebehavior import tablebehaviorMessageFactory as _


class ITablebehaviorView(Interface):
    """
    tablebehavior view interface
    """


class TablebehaviorView(BrowserView):
    """
    tablebehavior browser view
    """
    implements(ITablebehaviorView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def javascript(self):
        return ""

    @property
    def construct_url(self):
        """returns the urls that will embed the map
          """

        return ""

