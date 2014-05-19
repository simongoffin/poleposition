# -*-coding:utf-8 -*
#!/usr/bin/python
import os

path = os.path.abspath(os.path.dirname(__file__))
dict =open(os.path.join(path, "mon_dico_full_a.txt")).read().split()
dict_full=open(os.path.join(path, "mon_dico_full.txt")).read().split()
dic=open(os.path.join(path, "mon_dico_full_a.txt")).read()
dico_v=open(os.path.join(path, "mon_dico_full.txt")).read()


box={}
index=0
for mot in dict:
    box[mot]=index
    index+=1