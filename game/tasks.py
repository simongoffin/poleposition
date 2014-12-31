from __future__ import absolute_import

from poleposition.celery import app
from game.Algo.core import run
from game.Algo.parser import requete_mot

app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)

@app.task()
def do_work(tuple):
    """ Get some rest, asynchronously, and update the state all the time """
    result = run(tuple)
    if result:
        try:
            definition = requete_mot(result)
        except:
            definition = 'Definition introuvable'
    else:
        definition = 'Pas de solution trouvee'
    return {'current': 'SUCCESS', 'result': result, 'definition': definition}