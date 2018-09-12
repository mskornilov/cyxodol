from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField('Имя', max_length=60)
    email = models.EmailField('E-mail')
    message = models.TextField('Отзыв')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Отзыв от {}'.format(self.name)

    class Meta:
        ordering = ['-created']
