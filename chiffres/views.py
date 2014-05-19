# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from chiffres.forms import ChiffresForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from connexion.models import Connexion



# Create your views here.

@login_required(login_url='/connexion/connexion/')
def home(request):
    from Algo.core import run
    solution=False
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ChiffresForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            conn=Connexion.objects.filter(user_name=request.user.username).latest('date')
            conn.nb_run_chiffres+=1
            conn.save()
            # Ici nous pouvons traiter les données du formulaire
            arg1 = form.cleaned_data['arg1']
            arg2 = form.cleaned_data['arg2']
            arg3 = form.cleaned_data['arg3']
            arg4 = form.cleaned_data['arg4']
            arg5 = form.cleaned_data['arg5']
            arg6 = form.cleaned_data['arg6']
            arg7 = form.cleaned_data['arg7']
            tuple=(arg1,arg2,arg3,arg4,arg5,arg6)
            resultat=run(tuple,arg7)
            op=[]
            for i in range(0,len(resultat)):
                op.append(resultat[i])
            solution=True
            return render(request, 'chiffres/home.html',locals())

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ChiffresForm()  # Nous créons un formulaire vide

    return render(request, 'chiffres/home.html',locals())
    
@login_required(login_url='/connexion/connexion/')
def random(request):
    import random
    solution=False
    data = {'arg1': random.randrange(1,100),
            'arg2': random.randrange(1,100),
            'arg3': random.randrange(1,100),
            'arg4': random.randrange(1,100),
            'arg5': random.randrange(1,100),
            'arg6': random.randrange(1,100),
            'arg7': random.randrange(100,1000)}
    form = ChiffresForm(data)
    return render(request, 'chiffres/home.html',locals())
    
