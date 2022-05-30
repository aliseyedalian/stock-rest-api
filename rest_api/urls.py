from django.urls import path,include
from . import views
from rest_framework import routers # GET and POST Request


router = routers.DefaultRouter()
router.register('symbols',views.SymbolView)

urlpatterns = [
    path('',include(router.urls))
]
