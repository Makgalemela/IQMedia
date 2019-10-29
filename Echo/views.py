from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'Echo/maps.html'
class LocationView(TemplateView):
    template_name = 'Echo/home.html'