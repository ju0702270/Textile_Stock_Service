# -*- coding: utf-8 -*-
## author : Rochez Justin,Dif Nassim, Becquet Emilien
"""
Commom
--------------------------
Document avec les différentes Class commune
Consigne: 
-Ne rien supprimer sans l'accord des 2 autres.  au pire on mets en commentaire
-Toutes modifications doit être vraiment bien testée. (ex: on améliore des lignes de code)
-Ajouter est permis et encoragé. Attention à ne pas creer des fonctions ou procédure déja créée. 

-Votre Code doit être commenté correctement. 
-2 espaces entre les classe et 1 espace entre les fonctions et procedure. 
-Toutes les library se trouve en haut dans Import de library
-Toutes les variables globales dans Variables Global (on en utilise le moins possible)

-Ne dépassez pas les 170 caractères sur une ligne (pour rester lisible)

"""
##########Import de library ##############
from tkinter import ttk,messagebox,Tk
from decimal import Decimal,ROUND_HALF_UP
from datetime import datetime

###########Variables globales #############
CouleurBlanc = "#FFFFFF"

##########Fin variables globales###########

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
        self.frm_Stock = "" #Frame de la gestion de stock ( Justin )
        self.frm_Stat = "" # Frame de la gestion des statistiques (Nassim)
        self.frm_Vente = "" # Frame de la Gestion des ventes (???)
        self.frm_Employé = "" # Frame de la gestion des Employe (???)


class Stock:
    """La Class Stock contient tout les objets Vetements. C'est un peux la Table principale du programme
    """
    def __init__(self):
        self.lstVetement = [] #Liste contenant tout les vetements du stock. 
        self.lstEnsemble = [] #Liste contenant tout les ensembles du stock. ATTENTION un ensemble est constitué de vetements. C'est une composition
        

    def __add__(self, vetement):
        """ Ajoute un vetement à la liste sans risque d'avoir 2 fois le même vetement (suivant l'idVet)
        ex: Stock + vetement = Stock.lstVetement.append(vetement) à condition que le EAN du vetements ne soit pas déja dans la liste. 
        
        :param vetement: Le vetements qu'on ajoute
        :type vetement: Vetement
        """
        if isinstance(vetement,Vetement):
            if len(self.lstVetement) == 0:
                self.lstVetement.append(vetement)
            elif str(vetement.idVet) not in [str(v.idVet) for v in self.lstVetement]:
                self.lstVetement.append(vetement) 
            else:
                for vetm in self.lstVetement:
                    if str(vetm.idVet) == str(vetement.idVet):
                        vetm.quantite += vetement.quantite
                        break

    def calculValeur(self):
        valeurStock = 0
        for vtm in self.lstVetement:
            valeurStock += vtm.quantite * vtm.prixHTVA
        return valeurStock 


class Vetement:
    """class qui représente le vêtement, les objets Vetements sont la base du programme
    """
    def __init__(self,idVet,strLibelle, strMarque,  strCouleur, strCategorie, dblPrixHTVA, dblTauxTVA,dblPrixAchat, taille = "Unique",Quantite =1,lstAssorti = []):
        
        self.idVet= idVet #numero EAN unique à chaque Vetement
        self.libelle =strLibelle
        self.marque= strMarque
        self.couleur= strCouleur
        self.categorie = strCategorie
        self.prixHTVA = float(dblPrixHTVA)
        self.tauxTVA = float(dblTauxTVA)
        self.prixAchat = float(dblPrixAchat)
        self.taille = taille
        self.quantite =int(Quantite)
        self.lstAssorti = lstAssorti #Le vetement self est bien assorti avec lstAssorti

        self.reduction = 1 # si reduction, par défault = 1

    def __str__(self):
        """Utile pour afficher tous les attributs du Vetement. 
        par Exemple lors d'un messagebox.showinfo
        :return: La plupart des attributs du vetement chacun à la ligne
        :rtype: str
        """
        return "Article:\nEAN : %s\nLibelle : %s\nMarque : %s\nQuantité : %s\nPrix : %s\nTaille : %s\nCatégorie : %s\nCouleur : %s"\
            %(self.idVet,self.libelle,self.marque,self.quantite,self.prixTVAC(),self.taille,self.categorie,self.couleur)
    
    def prixTVAC(self):
        """retourne le prix TVAC arrondi 2 chiffres après la virgule
        
        :return: retourne un prix 2 chiffres après la virgule
        :rtype: Decimal
        """
        return Decimal(self.prixHTVA * ((self.tauxTVA/100.0) + 1.0) * self.reduction).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)


class Ensemble:
    """à améliorer
    
    :return: [description]
    :rtype: [type]
    """
    def __init__(self,lstVetement,prixHTVA,tauxTVA):
        self.lstVetement = lstVetement
        self.prixHTVA = prixHTVA
        self.tauxTVA = tauxTVA

        self.reduction = 1

    def prixEnsemble(self):
        return self.prixHTVA * ((self.tauxTVA / 100) + 1) * self.reduction


class HistoriqueInOut:
    """Class conteneur, qui contient tout les lignes de transaction d'entrée et sortie de stock
    """
    def __init__(self):
        """:param self.idInOut = le numéro de la ligne, elle est unique dans la table HistoriqueInOut
        :param self.lstInOutStock = La liste contenant tout les Objet InOutStock
        :param self.lstLog = La liste contenant tout les Objet LogInOut 
        """
        self.idInOut = 0
        self.lstInOutStock= []
        self.lstLog =[]

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


class LogInOut:
    """les object de Log in ou Log out, a chaque fois qu'un employée se connecte ou se déconnecte on en crée un
    """
    def __init__(self, numId, InOut, emp):
        self.intNumLog = numId
        self.dateTimeLog = datetime.now()
        self.employee = emp
        self.InOut = InOut

class tableEmployee:
    """à définir
    """
    def __init__(self):
        self.lstEmp = []

class Employe:
    """a définir
    """
    pass


class Admin(Employe):
    """a définir
    
    :param Employe: [description]
    :type Employe: [type]
    """
    def __init__(self):
        super.__init__(self)


if __name__ == "__main__":
    pass