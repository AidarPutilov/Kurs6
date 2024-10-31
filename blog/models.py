from django.db import models

class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="заголовок",
        help_text='Введите заголовок статьи'
    )
    text = models.TextField(
        verbose_name="содержимое",
        null=True,
        blank=True,
        help_text='Введите текст статьи'
    )
    picture = models.ImageField(
        upload_to="pictures/",
        verbose_name="изображение",
        null=True,
        blank=True,
        help_text='Загрузите изображение'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="дата создания",
    )
    view_counter =models.PositiveIntegerField(
        verbose_name='счётчик просмотров',
        default=0
    )

    def __str__(self):
        return f"{self.title} от {self.created_at}"

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('created_at',)
