"""
TSS Package
--------------------------
Documentation Générale
"""


# -*- coding: utf-8 -*-
## author : Rochez Justin

########Import##########
from common import HistoriqueInOut,Stock,tableEmployee,Vetement,InOutStock,CouleurBlanc


#toAdd on common 
from tkinter import *
from tkinter import messagebox, ttk


#importTest
from random import *


########Global########## 


########Class###########
class baseRoot(Tk):
    """Class d'initiation à la root Tkinter, C'est cet objet qui supporte tout le programme.
    Chaque Frame que vous faites doit être integrée dedans. 
    
    :param Tk: Tkinter.Tk
    :type Tk: Tk()
    :param stockVetement: c'est un objet stock contenant des vetements 
    :type stockVetement: Stock()
    :param Historique: c'est l'historique de toute les transactions
    :type Historique: HistoriqueInOut()
    """
    def __init__(self,stockVetement, Historique, tableEmp):
        Tk.__init__(self)
        self.title("TSS")
        self.minsize(1050,400)
        #self.iconbitmap("""monIconeAChoisir.ico""")

        ##### ici c'est uyn peu la base de données du programme avec 3 grosses tables
        self.stock = stockVetement
        self.Historique = Historique
        self.employe = tableEmp 
        
        self.frm_Login = "" # Frame du Login (Emilien)

        self.frm_Stock = FrmStock(self) #Frame de la gestion de stock ( Justin )
        self.frm_Stock.pack()

        self.frm_Stat = "" # Frame de la gestion des statistiques (Nassim)
        self.frm_Vente = "" # Frame de la Gestion des ventes (???)
        self.frm_Employé = "" # Frame de la gestion des Employe (???)

