from sys import version_info
from tkinter import *
from common import *
from datetime import *
from datetime import date
#from tkinter.ttk import *

import tkinter as tk

from tkinter import *
from tkinter import ttk
"""class statistiqueFrame()"""
Mafenetre = Tk()
Mafenetre.title("Textile stock service")
Mafenetre.resizable(False, False)




# variables globales comprises dans la frameH
global valHtvaTotal
valHtvaTotal =0.0

global benefTotal
benefTotal =0.0

global depenseTotal
depenseTotal =0.0


stockVet = Stock()
historiqueVente = HistoriqueInOut()



def valRadioButtT(valButt):
    return True

def valRadioButtF(valButt):
    return False




#def affichageFrameA:

# pas besoin ici
def affichageFrameB():
    frameB.place(x=1050, y=200)

    nom = Label(frameB, text="Nom : %s")
    nom.grid(row=0, column=0, padx=5, pady=5)

    statut = Label(frameB, text="Statut : %s")
    statut.grid(row=1, column=0, padx=5, pady=5)

    report = Button(frameB, text="Log-out")
    report.grid(row=1, column=1, padx=5, pady=5)


def affichageFrameC():
    frameC.place(x=20, y=200)

    voirStock = Button(frameC, text="Stock", height=1, width=15, command=lambda: remplirTreeviewStock(stockVet))
    voirStock.pack(side=BOTTOM)

    top = Button(frameC, text="Top10", height=1, width=15,
                 command=lambda: remplirTreeviewTop10(stockVet, historiqueVente))
    top.pack(side=BOTTOM)

    report = Button(frameC, text="Daily report", height=1, width=15,
                    command=lambda: remplirTreeviewDailyReport(stockVet, historiqueVente))

    report.pack(side=BOTTOM)

    excel = Button(frameC, text="Exporter en Excel", height=1, width=15)
    excel.pack(side=BOTTOM)


def affichageFrameD():
    frameD.place(x=20, y=320)

    vente = Button(frameD, text="Vente", height=1, width=15)
    vente.pack(side=BOTTOM)

    gestionStock = Button(frameD, text="Gestion stock", height=1, width=15)
    gestionStock.pack(side=BOTTOM)

    stat = Button(frameD, text="Statistique", height=1, width=15)
    stat.pack(side=BOTTOM)

    employe = Button(frameD, text="Gestion employé", height=1, width=15)
    employe.pack(side=BOTTOM)



def affichageFrameE():
    frameE.place(x=150, y=0)

    recherche = Label(frameE, text="Rechercher par:")
    recherche.grid(row=0, column=0, padx=5, pady=5)

    ####

    num = Label(frameE, text="Numéro d'article:")
    num.grid(row=1, column=0, padx=5, pady=5)


    entreeNumArt = Entry(frameE, textvariable="valnum", width=30)
    entreeNumArt.grid(row=1, column=1, padx=5, pady=5)

    ###

    libelle = Label(frameE, text="Libellé:")
    libelle.grid(row=2, column=0, padx=5, pady=5)

    vallib = tk.StringVar()
    entreeLibelle = Entry(frameE, textvariable=vallib, width=30)
    entreeLibelle.grid(row=2, column=1, padx=5, pady=5)

    ###

    dateDeb = Label(frameE, text="Date début:")
    dateDeb.grid(row=3, column=0, padx=5, pady=5)

    valDeb = tk.StringVar()
    entreeDateDeb = Entry(frameE, textvariable=valDeb, width=30)
    entreeDateDeb.grid(row=3, column=1, padx=5, pady=5)

    ###

    dateFin = Label(frameE, text="Date fin:")
    dateFin.grid(row=4, column=0, padx=5, pady=5)

    valFin = tk.StringVar()
    entreeDateFin = Entry(frameE, textvariable=valFin, width=30)
    entreeDateFin.grid(row=4, column=1, padx=5, pady=5)

    ############# col 2 #############

    tailleV = Label(frameE, text="Taille:")
    tailleV.grid(row=1, column=2, padx=5, pady=5)

    valTaille = tk.StringVar()
    entreeTaille = Entry(frameE, textvariable=valTaille, width=30)
    entreeTaille.grid(row=1, column=3, padx=5, pady=5)

    ###

    couleurV = Label(frameE, text="Couleur:")
    couleurV.grid(row=2, column=2, padx=5, pady=5)


    entreeCouleur = Entry(frameE, textvariable="valCouleur", width=30)
    entreeCouleur.grid(row=2, column=3, padx=5, pady=5)

    ###

    categorieV = Label(frameE, text="Catégorie:")
    categorieV.grid(row=3, column=2, padx=5, pady=5)

    valCat = StringVar()
    entreeCategorie = Entry(frameE, textvariable=valCat, width=30)
    entreeCategorie.grid(row=3, column=3, padx=5, pady=5)

    ###

    entrSort = Label(frameE, text="Entrée/sortie:")
    entrSort.grid(row=4, column=2, padx=5, pady=5)

    inOutRadioButton = tk.IntVar()

    boutonEnt = Radiobutton(frameE, text="in", variable=inOutRadioButton, value=0)
    boutonEnt.grid(row=4, column=3, padx=1, pady=1)

    boutonSort = Radiobutton(frameE, text="out", variable=inOutRadioButton, value=1)
    boutonSort.grid(row=4, column=4, padx=1, pady=1)


    searchButton = Button(frameE, text="rechercher", command=lambda: remplirTreeview(stockVet, historiqueVente,
                                                                                     rechercheVet(stockVet, historiqueVente,
                                                                                                   entreeNumArt.get(),
                                                                                                  entreeLibelle.get(), entreeDateDeb.get(),
                                                                                                  entreeDateFin.get(),entreeTaille.get(),
                                                                                                  entreeCouleur.get(),entreeCategorie.get(),
                                                                                                  inOutRadioButton.get())))
    searchButton.grid(row=5, column=3, padx=1, pady=1)


