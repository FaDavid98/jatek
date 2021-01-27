#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:30:19 2021

@author: david
"""
##
from random import randint

compwin=0
userwin=0
print('jeloles:')
print('1 = ko')
print('2 = papir')
print('3 = ollo')

while True:
    comp=randint(1,3)
    user=int(input('valasszon a megadott harom lehetoseg kozul egyet: '))
    print()
    if user==1:
        print('on a kovet valasztotta')
    elif user==2:
        print('on a papirt valasztotta')
    elif user==3:
        print('on az ollot valasztotta')
    else:
        quit
    if comp==1:
        print('a szamitogep a kovet valasztotta')
    elif comp==2:
        print('a szamitogep a papirt valasztotta')
    else:
        print('a szamitogep az ollot valasztotta')
    print()
    if 1<=user<=3: 
        if abs(comp-user)==1:
            if comp>user:
                print('vesztett')
                compwin+=1
            else:
                print('nyert')
                userwin+=1
        elif abs(comp-user)==2:
            if comp>user:
                print('nyert')
                userwin+=1
            else:
                print('vesztett')
                compwin+=1
        else:
            print('dontetlen')
    else:
        print('ez nem megfelelo! Ellenorizze a jelolest es adjon meg megfelelo erteket.')
    print()
    print('a jatekos gyozelmeinek szama: ',userwin)
    print('a szamitogep gyozelmeinek szama: ',compwin)
    print()
    print('szeretne meg jatszani (igen/nem)?')
    m=str(input('kerem a valaszt: '))
    if m=='igen':
        continue
    elif m=='nem':
        print('koszonom a jatekot')
        break
    else:
        print('hasznalja a kert jelolest: ')
        m=str(input('kerem a valaszt: '))
        

