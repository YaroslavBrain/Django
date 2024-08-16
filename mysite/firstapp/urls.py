from django.urls import path,  register_converter
from . import views, converters

register_converter(converters.FourDigitConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cat/', views.categories, name='cats'),
    path('cat/<int:cat_id>/', views.categories_certain, name='cats_id'),
    path('cat/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    path("archive/<year4:year>/", views.archive, name='archive'),

]
