from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор")
    group = models.ForeignKey(
        "Group",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Группа")


class Group(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название")
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name="Идентификатор")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title
