from django.urls import path

from .views import home_view, FormsView, PhoneFormView, BrandFormView, reports_view

urlpatterns = [
    path('', home_view, name='home_page'),
    path('form/', FormsView.as_view(), name='forms_page'),
    path('form/phone/', PhoneFormView.as_view(), name='phone_form_page'),
    path('form/brand/', BrandFormView.as_view(), name='brand_form_page'),
    path('reports/', reports_view, name='reports_page'),
]
