from django.test import TestCase
from documents.models import DocPage, Document
from django.core.files.uploadedfile import SimpleUploadedFile


class DocumentTestPage(TestCase):
    @classmethod
    def setUpTestData(self):

        testdoc = SimpleUploadedFile('testdocument.docx', b'',
                                     content_type='text/plain')
        self.doc = Document.objects.create(name='Document1',
                                           upload=testdoc)
        self.doc.save()
        self.dcpage = DocPage.objects.create(name='Info', slug='info',
                                             text='Created new text')
        self.dcpage.files.add(self.doc)
        self.dcpage.save()
        testdoc.close()

    def test_exact_page_exist(self):
        response = self.client.get('/documents/')
        self.assertEqual(response.status_code, 200)

    def test_docpage_exist(self):
        response = self.client.get('/documents/info/')
        self.assertEqual(response.status_code, 200)

    def test_page_template(self):
        response = self.client.get('/documents/')
        self.assertTemplateUsed(response, 'documents/docpage_list.html')

    def test_exact_page_template(self):
        response = self.client.get('/documents/info/')
        self.assertTemplateUsed(response, '/documents/docpage_detail.html/')
