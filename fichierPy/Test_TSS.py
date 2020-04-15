"""
Test_TSS Package
--------------------------
Documentation Générale
"""


# -*- coding: utf-8 -*-
## author : Rochez Justin

from tkinter import *
from tkinter import ttk,messagebox
from copy import deepcopy
from datetime import datetime

class lstDePrimitif:
    """
    class permettant de creer une liste qui ne contient pas 2 fois le même primitif
    """
    
    def __init__(self):
        """:param self.lst = La liste de primitif
        """
        self.lst = []
    
    def __add__(self, primitif):
        """Surcharge de l'addition avec un primitif
        
        :param primitif: int, str, float. Eviter les objets
        :type primitif: primitif
        """
        if primitif not in self.lst:
            self.lst.append(primitif)

class Vetement:
    """class qui représente le vêtement, les objets Vetements sont là base du programme
    """
    def __init__(self,EAN,strLibelle, strMarque,  strCouleur, strCategorie, dblPrixHTVA, dblTauxTVA,Quantite =1, taille = "M",lstAssorti = []):
        """__ini__
        
        :param strLibelle: libellé du vetement
        :type strLibelle: String
        :param strMarque: Marque (ex: Nike)
        :type strMarque: String
        :param strCouleur: couleur principal du vêtement
        :type strCouleur: String
        :param strCategorie: catégorie principal du vêtement (ex: Sport, nuit, bébé)
        :type strCategorie: String
        :param dblPrixHTVA: Prix HTVA 
        :type dblPrixHTVA: float
        :param dblTauxTVA: Pourcentage TVA
        :type dblTauxTVA: float
        :param lstAssorti: liste des objets vetements qui seraient bien assorti avec self, defaults to []
        :type lstAssorti: list, Vetement()
        """
        self.EAN= EAN
        self.strLibelle =strLibelle
        self.strMarque= strMarque
        self.lstAssorti = lstAssorti
        self.strCouleur= strCouleur
        self.strCategorie = strCategorie
        self.dblPrixHTVA = float(dblPrixHTVA)
        self.dblTauxTVA = float(dblTauxTVA)
        self.Quantite =int(Quantite)
        self.Taille = taille

    def lst(self):
        """Liste de plusieurs attribut du vetement
        
        :return: list de EAN 0 , strLibelle 1, Quantite 2, strMarque 3, dblPrixHTVA 4, Taille 5, strCategorie 6 , strCouleur 7
        :rtype: list
        """
        return [self.EAN,self.strLibelle,self.Quantite,self.strMarque,self.dblPrixHTVA,self.Taille,self.strCategorie,self.strCouleur]

    def __str__(self):
        """Utile pour afficher tous les attributs du Vetement. 
        par Exemple lors d'un messagebox.showinfo
        :return: La plupart des attributs du vetement chacun à la ligne
        :rtype: str
        """
        return "Article:\nEAN : %s\nLibelle : %s\nMarque : %s\nQuantité : %s\nPrix : %s\nTaille : %s\nCatégorie : %s\nCouleur : %s"\
            %(self.EAN,self.strLibelle,self.strMarque,self.Quantite,self.dblPrixHTVA,self.Taille,self.strCategorie,self.strCouleur)
    
class HistoriqueInOut:
    """Class conteneur, qui contient tout les lignes de transaction d'entrée et sortie de stock
    """
    def __init__(self):
        """:param self.idInOut = le numéro de la ligne, elle est unique dans la table HistoriqueInOut
        :param self.lstInOutStock = La liste contenant tout les Objet InOutStock
        """
        self.idInOut = 0
        self.lstInOutStock= []

    def In(self, Vetement):
        """procédure d'entrée en stock. Si on ajoute un quantité, ou un Vetement Non existant dans le Stock
        
        :param Vetement: Le Vetement qui fait un In
        :type Vetement: Vetement()
        """
        self.idInOut +=1
        self.lstInOutStock.append(InOutStock(self.idInOut, True, Vetement))

    def Out(self, Vetement):
        """Procédure de sortie de stock, si on supprime ou qu'on diminue une quantité
        
        :param Vetement: Le Vetement qui fait un In
        :type Vetement: Vetement()
        """
        self.idInOut +=1
        self.lstInOutStock.append(InOutStock(self.idInOut, False, Vetement))



