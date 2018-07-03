# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
from project.boards.views import home
from project.boards.models import Board, Question, Answer
from project.accounts.models import Profile
# Adding tests for al models.


class TestProfile(TestCase):
	"""test if users can add will be able to make their own profiles"""

	def setUp(self):
		user = get_user_model().objects.create_superuser(
			username="username", email="email@buza.com", password="password")
		self.client.login(username=user.username, password=user.password)

