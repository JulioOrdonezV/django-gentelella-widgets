from django.conf.urls import url
from django.urls import path, include

from demoapp.cruds import Personclass, Countryclass, MenuItemclass
from demoapp.views import (
    create_notification_view,
    color_widget_view,
    knobView,
    MyTableView
)

pclss = Personclass()
countryclss = Countryclass()
menuclss = MenuItemclass()

urlpatterns = [
    path('create/notification', create_notification_view),
    url(r'^markitup/', include('markitup.urls')),
    path('knobwidget/testform', knobView, name="knobwidgets"),
    path('colorwidgets', color_widget_view, name="colorwidgets"),
    path('datatable/person_model_data', MyTableView, name="table_data"),
] + pclss.get_urls() + countryclss.get_urls() + menuclss.get_urls()