class InOutStock:
    """Les Object de transaction. à chaque entrée ou sortie de stock un object InOutStock doit être crée
    """
    def __init__(self, numId, InOut, lst = []):
        self.intNumInOutStock = numId
        self.dateTime = datetime.now()
        self.lstVetement = lst
        self.InOut = InOut #True = In False = Out


class Stock:
    """La Class Stock contient tout les objets Vetements. C'est un peux la Table principale du programme
    """
    def __init__(self):
        self.lstVetement = []
        self.lstCouleur = lstDePrimitif()
        self.lstTaille = lstDePrimitif()
        self.lstMarque = lstDePrimitif()
        self.lstCategorie = lstDePrimitif()

    def __add__(self, vetement):# ????
        if len(self.lstVetement) !=0:
            if str(vetement.EAN) in [str(e.EAN) for e in self.lstVetement]:
                for vetm in self.lstVetement:
                    if str(vetm.EAN) == str(vetement.EAN):
                        vetm.Quantite += vetement.Quantite
            else:
                self.lstVetement.append(vetement)
        else:
            self.lstVetement.append(vetement)
    
    def __str__(self):
        return str(self.lstVetement)

    def calculValeur(self):
        valeurStock = 0
        for vtm in self.lstVetement:
            valeurStock += vtm.Quantite * vtm.dblPrixHTVA
        return valeurStock
    
    def __sub__(self, vetement):
        if len(self.lstVetement) > 0:
            self.lstVetement.remove(vetement)

    def updateLst(self):
        """Met à jour toute les listes lstCouleur, lstTaille, lstMarque, lstCatégorie afin de les integrer sans répétition dans le programme.
        """
        self.lstCouleur = lstDePrimitif()
        self.lstTaille = lstDePrimitif()
        self.lstMarque = lstDePrimitif()
        self.lstCategorie = lstDePrimitif()
        for v in self.lstVetement: 
            self.lstTaille + str(v.Taille)
            self.lstMarque + v.strMarque
            self.lstCouleur + v.strCouleur
            self.lstCategorie + v.strCategorie
        

    
    


class baseRoot(Tk):
    """Class d'initiation à la root Tkinter, C'est cet objet qui supporte tout le programme.
    
    :param Tk: Tkinter.Tk
    :type Tk: Tk()
    :param stockVetement: c'est un objet stock contenant des vetements 
    :type stockVetement: Stock()
    :param Historique: c'est l'historique de toute les transactions
    :type Historique: HistoriqueInOut()
    """
    def __init__(self,stockVetement, Historique):
        Tk.__init__(self)
        self.title("TSS")
        self.minsize(1050,400)
        self.stock = stockVetement
        self.Historique = Historique
        self.mainStock = mainFrame(self.stock, self)
        self.mainStock.pack()
        self.Stat = Frame(self, bg ="#FFFFFF")
        
        #self.iconbitmap("""chapeau_sRy_2.ico""")
    
    


