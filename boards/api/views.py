from rest_framework import generics

from boards.models import (
	Question, Board, Answer, AnswerComment, QuestionComment)
from .serializers import (
	QuestionSerializer,
 	SubjectSerializer, AnswerSerializer)


class QuestionView(generics.RetrieveUpdateDestroyAPIView):

	"""this is the view that will be used to render, edit and delte questions"""

	pass
	lookup_field = 'pk'  # this is what identifies the question
	serializer_class = QuestionSerializer  # JSON conversion

	def get_queryset(self):
		return Question.objects.all()
