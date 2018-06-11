from rest_framework import generics

from boards.models import (
	Question, Board, Answer, AnswerComment, QuestionComment)
from .serializers import (
	QuestionSerializer,
 	SubjectSerializer, AnswerSerializer)


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
	"""this is the view that will be used to create and view questions"""

	lookup_field = 'pk'  # this is what identifies the question
	serializer_class = QuestionSerializer  # JSON conversion

	def get_queryset(self):
		return Question.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class AskQuestionView(generics.CreateAPIView):
	"""this is the view that will be used to render, edit and delete questions"""

	lookup_field = 'pk'  # this is what identifies the question
	serializer_class = QuestionSerializer  # JSON conversion

	def get_queryset(self):
		return Question.objects.all()
