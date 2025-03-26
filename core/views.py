from django.shortcuts import render
from django.views import View

# Create your views here.


class Spotlight(View):
    def __init__(self):
        self.list_of_url = ["anime", "admin", "config"]

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = self.loading_page(request)
        elif request.method == "OPTIONS":
            self.http_method_names = ["get", "options"]
            response = self.options()
        return response

    def loading_page(self, request):
        return render(
            request, "html/spotlight_landing.html", {"list_of_urls": self.list_of_url}
        )
