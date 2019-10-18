from django.urls import path, include
from. import views



app_name = 'users'

urlpatterns = [
    path('register', views.register, name="register"),
    path('logout', views.logout_request, name="logout"),
    path('login', views.login_request, name="login"),
    # path('', views.UserListView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate_account, name='activate'),

]