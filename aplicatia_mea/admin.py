from django.contrib import admin
# from .models import Locatie
from .models import Parfum, Furnizor, Stoc, Categorie, CompozitiaParfumului, VanzariZilnice, CustomUser



   

class FurnizorAdmin(admin.ModelAdmin):
    search_fields = ('nume_brand', 'este_premium') 
    fieldsets = (
        ('Informatii Obligatorii', {
            'fields': ('nume_brand', 'tara')
        }),
        ('Optiuni Suplimentare', {
            'classes': ('collapse',),
            'description': 'Campuri optionale pentru furnizor',
            'fields': ('este_premium', 'telefon'),
        }),
    )   
    
class ParfumAdmin(admin.ModelAdmin):
    list_display = ('nume_parfum', 'pret', 'gen_parfum', 'volum')
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
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nume', 'blocat', 'is_staff')
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.groups.filter(name='Moderatori').exists() and not request.user.is_superuser:
            return ['nume', 'first_name', 'last_name', 'email', 'blocat']
        return fields

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Moderatori').exists() and not request.user.is_superuser:
            all_fields = [f.name for f in self.model._meta.fields]
            allowed = ['nume', 'first_name', 'last_name', 'email', 'blocat']
            return [f for f in all_fields if f not in allowed]
        return super().get_readonly_fields(request, obj)

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
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.site_header = "Panou de Administrare Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Bine ai venit in panoul de administrare"