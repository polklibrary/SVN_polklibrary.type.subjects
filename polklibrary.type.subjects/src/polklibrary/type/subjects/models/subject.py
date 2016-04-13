from plone import api
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class ISubject(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )
        
    body = RichText(
            title=u"Body",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
        
        

        
        