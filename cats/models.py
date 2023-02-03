from django.db import models

class Cat (models.Model):
    name = models.CharField('nome', max_length=50)
    age = models.IntegerField('idade', default=0)
    description = models.CharField('descrição', max_length=255)
    image = models.ImageField('foto', upload_to='images/')

    class Meta:
        db_table = "cats"