
# the views for the API
from .views import QuestionView

from django.conf.urls import url


urlpatterns = [
	# url(r'^login/$', views.user_login, name='login')
	# example: http://localhost:8000/api/question/1/this-is-a-question-about-mathematics/
	url(r'^question/(?P<pk>\d+)/(?P<question_slug>[\-\w]+)/$', QuestionView.as_view(), name='question_view'),

	]