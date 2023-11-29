# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint
from colorama import Back,Fore,Style,init
init()


def generate_map(size_map,proportion_wall):
    L=[[0]*size_map[0] for i in range(size_map[1])]
    nbr_wall=(int(size_map[0]*size_map[1]*proportion_wall))
    walls_in_map=[]
    while len(walls_in_map)<nbr_wall:
        a=randint(0,size_map[0]-1)
        b=randint(0,size_map[1]-1)
        if (a,b) not in walls_in_map:
            walls_in_map.append((a,b))
    for i,j in walls_in_map:
        L[j][i]=1
    
    return L
            
    
def copy_matrice(m):
    nouvmatrice=[]
    for i in m:
        nouvmatrice.append(i[:])
    return nouvmatrice
    
def create_map(m,d):
    L=copy_matrice(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            L[i][j]=d[m[i][j]]
    return L

def display_map(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()
        
map = generate_map((9,5), 0.2)
dico = {0:' ',1:'#'}
#print(create_map(map, dico))

def create_perso(depart):
    return {"char": Fore.YELLOW + Style.BRIGHT +"☺" + Style.RESET_ALL, "x": depart[0], "y": depart[1], "score":0}

personnage = create_perso((3, 2))
#print(personnage)

def create_map_and_char(m,d,p):
    L=create_map(m, d)
    L[p["y"]][p["x"]]=p["char"]
    return L

def display_map_and_char(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()
        
#print(create_map_and_char(map,dico,personnage))
    
#Ex 2.3

def update_p(letter,p,m):
    if (letter=="z") and (p["y"]>0) and (m[p["y"]-1][p["x"]] != '#'):
            p["y"]-=1
    if (letter=="q") and (p["x"]>0) and (m[p["y"]][p["x"]-1] != '#'):
            p["x"]-=1
    if (letter=="s") and (p["y"]<len(m)-1) and (m[p["y"]+1][p["x"]] != '#'):
            p["y"]+=1
    if (letter=="d") and (p["x"]<len(m[0])-1) and (m[p["y"]][p["x"]+1] != '#'):
            p["x"]+=1
    return p


def create_objects(nombre_objet,m):
    s=[]
    while len(s)<nombre_objet:
        n=randint(0,4)
        k=randint(0,3)
        if m[k][n]!='#' and ((n,k) not in s) and m[k][n]!='☺':
            s.append((n,k))
    return s


def create_map_char_and_objects(m,d,p,s):
    L=create_map_and_char(m,d,p)
    for i,j in s:
        L[j][i]=Fore.RED + Style.BRIGHT +"⁎"+ Style.RESET_ALL
    return L

def display_map_and_char_and_objects(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()
    print(Fore.CYAN + Style.BRIGHT + "SCORE : %d" % personnage["score"] + Style.RESET_ALL)
    
def update_objects(p,objects):
     if (p['x'],p['y']) in objects:
         p['score']+=1
         objects.remove((p['x'],p['y']))

map_perso=create_map_and_char(map, dico, personnage)
objects=create_objects(4,map_perso)
map_perso_objects=create_map_char_and_objects(map, dico, personnage,objects)
display_map_and_char_and_objects(map_perso_objects)

while True: 
    personnage = update_p(input("z(↑),q(←),s(↓) ou d(→)?"), personnage,map_perso)
    update_objects(personnage,objects)
    map_perso=create_map_char_and_objects(map, dico, personnage,objects)
    display_map_and_char_and_objects(map_perso)
    



