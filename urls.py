from django.conf.urls import patterns, url
from lbt.views import QuizView, ResultView

urlpatterns = patterns('',
    (r'^$', QuizView.as_view()),
    (r'^result$', ResultView.as_view()),
)