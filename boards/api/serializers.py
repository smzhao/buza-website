from rest_framework import serializers

from rest_framework.serializers import(
	SerializerMethodField,
	ModelSerializer,
	HyperlinkedIdentityField)
from boards.models import Board, Question, Answer

"""a serializer converts the data into a JSON
This can then be used to pass data to our apps """


class SubjectSerializer(ModelSerializer):
	class Meta:
		model = Board
		fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
	#answer_count = SerializerMethodField()
	#answers = SerializerMethodField()
	#user = SerializerMethodField()

	class Meta:
		model = Question
		fields = '__all__'

	def get_answers(self, obj):
		if obj.answers.all():
			return obj.answers.all()
			# check if any of these answers are mine
		return None

	def get_answer_count(self, obj):
		if obj.answers.all():
			return obj.answers.count()
		return 0


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'
