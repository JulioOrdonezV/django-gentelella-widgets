from django.conf.urls import url
from django.urls import path, include

from demoapp.cruds import Personclass, Countryclass, MenuItemclass
from demoapp.views import (
    create_notification_view,
    color_widget_view,
    knobView,
    MyTableView,
    my_table_view_template
)

pclss = Personclass()
countryclss = Countryclass()
menuclss = MenuItemclass()

urlpatterns = [
    path('create/notification', create_notification_view),
    url(r'^markitup/', include('markitup.urls')),
    path('knobwidget/testform', knobView, name="knobwidgets"),
    path('colorwidgets', color_widget_view, name="colorwidgets"),
    path('datatable/data', MyTableView.as_view(), name="table_data"),
    path('datatable/person_model_table', my_table_view_template, name="person_table")
] + pclss.get_urls() + countryclss.get_urls() + menuclss.get_urls()
