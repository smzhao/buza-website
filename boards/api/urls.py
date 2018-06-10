
# the views for the API
from .views import QuestionView, AskQuestionView

from django.conf.urls import url


urlpatterns = [
	# url(r'^login/$', views.user_login, name='login')
	# example: http://localhost:8000/api/question/1/this-is-a-question-about-mathematics/
	url(r'^ask-question/$', AskQuestionView.as_view(), name='ask_question'),
	url(
		r'^question/(?P<pk>\d+)/(?P<question_slug>[\-\w]+)/$',
		QuestionView.as_view(), name='question_view'),

]