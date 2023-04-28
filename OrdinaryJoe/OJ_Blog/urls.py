from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogPostPage, HomeView
from ckeditor_uploader import views as ckeditor_views


urlpatterns = [

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditorupload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditorbrowse/', ckeditor_views.browse, name='ckeditor_browse'),
    path("", HomeView.as_view(), name="blog-home"),
    path('<str:title>/', BlogPostPage.as_view(), name='Post_Page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
