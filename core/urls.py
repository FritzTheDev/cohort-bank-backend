from django.contrib import admin
from django.urls import path, include
from .views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('branches.urls')),
    path('login/', LoginView.as_view()),
    path('auth/', include('knox.urls'))
]
