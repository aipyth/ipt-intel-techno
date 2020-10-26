from django.views.generic import DetailView
from .models import Competitor


class CompetitorDetail(DetailView):
    model = Competitor
    template_name = 'accounts/competitor_detail.html'
    context_object_name = 'competitor'
