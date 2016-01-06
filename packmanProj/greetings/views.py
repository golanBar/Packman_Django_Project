from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    """
    i only want to present a home page with a greeting to the players.
    i will use a simple CBV. It's a generic view which has all the required functionality - the TemplateView.
    """
    template_name = 'greetings/home.html'