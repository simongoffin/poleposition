#-*- coding: utf-8 -*-
def no_space(adresse):
    ad=''
    for i in range(0,len(adresse)):
        l=adresse[i]
        if not l==' ':
            ad=ad+l
    return ad