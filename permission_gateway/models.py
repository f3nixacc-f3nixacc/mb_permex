from django.db import models


class Platform(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	url = models.URLField()

	def __str__(self):
		return self.name


class PlatformApplication(models.Model):
	platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class PlatformPermission(models.Model):
	platform_application = models.ForeignKey(PlatformApplication, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	permission = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class UserPlatformPermission(models.Model):
	user = models.ForeignKey('uac.Profile', on_delete=models.CASCADE)
	platform_permission = models.ForeignKey(PlatformPermission, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)