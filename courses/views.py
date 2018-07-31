from django.shortcuts import render
from django.views import View


class CourseView(View):
    template_name = "about.html"
    # GET method
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {})

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})