from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"),
    path("despre/", views.despre, name="despre"),
    path("produse/", views.produse, name="produse"),
    path("contact/", views.contact, name="contact"),
    path("cos_virtual/", views.cos_virtual, name="cos_virtual"),
    path("ghid_arome/", views.ghid_arome, name="ghid_arome"),
    path("pachete_cadou/", views.pachete_cadou, name="pachete_cadou"),
    path("info/",views.info, name="info"),
    path("log/", views.log_view, name="log_view"),
    path('produs/<int:id_produs>/', views.detalii_produs, name='detalii_produs'),
    path('categorii/<str:nume_cat>/', views.pagina_categorie, name='pagina_categorie'),
    path('confirma_resetarea/', views.confirma_resetarea, name='confirma_resetarea'),
    path('adauga_parfum/', views.adauga_parfum, name='adauga_parfum'),
]