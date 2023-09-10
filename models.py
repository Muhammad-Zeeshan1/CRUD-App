from django.db import models

class Projects (models.Model):
    project_title = models.CharField(max_length=50)

    def __str__(self):
        return self.project_title

class Students (models.Model):
    std_name = models.CharField(max_length=50)
    std_name2 = models.CharField(max_length=50, default='')
    std_roll = models.CharField(max_length=50)
    std_contact = models.CharField(max_length=50)
    std_address = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.std_name

# Create your models here.
