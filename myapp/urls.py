from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('products',Products)

urlpatterns = [
    path('books/',BookListCreateAPIView.as_view()),
    path('book/<id>',book),
    path('authors/',AuthorListCreateView.as_view()),
    path('cars/',Cars.as_view()),
    path('cars/<int:id>',CarsById.as_view()),
    path('rout',include(router.urls))
]
