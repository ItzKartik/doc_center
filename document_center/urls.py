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
    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    # url('', views.update_database, name="update_database"),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

