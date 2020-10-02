from django.test import TestCase
from documents.models import DocPage, Document

class DocumentTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.doc = Document.objects.create(name = 'Document1')
        self.doc.save()
        self.dcpage = DocPage.objects.create(name = 'DocPage 1', text = 'Created new text')
        self.dcpage.save()
    def test_doc_created_properly(self):
        self.assertEqual('Document1',self.doc.__str__())
        #self.assertFalse()
        #TODO: check if the uploaded string is empty