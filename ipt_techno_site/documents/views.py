from django.views import generic

from .models import DocPage


class DocPageDetail(generic.DetailView):
    model = DocPage
    template_name = 'documents/docpage_detail.html'