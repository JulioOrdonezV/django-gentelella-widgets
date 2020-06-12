"""
Server side rendering of data, ordering and other actions
for the datatable.net JQuery plugin using django rest framework
"""
from rest_framework import generics

class DataTableView(generics.ListAPIView):
    """class that needs to be implemented by the user"""
    model = None
    fields = [] #fields that the will show up in the json response
    pagination_class = None
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