from django.db.models import F
from . import models

def SendView(chapter_id):
    try:
        chapter = models.Chapter.objects.filter(id = chapter_id)[0]
        chapter.views = F('views') + 1
        chapter.save()
    except Exception as e:
        pass

def SendLike(chapter_id):
    try:
        chapter = models.Chapter.objects.filter(id = chapter_id)[0]
        chapter.likes = F('likes') + 1
        chapter.save()
    except Exception as e:
        pass