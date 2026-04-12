from django.urls import path
from .views import article_detail, article_list

urlpatterns = [
    path("", article_list, name="article_list"), # Article List view
    path("<slug:slug>/", article_detail, name="article_detail"), # Article Detail view
]
