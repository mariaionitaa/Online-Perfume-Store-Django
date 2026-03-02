# Create your views here.

import json
import os
import time
from django.http import HttpResponse 
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Accesare, Parfum, Categorie
from collections import Counter
from .middleware import accesari_globale
from django.core.paginator import Paginator
from .forms import ParfumFilterForm, ContactForm, ParfumForm, CustomUserCreationForm
from django import forms
from django.conf import settings
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm
import logging
from django.conf import settings
from django.core.exceptions import PermissionDenied



logger = logging.getLogger('django')


def get_ip(request):
    req_headers = request.META
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR')
       

def log_view(request):
    n_cerut_str = request.GET.get('ultimele')
    eroare_critica = None       # pt erori cu ex: numere negative
    eroare_informativa = None   # pt n > k
    accesari_de_afisat = accesari_globale
    k = len(accesari_globale)
    tip_vizualizare = request.GET.get("accesari")
         
    dubluri_permise = request.GET.get("dubluri", "false").lower() == "true"
    iduri_raw = request.GET.getlist("iduri")
    
    id_uri_procesate = []
    for intrare in iduri_raw:
        parti = intrare.split(",")
        for p in parti:
            val = int(p.strip())
            if dubluri_permise or (val not in id_uri_procesate):
                id_uri_procesate.append(val)
    
    if id_uri_procesate:
        dict_accesari = {acc.id: acc for acc in accesari_globale}
        accesari_de_afisat = [dict_accesari[i] for i in id_uri_procesate if i in dict_accesari]
    else:
        n_cerut_str = request.GET.get('ultimele')
        if n_cerut_str:
            try:
                n = int(n_cerut_str)
                if n < 0:
                    eroare_critica = "Parametrul 'ultimele' trebuie sa fie un numar intreg pozitiv!"
                    return render(request, "aplicatia_mea/log.html", {
                        "mesaj_eroare_critica": eroare_critica,
                        "accesari": []
                    }, status=400)
            
                if n > k:
                    eroare_informativa = f"Exista doar {k} accesari fata de {n} accesari cerute."
                    accesari_de_afisat = accesari_globale
                else:
                    accesari_de_afisat = accesari_globale[-n:]
                
            except ValueError:
                eroare_critica = "Parametrul 'ultimele' trebuie sa fie un numar intreg!"
                return render(request, "aplicatia_mea/log.html", {
                    "mesaj_eroare_critica": eroare_critica
                }, status=400)
        
    param_tabel = request.GET.get("tabel")
    coloane_de_afisat = []

    if param_tabel == "tot":
        coloane_de_afisat = ["id", "ip_client", "url", "pagina", "data"]
    elif param_tabel:
        coloane_de_afisat = [s.strip() for s in param_tabel.split(",")]
    else:
        coloane_de_afisat = ["id", "ip_client", "url", "pagina", "data"]

    toate_paginile = [acc.pagina() for acc in accesari_globale]
    
    pagina_max = None
    pagina_min = None

    if toate_paginile:
        numaratoare = Counter(toate_paginile)
        
        pagina_max = max(numaratoare, key=numaratoare.get)
        pagina_min = min(numaratoare, key=numaratoare.get)

    return render(request, "aplicatia_mea/log.html", {
        "accesari": accesari_de_afisat,
        "coloane": coloane_de_afisat,
        "mesaj_eroare": eroare_informativa,
        "k": k,
        "dubluri": dubluri_permise,
        "tip_vizualizare": tip_vizualizare,
        "pagina_max": pagina_max,
        "pagina_min": pagina_min
    })
    

def index (request):
    return render(request, "aplicatia_mea/index.html")

def despre(request):
    return render(request, "aplicatia_mea/despre.html")

def produse(request):
    form = ParfumFilterForm(request.GET)
    
    sort_param = request.GET.get('sort')
    if sort_param == 'a':
        criteriu = 'pret'
    elif sort_param == 'd':
        criteriu = '-pret'
    else:
        criteriu = 'id_parfum'
    
    parfumuri = Parfum.objects.all().order_by(criteriu) 
    
    per_page = request.GET.get('elemente_pe_pagina', '5')
    if not per_page.isdigit(): per_page = '5'
    
    show_repro_message = False
    old_per_page = request.session.get('old_per_page')
    
    if request.GET.get('page') and old_per_page and old_per_page != per_page:
        show_repro_message = True
    
    request.session['old_per_page'] = per_page
    
    if form.is_valid():
        if form.cleaned_data['nume']:
            parfumuri = parfumuri.filter(nume_parfum__icontains=form.cleaned_data['nume'])
        if form.cleaned_data['pret_min']:
            parfumuri = parfumuri.filter(pret__gte=form.cleaned_data['pret_min'])
        if form.cleaned_data['pret_max']:
            parfumuri = parfumuri.filter(pret__lte=form.cleaned_data['pret_max'])
        if form.cleaned_data['gen']:
            parfumuri = parfumuri.filter(gen_parfum=form.cleaned_data['gen'])
        if form.cleaned_data['volum']:
            parfumuri = parfumuri.filter(volum=form.cleaned_data['volum'])
        categorie_selectata = form.cleaned_data.get('categorie')
        if categorie_selectata:
            parfumuri = parfumuri.filter(nume_categorie=categorie_selectata)
    
    paginator = Paginator(parfumuri, int(per_page))
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.get_page(1)
    
    return render(request, "aplicatia_mea/produse.html", {
        "parfumuri": page_obj,
        "show_repro_message": show_repro_message,
        "form": form,
        "current_sort": sort_param,
        "toate_categoriile": Categorie.objects.all()
    })
    
