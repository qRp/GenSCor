# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename
import tkinter.ttk as ttk
import codecs
import datetime
from pprint import pprint
import cProfile
import re
import threading
import os
import ntpath

#from pycallgraph import PyCallGraph
#from pycallgraph.output import GraphvizOutput

################################################################################
# Developped by Quentin Riché Piotaix : quentin.riche.piotaix@univ-poitiers.fr #
#     GenSCor is a free software: you can redistribute it and/or modify        #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details                               #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.    #
#                                                                              #
################################################################################

#######
#Gestion de la langue
L = {"L_open": {'EN':"Open",'FR':"Ouvrir"},
    "L_refresh":{'EN':"Refresh",'FR':"Rafraichir"},
    "L_Coeff":{'EN':"Coefficient",'FR':"Coefficient"},
    "L_if":{'EN':"If",'FR':"Si"},
    "L_column":{'EN':"column",'FR':"colonne"},
    "L_operator":{'EN':"operator",'FR':"opérateur"},
    "L_ref_value":{'EN':"reference value",'FR':"valeur référence"},
    "L_then":{'EN':"then",'FR':"alors"},
    "L_direction":{'EN':"direction",'FR':"direction"},
    "L_score_of":{'EN':"score by",'FR':"score de"},
    "L_score_value":{'EN':"Score value",'FR':"valeur score"},
    "L_remove":{'EN':"Remove",'FR':"Supprimer"},
    "L_save_as":{'EN':"Save as...",'FR':"Enregistrer sous..."},
    "L_text":{'EN':"text files",'FR':"fichiers texte"},
    "L_all":{'EN':"all files",'FR':"tous les fichiers"},
    "L_export_as":{'EN':"Export as...",'FR':"Exporter sous..."},
    "L_browse":{'EN':"Browse",'FR':"Parcourir"},
    "L_csv":{'EN':"csv files",'FR':"fichiers csv"},
    "L_data_param":{'EN':"Data parameters",'FR':"Paramètres de données"},
    "L_separator":{'EN':"Separator : ",'FR':"Séparateur : "},
    "L_header":{'EN':"There is a header",'FR':"Présence d'un entête"},
    "L_jump_lines":{'EN':"Number of lines to jump",'FR':"Nombre de lignes à sauter"},
    "L_try":{'EN':"Try",'FR':"Essayer"},
    "L_save":{'EN':"Save",'FR':"Enregistrer"},
    "L_name":{'EN':"my soft name",'FR':"ajouter un nom ici"},
    "L_welcome":{'EN':"Welcome",'FR':"Bienvenue"},
    "L_foot":{'EN':"This is a footer",'FR':"Ceci est un pied de page"},
    "L_load_data":{'EN':"Load data",'FR':"Charger des données"},
    "L_export":{'EN':"Export",'FR':"Export"},
    "L_load_rules":{'EN':"Load rules",'FR':"Charger des règles"},
    "L_undo":{'EN':"Undo",'FR':"Annuler"},
    "L_quit":{'EN':"Quit",'FR':"Quitter"},
    "L_file":{'EN':"File",'FR':"Fichier"},
    "L_edit":{'EN':"Edit",'FR':"Edition"},
    "L_add_1":{'EN':"Add 1 line",'FR':"Ajouter 1 ligne"},
    "L_add_3":{'EN':"Add 3 lines",'FR':"Ajouter 3 lignes"},
    "L_add_5":{'EN':"Add 5 lines",'FR':"Ajouter 5 lignes"},
    "L_print_increasing":{'EN':"sort increasing",'FR':"Tri croissant"},
    "L_print_decreasing":{'EN':"sort decreasing",'FR':"Tri décroissant"},
    "L_parameters":{'EN':"Parameters",'FR':"Paramètres"},
    "L_opening_parameters":{'EN':"Opening parameters",'FR':"Paramètres d'ouverture"},
    "Contains":{'EN':"Contains",'FR':"contient"},
    "Don't contains":{'EN':"Don't contains",'FR':"ne contient pas"},
    "Increase":{'EN':"Increase",'FR':"Augmenter"},
    "Decrease":{'EN':"Decrease",'FR':"Diminuer"},
    "L_no_visual":{'EN':"No visual mode",'FR':"Mode non visuel"},
    "Browse save":{'EN':"Browse saves",'FR':"Parcourir les sauvegardes"},
    "Browse data":{'EN':"Browse data", 'FR':"Parcourir les données"},
    "L_variant":{'EN':"variant files",'FR':"Fichier variant"},
    "L_multiple_files":{'EN':"Choose files",'FR':"Choisissez des fichiers"},
    "L_go":{'EN':"Go !",'FR':"Lancer !"},
    "multiple":{'EN':"Multiple",'FR':"Multiple"},
    "add_multiple":{'EN':"Add multiple",'FR':"Ajouter multiple"},
    "L_all_multiple":{'EN':"All the lines below are true", 'FR':"Toutes les lignes ci dessous sont vraies"},
    "L_add_condition":{'EN':"Add condition",'FR':"Ajouter une condition"},
    "next_colonne":{'EN':"Print Next columns", 'FR':"Afficher les colonnes suivantes"},
    "lang_label":{'EN':"Language",'FR':"Langage"},
    "mode_fenetre":{'EN':"Windows use",'FR':"Mode de fenêtre"},
    "mode_fenetre_on":{'EN':"Use different windows",'FR':"Utiliser plusieurs fenêtres"},
    "quit":{'EN':"Quit",'FR':"Quitter"},
    "Do you want to quit?":{'EN':"Do you want to quit?",'FR':"Voulez vous vraiment quitter ?"},
    "L_or":{'EN':"OR",'FR':"OU"},
    "L_add_or_condition":{'EN':"Add OR condition",'FR':"Ajouter condition OU"},
    "L_add_or_group":{'EN':"Add new OR group", 'FR':"Ajouter nouveau groupe OU"},
    "L_validate":{'EN':"Validate",'FR':"Valider"},
    "L_ignore":{'EN':"Ignore this column",'FR':"Ignorer la colonne"},
    "OR_bloc":{'EN':"OR bloc ",'FR':"Bloc OU "}

}


#######
#Variables globales
line_list=[]
score_ligne={}
rules={}
no_vis_filenames=()
no_vis_data=()
no_visual_option="keep"
#ontologie=open("ontology.txt", "r+")
#bases_dict={}
nextline=1
date=""
filename=""
Prompt_Dropdown_Ok_Cancel_Selection = None
#separateur="\t"
nombre_ligne=0
page=1
seuil_affichage=15
seuil_colonne=15
seuil_data=100
#entete="oui"
affichage="decroissant"
importance_var={}
colonne_var={}
operateur_var={}
valeur_var={}
sens_var={}
score_var={}
colonne_hash={}
values_hash={}
values_widget={}
operateur_widget={}
colonne_widget={}
bouton_supprimer={}
seuil_data=100
lang='EN'
#mode_fenetre=True


########
#Fonctions classiques
##########
#FONCTION MOTEUR
#Fonction pour quitter le program, obvious

def open_filename():
	print(datetime.datetime.now(),"open_filename")
	global line_list
	global firstline
	global nombre_ligne
	global filename
	global separateur
	global lang
	line_list=[]
	linesplit=[]
	#try:
	#with codecs.open(filename,'rb',encoding='utf-8-sig', errors="ignore") as file:
	filename=askopenfilename(title=L["L_open"][lang], defaultextension="*.csv", filetypes=[("Tous","*"),("CSV","*.csv"),("Variants","*.variant")], parent=root_window)
	file=open(filename,'r',encoding='utf-8-sig')
	cpt=0
	for l in file:
		if cpt==nombre_ligne:
			line=l.rstrip()
			firstline=line
		elif cpt > nombre_ligne:
			line=l.rstrip()
			temp=tk.IntVar()
			temp.set(0)
			tup=[line, temp]
			line_list.append(tup)
			linesplit.append(line.split(separateur))
		cpt+=1
	set_title(filename)
	populate_footpage()
	create_set_from_data(linesplit)
	afficher_module("first")
	#except:
	#	print("mauvais chargement")
	#	afficher_module("blank")

def create_set_from_data(linesplit):
	print(datetime.datetime.now(),"create_set_from_data")
	global line_list
	global firstline
	firstlist=firstline.split(separateur)
	for i in range(len(firstlist)-1):
		#print(i)
		myset=set([row[i] for row in linesplit])
		values_hash[firstlist[i]]=myset

def Prompt_Dropdown_Ok_Cancel(title, message, options, default_selection=0):
    master = tk.Tk()
    master.title(title)
    var = tk.StringVar(master)
    var.set(options[default_selection]) # default value
    l = tk.Label(master, text=message)
    l.pack()
    w = tk.OptionMenu(master, var, *options)
    w.pack(fill=tk.BOTH, expand=1)

    def ok():
        global Prompt_Dropdown_Ok_Cancel_Selection
        Prompt_Dropdown_Ok_Cancel_Selection = str(var.get())
        master.quit()
        master.destroy()

    def cancel():
        master.quit()
        master.destroy()

    button = tk.Button(master, text=L["L_validate"][lang], command=ok)
    button.pack(side=tk.LEFT)
    b2 = tk.Button(master, text=L["L_ignore"][lang], command=cancel)
    b2.pack(side=tk.LEFT)
    master.mainloop()
    return Prompt_Dropdown_Ok_Cancel_Selection

