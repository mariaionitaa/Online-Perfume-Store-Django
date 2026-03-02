from django import forms
from .models import Parfum, Categorie
from django.core.exceptions import ValidationError
from datetime import date, datetime
import re
from decimal import Decimal

class ParfumFilterForm(forms.Form):
    nume = forms.CharField(
        required=False, 
        initial='',
        widget=forms.TextInput(attrs={'placeholder': 'Cauta dupa nume...', 'class': 'form-control'})
    )
    
    pret_min = forms.DecimalField(
        required=False, 
        widget=forms.NumberInput(attrs={'step': '10', 'placeholder': 'Min', 'class': 'form-control'})
    )
    pret_max = forms.DecimalField(
        required=False, 
        widget=forms.NumberInput(attrs={'step': '10', 'placeholder': 'Max', 'class': 'form-control'})
    )
    
    volum = forms.IntegerField(
        required=False, 
        widget=forms.NumberInput(attrs={'placeholder': 'ml', 'class': 'form-control'})
    )
    
    gen = forms.ChoiceField(
        choices=[('', 'Toate genurile')] + Parfum.GEN_PARFUM_CHOICES,
        initial='Toate genurile',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        empty_label="Toate categoriile",
        label="Categorie"
    )
    
    elemente_pe_pagina = forms.ChoiceField(
        choices=[('2', '2'), ('5', '5'), ('10', '10'), ('20', '20')],
        initial='5',
        required=False,
        label="Produse pe pagina"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        p_min = cleaned_data.get("pret_min")
        p_max = cleaned_data.get("pret_max")

        if p_min and p_max and p_min > p_max:
            raise forms.ValidationError(
                "Pretul minim nu poate fi mai mare decat cel maxim! Verifica intervalul de pret."
            )
        return cleaned_data

    def clean_nume(self):
        nume = self.cleaned_data.get('nume')
        if nume and len(nume) < 2:
            raise forms.ValidationError(
                "Te rugam sa introduci cel putin 2 caractere pentru a cauta un parfum."
            )
        return nume

    def clean_volum(self):
        volum = self.cleaned_data.get('volum')
        if volum is not None and volum <= 0:
            raise forms.ValidationError(
                "Volumul trebuie sa fie un numar pozitiv. Nu vindem parfumuri invizibile!"
            )
        return volum
    
    


def valideaza_major(value):
    today = date.today()
    varsta = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    
    if varsta < 18:
        raise ValidationError("Trebuie sa aveti peste 18 ani pentru a trimite acest mesaj.")

def valideaza_numar_cuvinte(value):
    cuvinte = re.findall(r'\w+', value)
    nr_cuvinte = len(cuvinte)
    
    if nr_cuvinte < 5 or nr_cuvinte > 100:
        raise ValidationError("Mesajul trebuie sa contina intre 5 si 100 de cuvinte.")
        
def valideaza_lungime_maxima_cuvant(value):
    cuvinte = re.findall(r'\w+', value)
    
    for cuvant in cuvinte:
        if len(cuvant) > 15:
            raise ValidationError("Lungimea maxima permisa pentru un singur cuvant este de 15 caractere.")
            
def fara_linkuri(value):
    text = value.lower()
    if "http://" in text or "https://" in text:
        raise ValidationError("Nu este permisa introducerea link-urilor (http/https) in acest camp.")
    
def valideaza_selectie_mesaj(value):
    if value == 'neselectat':
        raise ValidationError("Va rugam sa selectati un tip de mesaj valid.")

def valideaza_cnp_doar_cifre(value):
    if not value.isdigit():
        raise ValidationError("CNP-ul trebuie sa contina doar cifre. Va rugam sa eliminati literele sau spatiile.")

def valideaza_structura_cnp(value):
    if not value or len(value) != 13 or not value.isdigit():
        return  

    prima_cifra = value[0]
    if prima_cifra not in ['1', '2', '5', '6']:
        raise ValidationError("CNP-ul trebuie sa inceapa cu 1, 2 (secolul XX) sau 5, 6 (secolul XXI).")

    an_fragment = value[1:3]
    luna_fragment = value[3:5]
    zi_fragment = value[5:7]

    secol = "19" if prima_cifra in ['1', '2'] else "20"
    an_complet = secol + an_fragment

    try:
        datetime.strptime(f"{an_complet}{luna_fragment}{zi_fragment}", "%Y%m%d")
    except ValueError:
        raise ValidationError("Secventa  din CNP nu reprezinta o data valida.")

def fara_email_temporar(value):
    domenii_interzise = ['guerillamail.com', 'yopmail.com']
    
    try:
        domeniu = value.split('@')[1].lower()
    except IndexError:
        return 

    if domeniu in domenii_interzise:
        raise ValidationError("Domeniul este blocat. Va rugam sa folositi o adresa de e-mail valida, nu una temporara.")

def valideaza_text_specific(value):
    if not value:
        return

    if not value[0].isupper():
        raise ValidationError("Textul trebuie sa inceapa cu litera mare.")

    text_curat = value.replace(" ", "").replace("-", "")
    
    if not text_curat.isalpha():
        raise ValidationError("Sunt permise doar litere, spatii si cratima.")

def valideaza_majuscula_dupa_separator(value):
    if not value:
        return

    for i in range(len(value) - 1):
        if value[i] in [' ', '-']:
            if not value[i+1].isupper():
                raise ValidationError("Dupa spatiu sau cratima trebuie sa urmeze o litera mare.")


def calculeaza_varsta_detaliata(data_nastere):
    azi = date.today()
    
    ani = azi.year - data_nastere.year
    luni = azi.month - data_nastere.month
    if azi.day < data_nastere.day:
        luni -= 1
    if luni < 0:
        ani -= 1
        luni += 12
    return f"{ani} de ani si {luni} luni"


class ContactForm(forms.Form):
    TIP_MESAJ_CHOICES = [
        ('neselectat', 'Neselectat'),
        ('reclamatie', 'Reclamatie'),
        ('intrebare', 'Intrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
    ]

    nume = forms.CharField(
        max_length=10,
        required=True,
        label="Nume",
        validators=[valideaza_text_specific, valideaza_majuscula_dupa_separator]
    )
    prenume = forms.CharField(
        max_length=10,
        required=False,
        label="Prenume",
        validators=[valideaza_text_specific, valideaza_majuscula_dupa_separator]
    )
    
    cnp = forms.CharField(
        min_length=13, 
        max_length=13, 
        required=False, 
        label="CNP",
        validators=[valideaza_cnp_doar_cifre, valideaza_structura_cnp]
    )
    
    data_nasterii = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Data nasterii",
        validators=[valideaza_major]
    )
    
    email = forms.EmailField(
        required=True,
        label="E-mail",
        validators=[fara_email_temporar]
    )
    confirmare_email = forms.EmailField(required=True, label="Confirmare e-mail")
    
    tip_mesaj = forms.ChoiceField(
        choices=TIP_MESAJ_CHOICES,
        initial='neselectat',
        label="Tip mesaj",
        validators=[valideaza_selectie_mesaj]
    )
    
    subiect = forms.CharField(
        max_length=100,
        required=True,
        label="Subiect",
        validators=[fara_linkuri, valideaza_text_specific]
    )
    
    zile_asteptare = forms.IntegerField(
        min_value=0,
        max_value=30,
        required=True,
        label="Minim zile asteptare",
        help_text="Pentru review-uri/cereri minimul de zile de asteptare trebuie setat de la 4 incolo iar pentru intrebari de la 2 incolo. Maximul e 30."
    )
    
    mesaj = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        required=True,
        label="Mesaj (Va rugam sa va si semnati la finalul mesajului)",
        validators=[valideaza_numar_cuvinte, valideaza_lungime_maxima_cuvant, fara_linkuri]
    )

    def clean(self):
        cleaned_data = super().clean()
        nume = cleaned_data.get("nume")
        mesaj = cleaned_data.get("mesaj")
        email = cleaned_data.get("email")
        cemail = cleaned_data.get("confirmare_email")
        tip = cleaned_data.get("tip_mesaj")
        zile = cleaned_data.get("zile_asteptare")
        cnp = cleaned_data.get("cnp")
        data_nasterii = cleaned_data.get("data_nasterii")

        if email and cemail and email != cemail:
            raise ValidationError("Adresele de e-mail nu coincid!")

        if nume and mesaj:
            cuvinte_mesaj = re.findall(r'\w+', mesaj)
            
            if cuvinte_mesaj:
                ultima_semnatura = cuvinte_mesaj[-1]
                if ultima_semnatura.lower() != nume.lower():
                    self.add_error('mesaj', "Lipsa semnatura! Ultimul cuvant din mesaj trebuie sa fie numele dumneavoastra.")

        if zile is not None:
            if tip in ['review', 'cerere'] and zile < 4:
                self.add_error('zile_asteptare', "Pentru review/cerere, minimul este 4 zile.")
            elif tip in ['intrebare'] and zile < 2:
                self.add_error('zile_asteptare', "Pentru intrebare, minimul este 2 zile.")
        
        if cnp and data_nasterii:
            an_calendar = str(data_nasterii.year)[2:]
            luna_calendar = str(data_nasterii.month).zfill(2)
            zi_calendar = str(data_nasterii.day).zfill(2)
            
            data_formatata_calendar = f"{an_calendar}{luna_calendar}{zi_calendar}"
            
            data_din_cnp = cnp[1:7]

            if data_formatata_calendar != data_din_cnp:
                self.add_error('cnp',"CNP-ul nu corespunde cu data nasterii selectata.")
        
        if data_nasterii:
            cleaned_data['varsta_procesata'] = calculeaza_varsta_detaliata(data_nasterii)
        
        cleaned_data['urgent'] = False

        if tip and zile is not None:
            minim_zile = 0
            if tip in ['review', 'cerere']:
                minim_zile = 4
            elif tip in ['intrebare']: 
                minim_zile = 2
            
            if zile == minim_zile:
                cleaned_data['urgent'] = True
        
        return cleaned_data
    
    def clean_mesaj(self):
        mesaj = self.cleaned_data.get('mesaj')
        
        if mesaj:
            mesaj = mesaj.replace('\n', ' ').replace('\r', ' ')
            mesaj = re.sub(r'\s+', ' ', mesaj).strip()
            def majuscula_callback(match):
                return match.group(1) + match.group(2) + match.group(3).upper()
            pattern = r'([\.\!\?]+)(\s+)([a-zăîâșț])'
            mesaj = re.sub(pattern, majuscula_callback, mesaj)
            if mesaj:
                mesaj = mesaj[0].upper() + mesaj[1:]
                
        return mesaj
    
    
    
    
