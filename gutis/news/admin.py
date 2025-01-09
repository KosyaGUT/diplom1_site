from django.contrib import admin
from .models import News
from ckeditor.widgets import CKEditorWidget
from django import forms

class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'

# Настройка отображения модели в админке
class NewsAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке объектов
    list_display = ('title', 'little_content', 'published_date', 'author', 'category', 'is_published', 'views')

    # Поля, которые можно редактировать прямо из списка
    list_editable = ('is_published',)

    # Поля, которые будут использоваться для фильтрации
    list_filter = ('category', 'is_published', 'published_date')

    # Поля, которые будут использоваться для поиска
    search_fields = ('title', 'content', 'author')

    # Поля, которые будут исключены из формы редактирования
    exclude = ('views',)

def get_published_news():
    # Возвращает только опубликованные новости
    return News.objects.filter(is_published=True).order_by('-published_date')

# Регистрация модели и ее настроек в админке
admin.site.register(News, NewsAdmin)
