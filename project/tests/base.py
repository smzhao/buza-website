from django.contrib.auth import get_user_model
from project.boards.models import Board, Question, Answer


def BuzaTestMixin(object):
	"""The methods for tests used in the Buza project"""
	def login_user(self, username="user", email="user@buza.com", password="password"):
		user = get_user_model().objects.create_superuser(
			username=username, email=email, password=password)
		self.client.login(username=user.username, password=user.password)

		return user

	def ask_question(self, user):
		subject = Board.objects.create(
			title="subject",
			description="a good subject",
			creator=user)
		subject.save()
		question = Question.objects.create(
			title="question",
			body="a question",
			user=user,
			board=subject)
		question.save()
		return question

	def mk_answer(self, user, question, answer_text="first comment"):
		answer = Answer.objects.create(
			answer=answer_text, user=user, question=question)
		answer.save()
		return answer