class FrmStock(Frame):
    """C'est la Frame qui contient la Gestion du stock.
    
    :param Frame: Tkiner.Frame
    :type Frame:Frame()
    :param stockVetement: c'est un objet stock contenant des vetements 
    :type stockVetement: Stock()
    :params parent: C'est la fenetre parent Dans notre cas ici, nous utilisons le plus souvent baseRoot
    :type parent: baseRoot()
    """
    def __init__ (self,parent):
        Frame.__init__(self)
        self.parent = parent
        
        self.l = LabelFrame(self, text="Gestion_Stock", padx=10, pady=5)
        self.FrFond = Frame(self.l,relief = GROOVE, border = 2,  bg =CouleurBlanc)
        self.FrFond.pack (ipadx = 73, ipady =5)

        self.frmRecherche = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmAjout = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmModif =Frame(self.FrFond, bg =CouleurBlanc)

        self.key = ["Numéro d'article","Libéllé","Marque","Quantité","PrixHTVA","Tva","Taille","Catégorie","Couleur"]
        self.frmrecherche()
        self.tree = ttk.Treeview(self.l, columns = [k for k in self.key[1:None]],height=10)
        for i,k in enumerate(self.key):
            self.tree.heading('#%s' %(i),text = k)
            if k[0] not in ["T","P","Q"]:
                self.tree.column('#%s' %(i), minwidth=110,width=110)
            else:
                self.tree.column('#%s' %(i), minwidth=60,width=60)  
         
        self.tree.pack()
        self.updateStock()
        self.frmButton = Frame(self, bg = CouleurBlanc, relief = GROOVE, border = 2)
        self.frmButton.grid(row = 0, column = 0, ipadx = 30 , ipady = 23)
        Frame(self.frmButton,height = 30,bg = CouleurBlanc).pack()
        ttk.Button(self.frmButton, text = "Rechercher", command = self.test, width = 15).pack()
        ttk.Button(self.frmButton, text = "Ajouter", command = self.test,width = 15).pack()
        ttk.Button(self.frmButton, text = "Modifier", command = self.test,width = 15).pack()
        ttk.Button(self.frmButton, text = "Supprimer", command = self.test,width = 15).pack()
        ttk.Button(self.frmButton, text = "exporter en Excel", command = self.test,width = 15).pack()
        #*************end Frame button*******
        #************Frame des bouton de Menu******
        self.frmMenu = Frame(self, bg = "#33b8ff", relief = GROOVE, border = 2)
        self.frmMenu.grid(row = 1, column = 0, ipadx = 5 , ipady = 13)
        Frame(self.frmMenu,height = 30,bg = "#33b8ff").pack()
        Button(self.frmMenu,text = "Vente",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_Stock",command = self.test, bg = "#989898", relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Statistique",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_employé",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        #************end bouton de menu************

        self.l.grid(row = 0, rowspan =2, column = 1)
      

    def test(self,event= None):
        messagebox.showinfo("TSS", "application en construction")
        #print(self.tree.focus())

    def updateStock(self):
        """
        Fonction qui va mettre à jour le Tree de la Frame Gestion Stock avec les toutes  données de l'object stock
        """
        self.tree.delete(*self.tree.get_children())
        for i,vetm in enumerate(self.parent.stock.lstVetement):
            self.tree.insert('', 'end', i , text=vetm.idVet,values = [vetm.libelle,vetm.marque, vetm.quantite,vetm.prixHTVA, vetm.tauxTVA, vetm.taille,vetm.categorie, vetm.couleur])
    


    def recherche(self, event = None):
        """
        Fonction du bouton Rechercher, qui va rechercher un Vetement correspondant aux Input utilisateur dans l'objet stock
        """
        PrixMin = 0.0
        PrixMax = 9999999.0
        entryRech = [self.idVetfrRech,self.libfrRech,  self.MarquefrRech,self.catfrRech,self.taillefrRech,self.couleurfrRech,self.tvafrRech,self.quantfrRech]
        self.tree.delete(*self.tree.get_children())
        try:
            if len(self.minPrixfrRech.get()) !=0:
                PrixMin = float(self.minPrixfrRech.get())
            if len(self.maxPrixfrRech.get()) !=0 :
                PrixMax = float(self.maxPrixfrRech.get())
        except :
            messagebox.showerror(title="Error", message="Erreur d'encodage dans le Prix!")  
        try:
            for i,vetm in enumerate(self.parent.stock.lstVetement):
                valeurComparative = [vetm.idVet,vetm.libelle,vetm.marque,vetm.categorie,vetm.taille,vetm.couleur,vetm.tauxTVA,vetm.quantite] 
                if PrixMin <= vetm.prixHTVA and PrixMax >= vetm.prixHTVA:
                    self.tree.insert('', 'end', i , text=vetm.idVet,values = [vetm.libelle,vetm.marque, vetm.quantite,vetm.prixHTVA, vetm.tauxTVA, vetm.taille,\
                        vetm.categorie, vetm.couleur])
                    for j,e in enumerate(entryRech[0:-2]):
                        if len(e.get())!=0 and str(valeurComparative[j]).upper() != e.get().upper() \
                            or (len(entryRech[-2].get())!=0 and float(entryRech[-2].get()) != valeurComparative[-2])\
                            or (len(entryRech[-1].get())!=0 and int(entryRech[-1].get()) > int(valeurComparative[-1])):
                            self.tree.delete(i) 
                            break  
        except :
            messagebox.showerror(title="Error", message="Erreur d'encodage!") 
            self.updateStock() 
                    

    def frmrecherche(self): # à améliorer
            """Fonction de création de la Frame de Recherche
            """
            #self.tree.unbind("<Button-1>")
            #self.frmAjout.pack_forget()
            #self.frmModif.pack_forget()
            self.frmRecherche.pack()
            Label(self.frmRecherche, text = "rechercher par:" ,bg =CouleurBlanc).grid(row = 0, column = 0, padx = 20, pady = 1)          
            for i,k in enumerate(self.key):
                if k != "PrixHTVA":
                    if i < int(len(self.key)/2):
                        Label(self.frmRecherche, text = "%s :" %(k) ,bg =CouleurBlanc).grid(row = i+1, column = 0, padx = 20, pady = 1)
                    else:
                        Label(self.frmRecherche, text = "%s :" %(k) ,bg =CouleurBlanc).grid(row = i-int(len(self.key)/2), column = 2, padx = 20, pady = 1)
                else:
                    Label(self.frmRecherche, text = "PrixMin :" ,bg =CouleurBlanc).grid(row = 5, column = 0, padx = 20, pady = 1)
                    Label(self.frmRecherche, text = "PrixMax :" ,bg =CouleurBlanc).grid(row = 5, column = 2, padx = 20, pady = 1)
                    self.minPrixfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = 21)
                    self.maxPrixfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = 21)  
            self.idVetfrRech =ttk.Combobox(self.frmRecherche,width = 20,values = [vetm.idVet for vetm in self.parent.stock.lstVetement])     
            self.tvafrRech =ttk.Combobox(self.frmRecherche,width = 20,values = sorted(self.parent.stock.lstNonRep()["tva"]))
            self.libfrRech =ttk.Combobox(self.frmRecherche,width = 20,values = [vetm.libelle for vetm in self.parent.stock.lstVetement])
            self.quantfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = 21)
            self.MarquefrRech =ttk.Combobox(self.frmRecherche,width = 20, values = self.parent.stock.lstNonRep()["marque"])
            self.taillefrRech =ttk.Combobox(self.frmRecherche,width = 20,values = self.parent.stock.lstNonRep()["taille"])
            self.catfrRech =ttk.Combobox(self.frmRecherche,width = 20,values = self.parent.stock.lstNonRep()["cat"])
            self.couleurfrRech =ttk.Combobox(self.frmRecherche,width = 20,values = self.parent.stock.lstNonRep()["color"])
            lstCombo = [self.idVetfrRech,self.libfrRech,self.MarquefrRech,self.quantfrRech,self.minPrixfrRech, self.tvafrRech,self.taillefrRech,self.catfrRech,\
                self.couleurfrRech,self.maxPrixfrRech]
            for i,w in enumerate(lstCombo):
                if i < int(len(lstCombo)/2):
                    w.grid(row = i+1, column = 1,padx = 20, pady = 1)
                else:
                    w.grid(row = i-int(len(lstCombo)/2)+1, column = 3,padx = 20, pady = 1)
                w.bind("<Return>", self.recherche)
            ttk.Button(self.frmRecherche, text ="Confirmer" , command = self.recherche).grid(row = 0, rowspan = 7, column = 4)
            

if __name__ == "__main__":
    _stock = Stock()
    _Historique = HistoriqueInOut()
    _emp = tableEmployee()

    #Data test 
    Color = ["Rouge","Vert","Bleu","Gris","Arc-En-Ciel","Noir","Rose"]
    Cat =["Sport","Femme","Homme","Enfant","intello","baraki"]
    tva =[21.0,6.0,12.5]
    size = ["S","XS","M","L","XL","XXL","XXL"]
    for i in range(145):
        _stock + Vetement(5414+i,"Lib%s" %(i),"Marque %s" %(i),choice(Color),choice(Cat),randrange(145),choice(tva),50+i, choice(size),randrange(50))
    
    #print(_stock.lstVetement[-1])

     
    mainFen = baseRoot(_stock, _Historique, _emp)

    mainFen.mainloop() 