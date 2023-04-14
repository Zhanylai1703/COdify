from django.urls import path, include

from apps.form.views import FormCreateView, FormHistoryListAPIView


urlpatterns = [
    path('', FormCreateView.as_view(), name='create_form'),
    path('formhistory/', FormHistoryListAPIView.as_view(), name='create_form'),
]