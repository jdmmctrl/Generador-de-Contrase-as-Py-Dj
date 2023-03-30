
from django.urls import path
from generator import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('password', views.password, name='password')
]