def tri():
	print(datetime.datetime.now(),"tri")
	global affichage
	global line_list
	if affichage == "croissant":
		print("tri croissant !")
		line_list.sort(key=lambda x: x[1].get(), reverse=False)
	else:
		print("Tri decroissant")
		line_list.sort(key=lambda x: x[1].get(), reverse=True)
	print("fin_tri")
	return 0

def afficher_data_thread(page_set, fenetre=0, separateur_widget=0, nombre_ligne_widget=0):
	#global afficher_thread
	#afficher_thread = threading.Thread(target= lambda : afficher_data(page_set, fenetre, separateur_widget, nombre_ligne_widget))
	#afficher_thread.daemon=True
	#afficher_thread.start()
	#root_window.after(20,check_afficher_thread)
	afficher_data(page_set, fenetre, separateur_widget, nombre_ligne_widget)

def check_afficher_thread():
	if afficher_thread.is_alive():
		root_window.after(20,check_afficher_thread)
	else :
		print("fin afficher thread")

def afficher_data(page_set, fenetre=0, separateur_widget=0, nombre_ligne_widget=0):
	print(datetime.datetime.now(),"afficher data")
	def callback():
		global page
		global seuil_affichage
		global separateur
		global entete
		global affichage
		global line_list
		global firstline
		global nombre_ligne
		global lang
		global zut
		global seuil_colonne
		global seuil_data
		if separateur_widget != 0 :
			separateur = separateur_widget.get()
			nombre_ligne = nombre_ligne_widget.get()
			entete = zut.get()
		page = page_set
		shift=len(importance_var)+1+100
		print(datetime.datetime.now(),"page",page)
		for label in frame_b.grid_slaves():
			if int(label.grid_info()["row"]) > len(importance_var)+15:
				label.destroy()
		#si le separateur est une tabulation ou un espace, cas particulier
		if separateur == "tabulation" or separateur=="tab" or separateur=="\t":
			separateur="\t"
		if separateur == "espace" or separateur == "space" or separateur == " ":
			separateur=" "
		#on récupère la première ligne
		try :
				first=firstline.split(separateur)
		except :
			first=[]
		#print(datetime.datetime.now(),"gestion séparateur")
		#on découpe la première ligne en colonnes d'entrée
		bouton_refresh = tk.Button(frame_b, text=L["L_refresh"][lang], command= lambda : rafraichir())
		bouton_refresh.grid(row=0+shift,column=0)

		for i in range(len(first)):
			colonne_name=tk.Entry(frame_b, textvariable=first[i], width=15)
			colonne_name.delete(0,tk.END)
			#s'il y a un entete, on mets les noms qui vont bien
			if entete=="oui":
				colonne_name.delete(0,tk.END)
				colonne_name.insert(0, first[i])
			else :
				colonne_name.delete(0,tk.END)
				colonne_name.insert(0,i)
			colonne_name.grid(row=0+shift, column=i+1, sticky=tk.NW)
		#on gère le décalage (saut de ligne + entete)
		shift1=int(nombre_ligne)
		#on rempli le tableau
		#print(datetime.datetime.now(),"gestion header")
		stop=0
		#print(datetime.datetime.now(),"avant tri")

		#print(datetime.datetime.now(),"après tri, avant affichage")
		for i in range((page_set-1)*seuil_affichage,(page_set-1)*seuil_affichage+seuil_affichage,1):
		#for i in range(len(line_list) - shift1 +page_set*seuil_affichage):
			#calcul_score(line_list)
			if stop > seuil_affichage:
				break
			else:
				stop=stop+1
			try :
				liste=line_list[i+shift1][0].split(separateur)
			except:
				break
			for j in range(len(liste)):
				if j>seuil_colonne:
					bouton_next_colonne = tk.Button(frame_b, text=L["next_colonne"][lang], command = lambda : next_colonne())
					bouton_next_colonne.grid(row=shift+4, column=j+2)
					break
				score_label = tk.Label(frame_b, textvariable=line_list[i+shift1][1], text="test")
				score_label.grid(row=i+shift+2, column=0, sticky=tk.NW)
				if len(liste[j]) > seuil_data :
					to_print=liste[j][:seuil_data]
				else :
					to_print = liste[j]
				data_label=tk.Label(frame_b, text=to_print)
				data_label.grid(column=j+1, row=i+2+shift, padx=2, pady=2, ipadx=2, ipady=2, sticky=tk.NW)
		label_fin=tk.Label(frame_b, text="fin")
		label_fin.grid(row=120+shift,column=0)
		#frame_b.update_idletasks()
		#print(datetime.datetime.now(),"après affichage")
		naviguation_pied_page()
		#print(datetime.datetime.now(),"pied de page")
	root_window.after_idle(callback)
	#print(line_list[0][0], "ligne")
	#print(line_list[0][1].get(), "score")
	print(datetime.datetime.now(),"Fin d'affichage")

def next_colonne():
	global seuil_colonne
	seuil_colonne+=15
	afficher_module("redraw")

def rafraichir():
	print(datetime.datetime.now(),"rafraichir")
	calculer_score("complet")
	tri()
	afficher_data_thread(1)

def premiere_ligne():
	global lang
	print(datetime.datetime.now(),"premiere_ligne")
	#importance
	importance_label = tk.Label(frame_t, text=L["L_Coeff"][lang], bg="#dfdfdf")
	importance_label.grid(column=1, row=0, sticky=tk.NW)
	si_label = tk.Label(frame_t, text=L["L_if"][lang], bg="#dfdfdf")
	si_label.grid(column=2, row=0, sticky=tk.NW)
	colonne_label = tk.Label(frame_t, text=L["L_column"][lang], bg="#dfdfdf")
	colonne_label.grid(column=3, row=0, sticky=tk.NW)
	operateur_label = tk.Label(frame_t, text=L["L_operator"][lang], bg="#dfdfdf")
	operateur_label.grid(column=4, row=0, sticky=tk.NW)
	valeur_label = tk.Label(frame_t, text=L["L_ref_value"][lang], bg="#dfdfdf")
	valeur_label.grid(column=5, row=0, sticky=tk.NW)
	alors_label = tk.Label(frame_t, text=L["L_then"][lang], bg="#dfdfdf")
	alors_label.grid(column=6, row=0, sticky=tk.NW)
	sens_label = tk.Label(frame_t, text=L["L_direction"][lang], bg="#dfdfdf")
	sens_label.grid(column=7, row=0, sticky=tk.NW)
	score_de_label = tk.Label(frame_t, text=L["L_score_of"][lang], bg="#dfdfdf")
	score_de_label.grid(column=8, row=0, sticky=tk.NW)
	valeur_score_label = tk.Label(frame_t, text=L["L_score_value"][lang], bg="#dfdfdf")
	valeur_score_label.grid(column=9, row=0, sticky=tk.NW)
	suppression_label = tk.Label(frame_t, text=L["L_remove"][lang], bg="#dfdfdf")
	suppression_label.grid(column=10, row=0, sticky=tk.NW)

def changement_importance(row):
	global importance_var
	print(datetime.datetime.now(),"changement_importance")
	module_ligne(row)
	calculer_score("visuel")

