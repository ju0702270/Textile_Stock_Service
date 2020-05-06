# -*- coding: utf-8 -*-
## author : Rochez Justin,Dif Nassim, Becquet Emilien
"""
interface
--------------------------
Ce document est le document main à lancer pour faire fonctionner la solution
"""
from tkinter import ttk,messagebox,Tk,X,BOTH,Y,Frame,GROOVE,Button,LEFT
from framelogin import User,FrmAcceuil
from framegestionstock import FrmStock
from framevente import FrmVente
from common import Stock,HistoriqueInOut,tableEmployee,Vetement,Ensemble
from pathlib import Path
#importTest
from random import choice,randrange
directory = Path(__file__).parent
########Global########## 
CouleurBlanc = "#FFFFFF"
CouleurBleu ="#33b8ff"
CouleurGris = "#989898"

widthSpinBox = 21
widthEntry = 23
widthLabel = 20
widthCombo = 20

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
        self.iconbitmap("{}\\TSS_logo-ConvertImage.ico".format(directory))
        self.frPosn = Frame(self) # Ceci est la Frame qui va permettre que le programme soit correctement centré
        self.frPosn.pack(side=LEFT)
        ###### Frame en bas à gauche avec le choix des menus Vente, stat etc
        self.frmMenu = Frame(self.frPosn, bg = CouleurBleu,relief = GROOVE, border = 2)
        self.frmMenu.grid(row = 1, column = 0, ipadx = 5 , ipady = 13)
        Frame(self.frmMenu,height = 30,bg = CouleurBleu).pack()
        self.btV=Button(self.frmMenu,text = "Vente",command = self.switchFrameV, bg = CouleurBlanc, relief = GROOVE, width = 20)
        self.btV.pack(pady= 2)
        self.btS=Button(self.frmMenu,text = "Gestion_Stock",command = self.switchFrameS, bg = CouleurGris, relief = GROOVE, width = 20)
        self.btS.pack(pady= 2)
        self.btStat=Button(self.frmMenu,text = "Statistique",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20)
        self.btStat.pack(pady= 2)
        self.btE=Button(self.frmMenu,text = "Gestion_employé",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20)
        self.btE.pack(pady= 2)
        
        ##### ici c'est uyn peu la base de données du programme avec 3 grosses tables
        self.stock = stockVetement
        self.Historique = Historique
        self.employe = tableEmp 
        
        # Init de la Frame des boutons Dans votre Class vous passer le parametre de l'objet baseroot vous placez les boutons principaux dans cette frame. 
        self.frmButton = Frame(self.frPosn, bg = CouleurBlanc, relief = GROOVE, border = 2)
        self.frmButton.grid(row = 0, column = 0, ipadx = 30 , ipady = 23)
       
        ###### Toutes les Class FRAME
        self.frm_Login = FrmAcceuil(self) 
        #self.frm_Login.pack(fill=X, expand=1)# Frame du Login (Emilien)
        self.frm_Vente = FrmVente(self)# Frame de la Gestion des ventes (???)
        #self.frm_Vente.pack()
        self.frm_Stock = FrmStock(self) #Frame de la gestion de stock ( Justin )
        #self.frm_Stock.pack(side = LEFT) 

        self.frm_Stat = "" # Frame de la gestion des statistiques (Nassim)
        self.frm_Employé = "" # Frame de la gestion des Employe (???)

        self.switchFrameV()



        

        
    

    def test(self):
        print("test interface")


    def switchFrameV(self):
        self.frm_Stock.frmButton.pack_forget()
        self.frm_Vente.frmButton.pack()
        self.btV.config(bg = CouleurGris)
        self.btS.config(bg = CouleurBlanc)
        self.frm_Stock.pack_forget()
        self.frm_Vente.pack(side = LEFT)
    
    def switchFrameS(self):
        self.frm_Vente.frmButton.pack_forget()
        self.frm_Stock.frmButton.pack()
        self.btS.config(bg = CouleurGris)
        self.btV.config(bg = CouleurBlanc)
        self.frm_Vente.pack_forget()
        self.frm_Stock.pack(side = LEFT)


if __name__ == "__main__":
    _stock = Stock()
    _Historique = HistoriqueInOut()
    _emp = tableEmployee()

    #Data test 
    Color = ["Rouge","Vert","Bleu","Gris","Arc-En-Ciel","Noir","Rose"]
    Cat =["Sport","Femme","Homme","Enfant","intello","baraki"]
    marque = ["Nike","Fila","DolceGabana","Audi","samsung","Sony","decomode","LaMarque"]
    tva =[21.0,6.0,12.5]
    size = ["S","XS","M","L","XL","XXL","XXL"]
    for i in range(145):
        _stock + Vetement(5414+i,"Lib%s" %(i),choice(marque),choice(Color),choice(Cat),randrange(145),choice(tva),50+i, choice(size),randrange(50))

    ens = Ensemble("AAAA","Ensemble Ete",[],50.0,21.0)
    ens.addVet(_stock.lstVetement[1])
    ens.addVet(_stock.lstVetement[2])
    ens.addVet(_stock.lstVetement[3])
    _stock + ens


  
        
    
    
    for i,v in enumerate(_stock.lstVetement[0:2]):
        v.lstAssorti.append(_stock.lstVetement[i])
       
    

    mainFen = baseRoot(_stock, _Historique, _emp)

    mainFen.mainloop() 
    