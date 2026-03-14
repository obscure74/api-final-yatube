from rest_framework.pagination import LimitOffsetPagination


class MaybeLimitOffsetPagination(LimitOffsetPagination):
    """
    Пагинация, которая работает только при наличии параметров limit или offset.
    В остальных случаях возвращает обычный список.
    """

    def paginate_queryset(self, queryset, request, view=None):
        if (not request.query_params.get('limit')
                and not request.query_params.get('offset')):
            return None
        return super().paginate_queryset(queryset, request, view)
