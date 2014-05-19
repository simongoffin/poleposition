from django.shortcuts import render
from challenge.models import Score
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/connexion/connexion/')
def vous(request):
    from Algo.Space import space
    liste=Score.objects.filter(user_name=request.user.username).order_by('-score','temps')
    resultat=''
    if len(liste)==0:
        jouer=False
    else:
        jouer=True
        l0='nom: '+space(liste[0].user_name)+' score: '+str(liste[0].score)+' temps: '+str(liste[0].temps)+' sec'
        
    return render(request, 'vous/vous.html',locals())
