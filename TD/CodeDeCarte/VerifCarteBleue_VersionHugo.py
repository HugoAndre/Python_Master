# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:50:57 2019

@author: ah78416h
"""

def EtTaSoeur(Code):
    """ Fonction qui vérifie que le code respecte l'algorithme de Carte Bleue  
    Si le code fait pas 12 chiffres, une alerte est donnée..."""

    if isinstance(Code,int)==0:
        disp('Problème: la variable d\'entrée n\'est pas de type entier')
    else:
        Code_ListDeCaracter=list(str(Code)) #  converti le code (12 chiffres) en liste de caractère
        NewCode = [] # déclaration de la variable qui va se souvenir du Nouveau code de carte bleue ! 
        for index in range(16):
            if index%2==0:
                NewNumber=int(Code_ListDeCaracter[index])
                print('numéro '+str(index)+' \t\t: '+Code_ListDeCaracter[index] + '\t -> ' + str(NewNumber) )
                
            else:
                NewNumber_str=str(int(Code_ListDeCaracter[index])*2) # on multiplie le nombre par 2! attention au type de format ! 
                if len(NewNumber_str)==2:
                    NewNumber=int(NewNumber_str[0])+int(NewNumber_str[1])
                else:
                    NewNumber=int(NewNumber_str[0])
                print('numéro ' + str(index) + '\t *2\t: ' + NewNumber_str + '\t -> ' + str(NewNumber) )
            NewCode.append(NewNumber)

        Valid=sum(NewCode)%10
        if Valid==0:
            print('Nouveau Code: '+str(NewCode)+' \t somme = '+str(sum(NewCode)) + ' = ',str(Valid),'%10\t CODE CORRECT!')
            return 1
        else:
            print('Nouveau Code: '+str(NewCode)+' \t somme = '+str(sum(NewCode)) + ' = ',str(Valid),'%10\t CODE FAUX!')
            return 0
    
EtTaSoeur(1234567890123456)
EtTaSoeur(5121314151617282)