# -*- coding: utf-8 -*-
## author : Rochez Justin,Dif Nassim, Becquet Emilien
"""
Common
--------------------------
Document avec les différentes Class commune
Il représente la base du programme.
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
from datetime import datetime
from decimal import Decimal ,ROUND_HALF_UP
import copy
###########Variables globales #############


##########Fin variables globales###########



class Stock:
    """La Class Stock contient tout les objets Vetements. C'est un peux la Table principale du programme
    """
    def __init__(self):
        self.lstVetement = [] #Liste contenant tout les vetements du stock. 
        self.lstEnsemble = [] #Liste contenant tout les ensembles du stock. ATTENTION un ensemble est constitué de vetements. C'est une composition
        


    def __add__(self, vetement):
        """ Ajoute un vetement à la liste sans risque d'avoir 2 fois le même vetement (suivant l'idVet)
        ex: Stock + vetement = Stock.lstVetement.append(vetement) à condition que le EAN du vetements ne soit pas déja dans la liste. 
        
        :param vetement: Le vetements qu'on ajoute OU Ensemble 
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
        elif isinstance(vetement,Ensemble):
            if len(self.lstEnsemble) == 0:
                self.lstEnsemble.append(vetement)
            elif str(vetement.idEns) not in [str(e.idEns) for e in self.lstEnsemble]:
                self.lstEnsemble.append(vetement) 
            else:
                for ens in self.lstEnsemble:
                    if str(ens.idEns) == str(vetement.idEns):
                        ens.quantite += vetement.quantite
                        break
    
    def __sub__(self,obj):
        if obj in self.lstVetement:
            self.lstVetement.remove(obj)
        elif obj in self.lstEnsemble:
            self.lstEnsemble.remove(obj)
            

    def get(self, id,obj = None):
        """récupere un obj Vetement ou Ensemble dans le stock

        :param id: id du vetment ou Ensemble
        :type id: string
        :return: objet Vetement/Ensemble
        :rtype: Vetement/Ensemble
        """        
        if obj is not None:
            if isinstance(obj,Vetement):
                id = obj.idVet
            elif isinstance(obj,Ensemble):
                id = obj.idEns
        if str(id) in [str(v.idVet) for v in self.lstVetement]:
            for Vet in self.lstVetement:
                if str(Vet.idVet) == str(id):
                    return Vet
        elif str(id) in [str(e.idEns) for e in self.lstEnsemble]:
            for ens in self.lstEnsemble:
                if ens.idEns == str(id) : 
                    return ens

    def calculValeur(self):
        """Calcul de la valeur total du stock HTVA

        :return: la valeur monétaire du stock HTVA
        :rtype: Decimal
        """        
        valeurStock = 0
        for vtm in self.lstVetement:
            valeurStock += vtm.quantite * vtm.prixHTVA
        for ens in self.lstEnsemble:
            valeurStock += ens.quantite * ens.prixHTVA
        return Decimal(valeurStock).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

    def calculTVAC(self):
        """Fonction qui calcul le prix TVAC total du stock

        :return: le prix TVAC du stock
        :rtype: decimal
        """
        prixTVAC= 0
        for v in self.lstVetement:
            prixTVAC += v.prixTVAC()*v.quantite
        for e in self.lstEnsemble:
            prixTVAC += e.prixTVAC()*e.quantite
        return Decimal(prixTVAC).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

    def coutTVA(self):
        """fonction qui renvoi le cout total de la TVA

        :return: le cout total de la TVA du stock
        :rtype: decimal
        """
        cout = 0
        for v in self.lstVetement:
            cout += v.coutTVA()*v.quantite
        for e in self.lstEnsemble:
            cout += e.coutTVA()*e.quantite
        return Decimal(cout).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

  
    def lstNonRep(self):
        """Cree un disctionnaire non répétitif de plusieurs attribut de stock
        
        :return: disctionnaire de marque, color,car,taille,tva
        :rtype: dict
        """
        lstNonRep = {}
        for a in ["marque","color","cat","taille","tva"]:
            lstNonRep[a]= []
        for v in self.lstVetement:
            if v.marque not in lstNonRep["marque"]:
                lstNonRep["marque"].append(v.marque)
            if v.couleur not in lstNonRep["color"]:
                lstNonRep["color"].append(v.couleur)
            if v.categorie not in lstNonRep["cat"]:
                lstNonRep["cat"].append(v.categorie)
            if v.taille not in lstNonRep["taille"]:
                lstNonRep["taille"].append(v.taille)
            if v.tauxTVA not in lstNonRep["tva"]:
                lstNonRep["tva"].append(v.tauxTVA)
        return lstNonRep


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
        le prix unitaire
        
        :return: retourne un prix 2 chiffres après la virgule
        :rtype: Decimal
        """
        return Decimal(self.prixHTVA * ((self.tauxTVA/100.0) + 1.0) * self.reduction).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    
    def coutTVA(self):
        """fonction de calcul du cout de la TVA pour une quantité de 1

        :return: le cout de la TVA
        :rtype: Decimal
        """
        return Decimal(float(self.prixTVAC())-self.prixHTVA).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)



class Ensemble:
    """à améliorer
    
    :return: [description]
    :rtype: [type]
    """
    def __init__(self,idEns, lib,lstVetement, quant =1):
        self.idEns= idEns
        self.libelle = lib
        self.lstVetement = lstVetement
        self.quantite = quant
        self.prixHTVA = self.calculPrixHTVA()

        self.reduction = 1

    def calculPrixHTVA(self):
        """calcul de la valeur de l'ensemble de vetement basé sur le prix HTVA de chaque vetement dans l'ensemble.

        :return: le prix HTVA de l'ensemble
        :rtype: float
        """
        prix = 0
        for v in self.lstVetement:
            prix +=v.prixHTVA*v.quantite
        return prix

    def addVet(self,objVet,quant =1):
        if isinstance(objVet, Vetement):
            copyVet= copy.deepcopy(objVet)
            if objVet.quantite >= quant:
                copyVet.quantite = quant
                objVet.quantite -= quant
                if len(self.lstVetement) == 0:
                    self.lstVetement.append(copyVet)
                elif str(copyVet.idVet) not in [str(v.idVet) for v in self.lstVetement]:
                    self.lstVetement.append(copyVet) 
                else:
                    for vetm in self.lstVetement:
                        if str(vetm.idVet) == str(copyVet.idVet):
                            vetm.quantite += copyVet.quantite
                            break
                self.tva()
            self.prixHTVA = self.calculPrixHTVA()
            

    def prixTVAC(self):
        """Fonction qui retroune le prixTVAC de l'ensemble

        :return: une prix TVAC
        :rtype: Decimal
        """
        return Decimal(self.prixHTVA * ((self.tauxTVA/100.0) + 1.0) * self.reduction).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    
    def tva(self):
        """Fonction qui attribue le taux de TVA le plus élevé de la lstVetement
        """
        self.tauxTVA=sorted([v.tauxTVA for v in self.lstVetement])[-1]
    
    def coutTVA(self):
        """fonction de calcul du cout de la TVA pour une quantité de 1

        :return: le cout de la TVA
        :rtype: Decimal
        """
        return Decimal(float(self.prixTVAC())-self.prixHTVA).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)


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

    def In(self, Vetement,quant=1):
        """Methode d'incrémentation de la lstInOutStock en ajoutant un objet InOutStock. 
        Utilisation de copy.deepcopy afin de copier l'objet Vetement et pouvoir changer son état sans toucher au reel Vetement.

        :param Vetement: c'est le vetement qu'on entre dans le stock
        :type Vetement: Vetement()
        :param quant: la quantité du Vetement
        :type quant: int
        """      
        copyVet =  copy.deepcopy(Vetement)
        copyVet.quantite = int(quant)
        self.idInOut +=1
        self.lstInOutStock.append(InOutStock(self.idInOut, True, copyVet))
            
    def Out(self, Vetement,quant=1):
        """Methode d'incrémentation de la lstInOutStock en ajoutant un objet InOutStock. 
        Utilisation de copy.deepcopy afin de copier l'objet Vetement et pouvoir changer son état sans toucher au reel Vetement.

        :param Vetement: c'est le vetement qu'on sort du stock
        :type Vetement: Vetement()
        :param quant: la quantité du Vetement
        :type quant: int
        """        
        copyVet =  copy.deepcopy(Vetement)
        copyVet.quantite = int(quant)
        self.idInOut +=1
        self.lstInOutStock.append(InOutStock(self.idInOut, False, copyVet))
        


class InOutStock:
    """Les Object de transaction. à chaque entrée ou sortie de stock un object InOutStock doit être crée
    """
    def __init__(self, numId, InOut, vetm):
        self.intNumInOutStock = numId
        self.dateTime = datetime.now()
        self.vetement = vetm
        self.InOut = InOut #True = In False = Out
        #self.quantHist = quant
    
    def juTestStr(self):
        return str("ID: %s\nDateTime : %s\nVetement : %s\nIn ou Out : %s" %(self.intNumInOutStock,self.dateTime,self.vetement,self.InOut))


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