#


def affichageFrameG():
    tree.place(x=150, y=200)

    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")

    tree.column("1", width=100)
    tree.column("2", width=100)
    tree.column("3", width=100)
    tree.column("4", width=100)
    tree.column("5", width=100)
    tree.column("6", width=100)
    tree.column("7", width=100)

    tree.heading("1", text="idVet")
    tree.heading("2", text="Libellé")
    tree.heading("3", text="Quantité")
    tree.heading("4", text="PrixAchat")
    tree.heading("5", text="PrixHTVA")
    tree.heading("6", text="Prix de vente")
    tree.heading("7", text="Date")

    treeScroll = ttk.Scrollbar()

    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)

    treeScroll.pack(side=LEFT, pady=100)
    treeScroll.place(x=150, y=200)


def affichageFrameH(valHtvaTotal,benefTotal,depLabelTot):
    frameH.place(x=800, y=450)


    valTotalHTVA = Label(frameH, text="Valeur HTVA: %s" % (valHtvaTotal))
    valTotalHTVA.grid(row=0, column=0, padx=5, pady=5)


    beneficeTotal = Label(frameH, text="Bénéfice total: %s" % (benefTotal))
    beneficeTotal.grid(row=10, column=0, padx=5, pady=5)


    depenseTotal = Label(frameH, text="Dépenses: %s" % (depLabelTot))
    depenseTotal.grid(row=20, column=0, padx=5, pady=5)




############################################## Comparaison de chaine de caractère ##############################################

def comparaisonString(chaineA,chaineB):
    chaineA = str.lower(chaineA)
    chaineB = str.lower(chaineB)
    caraB = 0

    for caraA in chaineA:
        if not (caraA == chaineB[caraB]):
            return False
        caraB += 1
    return True



############################################## Récup list id Vetement et quantite ##############################################

def idVetLst(stock,histo,inOrOut):
    listIdVet =[]
    for vet in stock.lstVetement:
        listIdVet.append([(vet),0])
    print(listIdVet)

    for tupl in listIdVet:
        print(tupl)
        for instInOut in histo.lstInOutStock:
         #   print(tupl[0])
            if instInOut.InOut == inOrOut and tupl[0].idVet == (instInOut.vetement).idVet:
                    tupl[1] += 1
                    print(tupl[1])

    return listIdVet


############################################## TOP 10 ##############################################

def top10Vet(listStock,listHisto):
    listClassement = idVetLst(listStock,listHisto,False)
    i = 1

    while i < len(listClassement):
        k = i
        while k > 0 and listClassement[k][1] > listClassement[k - 1][1]:
            tuplTempo = listClassement[k]
            listClassement[k] = listClassement[k - 1]
            listClassement[k - 1] = tuplTempo
            k = k-1
        i = i+1


    if len(listClassement)<10:
        return listClassement[:len(listClassement)]

    else:
        return listClassement[:10]



############################################## Rapport hebdomadaire ##############################################

def dailyReport(listStock,listHisto):
    listDaily = []
    dateToday = datetime.now()

    for ligne in listHisto.lstInOutStock:
        dateCommande = ligne.dateTime
        if dateCommande <= dateToday and dateCommande > (dateToday - timedelta(days=7)) and ligne.InOut==False:
            listDaily.append(ligne)

    return listDaily

#        self.lstInOutStock.append(InOutStock(self.idInOut, False, Vetement))

############################################## Rechercher ##############################################

