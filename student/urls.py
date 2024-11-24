from django.urls import path
from . views import StudentLoginView, LogoutView
urlpatterns = [
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('logout/', LogoutView.as_view(), name='student-logout'),
]
