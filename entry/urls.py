from django.urls import path
from entry import views


urlpatterns = [
path ('',views.all),
path ("article/<int:object_id>/",views.detail),
path("add/",views.add),
]