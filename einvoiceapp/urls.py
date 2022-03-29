from django.urls import path
from .views import IndexView, QRCodeFormView, SuccessView

urlpatterns = [
    path('', QRCodeFormView.as_view(), name='index'),
    path('success/', SuccessView.as_view(), name='success'),

]
