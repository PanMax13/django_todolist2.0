from django.db import models

# Create your models here.

from django.db import models
# Create your models here.


class Tables(models.Model):
    category = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=400)

    class Meta:
        db_table = "Tables"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class Tasks(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name="Заголовок")
    discription = models.CharField(max_length=1000, null=False, verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    category = models.ForeignKey(to=Tables, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = "Tasks"
        verbose_name = "Задачу"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