class mainFrame(Frame):
    """C'est la Frame qui contient la Gestion du stock.
    
    :param Frame: Tkiner.Frame
    :type Frame:Frame()
    :param stockVetement: c'est un objet stock contenant des vetements 
    :type stockVetement: Stock()
    :params parent: C'est la fenetre parent Dans notre cas ici, nous utilisons le plus souvent baseRoot
    :type parent: baseRoot()
    """
    def __init__ (self,stockVetement, parent):
        Frame.__init__(self)
        self.parent= parent
        self.stock = stockVetement
        self.historique = self.parent.Historique
        self.stock.updateLst()
        self.stockAffiche = deepcopy(self.stock) #Il s'agit du stock affiché dans le TreeView

        self.l = LabelFrame(self, text="Gestion_Stock", padx=10, pady=5)
        self.FrFond = Frame(self.l,relief = GROOVE, border = 2,  bg ="#FFFFFF")
        self.FrFond.pack (ipadx = 73, ipady =5)

        self.frmRecherche = Frame(self.FrFond, bg ="#FFFFFF")
        self.frmAjout = Frame(self.FrFond, bg ="#FFFFFF")
        self.frmModif =Frame(self.FrFond, bg ="#FFFFFF")
        #*************Frame Recherche**********
        
        
        
        #*************End Frame Recheche*******
        #***************TreeView**************
        key = ["Numéro d'article","Libéllé","Quantité","Marque","PrixUHTVA","Taille","Catégorie","Couleur"]
        self.tree = ttk.Treeview(self.l, columns = [k for k in key[1:None]],height=10)
        #vsb = Scrollbar(tree, orient="vertical", command=tree.yview)
        #vsb.place(x=890, y=0, height=430)
        for i,k in enumerate(key):
            self.tree.heading('#%s' %(i),text = k)
            if k != "Quantité" and k !="Taille":
                self.tree.column('#%s' %(i), minwidth=120,width=120)
            else:
                self.tree.column('#%s' %(i), minwidth=len(k)*8,width=len(k)*8)   
        self.updateStock()
        self.tree.pack()

        self.frmrecherche()
        #*************end Treeview *************
        #*************Frame des boutons************ à effacer
        self.frmButton = Frame(self, bg = "#FFFFFF", relief = GROOVE, border = 2)
        self.frmButton.grid(row = 0, column = 0, ipadx = 30 , ipady = 23)
        Frame(self.frmButton,height = 30,bg = "#FFFFFF").pack()
        ttk.Button(self.frmButton, text = "Rechercher", command = self.frmrecherche, width = 15).pack()
        ttk.Button(self.frmButton, text = "Ajouter", command = self.Ajouter,width = 15).pack()
        ttk.Button(self.frmButton, text = "Modifier", command = self.Modifier,width = 15).pack()
        ttk.Button(self.frmButton, text = "Supprimer", command = self.Supprimer,width = 15).pack()
        ttk.Button(self.frmButton, text = "exporter en Excel", command = self.test,width = 15).pack()
        #*************end Frame du Total*******
        #************Frame des bouton de Menu******
        self.frmMenu = Frame(self, bg = "#33b8ff", relief = GROOVE, border = 2)
        self.frmMenu.grid(row = 1, column = 0, ipadx = 5 , ipady = 13)
        Frame(self.frmMenu,height = 30,bg = "#33b8ff").pack()
        Button(self.frmMenu,text = "Vente",command = self.closeFrame, bg = "#FFFFFF", relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_Stock",command = self.test, bg = "#989898", relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Statistique",command = self.closeFrame, bg = "#FFFFFF", relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_employé",command = self.closeFrame, bg = "#FFFFFF", relief = GROOVE, width = 20).pack(pady= 2)
        #************end bouton de menu************

        self.l.grid(row = 0, rowspan =2, column = 1)

    

    def test(self,event= None):
        messagebox.showinfo("TSS", "application en construction")
        #print(self.tree.focus())

    def Ajouter(self, event = None):
        """Creation de la Frame D'ajout
        
        """
        try:
            self.recherche()
            self.frmModif.pack_forget()
            self.frmRecherche.pack_forget()
            self.frmAjout.pack(padx =11, pady = 1)
            Label(self.frmAjout,text = "article à ajouter: ",bg ="#FFFFFF").grid(row= 0, column = 0)
            self.dctAjout = {}
            for s in ["numArt","libArt","tvaArt", "marqueArt", "prixArt", "tailleArt", "catArt", "couleurArt",'quantArt', "AssortiEAN"]:
                self.dctAjout[s]= StringVar()
                
            Row =1
            self.entreeAj = {}
            
            for s in self.dctAjout.keys():
                if Row <= 5 :
                    Label(self.frmAjout, text = ("%s :" %(s)),bg ="#FFFFFF").grid(row = Row, column = 0, padx = 20, pady = 1)
                    self.entreeAj[s]=ttk.Entry(self.frmAjout,textvariable = self.dctAjout[s] ,width = 23)
                    self.entreeAj[s].grid(row = Row, column = 1, padx = 20, pady = 1)
                else:
                    Label(self.frmAjout, text = ("%s :" %(s)),bg ="#FFFFFF").grid(row = Row-5, column = 2, padx = 20, pady = 1)
                    self.entreeAj[s]=ttk.Entry(self.frmAjout,textvariable = self.dctAjout[s] , width = 23)
                    self.entreeAj[s].grid(row = Row-5, column = 3, padx = 20, pady = 1)
                Row +=1
            ttk.Button(self.frmAjout, text ="Confirmer" , command = self.ajouterVetement).grid(row = 0, rowspan = 6, column = 4)
            self.tree.bind("<Button-1>", self.updateAssortiEan)
            for w in self.entreeAj.values(): 
                w.bind("<Return>", self.ajouterVetement)
            
        except:
            messagebox.showerror(title="Error", message="l'ajout à échoué!")
        
    def updateAssortiEan(self,event= None):
        """Cette fonction va placer le numéro EAN d'un vetement bien assorti dans le Entry self.entreeAj["AssortiEAN"]
        
        """
        if len(self.tree.focus()) !=0:
            self.dctAjout["AssortiEAN"].set(self.stockAffiche.lstVetement[int(self.tree.focus())].EAN)

    def ajouterVetement(self,event = None):
        """Fonction d'ajout de Vetement dans le stock
        à condition que tout les cases soit remplie.
        
        """
        try:
            valeur = [v.get() for v in self.dctAjout.values()]
            if str(valeur[0]) in [str(v.EAN) for v in self.stock.lstVetement]:
                if messagebox.askyesno("Déjà en stock","Le vêtement EAN%s est déjà dans le stock l'ajouter ne fera que changer"+\
                    "sa quantité, celà ne modifiera en rien son prix ou autres attributs.\nSouhaitez-vous continuer?" %(self.stockAffiche.lstVetement[int(self.tree.focus())].EAN)):
                    if len(self.tree.focus()) !=0: 
                        valeur[9] = (self.stockAffiche.lstVetement[int(self.tree.focus())])
                    self.stock + Vetement(valeur[0],valeur[1],valeur[3],valeur[7],valeur[6],valeur[4],valeur[2],int(valeur[8]),valeur[5],valeur[9])
                    self.historique.In(self.stock.lstVetement[int(self.tree.focus())])
                    messagebox.showinfo("Ajout effectué", str(self.stock.lstVetement[-1]))
                else:
                    messagebox.showinfo("Annulation Ajout", "Le Vetement n'as pas été encodé")
            else:
                if len(self.tree.focus()) !=0: 
                    valeur[9] = (self.stockAffiche.lstVetement[int(self.tree.focus())])
                    self.stock + Vetement(valeur[0],valeur[1],valeur[3],valeur[7],valeur[6],valeur[4],valeur[2],int(valeur[8]),valeur[5],valeur[9])
                    self.historique.In(self.stock.lstVetement[int(self.tree.focus())])
                    messagebox.showinfo("Ajout effectué", str(self.stock.lstVetement[-1]))
                else:
                    messagebox.showerror(title="Error", message="l'ajout à échoué!\nToutes les cases doivent être remplie")
            self.fullStock()
        except :
            messagebox.showerror(title="Error", message="l'ajout à échoué!\nToutes les cases doivent être remplie")


    def frmrecherche(self): # à améliorer
        """Fonction de création de la Frame de Recherche
        """
        self.tree.unbind("<Button-1>")
        self.frmAjout.pack_forget()
        self.frmModif.pack_forget()
        self.frmRecherche.pack()
        Label(self.frmRecherche, text = "rechercher par:" ,bg ="#FFFFFF").grid(row = 0, column = 0, padx = 20, pady = 1)
        Label(self.frmRecherche, text= "numéro d'article :",bg ="#FFFFFF").grid(row = 1, column = 0 ,padx = 20, pady = 1)
        self.num_art_recherche =ttk.Combobox(self.frmRecherche,width = 20,values = [vetm.lst()[0] for vetm in self.stock.lstVetement])
        self.num_art_recherche.grid(row = 1, column = 1, padx = 20, pady = 1)
        Label(self.frmRecherche, text= "Libellé :",bg ="#FFFFFF").grid(row = 2, column = 0, padx = 20, pady = 1)
        self.libelle_art_recherche =ttk.Combobox(self.frmRecherche,width = 20,values = [vetm.lst()[1] for vetm in self.stock.lstVetement])
        self.libelle_art_recherche.grid(row = 2, column = 1, padx = 20, pady = 1)
        Label(self.frmRecherche, text= "Prix Minimum :",bg ="#FFFFFF").grid(row = 3, column = 0, padx = 20, pady = 1)
        self.minPrix_art_recherche =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = 21)
        self.minPrix_art_recherche.grid(row = 3, column = 1, padx = 20, pady = 1)
        Label(self.frmRecherche, text= "Prix Maximum :",bg ="#FFFFFF").grid(row = 4, column = 0, padx = 20, pady = 1)
        self.maxPrix_art_recherche =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = 21)
        self.maxPrix_art_recherche.grid(row = 4, column = 1, padx = 20, pady =1)
        
        Label(self.frmRecherche, text= "taille :",bg ="#FFFFFF").grid(row = 1, column = 2, padx = 20, pady = 1)
        self.taille_art_recherche =ttk.Combobox(self.frmRecherche,width = 20,values = self.stock.lstTaille.lst)
        self.taille_art_recherche.grid(row = 1, column = 3, padx = 20, pady = 1)
        Label(self.frmRecherche, text= "couleur :",bg ="#FFFFFF").grid(row = 2, column = 2, padx = 20, pady = 1)
        self.couleur_art_recherche =ttk.Combobox(self.frmRecherche,width = 20,values = self.stock.lstCouleur.lst)
        self.couleur_art_recherche.grid(row = 2, column = 3,padx = 20, pady = 1)
        Label(self.frmRecherche, text= "catégorie :",bg ="#FFFFFF").grid(row = 3, column = 2,padx = 20, pady = 1)
        self.cat_art_recherche =ttk.Combobox(self.frmRecherche,width = 20,values = self.stock.lstCategorie.lst)
        self.cat_art_recherche.grid(row = 3, column = 3,padx = 20, pady = 1)
        Label(self.frmRecherche, text= "Marque :",bg ="#FFFFFF").grid(row = 4, column = 2,padx = 20, pady = 1)
        
        self.Marque_art_recherche =ttk.Combobox(self.frmRecherche,width = 20, values = self.stock.lstMarque.lst)
        self.Marque_art_recherche.grid(row = 4, column = 3,padx = 20, pady = 1)
        lstCombo = [self.num_art_recherche,self.libelle_art_recherche,self.minPrix_art_recherche,self.maxPrix_art_recherche,self.taille_art_recherche\
            ,self.couleur_art_recherche,self.cat_art_recherche,self.Marque_art_recherche]
        for w in lstCombo:
            w.bind("<Return>", self.recherche)
        ttk.Button(self.frmRecherche, text ="Confirmer" , command = self.recherche).grid(row = 0, rowspan = 5, column = 4)
        


    def Modifier(self, event = None):
        """Fonction de création de la Frame de modification
        """
        try:
            self.frmRecherche.pack_forget()
            self.frmAjout.pack_forget()
            self.frmModif.pack(padx = 12, pady = 1)
            self.tree.bind("<Button-1>", self.Modifier)
            Label(self.frmModif,text = "article à modifier: ",bg ="#FFFFFF").grid(row= 0, column = 0)
            self.dctStvModif = {}
            
            for i,s in enumerate(list(["numArt","libArt","quantArt", "marqueArt", "prixArt", "tailleArt", "catArt", "couleurArt"])):
                self.dctStvModif[s]= StringVar()
                try:
                    if len(self.tree.focus()) != 0:
                        print(1)
                        self.dctStvModif[s].set(self.stockAffiche.lstVetement[int(self.tree.focus())].lst()[i])
                except :
                    print("error")
                    self.dctStvModif[s].set('')      
            Row =1
            self.entree = {}
            for s in self.dctStvModif.keys():
                if Row <= 4 :
                    Label(self.frmModif, text = ("%s :" %(s)),bg ="#FFFFFF").grid(row = Row, column = 0, padx = 20, pady = 1)
                    self.entree[s]=ttk.Entry(self.frmModif, textvariable = self.dctStvModif[s], width = 23)
                    self.entree[s].grid(row = Row, column = 1, padx = 20, pady = 1)
                else:
                
                    Label(self.frmModif, text = ("%s :" %(s)),bg ="#FFFFFF").grid(row = Row-4, column = 2, padx = 20, pady = 1)
                    self.entree[s]=ttk.Entry(self.frmModif, textvariable = self.dctStvModif[s], width = 23)
                    self.entree[s].grid(row = Row-4, column = 3, padx = 20, pady = 1)
                Row +=1
            ttk.Button(self.frmModif, text ="Confirmer" , command = self.ModifierVetement).grid(row = 0, rowspan = 5, column = 4)
            
            for w in self.entree.values(): 
                w.bind("<Return>", self.ModifierVetement)
            self.fullStock()
            
        except:
            messagebox.showerror(title="Error", message="Aucun vetement n'as été selectionné!")
            

    def ModifierVetement (self, event= None):
        """Fonction de confirmation de modification d'un vetement. 
        Si le EAN vetement existe déjà, la modification ne se fera que sur la quantité et sera prise en compte par l'Historique
        """
        try:
            if messagebox.askyesno("Modification","Voulez vous modifier le vêtement EAN%s" %(self.stockAffiche.lstVetement[int(self.tree.focus())].EAN)):
                if str(self.stockAffiche.lstVetement[int(self.tree.focus())].EAN) in [str(v.EAN) for v in self.stock.lstVetement]:
                    #print('modifié')
                    for v in self.stock.lstVetement:
                        if self.stockAffiche.lstVetement[int(self.tree.focus())].EAN == v.EAN:
                            v.EAN = self.entree["numArt"].get()
                            v.strLibelle= self.entree["libArt"].get()
                            v.strMarque= self.entree["marqueArt"].get()
                            v.dblPrixHTVA = float(self.entree["prixArt"].get())
                            v.Taille = self.entree["tailleArt"].get()
                            v.strCategorie = self.entree["catArt"].get()
                            v.strCouleur = self.entree["couleurArt"].get()
                            if v.Quantite < int(self.entree["quantArt"].get()):
                                if (messagebox.askyesno("Modification","Voulez vous modifier la quantité. Cette manoeuvre est équivalente à une Transaction")):
                                    dif =int(self.entree["quantArt"].get())-v.Quantite
                                    v.Quantite = dif 
                                    self.parent.Historique.In([v])
                                    #print(self.parent.Historique.lstInOutStock[0].lstVetement[0].Quantite)
                                    v.Quantite = int(self.entree["quantArt"].get())
                                    #print(v.Quantite)
                            elif v.Quantite > int(self.entree["quantArt"].get()):
                                if (messagebox.askyesno("Modification","Voulez vous modifier la quantité. Cette manoeuvre est équivalente à une Transaction")):
                                    dif =v.Quantite - int(self.entree["quantArt"].get())
                                    v.Quantite = dif 
                                    self.parent.Historique.Out([v])
                                    print(self.parent.Historique.lstInOutStock[0].lstVetement[0].Quantite)
                                    v.Quantite = int(self.entree["quantArt"].get())
                                    print(v.Quantite)
                self.recherche()
        except :
            messagebox.showerror(title="Error", message="Aucun vetement n'as été selectionné!")


    def closeFrame(self):
        """cache la Frame Stock pour permettre l'ouverture d'une autre
        """
        self.pack_forget()
        self.parent.Stat.pack(ipadx= 50, ipady= 50)# simule l'ouverture d'une autre fenetre

    def Supprimer(self):# à améliorer pour qu'on ne supprime pas n'importe quel object stock.
        """
        Fonction de suppression d'un vetement avec messages informatif
        """
        try:
            messagebox.showinfo(title="Suppression",message="%s" %(self.stock.lstVetement[int(self.tree.focus())]))
            if str(self.stock.lstVetement[int(self.tree.focus())].EAN) == str(self.stockAffiche.lstVetement[int(self.tree.focus())].EAN):
                self.historique.Out(self.stock.lstVetement[int(self.tree.focus())])
                del(self.stock.lstVetement[int(self.tree.focus())])
                del(self.stockAffiche.lstVetement[int(self.tree.focus())])
                self.updateStock()       
        except:
            messagebox.showerror(title="Error", message="Erreur dans la suppression de l'article!")

    def recherche(self, event = None):
        """
        Fonction du bouton Rechercher, qui va rechercher un Vetement correspondant aux Input utilisateur dans l'objet stock
        """
        self.stock.updateLst()
        self.frmModif.pack_forget()
        self.frmRecherche.pack()
        self.stockAffiche.lstVetement = []
        PrixMin = 0.0
        PrixMax = 9999999.0
        try:
            if len(self.minPrix_art_recherche.get()) !=0:
                PrixMin = float(self.minPrix_art_recherche.get())
            if len(self.maxPrix_art_recherche.get()) !=0:
                PrixMax = float(self.maxPrix_art_recherche.get())
        except :
            messagebox.showerror(title="Error", message="Erreur d'encodage dans le Prix!")
        
        if str(self.num_art_recherche.get()) in [str(v.EAN) for v in self.stock.lstVetement]:  
            for vetm in self.stock.lstVetement:
                if str(self.num_art_recherche.get()) == str(vetm.EAN) and (PrixMin <= vetm.dblPrixHTVA and PrixMax >= vetm.dblPrixHTVA):
                    self.stockAffiche.lstVetement.append(vetm)
                    break
        else: 
            for vetm in self.stock.lstVetement:
                if PrixMin <= vetm.dblPrixHTVA and PrixMax >= vetm.dblPrixHTVA:
                    self.stockAffiche.lstVetement.append(vetm)
                if vetm in self.stockAffiche.lstVetement :
                    if len(self.libelle_art_recherche.get())!=0 and str(vetm.strLibelle).upper() != self.libelle_art_recherche.get().upper():
                        self.stockAffiche.lstVetement.remove(vetm)
                    elif len(self.Marque_art_recherche.get()) and str(vetm.strMarque).upper() != self.Marque_art_recherche.get().upper():
                        self.stockAffiche.lstVetement.remove(vetm)
                    elif len(self.cat_art_recherche.get()) and str(vetm.strCategorie).upper() != self.cat_art_recherche.get().upper():
                        self.stockAffiche.lstVetement.remove(vetm)
                    elif len(self.taille_art_recherche.get()) and str(vetm.Taille).upper() != self.taille_art_recherche.get().upper():
                        self.stockAffiche.lstVetement.remove(vetm)
                    elif len(self.couleur_art_recherche.get()) and str(vetm.strCouleur).upper() != self.couleur_art_recherche.get().upper():
                        self.stockAffiche.lstVetement.remove(vetm)
                        
        self.updateStock()


    def updateStock(self):
        """
        Fonction qui va mettre à jour le Tree de la Frame Gestion Stock avec les données de l'object stock à afficher.
        """
        self.tree.delete(*self.tree.get_children())
        for i,vetm in enumerate(self.stockAffiche.lstVetement):
            self.tree.insert('', 'end', i , text=vetm.lst()[0],values = [v for v in vetm.lst()[1:len(vetm.lst())]])
    
    def fullStock(self):
        self.stockAffiche = deepcopy(self.stock)
        self.updateStock()


    


categorie = lstDePrimitif()
taille = lstDePrimitif()
couleur = lstDePrimitif()
if __name__ == "__main__":
    
    couleur + "rouge"
    couleur + "bleu"
    couleur + "vert"
    taille +"M"
    taille +"S"
    taille +"L"
    categorie +"sport"
    categorie + "nuit"
    categorie +"femme"

    _stock = Stock()
    for i in range(10):
        _stock + Vetement(5414489,"jupe courte","Dolce Gabana","rouge","adolescente",50,21,1,"S")
        _stock + Vetement(5414476,"jupe longue","Dolce Gabana","verte","adolescente",70,21,1,"L")
        _stock + Vetement(5414425,"pantalon troué","Lévis","gris","adolescent",150,21,1)
        _stock + Vetement(5414145,"Jeans","Lévis","gris","nuit",150,21,1,"S")
        _stock + Vetement(5411478,"basquet","Fila","blanc","sport",15,21,1)
        _stock + Vetement(5411457,"chaussure ville","Louis Viton","rouge","ville",150,21,1)
        _stock + Vetement(4786214,"basquet","Fila","blanc","sport",150,21,1)
    

    Historique = HistoriqueInOut()

    Stock = baseRoot(_stock, Historique)


    Stock.mainloop()
