from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

class QuizView(TemplateView):
    template_name = "lbt/index.html"

class ResultView(TemplateView):
    template_name = "lbt/result.html"

    def post(self, request):
        if 'eggs' in request.POST:
            context = {}
            if request.POST['eggs'] == 'three':
                context['result'] = 'ozzy'
            else:
                context['result'] = 'strut'
            return self.render_to_response(context)
        return redirect('/lbt/')