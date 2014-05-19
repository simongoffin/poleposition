# -*-coding:utf-8 -*
#!/usr/bin/python
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from challenge.forms import LettersForm
from challenge.forms import ChiffresForm
from django.contrib.sessions.backends.db import SessionStore
from challenge.models import Score
# Create your views here.

lettres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
voyelles=['a','e','i','o','u','y']
s = SessionStore()
nb_coups=6

@login_required(login_url='/connexion/connexion/')
def intro(request):
    finish=False
    s['point']=0
    s['tour']=0
    s['analyse']=0
    s['duree']=0
    s.save()
    return render(request, 'challenge/intro.html',locals())

@login_required(login_url='/connexion/connexion/')
def coup_lettres(request):
    import random
    import time
    try:
        if s['tour']>=nb_coups:
            duree=0
            point=0
            finish=True
            return render(request, 'challenge/next.html',locals())
    except:
        return redirect('challenge.views.intro')
    if s['tour']%2==0:
        arg1= lettres[random.randrange(0,26)]
        s['arg1']=arg1
        arg2= voyelles[random.randrange(0,6)]
        s['arg2']=arg2
        arg3=lettres[random.randrange(0,26)]
        s['arg3']=arg3
        arg4= lettres[random.randrange(0,26)]
        s['arg4']=arg4
        arg5= voyelles[random.randrange(0,6)]
        s['arg5']=arg5
        arg6= lettres[random.randrange(0,26)]
        s['arg6']=arg6
        arg7= lettres[random.randrange(0,26)]
        s['arg7']=arg7
        arg8= voyelles[random.randrange(0,6)]
        s['arg8']=arg8
        arg9= lettres[random.randrange(0,26)]
        s['arg9']=arg9
        s['time']=time.time()
        s['tour']+=1
        s.save()
        form = LettersForm()
        return render(request, 'challenge/lettres.html',locals())
    else:
        ch1=random.randrange(1,100)
        s['ch1']=ch1
        ch2=random.randrange(1,100)
        s['ch2']=ch2
        ch3=random.randrange(1,100)
        s['ch3']=ch3
        ch4=random.randrange(1,100)
        s['ch4']=ch4
        ch5=random.randrange(1,100)
        s['ch5']=ch5
        ch6=random.randrange(1,100)
        s['ch6']=ch6
        compte=random.randrange(100,1000)
        s['compte']=compte
        s['time']=time.time()
        s['tour']+=1
        s.save()
        form=ChiffresForm()
        return render(request, 'challenge/chiffres.html',locals())
    
@login_required(login_url='/connexion/connexion/')
def valide_lettres(request):
    from Algo.Lettres_check import lettres_check
    import time
    finish=False
    solution=False
    try:
        if s['tour']>nb_coups:
            duree=0
            point=0
            finish=True
            return render(request, 'challenge/next.html',locals())
        elif s['analyse']==s['tour']:
            duree=0
            point=0
            return render(request, 'challenge/next.html',locals())
    except:
        return redirect('challenge.views.intro')
    duree=time.time()-s['time']
    s['duree']+=duree
    s['analyse']+=1
    s.save()
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = LettersForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            mot = form.cleaned_data['solution']
            liste=[s['arg1'],s['arg2'],s['arg3'],s['arg4'],s['arg5'],s['arg6'],s['arg7'],s['arg8'],s['arg9']]
            temp=lettres_check(liste,mot)
            point=temp[1]
            if point>0:
                solution=True
                s['point']+=temp[1]
                s.save()
            if s['tour']==nb_coups:
                print 'Score save(on lettres valide)'
                finish=True
                score= Score(user_name=request.user.username,score=s['point'],temps=s['duree']).save()
            return render(request, 'challenge/next.html',locals())
        else:
            if s['tour']==nb_coups:
                print 'Score save(on lettres non valide)'
                finish=True
                score= Score(user_name=request.user.username,score=s['point'],temps=s['duree']).save()
                return render(request, 'challenge/next_chiffres.html',locals())
            elif s['tour']>nb_coups:
                finish=True
                return render(request, 'challenge/next_chiffres.html',locals())
            else:
                return render(request, 'challenge/next_chiffres.html',locals())
    else:
        if s['tour']>=nb_coups:
            finish=True
        return render(request, 'challenge/next.html',locals())
        
@login_required(login_url='/connexion/connexion/')
def valide_chiffres(request):
    from Algo.Chiffres_check import chiffres_check
    import time
    finish=False
    solution=False
    try:
        if s['tour']>nb_coups:
            duree=0
            point=0
            finish=True
            return render(request, 'challenge/next_chiffres.html',locals())
        elif s['analyse']==s['tour']:
            duree=0
            point=0
            return render(request, 'challenge/next.html',locals())
    except:
        return redirect('challenge.views.intro')
    duree=time.time()-s['time']
    point=0
    s['duree']+=duree
    s['analyse']+=1
    s.save()
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ChiffresForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            v=[]
            op1 = form.cleaned_data["op1"]
            if not op1=='':
                v.append(op1)
            op2 = form.cleaned_data["op2"]
            if not op2=='':
                v.append(op2)
            op3 = form.cleaned_data["op3"]
            if not op3=='':
                v.append(op3)
            op4 = form.cleaned_data["op4"]
            if not op4=='':
                v.append(op4)
            op5 = form.cleaned_data["op5"]
            if not op5=='':
                v.append(op5)
            liste=[s['ch1'],s['ch2'],s['ch3'],s['ch4'],s['ch5'],s['ch6']]
            temp=chiffres_check(v,liste,s['compte'])
            print temp
            point=temp[1]
            if point>0:
                solution=True
            if temp[0]:
                s['point']+=temp[1]
                s.save()
            if s['tour']==nb_coups:
                print 'Score save(on chiffres valide)'
                finish=True
                score= Score(user_name=request.user.username,score=s['point'],temps=s['duree']).save()
            return render(request, 'challenge/next_chiffres.html',locals())
        else:
            if s['tour']==nb_coups:
                print 'Score save(on chiffres non valide)'
                finish=True
                score= Score(user_name=request.user.username,score=s['point'],temps=s['duree']).save()
                return render(request, 'challenge/next_chiffres.html',locals())
            elif s['tour']>nb_coups:
                finish=True
                return render(request, 'challenge/next_chiffres.html',locals())
            else:
                return render(request, 'challenge/next_chiffres.html',locals())
    else:
        if s['tour']>=nb_coups:
            finish=True
        return render(request, 'challenge/next_chiffres.html',locals())
        
@login_required(login_url='/connexion/connexion/')
def fin(request):
    try:
        temps_total=s['duree']
        point_total=s['point']
        return render(request, 'challenge/fin.html',locals())
    except:
        return redirect('challenge.views.intro')