def module_ligne_simple(row):
	global separateur
	global firstline
	global colonne_hash
	global values_hash
	global values_widget
	global colonne_widget
	global operateur_widget
	global bouton_supprimer
	global lang
	global line_shift
	#fonction qui affiche une ligne, et qui la setup si c'est la première fois
	print(datetime.datetime.now(),"module ligne simple")
	#importance
	OPTIONS_importance = ["0","1","2","3","4","5"]
	if rules[row]["importance"].get() == "":
		rules[row]["importance"].set(OPTIONS_importance[1])


	if rules[row]["importance"].get() == "0" :
		font="-overstrike 1 "
		color="tomato2"
	elif rules[row]["importance"].get() == "1" :
		font="-overstrike 0"
		color="sky blue"
	elif rules[row]["importance"].get() == "2" :
		font="-overstrike 0"
		color="deep sky blue"
	elif rules[row]["importance"].get() == "3" :
		font="-overstrike 0"
		color="DeepSkyBlue2"
	elif rules[row]["importance"].get() == "4" :
		font="-overstrike 0"
		color="DeepSkyBlue3"
	elif rules[row]["importance"].get() == "5" :
		font="-overstrike 0"
		color="DeepSkyBlue4"
	#else :
	#	importance_var[row].set(importance)
	importance_widget = tk.OptionMenu(frame_t, rules[row]['importance'], *OPTIONS_importance,
	 command= lambda test="list value", row=row, valeur=rules[row]["importance"]: changement_importance(row))
	importance_widget.configure(font=font, bg=color)
	#importance_var[row].trace('r', lambda row=row, test=1, toto=2 :changement_importance(row,test,toto))

	importance_widget.grid(column=1,row=row)
	#label si
	si_label = tk.Label(frame_t, text=L["L_if"][lang], bg="#dfdfdf")
	si_label.configure(font=font, bg=color)
	si_label.grid(column=2, row=row, sticky=tk.NW)
	#colonne
	OPTIONS_colonne=[]
	first=firstline.split(separateur)
	for i in range(len(first)):
		colonne_hash[first[i]]=i
		OPTIONS_colonne.append(first[i])
	if  rules[row]["colonne"][0].get() == "" :
		rules[row]["colonne"][0].set(OPTIONS_colonne[0])
	#else:
	#	colonne_var[row].set(colonne)
	colonne_widget[row]={}
	colonne_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["colonne"][0], *OPTIONS_colonne, command = lambda valeur="list valeur": colonne_wrapper(row))
	colonne_widget[row][i].configure(font=font, bg=color)
	colonne_widget[row][i].grid(column=3,row=row, sticky=tk.NW)
	#operateur
	OPTIONS_operateur = ["=","≠",">","<","≤","≥",L["Contains"][lang],L["Don't contains"][lang]]
	if rules[row]["operateur"][0].get() == "" :
		rules[row]["operateur"][0].set(OPTIONS_operateur[0])
	#else :
	#	operateur_var[row].set(operateur)
	operateur_widget[row]={}
	operateur_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["operateur"][0], *OPTIONS_operateur, command = lambda valeur="list valeur": calculer_score("visuel"))
	operateur_widget[row][i].configure(font=font, bg=color)
	operateur_widget[row][i].grid(column=4, row=row, sticky=tk.NW)
	#valeur
	if rules[row]["values"][0].get() == "" :
		rules[row]["values"][0].set(0)
	#print(values_hash[colonne_var[row].get()])

	values_widget[row]={}
	values_widget[row][0] = ttk.Combobox(frame_t, textvariable=rules[row]["values"][0], validatecommand= lambda : OnValidate, validate="all")
	values=list(sorted(values_hash[rules[row]["colonne"][0].get()]))
	values_widget[row][0].config(values=values)
	#values_widget.configure(font=font, bg=color)
	values_widget[row][0].grid(column=5,row=row, pady=2)
	#alors
	alors_label = tk.Label(frame_t, text=L["L_then"][lang], bg="#dfdfdf")
	alors_label.configure(font=font, bg=color)
	alors_label.grid(column=6, row=row, sticky=tk.NW)
	#sens
	OPTIONS_sens = [L["Increase"][lang],L["Decrease"][lang]]
	if rules[row]["sens"].get() == "" :
		rules[row]["sens"].set(OPTIONS_sens[0])
	#else :
	#	sens_var[row].set(sens)
	sens_widget = tk.OptionMenu(frame_t,rules[row]["sens"], *OPTIONS_sens, command = lambda valeur="list valeur": calculer_score("visuel"))
	sens_widget.configure(font=font, bg=color)
	sens_widget.grid(column=7, row=row, sticky=tk.NW)
	#score
	score_de_label = tk.Label(frame_t, text=L["L_score_of"][lang], bg="#dfdfdf")
	score_de_label.configure(font=font, bg=color)
	score_de_label.grid(column=8, row=row, sticky=tk.NW)
	#valeur score
	if rules[row]["score"].get() == "":
		rules[row]["score"].set(0)
	score_widget = tk.Entry(frame_t, textvariable=rules[row]["score"], width=3, validatecommand= lambda : OnValidate, validate="all")
	score_widget.configure(font=font, bg=color)
	score_widget.grid(column=9, row=row, sticky=tk.NW)
	#boutn suppression
	bouton_supprimer = tk.Button(frame_t, text=L["L_remove"][lang], command= lambda : supprimer_ligne(row))
	bouton_supprimer.grid(column=10, row=row, sticky=tk.NW)

def module_ligne_multiple(row):
	global separateur
	global firstline
	global colonne_hash
	global values_hash
	global values_widget
	global colonne_widget
	global operateur_widget
	global bouton_supprimer
	global lang
	global line_shift
	#fonction qui affiche une ligne, et qui la setup si c'est la première fois
	print(datetime.datetime.now(),"module ligne multiple")
	#importance
	#première ligne
	OPTIONS_importance = ["0","1","2","3","4","5"]
	if rules[row]["importance"].get() == "":
		rules[row]["importance"].set(OPTIONS_importance[1])


	if rules[row]["importance"].get() == "0" :
		font="-overstrike 1 "
		color="tomato2"
	elif rules[row]["importance"].get() == "1" :
		font="-overstrike 0"
		color="sky blue"
	elif rules[row]["importance"].get() == "2" :
		font="-overstrike 0"
		color="deep sky blue"
	elif rules[row]["importance"].get() == "3" :
		font="-overstrike 0"
		color="DeepSkyBlue2"
	elif rules[row]["importance"].get() == "4" :
		font="-overstrike 0"
		color="DeepSkyBlue3"
	elif rules[row]["importance"].get() == "5" :
		font="-overstrike 0"
		color="DeepSkyBlue4"
	importance_widget = tk.OptionMenu(frame_t, rules[row]['importance'], *OPTIONS_importance,
	 command= lambda test="list value", row=row, valeur=rules[row]["importance"]: changement_importance(row))
	importance_widget.configure(font=font, bg=color)
	importance_widget.grid(column=1,row=row)
	#label si
	si_label = tk.Label(frame_t, text=L["L_if"][lang])
	si_label.configure(font=font, bg=color)
	si_label.grid(column=2, row=row, sticky=tk.NW)
	all_label = tk.Label(frame_t, text=L["L_all_multiple"][lang])
	all_label.configure(font=font, bg=color)
	all_label.grid(column=3, row=row, sticky=tk.NW)
	#alors
	alors_label = tk.Label(frame_t, text=L["L_then"][lang], bg="#dfdfdf")
	alors_label.configure(font=font, bg=color)
	alors_label.grid(column=6, row=row, sticky=tk.NW)
	#sens
	OPTIONS_sens = [L["Increase"][lang],L["Decrease"][lang]]
	if rules[row]["sens"].get() == "" :
		rules[row]["sens"].set(OPTIONS_sens[0])
	#else :
	#	sens_var[row].set(sens)
	sens_widget = tk.OptionMenu(frame_t,rules[row]["sens"], *OPTIONS_sens, command = lambda valeur="list valeur": calculer_score("visuel"))
	sens_widget.configure(font=font, bg=color)
	sens_widget.grid(column=7, row=row, sticky=tk.NW)
	#score
	score_de_label = tk.Label(frame_t, text=L["L_score_of"][lang], bg="#dfdfdf")
	score_de_label.configure(font=font, bg=color)
	score_de_label.grid(column=8, row=row, sticky=tk.NW)
	#valeur score
	if rules[row]["score"].get() == "" :
		rules[row]["score"].set(0)
	score_widget = tk.Entry(frame_t, textvariable=rules[row]["score"], width=3, validatecommand= lambda : OnValidate, validate="all")
	score_widget.configure(font=font, bg=color)
	score_widget.grid(column=9, row=row, sticky=tk.NW)


	#boucle sur les colonnes
	colonne_widget[row]={}
	operateur_widget[row]={}
	values_widget[row]={}
	bouton_supprimer={}
	for i in range(len(rules[row]["colonne"])):
		#colonne
		if rules[row]["type"][i]=="AND" :
			OPTIONS_colonne=[]
			first=firstline.split(separateur)
			for j in range(len(first)):
				colonne_hash[first[j]]=j
				OPTIONS_colonne.append(first[j])
			if rules[row]["colonne"][i].get() == "" :
				rules[row]["colonne"][i].set(OPTIONS_colonne[0])
			colonne_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["colonne"][i], *OPTIONS_colonne, command = lambda valeur="list valeur", row=row, i=i : colonne_wrapper(row, i))
			colonne_widget[row][i].configure(font=font, bg=color)
			colonne_widget[row][i].grid(column=3,row=row+i+1, sticky=tk.NW)
		#operateur
			OPTIONS_operateur = ["=","≠",">","<","≤","≥",L["Contains"][lang],L["Don't contains"][lang]]
			if rules[row]["operateur"][i].get() == "" :
				rules[row]["operateur"][i].set(OPTIONS_operateur[0])

			operateur_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["operateur"][i], *OPTIONS_operateur, command = lambda valeur="list valeur": calculer_score("visuel"))
			operateur_widget[row][i].configure(font=font, bg=color)
			operateur_widget[row][i].grid(column=4, row=row+i+1, sticky=tk.NW)
		#valeur
			if rules[row]["values"][i].get() == "" :
				rules[row]["values"][i].set(0)

			values_widget[row][i] = ttk.Combobox(frame_t, textvariable=rules[row]["values"][i], validatecommand= lambda : OnValidate, validate="all")
			values=list(sorted(values_hash[rules[row]["colonne"][i].get()]))
			values_widget[row][i].config(values=values)
			values_widget[row][i].grid(column=5,row=row+i+1, pady=2)

			bouton_supprimer[i] = tk.Button(frame_t, text=L["L_remove"][lang], command= lambda i=i : supprimer_condition(row, i))
			bouton_supprimer[i].grid(column=6, row=row+i+1, sticky=tk.NW)

		elif rules[row]["type"][i] == "OR" :
			or_label = tk.Label(frame_t, text=L["OR_bloc"][lang]+str(rules[row]["nbre"][i]))
			or_label.configure(font=font, bg=color)
			or_label.grid(column=3, row=row+i+1, sticky=tk.NW)
			OPTIONS_colonne=[]
			first=firstline.split(separateur)
			for j in range(len(first)):
				colonne_hash[first[j]]=j
				OPTIONS_colonne.append(first[j])
			if rules[row]["colonne"][i].get() == "" :
				rules[row]["colonne"][i].set(OPTIONS_colonne[0])
			colonne_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["colonne"][i], *OPTIONS_colonne, command = lambda valeur="list valeur", row=row, i=i : colonne_wrapper(row, i))
			colonne_widget[row][i].configure(font=font, bg=color)
			colonne_widget[row][i].grid(column=4,row=row+i+1, sticky=tk.NW)
		#operateur
			OPTIONS_operateur = ["=","≠",">","<","≤","≥",L["Contains"][lang],L["Don't contains"][lang]]
			if rules[row]["operateur"][i].get() == "" :
				rules[row]["operateur"][i].set(OPTIONS_operateur[0])

			operateur_widget[row][i] = tk.OptionMenu(frame_t, rules[row]["operateur"][i], *OPTIONS_operateur, command = lambda valeur="list valeur": calculer_score("visuel"))
			operateur_widget[row][i].configure(font=font, bg=color)
			operateur_widget[row][i].grid(column=5, row=row+i+1, sticky=tk.NW)
		#valeur
			if rules[row]["values"][i].get() == "" :
				rules[row]["values"][i].set(0)

			values_widget[row][i] = ttk.Combobox(frame_t, textvariable=rules[row]["values"][i], validatecommand= lambda : OnValidate, validate="all")
			values=list(sorted(values_hash[rules[row]["colonne"][i].get()]))
			values_widget[row][i].config(values=values)
			values_widget[row][i].grid(column=6,row=row+i+1, pady=2)

			bouton_supprimer[i] = tk.Button(frame_t, text=L["L_remove"][lang], command= lambda i=i : supprimer_condition(row, i))
			bouton_supprimer[i].grid(column=7, row=row+i+1, sticky=tk.NW)

			bouton_ajouter_ou = tk.Button(frame_t, text=L["L_add_or_condition"][lang], command= lambda i=i : ajouter_condition_ou(row, rules[row]["nbre"][i]))
			bouton_ajouter_ou.grid(column=8, row=row+i+1, sticky=tk.NW)

	bouton_ajouter = tk.Button(frame_t, text=L["L_add_condition"][lang], command= lambda : ajouter_condition(row))
	bouton_ajouter.grid(column=3, row=row+i+2, sticky=tk.NW)
	bouton_ajouter_ou_group = tk.Button(frame_t, text=L["L_add_or_group"][lang], command= lambda : ajouter_or_group(row))
	bouton_ajouter_ou_group.grid(column=4, row=row+i+2, sticky=tk.NW)

