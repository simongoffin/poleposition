# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from game.forms import LettersForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from connexion.models import Connexion


lettres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
voyelles=['a','e','i','o','u','y']


# Create your views here.

def auteur(request):
  text = """<h1>Première page</h1>
            <p>Simon Goffin</p>"""
  return HttpResponse(text)
  
def auteur2(request):
  return render(request, 'game/auteur2.html',locals())

@login_required(login_url='/connexion/connexion/')
def home(request):
    from Algo.core import run
    from Algo.parser import requete_mot
    import sys
    import random
    solution=False
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = LettersForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            conn=Connexion.objects.filter(user_name=request.user.username).latest('date')
            conn.nb_run_lettres+=1
            conn.save()
            # Ici nous pouvons traiter les données du formulaire
            arg1 = form.cleaned_data['arg1']
            arg2 = form.cleaned_data['arg2']
            arg3 = form.cleaned_data['arg3']
            arg4 = form.cleaned_data['arg4']
            arg5 = form.cleaned_data['arg5']
            arg6 = form.cleaned_data['arg6']
            arg7 = form.cleaned_data['arg7']
            arg8 = form.cleaned_data['arg8']
            arg9 = form.cleaned_data['arg9']
            if arg1==arg2==arg3==arg4==arg5==arg6==arg7==arg8==arg9:
                return render(request, 'game/home.html',locals())
            tuple=(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9)
            resultat=run(tuple)
            longueur_r=len(resultat)
            if longueur_r>0 and not resultat[0]=='':
                print resultat
                print longueur_r
                solution=True
                res=resultat[random.randrange(0,longueur_r)]
                try:
                    definition= requete_mot(res)
                except:
                    definition="Définition introuvable."
                res=res.decode('utf8')
            return render(request, 'game/home.html',locals())

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = LettersForm()  # Nous créons un formulaire vide

    return render(request, 'game/home.html',locals())
    
@login_required(login_url='/connexion/connexion/')
def random(request):
    import random
    solution=False
    data = {'arg1': lettres[random.randrange(0,26)],
            'arg2': voyelles[random.randrange(0,6)],
            'arg3': lettres[random.randrange(0,26)],
            'arg4': lettres[random.randrange(0,26)],
            'arg5': voyelles[random.randrange(0,6)],
            'arg6': lettres[random.randrange(0,26)],
            'arg7': lettres[random.randrange(0,26)],
            'arg8': voyelles[random.randrange(0,6)],
            'arg9': lettres[random.randrange(0,26)]}
    form = LettersForm(data)
    return render(request, 'game/home.html',locals())
    

