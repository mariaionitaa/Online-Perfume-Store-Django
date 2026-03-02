from django.db import models
from datetime import datetime
from urllib.parse import urlparse
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Accesare:
    _contor_id = 0

    def __init__(self, ip_client=None, url=None, data=None):
        Accesare._contor_id += 1
        self.id = Accesare._contor_id
        self.ip_client = ip_client
        self.url = url
        self.data = data or datetime.now()

    def lista_parametri(self):
        return [
            ("id", self.id),
            ("ip_client", self.ip_client),
            ("url", self.url),
            ("data", self.data),
        ]

    def url_complet(self):
        return self.url

    def data_formatata(self, format_str):
        return self.data.strftime(format_str)

    def pagina(self):
        if not self.url:
            return None
        return urlparse(self.url).path


class Furnizor(models.Model):
    id_brand = models.AutoField(primary_key=True)
    nume_brand = models.CharField(max_length=255, unique=True)
    tara = models.CharField(max_length=255)
    telefon = models.CharField(max_length=10, null=True, blank=True)
    este_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.nume_brand
    
class Categorie(models.Model):
    APA_DE_PARFUM = 'Apa de parfum'
    APA_DE_TOALETA = 'Apa de toaleta'
    ULEI_PARFUMAT = 'Ulei parfumat'
    CATEGORIE_CHOICES = [
        (APA_DE_PARFUM, 'Apa de parfum'),
        (APA_DE_TOALETA, 'Apa de toaleta'),
        (ULEI_PARFUMAT, 'Ulei parfumat'),
    ]
    
    nume_categorie = models.CharField(max_length=255, choices=CATEGORIE_CHOICES)
    descriere = models.CharField(max_length=255)
    iconita = models.CharField(max_length=50, blank=True, help_text="Ex: fa-spray-can, fa-wind")
    
    def __str__(self):
        return self.nume_categorie    

class Parfum(models.Model):
    GEN_BARBATESC = 'Barbatesc'
    GEN_DAME = 'Dame'
    GEN_UNISEX = 'Unisex'
    GEN_PARFUM_CHOICES = [
        (GEN_BARBATESC, 'Barbatesc'),
        (GEN_DAME, 'Dame'),
        (GEN_UNISEX, 'Unisex'),
    ]
    
    id_parfum = models.AutoField(primary_key=True)
    nume_parfum = models.CharField(max_length=255, unique=True, blank=True)
    descriere = models.CharField(max_length=500, null=True, blank=True)
    imagine = models.ImageField(upload_to='parfumuri/', null=True, blank=True)
    pret = models.DecimalField(max_digits=8, decimal_places=2)
    gen_parfum = models.CharField(max_length=20, choices=GEN_PARFUM_CHOICES, default=GEN_UNISEX)
    volum = models.IntegerField()
    nume_categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True, blank=True)
    
    furnizori = models.ManyToManyField(Furnizor) 

    def __str__(self):
        return f"Parfum {self.id_parfum}"
    
class CompozitiaParfumului(models.Model):
    parfum = models.ForeignKey('Parfum', on_delete=models.CASCADE, primary_key=True)
    varf = models.CharField(max_length=255, null=True)
    mijloc = models.CharField(max_length=255, null=True)
    baza = models.CharField(max_length=255, null=True)
    concentratie = models.IntegerField(null=True)
    
    def __str__(self):
        return f"Compozitia pentru {self.parfum.id_parfum}"
    
    
class Stoc(models.Model):
    id_stoc = models.AutoField(primary_key=True)
    parfum = models.ForeignKey('Parfum', on_delete=models.CASCADE)
    cantitate = models.IntegerField()
    actualizat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stoc ID: {self.id_stoc} - Parfum: {self.parfum.id_parfum}"
    
class VanzariZilnice(models.Model):
    id_vanzare = models.AutoField(primary_key=True)
    parfum = models.ForeignKey(Parfum, on_delete=models.CASCADE)
    data = models.DateField()
    cantitate = models.IntegerField()
    venit_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vanzare ID: {self.id_vanzare} la data de {self.data}"
    
    
class CustomUser(AbstractUser):
    # (username, email, password) sunt deja incluse prin AbstractUser
    
    nume = models.CharField(max_length=100, verbose_name="Nume Complet")
    telefon = models.CharField(max_length=10, verbose_name="Telefon")
    tara = models.CharField(max_length=50, verbose_name="Tara")
    oras = models.CharField(max_length=50, verbose_name="Oras")
    adresa_livrare = models.CharField(max_length=255, verbose_name="Adresa de livrare")
    data_inregistrare = models.DateTimeField(auto_now_add=True)
    
    blocat = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.username