def module_ligne(row):
	print(datetime.datetime.now(),"module_ligne")
	if "colonne" not in rules[row].keys() :
		module_ligne_simple(row)
	elif len(rules[row]["colonne"]) <= 1:
		#print("mode normal")
		#print(len(rules[row]["colonne"]))
		#pprint(rules[row]["colonne"])
		module_ligne_simple(row)
	elif len(rules[row]["colonne"]) > 1:
		#print("mode multiple")
		#print(len(rules[row]["colonne"]))
		#pprint(rules[row]["colonne"])
		module_ligne_multiple(row)

def colonne_wrapper(row, i=0):
	print(datetime.datetime.now(),"colonne_wrapper")
	global values_widget
	print("i : ",i)
	print("row : ",row)
	print(rules[row]["colonne"][i].get())
	values=list(sorted(values_hash[rules[row]["colonne"][i].get()]))
	values_widget[row][i].config(values=values)
	calculer_score("visuel")

def OnValidate():
	print(datetime.datetime.now(),"onvalidate")
	calculer_score("visuel")
	return True

def ajouter_condition(row):
	global rules
	global nextline
	nbre=len(rules[row]["colonne"])
	rules[row]["type"].append("AND")
	rules[row]["nbre"].append(0)
	rules[row]["colonne"].append(tk.StringVar())
	rules[row]["colonne"][nbre].set("")
	rules[row]["operateur"].append(tk.StringVar())
	rules[row]["operateur"][nbre].set("")
	rules[row]["values"].append(tk.StringVar())
	rules[row]["values"][nbre].set("")
	#decaler ligne suivante
	for i in sorted(rules.keys(), reverse=True):
		if i > row :
			rules[i+1]=rules[i]
			del rules[i]
	nextline+=1

	afficher_module("ajouter", row)

def supprimer_condition(row, i):
	global rules
	del rules[row]["colonne"][i]
	del rules[row]["values"][i]
	del rules[row]["operateur"][i]
	del rules[row]["type"][i]
	del rules[row]["nbre"][i]
	afficher_module("ajouter", row)

def ajouter_or_group(row):
	global rules
	num_max=max(rules[row]["nbre"])
	ajouter_condition_ou(row,num_max+1)
	ajouter_condition_ou(row,num_max+1)


def ajouter_condition_ou(row, num=0):
	global rules
	global nextline
	nbre=len(rules[row]["colonne"])	 
	rules[row]["type"].append("OR")
	rules[row]["nbre"].append(num)
	rules[row]["colonne"].append(tk.StringVar())
	rules[row]["colonne"][nbre].set("")
	rules[row]["operateur"].append(tk.StringVar())
	rules[row]["operateur"][nbre].set("")
	rules[row]["values"].append(tk.StringVar())
	rules[row]["values"][nbre].set("")
	#decaler ligne suivante
	for i in sorted(rules.keys(), reverse=True):
		if i > row :
			rules[i+1]=rules[i]
			del rules[i]
	nextline+=1

	pprint(rules)
	afficher_module("ajouter", row)


def supprimer_ligne(row):
	print(datetime.datetime.now(),"supprimer_ligne")
	global rules
	global bouton_supprimer
	global lang
	global nextline
	nbre_ligne=len(importance_var)
	#print(nbre_ligne)
	#print("Supprimer : row = ", row)
	sauvegarde(1)
	for label in frame_t.grid_slaves():
		if int(label.grid_info()["row"]) == row :
			label.destroy()
	del rules[row]
	afficher_module("supprimer")

def ajouter_ligne(nbre):
	global importance_var
	global nextline
	print(datetime.datetime.now(),"ajouter_ligne")
	nbre_ligne = len(importance_var.keys())
	for i in range(nbre):
		rules[nextline]={}
		rules[nextline]["colonne"]=[]
		rules[nextline]["operateur"]=[]
		rules[nextline]["values"]=[]
		rules[nextline]["type"]=[]
		rules[nextline]["nbre"]=[]
		rules[nextline]["importance"]=tk.StringVar()
		rules[nextline]["importance"].set("")
		rules[nextline]["sens"]=tk.StringVar()
		rules[nextline]["sens"].set("")
		rules[nextline]["score"]=tk.StringVar()
		rules[nextline]["score"].set("")
		rules[nextline]["colonne"].append(tk.StringVar())
		rules[nextline]["colonne"][0].set("")
		rules[nextline]["operateur"].append(tk.StringVar())
		rules[nextline]["operateur"][0].set("")
		rules[nextline]["values"].append(tk.StringVar())
		rules[nextline]["values"][0].set("")
		rules[nextline]["type"].append("BASE")
		rules[nextline]["nbre"].append(0)
		afficher_module("ajouter", nextline)
		nextline+=1

def ajouter_multiple():
	global importance_var
	global nextline
	print(datetime.datetime.now(),"ajouter multiple")
	nbre_ligne = len(importance_var.keys())
	rules[nextline]={}
	rules[nextline]["type"]=[]
	rules[nextline]["nbre"]=[]
	rules[nextline]["colonne"]=[]
	rules[nextline]["operateur"]=[]
	rules[nextline]["values"]=[]
	rules[nextline]["importance"]=tk.StringVar()
	rules[nextline]["importance"].set("")
	rules[nextline]["sens"]=tk.StringVar()
	rules[nextline]["sens"].set("")
	rules[nextline]["score"]=tk.StringVar()
	rules[nextline]["score"].set("")
	rules[nextline]["colonne"].append(tk.StringVar())
	rules[nextline]["colonne"].append(tk.StringVar())
	rules[nextline]["colonne"][0].set("")
	rules[nextline]["colonne"][1].set("")
	rules[nextline]["operateur"].append(tk.StringVar())
	rules[nextline]["operateur"].append(tk.StringVar())
	rules[nextline]["operateur"][0].set("")
	rules[nextline]["operateur"][1].set("")
	rules[nextline]["values"].append(tk.StringVar())
	rules[nextline]["values"].append(tk.StringVar())
	rules[nextline]["values"][0].set("")
	rules[nextline]["values"][1].set("")
	rules[nextline]["type"].append("AND")
	rules[nextline]["type"].append("AND")
	rules[nextline]["nbre"].append(0)
	rules[nextline]["nbre"].append(0)
	nextline=nextline+4
	afficher_module("ajouter", 1)

