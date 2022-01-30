
from django.urls import path,re_path
from url_shortener_app.views import home_view, redirect_url_view
appname = "url_shortener"
urlpatterns = [
    path("create/", home_view, name="create"),
    re_path(r'^s/(?P<shortened_part>\w+)$', redirect_url_view, name='redirect'),

]