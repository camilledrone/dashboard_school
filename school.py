##voici le code python excécuté dans l'invite de commante
## c'est ici que nous créons le serveur local et que nous appelons les scripts hmtl

#!/usr/bin/python

##import des librairies python
from flask import Flask
from flask import render_template
from flask import jsonify
import json
import requests

## création du serveur flask que nous nommons "school"

school = Flask(__name__)

########################################################################################################################

## le code suivant est commenté
## il permet de lire les données excel (ces données ne sont pas ici nécessaires, nous avons rentré à la main les valeurs)

## Function to import the data from excel

from itertools import combinations
import math as mt

import csv


##excel student course
##on crée une liste contenant chaque ligne dd l'excel sous forme d'un dictionnaire dont la clé est 'course'
## et la value est une liste de string correspondant à toutes les colonnes de la ligne
#file_course=open('D:/Users/Camille/OneDrive/Documents/Imt 2020-2021/codev/donnees/student.course.csv','r')
#reader=csv.DictReader(file_course,delimiter=',')
#list_course=[]
#for row in reader:
#    list_course.append({'course':row['COURSE'].split(",")})

#file_course.close

##excel student record
#file_record=open('D:/Users/Camille/OneDrive/Documents/Imt 2020-2021/codev/donnees/student.record.csv','r')
#reader=csv.DictReader(file_record,delimiter=',')

#list_record=[]
#for row in reader:
    #list_record.append({'record':row['RECORD'].split(",")})

#file_record.close

##test
#print(list_course[2])
#print(type(list_course[54]["course"]))
#print(list_record[0])
#print(len(list_course))
#print(len(list_record))
################################################################################################################################
################################################################################################################################

## création des différentes routes pour les différentes pages de notre DASHBOARD
## une fois que le programme python est lancé dans l'invite de commande
## il suffit d'ouvrir un navigateur web et d'entrer l'URL donné par l'invite de commande puis le chemin des pages ci dessous

## page principale
@school.route('/dashboard/')
def effectif():
    m=render_template("dash.html")
    return m

## page avec le graphe "last act test"
@school.route('/dashboard/gpa/')
def gpa():
    m=render_template("gpa.html")
    return m

##page pour la matière MATH
##(cette page est accessible en rentrant l'url complète ou à partir de la page principale en cliquant sur la bulle
## correspondant à la matière MATH (voir script dash.html))
@school.route('/dashboard/MATH/')
def MATH():
    m=render_template("MATH.html")
    return m

## page pour la matière PHYSCIS
@school.route('/dashboard/PHYSICS/')
def PHYSICS():
    m=render_template("PHYSICS.html")
    return m

##on lance le serveur 
if __name__ == '__main__':
    school.run(host='0.0.0.0', port=8080)