def calculer_score(mode="complet"):
	#mode = complet pour toutes les données ou visuel pour les données affichées
	init_score()
	print(datetime.datetime.now(),"Calculer score!")
	global line_list
	global colonne_hash
	global page
	global seuil_affichage
	global rules
	if mode == "complet" :
		start = 0
		end = len(line_list)
	elif mode == "visuel" :
		start = (page-1)*seuil_affichage
		end = seuil_affichage*page
	else :
		start = 0
		end = seuil_affichage
	#pour chaque condition
	#pprint(rules)
	print("start : ", start, " end : ", end)
	for i in rules.keys() :
			#test chaque condition de la liste
		for j in range(start, end, 1) :
			result = test_rule(i, j)
			#si la condition est positive, appliquer le score
			if result :
				score(i,j)

def test_rule(index_rule, index_data):
	#print(datetime.datetime.now(), " test rule")
	global separateur
	global rules
	global line_list
	global lang
	global colonne_hash
	ligne=line_list[index_data][0].split(separateur)
	retour=0
	cpt_condition=0
	hash_retour={}
	#pour chaque condition de la règle
	for i in range(len(rules[index_rule]["colonne"])):
		#si c'est un ou
		try :
			if rules[index_rule]["type"][i]=="OR":
				#cas du ou groupe déja vu
				try :
					hash_retour[rules[index_rule]["nbre"][i]]=hash_retour[rules[index_rule]["nbre"][i]]+calc_rule(i, index_rule, index_data, ligne)
				# cas du premier d'un groupe de ou
				except :
					hash_retour[rules[index_rule]["nbre"][i]]=calc_rule(i,index_rule,index_data, ligne)
			#cas du ET
			else :
				retour=retour+calc_rule(i, index_rule, index_data, ligne)
				cpt_condition+=1
		#cas du OU simple
		except :
			retour=retour+calc_rule(i, index_rule, index_data, ligne)
			cpt_condition+=1

	for i in range(1,len(hash_retour)+1):
		cpt_condition+=1
		if hash_retour[i] > 0 :
			retour+=1
	#si toutes les conditions ont été validées on renvoi vrai
	#if index_rule == 4 :
		#print("retour : ",retour)
	if retour > 0 and retour == cpt_condition:
		#print("True !", retour, len(rules[index_rule]["colonne"]))
		return True
	#sinon on retourne faux
	else :
		#print("False !", retour, len(rules[index_rule]["colonne"]))
		return False

def calc_rule(i, index_rule, index_data, ligne):
	global separateur
	global rules
	global line_list
	global lang
	global colonne_hash
	retour=0
	col_index = int(colonne_hash[rules[index_rule]["colonne"][i].get()])
	#print(ligne)
	#print(col_index)
	try :
		data=float(ligne[col_index])
		value=float(rules[index_rule]["values"][i].get())
		isint=True
	except :
		isint = False
		data=str(ligne[col_index])
		value=str(rules[index_rule]["values"][i].get())
	#print("isint : ", isint)
	#print("valeur ", ligne[col_index])
	#print("rules : ", rules[index_rule]["values"][i].get())
	#cas operateur égal
	if rules[index_rule]["operateur"][i].get() == "=" :
		#print("isint true")
		if data == value:
			#print("OKAY : = ")
			retour=1
	#cas operateur différent
	elif rules[index_rule]["operateur"][i].get() == "≠" :
		if data != value:
			#print("OKAY : dif ")
			retour=1
	#cas operateur inférieur
	elif isint and rules[index_rule]["operateur"][i].get() == "<" :
		if data < value:
			#print("OKAY : inf ")
			retour=1
	#cas operateur supérieur
	elif isint and rules[index_rule]["operateur"][i].get() == ">" :
		if data > value:
			#print("OKAY : supérieur ")
			retour=1
	#cas operateur inférieur ou égal
	elif isint and rules[index_rule]["operateur"][i].get() == "≤" :
		if data <= value:
			#print("OKAY : inférieur ou égal ")
			retour=1
	#cas operateur supérieur ou égal
	elif isint and rules[index_rule]["operateur"][i].get() == "≥" :
		if data >= value:
			#print("OKAY : superieur ou égal ")
			retour=1
	#cas operateur contient
	elif rules[index_rule]["operateur"][i].get() == L["Contains"][lang] :
		if value in data :
			#print("OKAY : contient ")
			retour=1
	#cas operateur ne contient pas
	elif rules[index_rule]["operateur"][i].get() == L["Don't contains"][lang] :
		if value not in data:
			#print("OKAY : ne contient ppas ")
			retour=1
	return retour

def score(index_rule, index_data):
	global rules
	global line_list
	global lang
	#print(datetime.datetime.now(), "score")
	if rules[index_rule]["sens"].get() == L["Increase"][lang] :
		line_list[index_data][1].set(line_list[index_data][1].get()+int(rules[index_rule]["score"].get())*int(rules[index_rule]["importance"].get()))
	elif rules[index_rule]["sens"].get() == L["Decrease"][lang] :
		line_list[index_data][1].set(line_list[index_data][1].get()-int(rules[index_rule]["score"].get())*int(rules[index_rule]["importance"].get()))

def init_score():
	global line_list
	print(datetime.datetime.now(),"init score")
	for i in range(len(line_list)):
		line_list[i][1].set(0)

def undo():
	load("save.txt")

def sauvegarde(auto=0):
	global lang
	print(datetime.datetime.now(),"sauvegarde")
	if auto == 0 :
		#filename=asksaveasfilename()
		filename=asksaveasfilename(title=L["L_save_as"][lang], defaultextension="*.txt", filetypes=[(L["L_text"][lang],"*.txt"),(L["L_all"][lang], "*")], initialfile="save.txt", parent=root_window)
		file=open(filename, 'w', encoding='utf-8')
	elif auto == 1 :
		file=open("save.txt",'w', encoding='utf-8')
	for i in rules.keys():
		file.write(rules[i]["importance"].get()+";")
		for j in rules[i]["colonne"] :
			file.write(j.get()+"/")
		file.write(";")
		for j in rules[i]["operateur"] :
			file.write(j.get()+"/")
		file.write(";")
		for j in rules[i]["values"] :
			file.write(j.get()+"/")
		file.write(";")
		for j in rules[i]["type"] :
			file.write(j+"/")
		file.write(";")
		for j in rules[i]["nbre"] :
			file.write(str(j)+"/")
		

		file.write(";")
		file.write(rules[i]["sens"].get()+";")
		file.write(rules[i]["score"].get())
		file.write("\n")

def export():
	global line_list
	global lang
	global separateur
	print(datetime.datetime.now(),"export")
	filename=asksaveasfilename(title=L["L_export_as"][lang], defaultextension="*.csv", filetypes=[(L["L_csv"][lang],"*.csv"),(L["L_all"][lang],"*")], initialfile="export.csv", parent=root_window)
	file=open(filename,'w',encoding='utf_8')
	file.write("Score"+separateur)
	file.write(firstline+"\n")
	for i in range(len(line_list)):
		file.write(str(line_list[i][1].get())+separateur)
		file.write(line_list[i][0]+"\n")

def verif_colonne(colonne_list,type_list,nbre_list,operateur_list,values_list):
	global colonne_hash
	#pprint(colonne_list)
	todel=[]
	for i in range(len(colonne_list)-1) :
		if colonne_list[i] not in colonne_hash.keys():
			title="Erreur de nom"
			text=colonne_list[i]+" n'existe pas, par quelle colonne souhaitez vous le remplacer ?"
			Prompt_Dropdown_Ok_Cancel_Selection=Prompt_Dropdown_Ok_Cancel(title,text,list(colonne_hash.keys()))
			if Prompt_Dropdown_Ok_Cancel_Selection is not None :
				colonne_list[i]=Prompt_Dropdown_Ok_Cancel_Selection
			else :
				todel.append(i)
	for i in todel :
		del colonne_list[i]
		del operateur_list[i]
		del values_list[i]
		del type_list[i]
		del nbre_list[i]
	#print(colonne_list)
	return colonne_list,type_list,nbre_list,operateur_list,values_list

def load(filename="toask"):
	global lang
	global rules
	global nextline

	print(datetime.datetime.now(),"load")
	if filename == "toask":
		filename=askopenfilename(filetypes =((L["L_all"][lang],"*.*"),(L["L_text"][lang], "*.txt"),(L["L_csv"][lang], "*.csv")), title = L["L_browse"][lang])
	file=open(filename,'r', encoding='utf-8')
	cpt=1
	rules={}
	lines = (line.rstrip() for line in file) # All lines including the blank ones
	lines = (line for line in lines if line) 
	for l in lines :
			#split line 
			#print(l)
			line1=l.rstrip()
			line=line1.strip()
			line = line.encode('utf-8').decode('utf-8-sig')
			line=line.split(';')
			#prep data sctructure
			rules[cpt]={}
			rules[cpt]["colonne"]=[]
			rules[cpt]["operateur"]=[]
			rules[cpt]["values"]=[]
			rules[cpt]["type"]=[]
			rules[cpt]["nbre"]=[]
			rules[cpt]["importance"]=tk.StringVar()
			rules[cpt]["sens"]=tk.StringVar()
			rules[cpt]["score"]=tk.StringVar()
			#set simple ones
			#pprint(line)
			rules[cpt]["importance"].set(line[0])
			rules[cpt]["score"].set(line[7])

			#set sens with the good lang setup
			for key, var_dict in L.items():
				for language, var_name in var_dict.items():
					try :
						if line[6] == var_name :
							if language != lang :
								line[6]=L[key][lang]
					except :
						#empty line
						erreur=1
			rules[cpt]["sens"].set(line[6])
			#setup of the (potentially) multiples ones
			colonne_list = line[1].split("/")
			operateur_list = line[2].split("/")
			values_list = line[3].split("/")
			type_list = line[4].split("/")
			nbre_list = line[5].split("/")
			colonne_list,type_list,nbre_list,operateur_list,values_list=verif_colonne(colonne_list,type_list, nbre_list, operateur_list, values_list);
			for i in range(len(colonne_list)):
				if len(colonne_list[i]) >=1 :
					rules[cpt]["colonne"].append(tk.StringVar())
					rules[cpt]["colonne"][i].set(colonne_list[i])
					#gestion du problème de langue pour les "contains"
					if operateur_list[i] not in ["≠",">","<","≤","≥"]:
						for key, var_dict in L.items():
							for language, var_name in var_dict.items():
								try :
									if var_name == operateur_list[i] :
										if language != lang :
											operateur_list[i]=L[key][lang]
								except :
									#empty line
									erreur=1
				rules[cpt]["operateur"].append(tk.StringVar())
				rules[cpt]["operateur"][i].set(operateur_list[i])
				rules[cpt]["values"].append(tk.StringVar())
				rules[cpt]["values"][i].set(values_list[i])
				rules[cpt]["type"].append(type_list[i])
				try : 
					rules[cpt]["nbre"].append(int(nbre_list[i]))
				except :
					empty=1
			if len(colonne_list) == 1 :
				cpt=cpt+1
			else :
				cpt=cpt+1+len(colonne_list)
	nextline+=cpt
	afficher_module("load")

