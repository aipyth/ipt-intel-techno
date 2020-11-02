from django.views import generic

from .models import DocPage


class DocPageDetail(generic.DetailView):
    model = DocPage
    template_name = 'documents/docpage_detail.html'


class DocPageList(generic.ListView):
    model = DocPage
    template_name = 'documents/docpage_list.html'
    paginate_by = 20
