from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogPostPage, ContactView
from ckeditor_uploader import views as ckeditor_views


urlpatterns = [

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditorupload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditorbrowse/', ckeditor_views.browse, name='ckeditor_browse'),
    path('__debug__/', include('debug_toolbar.urls')),

    # My URLs.
    path("", views.home, name="blog-home"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('<str:title>/', BlogPostPage.as_view(), name='Post_Page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
