"""
Server side rendering of data, ordering and other actions
for the datatable.net JQuery plugin using django rest framework
"""
from rest_framework import generics, pagination
from rest_framework.response import Response

class CustomPagination(pagination.LimitOffsetPagination):
    """returns the data with the proper structure for the datatable plugin"""
    default_limit = 10
    limit_query_param = "length"
    offset_query_param = "start"
    max_limit = 100
    draw = 0
    records_total = 0

    def paginate_queryset(self, queryset, request, view=None):
        """need to provide the "draw" param from the request back in the response"""
        self.draw = request.query_params.get('draw') if not None else 0
        self.records_total = queryset.count()
        return super().paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return Response({
            'draw': self.draw,
            'data': data,
            'recordsTotal': self.records_total,
            'recordsFiltered': self.records_total
        })

class DataTableView(generics.ListAPIView):
    """class that needs to be implemented by the user"""
    model = None
    fields = [] #fields that the will show up in the json response
    pagination_class = CustomPagination
    serializer_class = None #User should provide the serializer class to be used

    def get_queryset(self):
        """User should provide the model"""
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
        return self.model.objects.all()

    def get_serializer_class(self):
        """User should provide the serializer for the model"""
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.serializer_class