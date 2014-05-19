# -*-coding:utf-8 -*
#!/usr/bin/python
import sys
import os
import time
from dico import dic,box,dict_full

from .search import *

class LettresProblem(Problem):


    def __init__(self,init):
        self.dico={}
        self.symetrie=0
        self.solution=['']
        self.taille=0
        goal=''
        Problem.__init__(self, init, goal)

    
    def goal_test(self, state):
        return False
            
    def successor(self, state):
        for valeur1 in state:
            temp=state[:]
            temp=temp[0:temp.index(valeur1)]+temp[temp.index(valeur1)+1:len(temp)]
            for valeur2 in temp:
                if len(valeur2)==1:
                    if not valeur1+valeur2 in self.dico:
                        self.dico[valeur1+valeur2]=1
                        check=possible(valeur1,valeur2,self.taille)
                        self.symetrie+=1
                        if check[0]:
                            newmove=temp[:]
                            newmove=newmove[0:newmove.index(valeur2)]+newmove[newmove.index(valeur2)+1:len(newmove)]
                            newmove=newmove+(valeur1+valeur2,)
                            if check[1]>self.taille:
                                self.taille=check[1]
                                self.solution=check[2]
                            elif check[1]==self.taille:
                                for seq in check[2]:
                                    self.solution.append(seq)
                            etape=valeur1+' '+'+'+' '+valeur2+' '+'='+' '+valeur1+valeur2
                            yield (etape,newmove)
                        else: continue
                    
def possible(valeur1,valeur2,taille):
    seq=valeur1+valeur2
    if seq in dic:
        if len(seq)>=taille and seq in box:
            tab=dico_mots(seq)
            return [True,len(seq),tab]
        return [True,-1,valeur1+valeur2]
    else:
        return [False,-1,'']
        
def dico_mots(seq):
    res=[]
    index=box[seq]
    res.append(dict_full[index])
    index=index-1
    while not index in box.values() and index>=0:
        res.append(dict_full[index])
        index=index-1
    return res
    
        
def run(tuple):
    problem=LettresProblem(tuple)
    #example of bfs search
    debut=time.time()
    #node=breadth_first_tree_search(problem)
    node=depth_first_tree_search(problem)
    resultat=problem.solution
    fin=time.time()
    print fin-debut
    return resultat
    
    
if __name__ == "__main__":    
    tuple=('v','o','e','u','n','b','e','t','l')
    v=run(tuple)
    print v
    