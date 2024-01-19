from django.urls import path
from .views import raw_sql_type1, raw_sql_type2

urlpatterns = [
    path('m1/', raw_sql_type1),
    path('m2/', raw_sql_type2),
]
