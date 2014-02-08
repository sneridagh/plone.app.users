import copy
import logging
import transaction
from Products.CMFCore.utils import getToolByName

import plone.app.users.schemaeditor as ttw

logger = logging.getLogger('plone.app.users.setuphandlers')

FILE = 'userschema.xml'

def import_schema(context):
    """Import TTW Schema """
    data = context.readDataFile(FILE)
    if data is None:
        return
    model = ttw.load_ttw_schema(data)
    smodel = ttw.serialize_ttw_schema(model)
    ttw.set_schema(smodel)
    logger.info('Imported schema')


def export_schema(context):
    """Export TTW schema
    """
    portal = context.getSite()
    schema = ttw.serialize_ttw_schema()
    logger.info('Exported schema')
    context.writeDataFile(FILE, schema, 'text/xml')
