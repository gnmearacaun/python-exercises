from django.views import View
from django.urls import path

class CatView(View):
    pass


class DogView(View):
    pass


urlpatterns = (
    path("cat/", CatView.as_view()),
    path("dog/", DogView.as_view()),
)