def charge_score(filename):
	global rules
	file=open(filename,'r', encoding='utf-8')
	cpt=1
	rules={}
	lines = (line.rstrip() for line in file) # All lines including the blank ones
	lines = (line for line in lines if line) 
	for l in lines :
				#split line
			line1=l.rstrip()
			line=line1.strip()
			line = line.encode('utf-8').decode('utf-8-sig')
			line=line.split(';')
			#prep data sctructure
			rules[cpt]={}
			rules[cpt]["colonne"]=[]
			rules[cpt]["operateur"]=[]
			rules[cpt]["values"]=[]
			rules[cpt]["type"]=[]
			rules[cpt]["nbre"]=[]
			rules[cpt]["importance"]=tk.StringVar()
			rules[cpt]["sens"]=tk.StringVar()
			rules[cpt]["score"]=tk.StringVar()
			#set simple ones
			#pprint(line)
			rules[cpt]["importance"].set(line[0])
			rules[cpt]["score"].set(line[7])

			#set sens with the good lang setup
			for key, var_dict in L.items():
				for language, var_name in var_dict.items():
					try :
						if line[6] == var_name :
							if language != lang :
								line[6]=L[key][lang]
					except :
						#empty line
						erreur=1
			rules[cpt]["sens"].set(line[6])
			#setup of the (potentially) multiples ones
			colonne_list = line[1].split("/")
			operateur_list = line[2].split("/")
			values_list = line[3].split("/")
			type_list = line[4].split("/")
			nbre_list = line[5].split("/")
			for i in range(len(colonne_list)):
				if len(colonne_list[i]) >=1 :
					rules[cpt]["colonne"].append(tk.StringVar())
					rules[cpt]["colonne"][i].set(colonne_list[i])
					#gestion du problème de langue pour les "contains"
					if operateur_list[i] not in ["≠",">","<","≤","≥"]:
						for key, var_dict in L.items():
							for language, var_name in var_dict.items():
								try :
									if var_name == operateur_list[i] :
										if language != lang :
											operateur_list[i]=L[key][lang]
								except :
									#empty line
									erreur=1
				rules[cpt]["operateur"].append(tk.StringVar())
				rules[cpt]["operateur"][i].set(operateur_list[i])
				rules[cpt]["values"].append(tk.StringVar())
				rules[cpt]["values"][i].set(values_list[i])
				rules[cpt]["type"].append(type_list[i])
				try : 
					rules[cpt]["nbre"].append(int(nbre_list[i]))
				except :
					empty=1
			if len(colonne_list) == 1 :
				cpt=cpt+1
			else :
				cpt=cpt+1+len(colonne_list)



def load_save_no_visual():
	global no_vis_filenames
	no_vis_filenames=askopenfilenames(filetypes =((L["L_all"][lang],"*.*"),(L["L_text"][lang], "*.txt"),(L["L_csv"][lang], "*.csv")), title = L["L_browse"][lang])
	#label_save.configure(text=no_vis_filenames)

def load_data_no_visual():
	global no_vis_data
	no_vis_data = askopenfilenames(title=L["L_multiple_files"][lang], filetypes = ((L["L_all"][lang],"*.*"),(L["L_csv"][lang], "*.csv"),(L["L_variant"][lang], "*.variant")))
	#label_data.configure(text=no_vis_data)

def no_visual():
	global no_vis_filenames
	global no_vis_data
	global linesplit
	global separateur
	global colonne_hash
	global line_list
	global firstline
	global no_visual_option
	#print("no_visual "+str(len(line_list)))
	for filename in no_vis_data :
		#si on écrit dans le même fichier, on détermine le nom
		if no_visual_option=="keep":
			cpt_file_all=0
			if os.path.isfile(filename+".all_export.tsv"):
				cpt_file_all=1
				while True :
					if os.path.isfile(filename+".all_export("+str(cpt_file_all)+").tsv"):
						cpt_file_all=cpt_file_all+1
					else :
						break
				if cpt_file_all == 0 :
					outfile_name=filename+".all_export.tsv"
				else :
					outfile_name=filename+".all_export("+str(cpt_file_all)+").tsv"
			else :
				outfile_name=filename+".all_export.tsv"
		cpt_file=0
		#print("boucle filename "+str(len(line_list)))
	
		for rule_set in no_vis_filenames :
			#print("boucle rule "+str(len(line_list)))
			charge_score(rule_set)
			nom_save=ntpath.basename(rule_set)
			print("Fichier en cours : "+filename)
			print("Sauvegarde en cours :"+nom_save)
			line_list=[]
			colonne_hash={}
			#print(filename)
			if no_visual_option=="keep" and cpt_file>0 :
				file=open(outfile_name,'rU',encoding='utf-8')
				#print(outfile_name+" ouvert if")
			else :
				file=open(filename,'rU', encoding='utf-8')
				#print(filename+" ouvert else")
			#print("avant le chargement "+str(len(line_list)))
			file_lines = file.readlines()
			file.close()
			#print("file lines : "+str(len(file_lines)))
			cpt=0
			for l in file_lines:
				if cpt==0:
					line=l.rstrip()
					firstline=line
				else :
					line=l.rstrip()
					temp=tk.IntVar()
					temp.set(0)
					tup=[line, temp]
					line_list.append(tup)
				cpt=cpt+1
			#print("compteur "+str(cpt))
			#print("après le CHARGEMENT "+str(len(line_list)))
			first=firstline.split(separateur)
			for i in range(len(first)):
				colonne_hash[first[i]]=i
			print(datetime.datetime.now(),"Avant de lancer le calcul")
			calculer_score("complet")
			#print("après le SCORE "+str(len(line_list)))
			print(datetime.datetime.now(),"après le calcul avant le tri")
			tri()
			print(datetime.datetime.now(),"après le tri")
			#si on écrit dans le même fichier, on l'ouvre juste
			#print("après le tri "+str(len(line_list)))
	
			if no_visual_option == "keep" :
				outfile=open(outfile_name,'w',encoding='utf-8')
				outfile.write("\""+nom_save+"\""+separateur+firstline+"\n")
			#si on écrit dans plusieurs fichiers
			else : 
				cpt_file_split=0
				print(os.path.isfile(filename+".export.tsv"))
				if os.path.isfile(filename+".export.tsv"):
					cpt_file_split=1
					while True :
						if os.path.isfile(filename+nom_save+".export("+str(cpt_file_split)+").tsv"):
							cpt_file_split=cpt_file_split+1
						else :
							break
					if cpt_file_split == 0 :
						outfile=open(filename+nom_save+".export.tsv",'w',encoding='utf_8')
					else :
						outfile=open(filename+nom_save+".export("+str(cpt_file_split)+").tsv",'w', encoding='utf-8')
				outfile.write("\""+nom_save+"\""+separateur+firstline+"\n")
			#outfile.write(firstline+"\n")
			#print("ecriture "+str(len(line_list)))
			for i in range(len(line_list)):
				outfile.write(str(line_list[i][1].get())+separateur)
				outfile.write(line_list[i][0])
				outfile.write("\n")
			#print(i)
			print("Fichier terminé : "+filename)
			outfile.close()
			cpt_file=cpt_file+1
	rules={}

def launch_no_visual_thread():
		#global no_visual_thread
		#global progressbar
		#no_visual_thread = threading.Thread(target=no_visual)
		#no_visual_thread.daemon= True
		#progressbar.start()
		#no_visual_thread.start()
		#root_window.after(2000,check_no_visual_thread)
		no_visual()

def check_no_visual_thread():
	global no_visual_thread
	global progressbar
	if no_visual_thread.is_alive():
		root_window.after(2000,check_no_visual_thread)
	else :
		progressbar.stop()

