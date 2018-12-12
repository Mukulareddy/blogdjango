from django.db import models
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return "/category/{}".format(self.id)
class Entry(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
	title = models.CharField(max_length = 100)
	text = models.TextField()

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return "/article/{}".format(self.id)
