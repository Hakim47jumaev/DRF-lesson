from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('products',ProductViewSet)

urlpatterns = [
    path('books/',BookListCreateAPIView.as_view()),
    path('book/<id>',book),
    path('authors/',AuthorListCreateView.as_view()),
    path('cars/',Cars.as_view()),
    path('cars/<int:id>',CarsById.as_view()),
    path('rout',include(router.urls)),
    path('courses/',CourseListView.as_view()),
    path('courses/create/',CourseCreate.as_view()),
    path('courses/<int:pk>',CourseDelete.as_view()),
]
