from django.urls import path, re_path
from .views import HomePageView,PostDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),    
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),    
]

