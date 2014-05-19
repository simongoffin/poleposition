from django.shortcuts import render
from challenge.models import Score
# Create your views here.



def score(request):
    from Algo.Space import space
    liste=Score.objects.order_by('-score','temps')
    l0='nom: '+space(liste[0].user_name)+' score: '+str(liste[0].score)+' temps: '+str(liste[0].temps)+' sec'
    l1='nom: '+space(liste[1].user_name)+' score: '+str(liste[1].score)+' temps: '+str(liste[1].temps)+' sec'
    l2='nom: '+space(liste[2].user_name)+' score: '+str(liste[2].score)+' temps: '+str(liste[2].temps)+' sec'
    l3='nom: '+space(liste[3].user_name)+' score: '+str(liste[3].score)+' temps: '+str(liste[3].temps)+' sec'
    l4='nom: '+space(liste[4].user_name)+' score: '+str(liste[4].score)+' temps: '+str(liste[4].temps)+' sec'
    return render(request, 'score/score.html',locals())