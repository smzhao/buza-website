from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'user',
			'photo',
			'school',
			'grade',
			'bio',
			'interests',
			'grade',
			'reputation',
			'boards')
		model = Profile