def print_no_visual_window():
	#afficher_module("blank")
	global no_vis_filename
	global no_vis_data
	global label_save
	global label_data
	global no_visual_window
	global progressbar
	no_visual_window=tk.Toplevel(root_window)
	no_visual_window.attributes('-topmost', 'true')
	browse_save = tk.Button(no_visual_window, text=L["Browse save"][lang], command=load_save_no_visual)
	browse_save.grid(column=0,row=0)
	label_save = tk.Label(no_visual_window, text=no_vis_filenames[0:10])
	label_save.grid(column=1, row=0)
	browse_data = tk.Button(no_visual_window, text=L["Browse data"][lang], command=load_data_no_visual)
	browse_data.grid(column=0, row=1)
	label_data=tk.Label(no_visual_window, text=no_vis_data[0:10])
	label_data.grid(column=1, row=1)
	go_button = tk.Button(no_visual_window, text=L["L_go"][lang], command=launch_no_visual_thread)
	go_button.grid(column=0, row=2)

def naviguation_pied_page():
	global line_list
	global seuil_affichage
	global page
	print(datetime.datetime.now(),"naviguation_pied_page")
	for label in footpage_frame.grid_slaves():
		label.destroy()

	taille=len(line_list)
	nbre_page=int(taille/seuil_affichage)
	if nbre_page*seuil_affichage < taille :
		nbre_page += 1
	print("page : " + str(page) + "nbre page : "+str(nbre_page))
	if page-1<nbre_page or page==1:
		#la page actuelle, +1 pour notation non informatique
		page_nav= tk.Button(footpage_frame, text=page, command= lambda : afficher_data_thread(page), bg="red")
		page_nav.grid(row=0, column=page)
		#print("afficher : ",page)
		if page >=2 :
			#la page précédente, notation non informatique
			page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(page-1), text=page-1)
			page_nav.grid(row=0, column=page-1)
			#print("afficher page -1: ",page,"page >=2")
		if page >=3 :
			#la page -2
			page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(page-2), text=page-2)
			page_nav.grid(row=0, column=page-2)
			#print("afficher page -2: ",page,"page >=3")
			if page-2>1 :
				page_nav = tk.Button(footpage_frame, command= lambda : afficher_data_thread(1), text=1)
				page_nav.grid(row=0, column=1)
			if page-2>2 :
				page_nav = tk.Button(footpage_frame, command=lambda :afficher_data_thread(2), text=2)
				page_nav.grid(row=0, column=2)
			if page-2>3 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(3), text=3)
				page_nav.grid(row=0, column=3)
			if page-2>4 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(4), text=4)
				page_nav.grid(row=0, column=4)
			if page-2>5 :
				page_nav = tk.Button(footpage_frame, command= lambda : afficher_data_thread(5), text=5)
				page_nav.grid(row=0, column=5)
			if page-2>6 :
				page_nav = tk.Label(footpage_frame, text="...")
				page_nav.grid(row=0, column=6)

		if page+1 <= nbre_page:
			page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(page+1), text=page+1)
			page_nav.grid(row=0, column=page+1)
			#print("afficher page +1: ",page,"page +1 <= nbre_page")
		if page+2 <= nbre_page:
			page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(page+2), text=page+2)
			page_nav.grid(row=0, column=page+2)
			#print("afficher page +1: ",page,"page +2 <= nbre_page")
			if page+2<nbre_page :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(nbre_page), text=nbre_page)
				page_nav.grid(row=0, column=nbre_page)
			if page+2<nbre_page-1 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(nbre_page-1), text=nbre_page-1)
				page_nav.grid(row=0, column=nbre_page-1)
			if page+2<nbre_page-2 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(nbre_page-2), text=nbre_page-2)
				page_nav.grid(row=0, column=nbre_page-2)
			if page+2<nbre_page-3 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(nbre_page-3), text=nbre_page-3)
				page_nav.grid(row=0, column=nbre_page-3)
			if page+2<nbre_page-4 :
				page_nav = tk.Button(footpage_frame, command=lambda : afficher_data_thread(nbre_page-4), text=nbre_page-4)
				page_nav.grid(row=0, column=nbre_page-4)
			if page+2<nbre_page-5 :
				page_nav = tk.Label(footpage_frame, text="...")
				page_nav.grid(row=0, column=nbre_page-5)

	else :
		page=1
		print("else")
		naviguation_pied_page()
	footpage_frame.update_idletasks()
	print(datetime.datetime.now(),"fin pied de page")

def afficher_module(mode, row=0):
	#blank : pas de données
	#first : première ouverture du fichier
	#ajouter : ajout d'une ou plusieurs ligne de ocndition
	#open : ouverture d'un fichier de donnée
	#tri : affichage suite a un tri
	#redraw : chargement d'un fichier de ocnditions
	#supprimer : suppression d'une ligne
	global dernier_affichage
	print(datetime.datetime.now(),"afficher_module")
	print(mode)

	if mode == "blank":
	#si c'est la première ouverture du fichier, on efface tout, et c'est tout
		for label in frame_t.grid_slaves():
			label.destroy()
	elif mode == "open":
	#si on ouvre un fichier
	#on ouvre le fichier et c'est tout
		open_filename()
	elif mode == "first":
	#si c'est le premier affichage
	#s'il y a des règles déjà chargées on les garde et on affiche juste les données
		if len(rules)>0 :
			calculer_score("visuel")
			afficher_data_thread(1)
		else :
			#s'il n'y a pas de règles pré chargées
			#on affiche la premiere ligne
			premiere_ligne()
			#on ajoute trois lignes
			ajouter_ligne(3)
			#et on affiche les data
			afficher_data_thread(1)
	elif mode == "ajouter" :
		#on commence par supprimer les trucs (cas multiples surtout)
		for label in frame_t.grid_slaves():
			if int(label.grid_info()["row"]) >= row :
				label.destroy()
	#s'il faut ajouter une ligne, on lance juste le module sur les nouvelles lignes
		for i in rules.keys():
			if i >= row :
				module_ligne(i)
	elif mode == "load" :
		#si on vient de charger de nouvelles règles
		#on efface les règles d'avant
		for label in frame_t.grid_slaves():
			label.destroy()
		#on affiche les nouvelles règles
		for i in rules.keys():
			module_ligne(i)
		#on calcule
		calculer_score("complet")
		#on tri
		tri()
		#on affiche les données
		afficher_data_thread(1)
	elif mode == "tri" :
		#si le mode est tri, il faut trier et afficher les data
		tri()
		afficher_data_thread(1)
	elif mode == "supprimer" :
		calculer_score("visuel")
	elif mode == "redraw" :
		#si c'est un redraw, on raffiche juste les data
		afficher_data_thread(1)



############
# Fonction Graphiques

#Fonction qui défini le titre
def set_title(value):
	print(datetime.datetime.now(),"set_title")
	print(mode_fenetre, " mode fenetre")
	if mode_fenetre=="True" :
		top.title(value)
	else :
		root_window.title(value)

def afficher_croissant():
	global affichage
	affichage="croissant"
	afficher_module("tri")

def afficher_decroissant():
	global affichage
	affichage="decroissant"
	afficher_module("tri")

def populate_footpage():
	global line_list
	if len(line_list)>0:
		naviguation_pied_page()
#fonction pour lier les scrolls bars au canva

def onFrameConfigure(canvas):
	canvas.configure(scrollregion=canvas.bbox("all"))

def valid_param(separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget):
	print(datetime.datetime.now(), " valid_param")
	global separateur
	global nombre_ligne
	global entete
	global lang
	global mode_fenetre
	separateur=separateur_widget.get()
	entete=entete_w.get()
	nombre_ligne=nombre_ligne_widget.get()
	lang=lang_w.get()
	mode_fenetre=mode_fenetre_widget.instate(['selected'])
	print(" separateur : ",separateur)
	print("entete : ", entete)
	print("nombre_ligne : ", nombre_ligne)
	print(" langue : ", lang)
	print("mode fenetre : ", mode_fenetre)
	write_param()
	return True

def write_param():
	print(datetime.datetime.now(), "write_param")
	global lang
	global separateur
	global entete
	global nombre_ligne
	global mode_fenetre
	if separateur =="" :
		separateur=";"
	if entete == "":
		entete="oui"
	if nombre_ligne == "" :
		nombre_ligne = "0"

	file=open("param",'w', encoding='utf-8')
	file.write(separateur+"\t")
	file.write(entete+"\t")
	file.write(nombre_ligne+"\t")
	file.write(lang+"\t")
	file.write(str(mode_fenetre)+"\t")

def load_param():
	print(datetime.datetime.now()," load param")
	global lang
	global separateur
	global entete
	global nombre_ligne
	global mode_fenetre
	if os.path.isfile("param"):
		file=open("param","r", encoding='utf-8')
		cpt=0
		for l in file :
			line=l.rstrip().split("\t")
			separateur=line[0]
			entete=line[1]
			nombre_ligne=int(line[2])
			lang=line[3]
			mode_fenetre=line[4]
			if separateur=="tabulation":
				separateur="\t"
			elif separateur=="espace":
				separateur=" "
	else :
		separateur="\t"
		entete="non"
		nombre_ligne=0
		lang='EN'
		mode_fenetre="False"
	print(" separateur : ",separateur)
	print("entete : ", entete)
	print("nombre_ligne : ", nombre_ligne)
	print(" langue : ", lang)
	print("mode fenetre : ", mode_fenetre)

