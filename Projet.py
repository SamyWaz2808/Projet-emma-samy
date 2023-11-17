# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def display_map(m,d):
    L=m
    for i in range(len(m)):
        for j in range(len(m[i])):
            L[i][j]=d[m[i][j]]
    return L

map = [[0,0,0,1,1],[0,0,0,0,1],[1,1,0,0,0],[0,0,0,0,0]]
dico = {0:' ',1:'#'}
#print(display_map(map, dico))

def create_perso(depart):
    return {"char": "o", "x": depart[0], "y": depart[1]}

personnage = create_perso((3, 2))
#print(personnage)

def display_map_and_char(m,d,p):
    L=display_map(m, d)
    L[p["y"]][p["x"]]=p["char"]
    return L


#print(display_map_and_char(map,dico,personnage))
    
#Ex 2.3

def update_p(letter,p):
    if letter=="z":
        p["y"]-=1
    if letter=="q":
        p["x"]-=1
    if letter=="s":
        p["y"]+=1
    if letter=="d":
        p["x"]+=1
    return p

update_p(input("z,q,s ou d?"), personnage)
print(display_map_and_char(map, dico, personnage))



