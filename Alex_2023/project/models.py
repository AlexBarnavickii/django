from django.db import models
from django.utils import timezone

tz = timezone.get_default_timezone()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='image/')
    class Meta():
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
class Comment(models.Model):
    author = models.CharField("имя автора", max_length=50)
    body = models.TextField("текст коментария")
    cteated_on = models.DateTimeField("дата публикации")
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    class Meta():
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'