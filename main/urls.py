from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # Home page
    path('about/', views.about, name='about'),            # About Us page
    # path('gallery/', views.gallery, name='gallery'),   # Removed gallery
    path('courses/', views.courses, name='courses'),      # Courses list page
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),  # Course detail page
    path('contact/', views.contact, name='contact'),      # Contact page
    # You can optionally add a Facebook page link in navbar, no view required
]