def detalii_produs(request, id_produs):
    try:
        parfum = Parfum.objects.get(pk=id_produs)
        return render(request, "aplicatia_mea/detalii_produs.html", {"parfum": parfum})
    except Parfum.DoesNotExist:
        return render(request, "aplicatia_mea/404.html", status=404)

def pagina_categorie(request, nume_cat):
    
    categorie_obiect = get_object_or_404(Categorie, nume_categorie=nume_cat)
    
    data = request.GET.copy()
    if 'categorie' not in data:
        data['categorie'] = categorie_obiect.id
    
    form = ParfumFilterForm(data)
    if 'categorie' in form.fields:
        form.fields['categorie'].widget = forms.HiddenInput()
        form.fields['categorie'].widget.attrs['readonly'] = True
    
    produse_lista = Parfum.objects.filter(nume_categorie=categorie_obiect).order_by('id_parfum')
    
    if form.is_valid():
        id_primit = form.cleaned_data.get('categorie')
        
        if id_primit and id_primit.id != categorie_obiect.id:
            form.add_error('categorie', f" Categoria '{id_primit.nume_categorie}' nu corespunde cu pagina curenta.")
            produse_lista = Parfum.objects.none()
        else:
            if form.cleaned_data['nume']:
                produse_lista = produse_lista.filter(nume_parfum__icontains=form.cleaned_data['nume'])
            if form.cleaned_data['pret_min']:
                produse_lista = produse_lista.filter(pret__gte=form.cleaned_data['pret_min'])
            if form.cleaned_data['pret_max']:
                produse_lista = produse_lista.filter(pret__lte=form.cleaned_data['pret_max'])
            if form.cleaned_data['gen']:
                produse_lista = produse_lista.filter(gen_parfum=form.cleaned_data['gen'])
            if form.cleaned_data['volum']:
                produse_lista = produse_lista.filter(volum=form.cleaned_data['volum'])
        
    per_page = request.GET.get('elemente_pe_pagina', '5')
    paginator = Paginator(produse_lista.order_by('id_parfum'), int(per_page))
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, "aplicatia_mea/produse.html", {
        "parfumuri": page_obj,
        "form": form,
        "categorie_curenta": categorie_obiect,
        "este_pagina_categorie": True,
        "toate_categoriile": Categorie.objects.all() 
    })

def confirma_resetarea(request):
    referer = request.META.get('HTTP_REFERER', '/aplicatia_mea/produse/')
    
    if request.method == "POST":
        return redirect('produse') 

    return render(request, "aplicatia_mea/confirma_resetarea.html", {'referer': referer})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            date_formular = form.cleaned_data
            
            cale_folder = os.path.join(settings.BASE_DIR, 'mesaje')
            ip_utilizator = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            acum = datetime.now()
            timestamp_unix = int(time.time())
            
            sufix_urgent = "_urgent" if date_formular.get('urgent') else ""
            nume_fisier = f"mesaj_{timestamp_unix}{sufix_urgent}.json"
            cale_completa = os.path.join(cale_folder, nume_fisier)
            
            date_de_salvat = {
                'nume': date_formular.get('nume'),
                'prenume': date_formular.get('prenume'),
                'cnp': date_formular.get('cnp'),
                'varsta_la_momentul_mesajului': date_formular.get('varsta_procesata'),
                'email': date_formular.get('email'),
                'tip_mesaj': date_formular.get('tip_mesaj'),
                'subiect': date_formular.get('subiect'),
                'minim_zile_asteptare': date_formular.get('zile_asteptare'),
                'mesaj': date_formular.get('mesaj'),
                'urgent': date_formular.get('urgent'),
                
                'ip_utilizator': ip_utilizator,
                'data_sosire': acum.strftime("%d-%m-%Y"),
                'ora_sosire': acum.strftime("%H:%M:%S")
            }

            with open(cale_completa, 'w', encoding='utf-8') as f:
                json.dump(date_de_salvat, f, indent=4, ensure_ascii=False)

            return render(request, 'aplicatia_mea/contact_succes.html', {
                'nume_fisier': nume_fisier,
                'date_de_salvat': date_de_salvat
                })
    else:
        form = ContactForm()
    
    return render(request, 'aplicatia_mea/contact.html', {'form': form})

