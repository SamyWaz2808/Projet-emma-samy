# -- coding: utf-8 --
"""
Created on Thu Nov 30 18:47:14 2023

@author: emmaa
"""

from random import randint
from colorama import Back,Fore,Style


def generate_map(size_map,proportion_wall):
    L=[[0]*size_map[0] for i in range(size_map[1])]
    nbr_wall=(int(size_map[0]*size_map[1]*proportion_wall))
    walls_in_map=[]
    while len(walls_in_map)<nbr_wall:
        a=randint(0,size_map[0]-1)
        b=randint(0,size_map[1]-1)
        if (a,b) not in walls_in_map :
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

def choisir_difficulte():
    print("choisir niveau de difficulté :")
    print("1. easy")
    print("2. bof")
    print("3. hard")

    while True:
        try:
            diff = int(input("(1, 2 ou 3) : "))
            if 1 <= diff <= 3:
                break
            else:
                print("entrer un nombre entre 1 et 3.")
        except ValueError:
            print("entrer un nombre.")

    if diff == 1:
        size_map = (8, 4) 
        proportion_wall = 0.1  
    elif diff == 2:
        size_map = (14, 8)  
        proportion_wall = 0.2  
    else:
        size_map = (18, 10)  
        proportion_wall = 0.3  

    return size_map, proportion_wall

size_map, proportion_wall = choisir_difficulte()        
map = generate_map(size_map, proportion_wall)


dico = {0:' ',1:Fore.WHITE + Back.WHITE + Style.BRIGHT +'#' +Style.RESET_ALL}


def create_perso(depart):
    return {"char": Fore.YELLOW + Style.BRIGHT +"☺" + Style.RESET_ALL, "x": depart[0], "y": depart[1], "score":0}

a=randint(0,len(map[0])-1)
b=randint(0,len(map)-1)
while map[b][a]==1:
    a=randint(0,len(map[0])-1)
    b=randint(0,len(map)-1)

personnage = create_perso((a, b))

def create_map_and_char(m,d,p):
    L=create_map(m, d)
    L[p["y"]][p["x"]]=p["char"]
    return L

def display_map_and_char(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()


def update_p(letter, p, m):
    if letter == "z" and p["y"] > 0 and m[p["y"] - 1][p["x"]] != Fore.WHITE + Back.WHITE + Style.BRIGHT + '#' + Style.RESET_ALL:
        p["y"] -= 1
    if letter == "q" and p["x"] > 0 and m[p["y"]][p["x"] - 1] != Fore.WHITE + Back.WHITE + Style.BRIGHT + '#' + Style.RESET_ALL:
        p["x"] -= 1
    if letter == "s" and p["y"] < len(m) - 1 and m[p["y"] + 1][p["x"]] != Fore.WHITE + Back.WHITE + Style.BRIGHT + '#' + Style.RESET_ALL:
        p["y"] += 1
    if letter == "d" and p["x"] < len(m[0]) - 1 and m[p["y"]][p["x"] + 1] != Fore.WHITE + Back.WHITE + Style.BRIGHT + '#' + Style.RESET_ALL:
        p["x"] += 1
    return p

def create_objects(nombre_objet,m):
    s=[]
    while len(s)<nombre_objet:
        n=randint(0,len(m[0])-1)
        k=randint(0,len(m)-1)
        if m[k][n]!=Fore.WHITE + Back.WHITE + Style.BRIGHT +'#' +Style.RESET_ALL and ((n,k) not in s) and m[k][n]!=Fore.YELLOW + Style.BRIGHT +"☺" + Style.RESET_ALL:
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
         
def create_finish(m):
    while True:
        n=randint(0,len(m[0])-1)
        k=randint(0,len(m)-1)
        if m[k][n]!=Fore.WHITE + Back.WHITE + Style.BRIGHT +'#' +Style.RESET_ALL and m[k][n]!=Fore.YELLOW + Style.BRIGHT +"☺" + Style.RESET_ALL and m[k][n]!=Fore.RED + Style.BRIGHT +"⁎"+ Style.RESET_ALL :
            return (n,k)
         
def create_map_char_and_objects_and_finish(m,d,p,s,f):
    L=create_map_char_and_objects(m,d,p,s)
    L[f[1]][f[0]]="X"
    return L

def display_map_and_char_and_objects_and_finish(m):
    for i in m:
        for j in i:
            print (j, end='')
        print()
    print(Fore.CYAN + Style.BRIGHT + "SCORE : %d" % personnage["score"] + Style.RESET_ALL)

abandon=0
level=1
while True:
    map_perso=create_map_and_char(map, dico, personnage)
    objects=create_objects(6,map_perso)
    map_perso_objects=create_map_char_and_objects(map, dico, personnage,objects)
    finish=create_finish(map_perso_objects)
    map_perso_objects_finish=create_map_char_and_objects_and_finish(map, dico, personnage,objects,finish)
    display_map_and_char_and_objects_and_finish(map_perso_objects_finish)
    print("LEVEL : %d" %level)
    if level>1:
        print(Fore.GREEN + Style.BRIGHT+ "Prochain niveau!" + Style.RESET_ALL)
    while True: 
        personnage = update_p(input("z(↑),q(←),s(↓) ou d(→) ou e ?"), personnage,map_perso_objects)
        update_objects(personnage,objects)
        map_perso_objects_finish=create_map_char_and_objects_and_finish(map, dico, personnage,objects,finish)
        display_map_and_char_and_objects_and_finish(map_perso_objects_finish)
        print("LEVEL : %d sur 10" %level)
        if personnage["x"]==finish[0] and personnage["y"]==finish[1]:
            if personnage["score"]%6!=0:
                abandon=1
            break
    
    map = generate_map(size_map, proportion_wall)
    level+=1
    
    if level==11 or abandon==1:
        break

if abandon==1:
    print (Fore.GREEN + Style.BRIGHT+ "VOUS AVEZ ABANDONNÉ " + Style.RESET_ALL)
else:
    print (Fore.GREEN + Style.BRIGHT+ "BRAVO VOUS AVEZ GAGNÉ " + Style.RESET_ALL)
    
