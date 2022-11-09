from . import models
from . import serializers
from . import paginators
from . import answer_models
from . import celery
from . import tasks as t
import threading
from rest_framework.views import APIView
import asyncio
from django.http import JsonResponse
from threading import Thread

class TitleView(APIView):
    serializer_class = serializers.Title_serializer
    queryset = models.Title.objects.all()

    def get(self, request):
        pagination_class = paginators.PaginationWork(request, self.serializer_class, self.queryset, paginators.Pagination)
        res = pagination_class.Work()
        if res != None:
            return JsonResponse(answer_models.Alright(res.data), safe=False, encoder=answer_models.AnswerEncoder)
        else:
            return JsonResponse(answer_models.Error("Something went wrong"), safe=False, encoder=answer_models.AnswerEncoder)

class TomView(APIView):
    def get(self, request):
        if self.request.method == 'GET':
            try:
                title_id = self.request.GET['title_id'];
            except Exception as e:
                return JsonResponse(answer_models.Error("Use title_id params"), safe=False, encoder=answer_models.AnswerEncoder)

            i = int(title_id) if title_id.isdecimal() else None

            if i == None:
                return JsonResponse(answer_models.Error("Use title_id params"), safe=False, encoder=answer_models.AnswerEncoder)
            else:
                serializer_class = serializers.Volume_serializer
                queryset = models.Volume.objects.filter(title_id=i)
                pagination_class = paginators.PaginationWork(request, serializer_class, queryset, paginators.Pagination)
                res = pagination_class.Work()

                if res != None:
                    return JsonResponse(answer_models.Alright(res.data), safe=False, encoder=answer_models.AnswerEncoder)
                else:
                     return JsonResponse(answer_models.Error("Something went wrong"), safe=False, encoder=answer_models.AnswerEncoder)
        else:
            return JsonResponse(answer_models.Error("Use GET request"), safe=False, encoder=answer_models.AnswerEncoder)

class ChapterView(APIView):
    def get(self, request):
        try:
            if self.request.method == 'GET':
                try:
                    volume_id = self.request.GET['volume_id'];
                except Exception as e:
                    return JsonResponse(answer_models.Error("Use volume_id params"), safe=False, encoder=answer_models.AnswerEncoder)

                i = int(volume_id) if volume_id.isdecimal() else None

                if i == None:
                    return JsonResponse(answer_models.Error("Use volume_id params"), safe=False, encoder=answer_models.AnswerEncoder)
                else:
                    serializer_class = serializers.Chapter_serializer
                    queryset = models.Chapter.objects.filter(volume_id=i)
                    pagination_class = paginators.PaginationWork(request, serializer_class, queryset, paginators.PaginationChapter)
                    res = pagination_class.Work()

                    if res != None:
                        ch = getattr(queryset[0],'id')
                        SendView.Send(ch)
                        return JsonResponse(answer_models.Alright(res.data), safe=False, encoder=answer_models.AnswerEncoder)
                    else:
                         return JsonResponse(answer_models.Error("Something went wrongs"), safe=False, encoder=answer_models.AnswerEncoder)
            else:
                return JsonResponse(answer_models.Error("Use GET request"), safe=False, encoder=answer_models.AnswerEncoder)
        except Exception as e:
            return JsonResponse(answer_models.Error(e.args), safe=False, encoder=answer_models.AnswerEncoder)

class TitleDetailsView(APIView):

    serializer_class = serializers.Title_info_serializer

    def get(self, request):
        if self.request.method == 'GET':
            try:
                title_id = self.request.GET['id'];
            except Exception as e:
                return JsonResponse(answer_models.Error("Use ID params"), safe=False, encoder=answer_models.AnswerEncoder)

            i = int(title_id) if title_id.isdecimal() else None
            
            if i != None:
                try:
                    queryset = models.Title_info.objects.raw("select app_title.id as id, app_title.description as description, "
                    +"group_concat(DISTINCT app_tag.name) as tags, "
                    +"app_title.ru_name,app_title.en_name,app_title.alt_name from app_title "
                    +"left join app_title_tag on app_title_tag.title_id = app_title.id "
                    +"inner join app_tag on app_tag.id = app_title_tag.tag_id "
                    +"Where app_title.id = " + title_id
                    +" group by app_title.id")

                    res = queryset[0]

                    res.tag = getattr(res,'tags').split(",")

                    return JsonResponse(
                        answer_models.Alright(res, self.serializer_class), safe=False, encoder=answer_models.AnswerEncoder)
                except Exception as e:
                    return JsonResponse(answer_models.Error("Not find"), safe=False, encoder=answer_models.AnswerEncoder)
            else:
                return JsonResponse(answer_models.Error("Use ID params"), safe=False, encoder=answer_models.AnswerEncoder)
        else:
            return JsonResponse(answer_models.Error("Only get request"), safe=False, encoder=answer_models.AnswerEncoder)

class LikeView(APIView):
    def get(self, request):
        if self.request.method == 'GET':
            try:
                chapter_id = self.request.GET['chapter_id'];
            except Exception as e:
                return JsonResponse(answer_models.Error("Use chapter_id params"), 
                                    safe=False, encoder=answer_models.AnswerEncoder)

            i = int(chapter_id) if chapter_id.isdecimal() else None

            if i == None:
                return JsonResponse(answer_models.Error("Use chapter_id params"), safe=False, encoder=answer_models.AnswerEncoder)
            else:
                SendLike.Send(i);
                return JsonResponse(
                        answer_models.Alright("SUCCESS"), 
                        safe=False, encoder=answer_models.AnswerEncoder)
        else:
            return JsonResponse(answer_models.Error("Use GET request"), safe=False, encoder=answer_models.AnswerEncoder)


class SendView:
    def Send(chapter_id):
        try:
            thread1 = Thread(target=t.SendView, args=(chapter_id,))
            thread1.start()
            #thread1.join()
        except Exception as e:
            pass

class SendLike:
    def Send(chapter_id):
        try:
            thread1 = Thread(target=t.SendLike, args=(chapter_id,))
            thread1.start()
            #thread1.join()
        except Exception as e:
            pass
