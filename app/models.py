from django.db import models
from django.contrib import admin
max_l = 30

class Title(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    description = models.TextField()
    ru_name = models.TextField(max_length=100)
    en_name = models.TextField(max_length=100)
    alt_name = models.TextField(max_length=100)

    def __str__(self):
        return self.ru_name

class Tag(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    name = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Title_tag(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    title = models.ForeignKey("Title",on_delete=models.DO_NOTHING)
    tag = models.ForeignKey("Tag",on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title.ru_name[:max_l] + " - " + self.tag.name[:max_l]

class Volume(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    title = models.ForeignKey("Title",on_delete=models.DO_NOTHING)
    name = models.TextField(max_length=200)
    price = models.IntegerField()
    title_number = models.IntegerField()
    def __str__(self):
        return self.title.ru_name[:max_l] + " - " + self.name[:max_l]

class Chapter(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    content = models.TextField()
    chapter_number = models.IntegerField()
    volume = models.ForeignKey("Volume",on_delete=models.DO_NOTHING)
    likes = models.IntegerField()
    views = models.IntegerField()
    def __str__(self):
        return str(self.chapter_number) + " ch. " + str(self.volume.title.ru_name[:max_l]) + " - " + self.volume.name[:max_l]

class Title_info(models.Model):
    class Meta:
        managed = False
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    tags = models.TextField()
    ru_name = models.TextField()
    en_name = models.TextField()
    alt_name = models.TextField()

    tag = []


class ChapterInlines(admin.TabularInline):
    model = Chapter

class VolumeAdmin(admin.ModelAdmin):
    inlines = [ChapterInlines,]

class VolumeInline(admin.TabularInline):
    model = Volume

class TitleAdmin(admin.ModelAdmin):
    inlines = [ VolumeInline, ]
    search_fields = ['ru_name', ]