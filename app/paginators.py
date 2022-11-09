from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
    page_query_param = 'page'

class PaginationChapter(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1
    page_query_param = 'page'

class PaginationWork():
    def __init__(self, request, serializer, queryset, pagination_class):
        self.request = request
        self.serializer_class = serializer
        self.pagination_class = pagination_class
        self.queryset = queryset

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def Work(self):
        queryset = self.queryset

        try:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return serializer.data
        except Exception as e:
            return None