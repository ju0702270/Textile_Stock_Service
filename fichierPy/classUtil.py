# -*- coding: utf-8 -*-
## author : Rochez Justin,Dif Nassim, Becquet Emilien

from decimal import Decimal ,ROUND_HALF_UP

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

        self.lstAllElement=[self.idVet, self.libelle,self.marque,self.quantite,self.prixHTVA,self.tauxTVA,self.taille,self.categorie,self.couleur,self.lstAssorti]
    
    def updateLstAllElement(self):
        """ Effectue un update dynamique de lstAllElment
        """
        self.lstAllElement=[self.idVet, self.libelle,self.marque,self.quantite,self.prixHTVA,self.tauxTVA,self.taille,self.categorie,self.couleur,self.lstAssorti]

    def addVetAssort(self, vetm):
        """ fonction qui ajoute un vetement à la lstAssorti sans redondance
        """
        if vetm not in self.lstAssorti:
            self.lstAssorti.append(vetm)

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
