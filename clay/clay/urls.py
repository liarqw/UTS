from django.contrib import admin
from django.urls import path
from hexom import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.hexom,name='hexom'),
]