def rechercheVet(listStock,listHisto,numArt,libelle,dateDebut,dateFin,taille,couleur,categorie,inOut):

    listRech =[]

    numArt = str(numArt)
    libelle = str(libelle)
    dateDebut = str(dateDebut)
    dateFin = str(dateFin)
    taille = str(taille)
    couleur = str(couleur)
    categorie = str(categorie)

    print(numArt)

    if inOut == 0:
        inOut=True
    else:
        inOut=False

    print(inOut)
    print(len(libelle))

    for ligneVet in listHisto.lstInOutStock:

        if ligneVet.InOut == inOut:

            if dateDebut =="" or dateFin=="" or (ligneVet.dateTime >= dateDebut and ligneVet.dateTime <= dateFin):
                if (comparaisonString(numArt,ligneVet.vetement.idVet)) and comparaisonString(libelle,ligneVet.vetement.libelle)  \
                        and comparaisonString(taille,ligneVet.vetement.taille) \
                        and comparaisonString(couleur,ligneVet.vetement.couleur)\
                        and comparaisonString(categorie,ligneVet.vetement.categorie):

                    listRech.append(ligneVet)

    return listRech


############################################## methode remplir treeview stock ##############################################

#    def __init__(self, idVet, strLibelle, strMarque, strCouleur, strCategorie, dblPrixHTVA, dblTauxTVA, dblPrixAchat,
#                 taille="Unique", Quantite=1, lstAssorti=[]):

def remplirTreeviewStock(lstStock):
    viderTreeview(tree)
    i = 1

    valHtvaTotal = 0.0
    benefTotal = 0.0
    depenseTotal = 0.0

    for vet in lstStock.lstVetement:
        tree.insert("", "end", text = i, values=(vet.idVet,vet.libelle, vet.quantite, vet.prixAchat,vet.prixHTVA,  vet.prixTVAC(), "vet.date"))
        valHtvaTotal += (vet.prixHTVA*vet.quantite)
        benefTotal += (((vet.prixHTVA) - (vet.prixAchat))*vet.quantite)
        depenseTotal += (vet.prixAchat*vet.quantite)
        i += 1

    for c in frameH.winfo_children():
        c.destroy()


    affichageFrameH(valHtvaTotal,benefTotal,depenseTotal)



#tree.insert("", 10, values=("1A", "1b"))



############################################## methode remplir treeview top 10 ##############################################



def remplirTreeviewTop10(lstStock,lstHisto):
    viderTreeview(tree)
    lstTop10 = top10Vet(lstStock,lstHisto)

    print(lstTop10)

    valHtvaTotal = 0.0
    benefTotal = 0.0
    depenseTotal = 0.0

    i = 1
    for tupl in lstTop10:
        tree.insert("", "end", text = i, values=(tupl[0].idVet,tupl[0].libelle, tupl[1], tupl[0].prixAchat,tupl[0].prixHTVA,  tupl[0].prixTVAC(), ""))
        valHtvaTotal += tupl[0].prixHTVA * tupl[1]
        benefTotal += ((tupl[0].prixHTVA)-(tupl[0].prixAchat)) * tupl[1]
        depenseTotal += tupl[0].prixAchat * tupl[1]

        i += 1


    for c in frameH.winfo_children():
        c.destroy()


    affichageFrameH(valHtvaTotal,benefTotal,depenseTotal)


#tree.insert("", 10, values=("1A", "1b"))


############################################## methode remplir treeview du daily report ##############################################



