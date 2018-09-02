from django.db import models
import datetime
import django.utils.timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    """書籍"""
    READ_STATUS = (
        (0, '未読'),
        (1, '既読'),
    )
    name = models.CharField('書籍名', max_length=255)
    magazine_name = models.CharField('掲載誌名', max_length=255, blank=True)
    author_name = models.CharField('作者名', max_length=255, blank=True)
    score = models.IntegerField('スコア',
                                validators=[MinValueValidator(0), MaxValueValidator(100)],
                                default=0)
    comment = models.CharField('コメント', max_length=255, blank=True)
    date = models.DateField('日付', default=datetime.date.today())
    read_flg = models.IntegerField('既読フラグ', choices=READ_STATUS, default=0)
    created_at = models.DateTimeField('登録日', default=django.utils.timezone.now)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment