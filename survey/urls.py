from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question$', views.question, name='question'),
    url(r'^create$', views.create, name='create'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^(?P<question_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<question_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^all_questions$', views.all_questions, name='all_questions'),
    url(r'^form$', views.survey, name='survey'),
]