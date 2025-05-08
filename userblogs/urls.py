from django.urls import path
from .views import AddBlogView, ViewBlogView

urlpatterns = [
    path('add-blog/', AddBlogView.as_view(), name='add-blog'),
    path('view-blogs/', ViewBlogView.as_view(), name='view-blogs'),
]
