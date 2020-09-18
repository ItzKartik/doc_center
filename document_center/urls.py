from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from doc_center_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('getin/', views.getin, name="getin"),
    path('logout/', views.logout_view, name="signout"),
    path('req/', TemplateView.as_view(template_name="req.html"), name="req"),
    path('upload_docs/', views.upload_docs, name="upload_docs"),
    path('home/', TemplateView.as_view(template_name="homepages/home.html"), name="home"),
    path('docs/', views.docs, name="docs"),
    path('doc_view/<str:pk>', views.doc_view, name="doc_view"),
    path('activity/', TemplateView.as_view(template_name="homepages/activity.html"), name="activity"),
    path('membership/', views.membership, name="membership"),
    path('bids/', TemplateView.as_view(template_name="homepages/bids.html"), name="bids"),
    # url('', views.update_database, name="update_database"),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

