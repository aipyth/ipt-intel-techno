from django.test import TestCase
from documents.models import DocPage, Document
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentTest(TestCase):
    @classmethod
    def setUpTestData(self):

        testdoc = SimpleUploadedFile('testdocument.docx',b'',content_type='text/plain')
        self.doc = Document.objects.create(name = 'Document1', upload = testdoc)
        self.doc.save()
        self.dcpage = DocPage.objects.create(name = 'Info',slug = 'info', text = 'Created new text')
        self.dcpage.files.add(self.doc)
        self.dcpage.save()
        testdoc.close()
    def test_doc_created_properly(self):
        self.assertEqual('Document1',self.doc.__str__())
        self.assertIsInstance(self.doc, Document)

    def test_dcpage_created_properly(self):
        self.assertEqual('Info',self.dcpage.name)
        self.assertEqual('Created new text', self.dcpage.text)