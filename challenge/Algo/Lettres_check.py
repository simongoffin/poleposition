# -*-coding:utf-8 -*
#!/usr/bin/python
from dico import dico_v

caracteres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def lettres_check(lettres,mot):
    nb_t=0
    for l in mot:
        l=transforme(l)
        if l=='-':
            nb_t+=1
        elif l in lettres:
            lettres.remove(l)
        else:
            return [False,0]
    if mot.encode('utf-8') in dico_v:
        return [True,len(mot)-nb_t]
    else:
        return [False,0]
        
def transforme(l):
    if l==u'é' or l==u'è'or l==u'ê' or l==u'ë':
        return 'e'
    elif l==u'à' or l==u'ä'or l==u'â':
        return 'a'
    elif l==u'ô' or l==u'ö'or l==u'ò':
        return 'o'
    elif l==u'û' or l==u'ù'or l==u'ü':
        return 'u'
    elif l==u'î' or l==u'ï'or l==u'ì':
        return 'i'
    elif l==u'ç':
        return 'c'
    else:
        return l


