from django.contrib import admin
# from .models import Locatie
from .models import Parfum, Furnizor, Stoc, Categorie, CompozitiaParfumului, VanzariZilnice


# class CategorieInline(admin.TabularInline):
#     model = Categorie
#     extra = 1

   

class FurnizorAdmin(admin.ModelAdmin):
    search_fields = ('nume_brand', 'este_premium') 
    fieldsets = (
        ('Informatii Obligatorii', {
            'fields': ('nume_brand', 'este_premium')
        }),
        ('Opțiuni Suplimentare', {
            'classes': ('collapse',),
            'description': 'Campuri optionale pentru furnizor',
            'fields': ('tara', 'telefon'),
        }),
    )   
    
class ParfumAdmin(admin.ModelAdmin):
#     inlines = [CategorieInline]
    list_display = ('pret', 'gen_parfum', 'volum')
    search_fields = ('pret', 'gen_parfum')
    ordering= ('pret', '-volum')
    list_filter = ('pret', 'gen_parfum')
    list_per_page = 5
     
class StocAdmin(admin.ModelAdmin):
    search_fields = ('parfum', 'cantitate')

class CategorieAdmin(admin.ModelAdmin):
    search_fields = ('nume_categorie', 'descriere')
    
class CompozitiaParfumuluiAdmin(admin.ModelAdmin):
    search_fields = ('varf', 'concentratie')
    
class VanzariZilniceAdmin(admin.ModelAdmin):
    search_fields = ('data', 'cantitate')

# # admin.site.register(Locatie)


# # Register your models here.

# class LocatieAdmin(admin.ModelAdmin):
#     list_display = ('oras', 'judet')  # afișează câmpurile în lista de obiecte
#     list_filter = ('oras', 'judet')  # adaugă filtre laterale
#     search_fields = ('oras', )  # permite căutarea după anumite câmpuri
#     fieldsets = (
#         ('Date Generale', {
#             'fields': ('oras', 'judet')
#         }),
#         ('Date Specifice', {
#             'fields': ('adresa', 'cod postal'),
#             'classes': ('collapse',),  # secțiune pliabilă
#         }),
#     )


admin.site.register(Parfum, ParfumAdmin)
admin.site.register(Furnizor, FurnizorAdmin)
admin.site.register(Stoc, StocAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(CompozitiaParfumului, CompozitiaParfumuluiAdmin)
admin.site.register(VanzariZilnice, VanzariZilniceAdmin)


admin.site.site_header = "Panou de Administrare Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Bine ai venit in panoul de administrare"