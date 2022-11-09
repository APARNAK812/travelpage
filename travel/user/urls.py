from django.urls import path
from.import views 
app_name='user'



urlpatterns=[
    path('about',views.about),
    path('home',views.home),
    path('contact',views.contact),
    path('thingstodo',views.thingstodo),
    path('membership',views.membership),
    path('packages',views.packages),
]