from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='games/')

    def __str__(self):
        return self.name

class Highlight(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='highlights/')
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class UpcomingSchedule(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upcoming/')

    def __str__(self):
        return self.name

class RecentGame(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upcoming/')

    def __str__(self):
        return self.name