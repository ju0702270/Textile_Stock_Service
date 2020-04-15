from tkinter import *
from datetime import datetime
from datetime import date
from tkinter.ttk import *

from tkinter import *
from tkinter import ttk

Mafenetre = Tk()
Mafenetre.title("Textile stock service")
Mafenetre.resizable(False, False)

global stock
stock = []

global historique
historique =[]

############################################## methode remplir treeview ##############################################

def remplirTreeview(lstVetement):
    for vet in lstVetement:
        tree.insert("", "end", values=(vet.idVet,vet.nom, vet.quantite, vet.prixHTVA, vet.prixAchat, vet.prixVetement(), vet.date))
#tree.insert("", 10, values=("1A", "1b"))

############################################## classe stock ##############################################

"""
class Stock:
    vetement =[]
    def __init__(self):

    def calculValeurTotal(self):
        valeurStock = 0
        for i in self.vetement:
            valeurStock += i.quantite * i.prixVetement
        return valeurStock
"""



############################################## classe vetement ##############################################

class Vetement:

    reduction = 1.0


    def __init__(self,idVet,libelle,taille,idMarque,idCouleur,idCategorie,prixHTVA,tauxTVA,quantite,prixAchat):
        self.idVet = idVet
        self.nom = libelle
        self.marque = idMarque
        self.couleur = idCouleur
        self.categorie = idCategorie
        self.prixHTVA = prixHTVA
        self.tauxTVA = tauxTVA
        self.quantite = quantite
        self.taille = taille
        self.prixAchat = prixAchat
      # self.date = date.today()
        stock.append(self)

    def prixVetement(self):
        return round(self.prixHTVA * ((self.tauxTVA/100.0) + 1.0) * self.reduction,2)

    def __del__(self):
        print("Le vêtement %s est supprimé, son id est le suivant %s"%(self.nom,self.idVet))



############################################## classe ensemble ##############################################

class Ensemble:
    reduction = 1

    def __init__(self,lstVetement,prixHTVA,tauxTVA):
        self.lstVetement = lstVetement
        self.prixHTVA = prixHTVA
        self.tauxTVA = tauxTVA

    def prixEnsemble(self):
        return self.prixHTVA * ((self.tauxTVA / 100) + 1) * self.reduction

############################################## classe historique ##############################################


############################################## classe in out stock ##############################################

class InOutStock:
    def __init__(self,inOut,dicoVet,dicoEnsemble):
        self.inOut = inOut            # in = True   out = False
        self.dicoVet = dicoVet
        self.dicoEnsemble = dicoEnsemble
        self.date = datetime.now()
        if not(self.testDispo(self.dicoVet,self.dicoEnsemble)) and inOut :
            del self

        self.sommeTicket = self.prixTotal(self,dicoVet,dicoEnsemble)
        historique.append(self)



    def testDispo(self,vetement,ensemble):
        for vet, nombre in vetement.items():
            vet.quantite -= nombre

        for ens, nombre in vetement.items():
            for i in ens.lstVetement:
                i.quantite -= nombre

        for vet in vetement.keys():
            if vet.quantite<0:
                print("Erreur il n'y a pas assez de %s"%(vet))
                for vet, nombre in vetement.items():
                    vet.quantite += nombre

                for ens, nombre in vetement.items():
                    for i in ens.lstVetement:
                        i.quantite -= nombre

                return False


        for ens in ensemble.keys():
            for i in ens.lstVetement:
                if i.quantite<0:
                    print("Erreur il n'y a pas assez de %s"%(i))
                    for vet, nombre in vetement.items():
                        vet.quantite += nombre

                    for ens, nombre in vetement.items():
                        for i in ens.lstVetement:
                            i.quantite -= nombre

                    return False

        return True


    def prixTotal(self,vetement,ensemble):
        total = 0
        for vet, quantite in vetement.items():
            self.total += vet.prixVetement() * quantite

        for ens, quantite in vetement.items():
            self.total += ens.prixVetement() * quantite

        return total





######################################################################################################

#def calculBenefice(listeInOut):


######################################################################################################

Mafenetre.geometry('1280x1024')

frameA = Frame(Mafenetre)
frameB = Frame(Mafenetre)
frameC = Frame(Mafenetre)
frameD = Frame(Mafenetre)
frameE = Frame(Mafenetre)
frameF = Frame(Mafenetre)
frameG = Frame(Mafenetre)
tree = ttk.Treeview(Mafenetre)

frameH = Frame(Mafenetre)
frameI = Frame(Mafenetre)


############################################## frame A ##############################################



############################################## frame B ##############################################

frameB.place(x=1000,y=200)



nom = Label(frameB, text="Nom : %s")
nom.grid(row=0, column=0, padx=5, pady=5)

statut = Label(frameB, text="Statut : %s")
statut.grid(row=1, column=0, padx=5, pady=5)

