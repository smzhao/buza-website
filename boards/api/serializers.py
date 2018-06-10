from rest_framework import serializers

from rest_framework.serializers import(
	SerializerMethodField,
	ModelSerializer,
	HyperlinkedIdentityField)
from boards.models import Board, Question, Answer
from drf_extra_fields.fields import Base64ImageField
from accounts.models import Profile

"""a serializer converts the data into a JSON
This can then be used to pass data to our apps """


class SubjectSerializer(ModelSerializer):
	class Meta:
		model = Board
		fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
	# answer_count = SerializerMethodField()
	# answers = SerializerMethodField()
	# user = SerializerMethodField('user')
	read_only_fields = ['pk', 'user', 'created_at']
	media = Base64ImageField(max_length=None, use_url=True, required=False)

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

	def validate_question(self, value):
		qs = Question.objects.filter(title__iexact=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError("this question has already been asked")
		return value


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'