def modif_parameters():
	global separateur
	global nombre_ligne
	global entete
	global lang
	global mode_fenetre
	global separateur_w
	global nombre_ligne_w
	global lang_w
	global entete_w
	print(datetime.datetime.now(), "modif parameters")
	print(separateur, " separateur")
	print(entete, " entete")
	print(nombre_ligne, " nombre_ligne")
	print(lang, " lang")
	print(mode_fenetre, " mode_fenetre")

	param_window=tk.Toplevel(root_window)
	param_window.attributes('-topmost', 'true')
	param_window.geometry('400x400')
	param_window.title(L["L_data_param"][lang])
	for widget in param_window.grid_slaves():
		widget.destroy()

	#le label qui explique le champs séparateur
	separateur_label=tk.Label(param_window, text=L["L_separator"][lang] )
	separateur_label.grid(column=0,row=0)
	separateur_w = tk.StringVar()
	#le champs séparateur
	separateur_widget = ttk.Combobox(param_window, textvariable=separateur_w, validate="all", validatecommand= lambda : valid_param(separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget))
	values=[",","espace","tabulation",";","|"]
	if separateur == " ":
		separateur="espace"
	if separateur == "\t":
		separateur="tabulation"
	separateur_widget.config(values=values)
	separateur_widget.current(values.index(separateur))
	#values_widget.configure(font=font, bg=color)
	separateur_widget.grid(column=1,row=0, pady=2)

	#le label d'entete
	entete_label = tk.Label(param_window, text=L["L_header"][lang])
	entete_label.grid(column=0,row=1)


	OPTIONS_entete = ["oui","non"]
	entete_w = tk.StringVar()
	entete_w.set(OPTIONS_entete[OPTIONS_entete.index(entete)])
	entete_widget = tk.OptionMenu(param_window, entete_w, *OPTIONS_entete, command = lambda x: valid_param( separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget))
	entete_widget.grid(column=1, row=1, sticky=tk.NW)


	#le label du nombre de ligne
	nombre_ligne_label = tk.Label(param_window, text=L["L_jump_lines"][lang])
	nombre_ligne_label.grid(column=0, row=2, pady=4)
	nombre_ligne_w = tk.StringVar()
	#le champs séparateur

	nombre_ligne_w.set(nombre_ligne)
	nombre_ligne_widget = ttk.Combobox(param_window, textvariable=nombre_ligne_w, validate="all", validatecommand= lambda : valid_param( separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget))
	values=["0","1","2","3","4"]
	nombre_ligne_widget.config(values=values)
	nombre_ligne_widget.current(values.index(str(nombre_ligne))) 
	#values_widget.configure(font=font, bg=color)
	nombre_ligne_widget.grid(column=1,row=2, pady=2)
	#lang label
	lang_label = tk.Label(param_window, text=L["lang_label"][lang])
	lang_label.grid(column=0, row=3, pady=2)
	#lang option menu
	OPTIONS_lang = ["EN","FR"]
	lang_w = tk.StringVar()
	lang_w.set(OPTIONS_lang[OPTIONS_lang.index(lang)])
	lang_widget = tk.OptionMenu(param_window, lang_w, *OPTIONS_lang, command = lambda x: valid_param( separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget))
	lang_widget.grid(column=1, row=3, sticky=tk.NW)
	#mode label
	mode_fenetre_label = tk.Label(param_window, text=L["mode_fenetre"][lang])
	mode_fenetre_label.grid(column=0, row=4, pady=2)
	#mode checkbutton
	mode_fenetre_widget= ttk.Checkbutton(param_window, text=L["mode_fenetre_on"][lang], command= lambda : valid_param(separateur_widget, entete_w, nombre_ligne_widget, lang_w, mode_fenetre_widget))
	print("mode _ fenetre : ", mode_fenetre)
	if mode_fenetre == "True" :
		mode_fenetre_widget.state(['!alternate'])
		mode_fenetre_widget.state(['selected'])
	else :
		mode_fenetre_widget.state(['!alternate'])
	mode_fenetre_widget.grid(row=4, column=1, stick=tk.NW)
	#label version
	#le bouton de validation
	afficher_data_thread(1)

#######################
#CORE

#read_ontologie()


#########################
# COEUR GRAPHIQUE


#Création de l'interface graphique
root_window = tk.Tk()
font_overstrike="-overstrike 1"
seuil=tk.StringVar()
seuil.set(15)
zut=tk.StringVar()
load_param()

def on_closing():
    if messagebox.askokcancel(L["quit"][lang], L["Do you want to quit?"][lang]):
        root_window.destroy()

def myfunction_t(event):
    canvas_t.configure(scrollregion=canvas_t.bbox("all"))

def myfunction_b(event):
    canvas_b.configure(scrollregion=canvas_b.bbox("all"))


if mode_fenetre=="True" :
	top=tk.Toplevel(root_window)
	bottom=tk.Toplevel(root_window)
	root_window.withdraw()
else :
	m = tk.PanedWindow(orient=tk.VERTICAL)
	m.pack(fill=tk.BOTH, expand=1)
	top = tk.Frame(m,borderwidth=2,relief="solid")
	m.add(top)
	bottom = tk.Frame(m,borderwidth=2,relief="solid")
	m.add(bottom)

canvas_t=tk.Canvas(top)
frame_t=tk.Frame(canvas_t)
myscrollbar_t=tk.Scrollbar(top,orient="vertical",command=canvas_t.yview)
canvas_t.configure(yscrollcommand=myscrollbar_t.set)
myscrollbar_t.pack(side="right",fill="y")
canvas_t.pack(side="top",expand=True, fill="both")
canvas_t.create_window((0,0),window=frame_t,anchor='nw')
frame_t.bind("<Configure>",myfunction_t)

canvas_b=tk.Canvas(bottom)
frame_b=tk.Frame(canvas_b)
myscrollbar_by=tk.Scrollbar(bottom,orient="vertical",command=canvas_b.yview)
myscrollbar_bx=tk.Scrollbar(bottom,orient="horizontal",command=canvas_b.xview)
canvas_b.configure(yscrollcommand=myscrollbar_by.set)
canvas_b.configure(xscrollcommand=myscrollbar_bx.set)
myscrollbar_by.pack(side="right",fill="y")
myscrollbar_bx.pack(side="bottom",fill="x")
canvas_b.pack(side="top",expand=True, fill="both")
canvas_b.create_window((0,0),window=frame_b,anchor='nw')
frame_b.bind("<Configure>",myfunction_b)

footpage_frame = tk.Frame(bottom)
populate_footpage()
footpage_frame.pack(side="bottom", fill="x", expand=1, anchor=tk.S)
#footpage = tk.Label(footpage_frame, text=L["L_foot"][lang])
#footpage.grid(row=0, column=0)

# menu global

menubar=tk.Menu(frame_t)
filemenu=tk.Menu(menubar, tearoff=0)
filemenu.add_command(label=L["L_load_data"][lang], command= lambda : afficher_module("open"))
filemenu.add_command(label=L["L_save"][lang],command=sauvegarde)
filemenu.add_command(label=L["L_load_rules"][lang], command=load)
filemenu.add_command(label=L["L_export"][lang],command=export)
filemenu.add_command(label=L["L_undo"][lang], command=undo)
filemenu.add_command(label=L["L_no_visual"][lang], command=print_no_visual_window)
filemenu.add_separator()
filemenu.add_command(label=L["L_quit"][lang], command=on_closing)
menubar.add_cascade(label=L["L_file"][lang], menu=filemenu)

editmenu=tk.Menu(menubar, tearoff=0)
editmenu.add_command(label=L["L_add_1"][lang], command=lambda : ajouter_ligne(1))
editmenu.add_command(label=L["L_add_3"][lang], command=lambda : ajouter_ligne(3))
editmenu.add_command(label=L["L_add_5"][lang], command=lambda : ajouter_ligne(5))
editmenu.add_command(label=L["add_multiple"][lang], command=lambda : ajouter_multiple())
menubar.add_separator()
editmenu.add_command(label=L["L_print_increasing"][lang], command=afficher_croissant)
editmenu.add_command(label=L["L_print_decreasing"][lang], command=afficher_decroissant)
menubar.add_cascade(label=L["L_edit"][lang], menu=editmenu)

parammenu=tk.Menu(menubar, tearoff=0)
parammenu.add_command(label=L["L_opening_parameters"][lang], command=lambda : modif_parameters())
menubar.add_cascade(label=L["L_parameters"][lang], menu=parammenu)
if mode_fenetre == "True":
	top.config(menu=menubar)
	top.protocol("WM_DELETE_WINDOW", on_closing)
	bottom.protocol("WM_delete_window", on_closing)
else :
	root_window.config(menu=menubar)
	root_window.protocol("WM_DELETE_WINDOW", on_closing)
#on réparti les différentes frame et autre sur l'interface
#menu_left.grid(row=0, column=0, rowspan=4, sticky="nsew")
#title_frame.pack()
#canvas_area.grid(row=1, column=1, sticky="nsew")


afficher_module("blank")


#boucle principale
#root_window.grid_rowconfigure(1, weight=1)
#root_window.grid_columnconfigure(1, weight=1)

root_window.mainloop()