report = Button(frameB, text="Log-out")
report.grid(row=1, column=1, padx=5, pady=5)



############################################## frame C ##############################################

frameC.place(x=0,y=200)



rechercher = Button(frameC, text="rechercher")
rechercher.pack(side=BOTTOM)

top = Button(frameC, text="Top10")
top.pack(side=BOTTOM)

report = Button(frameC, text="Daily report")
report.pack(side=BOTTOM)

excel = Button(frameC, text="Exporter en Excel")
excel.pack(side=BOTTOM)


############################################## frame D ##############################################

frameD.place(x=0,y=320)



vente = Button(frameD, text="Vente")
vente.pack(side=BOTTOM)

gestionStock = Button(frameD, text="Gestion stock")
gestionStock.pack(side=BOTTOM)

stat = Button(frameD, text="Statistique")
stat.pack(side=BOTTOM)

employe = Button(frameD, text="Gestion employé")
employe.pack(side=BOTTOM)


############################################## frame E ##############################################

frameE.place(x=50,y=0)

recherche = Label(frameE, text="Rechercher par:")
recherche.grid(row=0, column=0, padx=5, pady=5)


####

num = Label(frameE, text="Numéro d'article:")
num.grid(row=1, column=0, padx=5, pady=5)

valnum = StringVar()
valnum.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=1, column=1, padx=5, pady=5)

###

libelle = Label(frameE, text="Libellé:")
libelle.grid(row=2, column=0, padx=5, pady=5)

vallib = StringVar()
vallib.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=2, column=1, padx=5, pady=5)

###

dateDeb = Label(frameE, text="Date début:")
dateDeb.grid(row=3, column=0, padx=5, pady=5)

valDeb = StringVar()
valDeb.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=3, column=1, padx=5, pady=5)

###

dateFin = Label(frameE, text="Date fin:")
dateFin.grid(row=4, column=0, padx=5, pady=5)

valFin = StringVar()
valFin.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=4, column=1, padx=5, pady=5)

############# col 2 #############

tailleV = Label(frameE, text="Taille:")
tailleV.grid(row=1, column=2, padx=5, pady=5)

valTaille = StringVar()
valTaille.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=1, column=3, padx=5, pady=5)

###

couleurV = Label(frameE, text="Couleur:")
couleurV.grid(row=2, column=2, padx=5, pady=5)

valCouleur = StringVar()
valCouleur.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=2, column=3, padx=5, pady=5)

###

categorieV = Label(frameE, text="Catégorie:")
categorieV.grid(row=3, column=2, padx=5, pady=5)

valCat = StringVar()
valCat.set("texte par défaut")
entree = Entry(frameE, textvariable="string", width=30)
entree.grid(row=3, column=3, padx=5, pady=5)

###

entrSort = Label(frameE, text="Entrée/sortie:")
entrSort.grid(row=4, column=2, padx=5, pady=5)

boutonEnt = Button(frameE, text="entrée")
boutonEnt.grid(row=4, column=3, padx=1, pady=1)

boutonSort = Button(frameE, text="sortie")
boutonSort.grid(row=5, column=3, padx=1, pady=1)


############################################## frame F ##############################################


############################################## frame G ##############################################

tree.place(x=100,y=200)

tree["columns"] = ("1","2","3","4","5","6","7")

tree.column("1", width=100)
tree.column("2", width=100)
tree.column("3", width=100)
tree.column("4", width=100)
tree.column("5", width=100)
tree.column("6", width=100)
tree.column("7", width=100)

tree.heading("1", text="Numéro d'article")
tree.heading("2", text="Libellé")
tree.heading("3", text="Quantité")
tree.heading("4", text="PrixHTVA")
tree.heading("5", text="PrixAchat")
tree.heading("6", text="Prix de vente")
tree.heading("7", text="Date")

### insert format -> insert(parent, index, iid=None, **kw)
### reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview


############################################## frame H ##############################################

frameH.place(x=800,y=450)



valTotalHTVA = Label(frameH, text="Valeur totota HTVA: %s")
valTotalHTVA.grid(row=0, column=0, padx=5, pady=5)

beneficeTotal = Label(frameH, text="Bénéfice total: %s")
beneficeTotal.grid(row=10, column=0, padx=5, pady=5)

depence = Label(frameH, text="Dépenses %s")
depence.grid(row=20, column=0, padx=5, pady=5)


############################################## frame I ##############################################

#frameI.grid(row=50, column=100, columnspan=350)


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
jeans = Vetement("00000","jeans","xxl","nike","bleu","bas",50.0,21.0,100,25.0)
pull = Vetement("00001","pull","xs","adidas","vert","haut",28.0,21.0,200,15.0)
blouse = Vetement("00002","blouse","m","tachini","rouge","manteau",70.0,21.0,500,30.0)

print(jeans.idVet)

print (5.0*13.2)
remplirTreeview(stock)

Mafenetre.mainloop()

print(datetime.now())


