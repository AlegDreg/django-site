from . import api
from django.urls import path


urlpatterns = [
    path('titles', api.TitleView.as_view()),
    path('getvol', api.TomView.as_view()),
    path('info', api.TitleDetailsView.as_view()),
    path('chapter', api.ChapterView.as_view()),
    path('like',api.LikeView.as_view())
]