def remplirTreeviewDailyReport(lstStock,lstHisto):
    viderTreeview(tree)
    lstReport = dailyReport(lstStock,lstHisto)

    i = 1

    valHtvaTotal = 0.0
    benefTotal = 0.0
    depenseTotal = 0.0

    for ligne in lstReport:
        tree.insert("", "end", text = i, values=(ligne.vetement.idVet ,ligne.vetement.libelle, "", ligne.vetement.prixAchat,ligne.vetement.prixHTVA,  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
        valHtvaTotal += ligne.vetement.prixHTVA
        benefTotal += ((ligne.vetement.prixHTVA)-(ligne.vetement.prixAchat))
        depenseTotal += ligne.vetement.prixAchat
        i += 1

    for c in frameH.winfo_children():
        c.destroy()

    affichageFrameH(valHtvaTotal,benefTotal,depenseTotal)


#tree.insert("", 10, values=("1A", "1b"))

############################################## methode remplir treeview recherche ##############################################

def remplirTreeviewSearch(lstStock,lstHisto):
    viderTreeview(tree)
    lstSearch = rechercheVet(lstStock,lstHisto)

    i = 1

    valHtvaTotal = 0.0
    benefTotal = 0.0
    depenseTotal = 0.0

    for ligne in lstSearch:
        tree.insert("", "end", text = i, values=(ligne.vetement.idVet,ligne.vetement.libelle, "", ligne.vetement.prixAchat,ligne.vetement.prixHTVA,  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
        valHtvaTotal += ligne.vetement.prixHTVA
        benefTotal += ((ligne.vetement.prixHTVA)-(ligne.vetement.prixAchat))
        depenseTotal += ligne.vetement.prixAchat
        i += 1

    for c in frameH.winfo_children():
        c.destroy()


    affichageFrameH(valHtvaTotal,benefTotal,depenseTotal)



############################################## methode remplir treeview ##############################################

def remplirTreeview(lstStock,lstHisto,lstAfficher):
    viderTreeview(tree)

    i = 1

    valHtvaTotal = 0.0
    benefTotal = 0.0
    depenseTotal = 0.0

    for ligne in lstAfficher:
        tree.insert("", "end", text = i, values=(ligne.vetement.idVet ,ligne.vetement.libelle, "", ligne.vetement.prixAchat,ligne.vetement.prixHTVA,  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
        valHtvaTotal += ligne.vetement.prixHTVA
        benefTotal += ((ligne.vetement.prixHTVA)-(ligne.vetement.prixAchat))
        depenseTotal += ligne.vetement.prixAchat
        i += 1

    for c in frameH.winfo_children():
        c.destroy()


    affichageFrameH(valHtvaTotal,benefTotal,depenseTotal)


############################################## Vider treeview ##############################################

def viderTreeview(tree):
    for i in tree.get_children():
        tree.delete(i)


############################################## classe ensemble ##############################################

class Ensemble:
    reduction = 1

    def __init__(self,lstVetement,prixHTVA,tauxTVA):
        self.lstVetement = lstVetement
        self.prixHTVA = prixHTVA
        self.tauxTVA = tauxTVA

    def prixEnsemble(self):
        return self.prixHTVA * ((self.tauxTVA / 100) + 1) * self.reduction






######################################################################################################

Mafenetre.geometry('1280x1024')

#frameA = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameB = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameC = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameD = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameE = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameF = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameG = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
tree = ttk.Treeview(Mafenetre)

frameH = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
frameI = Frame(Mafenetre, borderwidth=2, relief=GROOVE)


############################################## frame A ##############################################



############################################## frame B ##############################################

affichageFrameB()



############################################## frame C ##############################################

affichageFrameC()

############################################## frame D ##############################################

affichageFrameD()


############################################## frame E ##############################################


affichageFrameE()


############################################## frame F ##############################################


############################################## frame G ##############################################
affichageFrameG()

### insert format -> insert(parent, index, iid=None, **kw)
### reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview


############################################## frame H ##############################################

affichageFrameH(0.0,0.0,0.0)

############################################## frame I ##############################################

#frameI.place(x=800,y=100)


############################################## menu ##############################################

menubar = Menu(Mafenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer")
menu1.add_command(label="Editer")
menu1.add_separator()
menu1.add_command(label="Quitter", command=Mafenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Historique", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos")
menubar.add_cascade(label="Aide", menu=menu3)

Mafenetre.config(menu=menubar)


############################################## EXECUTION ##############################################

#         def __init__(self, idVet, strLibelle, strMarque, strCouleur, strCategorie, dblPrixHTVA, dblTauxTVA, dblPrixAchat,
#                  taille="Unique", Quantite=1, lstAssorti=[]):




jeans = Vetement(0,"jeans","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
pull = Vetement(1,"pull","adidas","vert","haut",28.0,21.0,15.0,"xs",200)
blouse = Vetement(2,"blouse","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
pantalon = Vetement(3,"pantalon","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
robe = Vetement(4,"robe","adidas","vert","haut",28.0,21.0,15.0,"xs",200)

jupe = Vetement(5,"jupe","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
chemise = Vetement(6,"chemise","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
sweat = Vetement(7,"sweat","adidas","vert","haut",28.0,21.0,15.0,"xs",200)
costume = Vetement(8,"costume","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
cravate = Vetement(9,"cravate","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)

tailleur = Vetement(10,"tailleur","adidas","vert","haut",28.0,21.0,15.0,"xs",200)
uniforme = Vetement(11,"uniforme","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)


stockVet+jeans
stockVet+pull
stockVet+blouse
stockVet+pantalon
stockVet+robe

stockVet+jupe
stockVet+chemise
stockVet+sweat
stockVet+costume
stockVet+cravate

stockVet+tailleur
stockVet+uniforme


historiqueVente.Out(blouse)
historiqueVente.Out(pull)
historiqueVente.Out(pull)
historiqueVente.Out(pull)
historiqueVente.Out(pull)
historiqueVente.Out(blouse)


remplirTreeviewStock(stockVet)


Mafenetre.mainloop()
