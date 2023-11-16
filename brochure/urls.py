from django.urls import path
from django.views.generic.base import TemplateView
from .import views

urlpatterns = [
    path('', views.index),
    path('upload', views.upload_pdf),
    path('update', views.update_pdf),
    path('delete', views.delete_pdf),
    path('<str:subLink>', views.result),

    path(r'^brochurepage/', TemplateView.as_view(template_name="brochure.html"),
                   name='page_brochure'),
    path(r'^404page/', TemplateView.as_view(template_name="404.html"),
                   name='page_404'),

]