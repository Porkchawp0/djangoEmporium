from django.db import models

# Create your models here.
class completeProject(models.Model):
    projectName = models.CharField()
    projectDescription = models.TextField()
    projectDate = models.DateTimeField(auto_now_add=True)
    projectMedia = models.ImageField()

    def __str__(self):
        return self.projectName