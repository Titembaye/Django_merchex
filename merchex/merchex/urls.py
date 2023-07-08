from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add', views.band_create, name='band-create'),
    path('bands/<int:band_id>/change/', views.band_update, name='band-update'),

    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:listing_id>/',
         views.listing_detail, name='listing-detail'),
    path('listings/add', views.listing_create, name='listing-create'),
    path('listings/<int:listing_id>/change/',
         views.listing_update, name='listing-update'),

    path('about-us/', views.about, name='a-propos'),
    path('contact-us/', views.contact, name='contact'),
    path('sent-mail/', views.sent_mail, name='sent-mail')
]