class ParfumForm(forms.ModelForm):
    pret_importator = forms.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        label="Pret cumparare importator",
        required=True
    )
    procent_adaos = forms.IntegerField(
        label="Procentaj adaos (%)",
        initial=20,
        required=True
    )
    
    nume_parfum = forms.CharField(
        max_length=10,
        required=True,
        help_text="Numele trebuie sa contina litere si nu poate include link-uri.",
        validators=[valideaza_text_specific, fara_linkuri],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    descriere = forms.CharField(
        validators=[fara_linkuri],
        help_text="Includeti obligatoriu numele parfumului in descriere.",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=True
    ) 
    
    class Meta:
        model = Parfum
        fields = [
            'nume_parfum', 'descriere', 'imagine', 
            'gen_parfum', 'volum', 
            'nume_categorie', 'furnizori'
        ]

        widgets = {
            'nume_parfum': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Introduceti numele parfumului...'
            }),
            'descriere': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Descrieti notele si persistenta...'
            }),
        }
        
        labels = {
            'nume_parfum': 'Denumire Parfum',
            'descriere': 'Descriere',
            'gen_parfum': 'Gen parfum',
            'volum': 'Volum (ml)',
            'nume_categorie': 'Categorie',
            'furnizori': 'Lista Furnizori'
        }
        
    def clean_nume_parfum(self):
        nume = self.cleaned_data.get('nume_parfum')
        if nume and not re.search('[a-zA-Z]', nume):
            raise ValidationError("Numele parfumului trebuie sa contina macar o litera.")
        return nume

    def clean_descriere(self):
        descriere = self.cleaned_data.get('descriere')
        if descriere and len(descriere) < 10:
            raise ValidationError("Descrierea este prea scurta. Introduceti minim 10 caractere.")
        return descriere

    def clean_volum(self):
        volum = self.cleaned_data.get('volum')
        if volum is not None and volum <= 0:
            raise forms.ValidationError(
                "Volumul trebuie sa fie un numar pozitiv. Nu vindem parfumuri invizibile!"
            )
        return volum
    
    def clean(self):
        cleaned_data = super().clean()
        
        nume = cleaned_data.get("nume_parfum")
        descriere = cleaned_data.get("descriere")

        if nume and descriere:
            if nume.lower() not in descriere.lower():
                self.add_error('descriere', f"Descrierea trebuie sa includa denumirea parfumului.")

        return cleaned_data
        
    def save(self, commit=True):
        instanta = super().save(commit=False)
            
        pret_baza = self.cleaned_data.get('pret_importator')
        adaos = self.cleaned_data.get('procent_adaos')

        if pret_baza and adaos is not None:
            multiplicator = Decimal('1') + (Decimal(str(adaos)) / Decimal('100'))
            instanta.pret = pret_baza * multiplicator

        if commit:
            instanta.save()
            self.save_m2m()
                
        return instanta