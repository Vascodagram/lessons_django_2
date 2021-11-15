from django.urls import path, include, re_path
from .views import index_test, render_test, redirect_test, page_one
urlpatterns = [
    re_path(r'^$', index_test),
    re_path(r'^render_test/$', render_test),
    re_path(r'^redirect_test/$', redirect_test),
    re_path(r'^redirect_test/page_one/$', page_one)
]