def adauga_parfum(request):
    if request.method == 'POST':
        form = ParfumForm(request.POST, request.FILES)
        if form.is_valid():
            instanta_parfum = form.save()
            return render(request, 'aplicatia_mea/adauga_parfum.html', {
                'form': form,
                'instanta_parfum': instanta_parfum
                })
        #     return redirect('pagina_succes') 
    else:
        form = ParfumForm()
        
    return render(request, 'aplicatia_mea/adauga_parfum.html', {
        'form': form
        })

def cos_virtual(request):
    return render(request, "aplicatia_mea/in_lucru.html")

def ghid_arome(request):
    return render(request, "aplicatia_mea/in_lucru.html")

def pachete_cadou(request):
    return render(request, "aplicatia_mea/in_lucru.html")

def afis_data(tip):
    now = datetime.now()

    zile = [
        "Luni", "Marti", "Miercuri",
        "Joi", "Vineri", "Sambata", "Duminica"
    ]

    luni = [
        "Ianuarie", "Februarie", "Martie", "Aprilie",
        "Mai", "Iunie", "Iulie", "August",
        "Septembrie", "Octombrie", "Noiembrie", "Decembrie"
    ]

    zi_sapt = zile[now.weekday()]
    zi_luna = now.day
    luna = luni[now.month - 1]
    an = now.year
    ora = now.strftime("%H:%M:%S")

    html = "<section>"
    html += "<h2>Data si ora</h2>"

    if tip == "zi":
        html += f"<p>{zi_sapt}, {zi_luna} {luna} {an}</p>"
    elif tip == "timp":
        html += f"<p>{ora}</p>"
    else:
        html += f"<p>{zi_sapt}, {zi_luna} {luna} {an}</p>"
        html += f"<p>{ora}</p>"

    html += "</section>"
    return html

def info(request):
    
    param = request.GET.get("data")
    
    nume_parametri = list(request.GET.keys())
    nr_parametri = len(nume_parametri)


    sectiune = ""
    if param is not None:
        sectiune = afis_data(param)

    return render(
        request,
        "aplicatia_mea/info.html",
        {
            "sectiune_data": sectiune,
            "nr_parametri": nr_parametri,
            "nume_parametri": nume_parametri,
        }
    )

    


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
    else:
        form = CustomUserCreationForm()
    return render(
        request,
        'aplicatia_mea/register.html',
        {
            'form': form
        }
    )


from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST, request=request)
        if form.is_valid():            
            user = form.get_user()
            
            if getattr(user, 'blocat', False):
                messages.error(request, "Contul tau a fost blocat. Contacteaza un administrator.")
                logger.warning(f"Tentativa de logare pe cont blocat: {user.username}")
                return render(request, 'aplicatia_mea/login.html', {'form': form})
            
            login(request, user)

            request.session['nume_complet'] = user.nume
            request.session['telefon_user'] = user.telefon
            request.session['oras_user'] = user.oras
            request.session['adresa_user'] = user.adresa_livrare
            
            if form.cleaned_data.get('ramane_logat'):
                request.session.set_expiry( 60 * 60 * 24)
            else:
                request.session.set_expiry(0)

            return redirect('profil')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'aplicatia_mea/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index') 

def profil_view(request):
    context = {
        'nume': request.session.get('nume_complet', 'Anonim'),
        'telefon': request.session.get('telefon_user', '-'),
        'oras': request.session.get('oras_user', '-'),
        'adresa': request.session.get('adresa_user', '-'),
    }
    return render(request, 'aplicatia_mea/profil.html', context)

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def schimba_parola_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Parola a fost actualizata!')
            return redirect('profil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'aplicatia_mea/schimba_parola.html', {'form': form})







def afisare_pagina(request):
    logger.debug('Acesta este un mesaj de debug.')
    logger.info('Acesta este un mesaj informativ.')
    logger.warning('Acesta este un avertisment.')
    logger.error('Acesta este un mesaj de eroare.')
    logger.critical('Acesta este un mesaj critic.')
    
def interzis_view(request):
    accesari_403 = request.session.get('accesari_403', 0) + 1
    request.session['accesari_403'] = accesari_403
    
    context = {
        'titlu': "Acces Restrictionat", 
        'mesaj_personalizat': "Nu aveti permisiunile necesare pentru a accesa aceasta zona administrativa.",
        'n_max': settings.N_MAX_403,
        'numar_accesari': accesari_403
    }
    
    return render(request, 'aplicatia_mea/403.html', context, status=403)

