from django.forms import ModelForm
from cms.models import Book, Impression


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'magazine_name', 'author_name', 'score', 'comment', 'date',
                  'read_flg', )


class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )