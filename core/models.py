from django.db import models
import json

class Question(models.Model):
    description = models.CharField('Descrição', max_length=600)
    options = models.CharField('Alternativas', max_length=200)

    def set_options(self, values):
        self.options = json.dumps(values)

    def get_options(self):
        return json.loads(self.options)

    def __str__(self):
            return self.description

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'