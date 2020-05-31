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
from framestatintegration import FrmStat
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
    :param _stockement: c'est un objet stock contenant des vetements 
    :type _stockement: Stock()
    :param Historique: c'est l'historique de toute les transactions
    :type Historique: HistoriqueInOut()
    """
    def __init__(self,_stockement, Historique, tableEmp):
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
        self.btStat=Button(self.frmMenu,text = "Statistique",command = self.switchFrameStat, bg = CouleurBlanc, relief = GROOVE, width = 20)
        self.btStat.pack(pady= 2)
        self.btE=Button(self.frmMenu,text = "Gestion_employé",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20)
        self.btE.pack(pady= 2)
        
        ##### ici c'est uyn peu la base de données du programme avec 3 grosses tables
        self.stock = _stockement
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

        self.frm_Stat = FrmStat(self) # Frame de la gestion des statistiques (Nassim)
        self.frm_Employé = "" # Frame de la gestion des Employe (???)

        self.switchFrameStat()



        

        
    

    def test(self):
        print("test interface")

    def switchFrameStat(self):
        self.frm_Stock.frmButton.pack_forget()
        self.frm_Vente.frmButton.pack_forget()
        self.frm_Stat.frmButton.pack()

        self.btV.config(bg = CouleurBlanc)
        self.btS.config(bg = CouleurBlanc)
        self.btStat.config(bg = CouleurGris)

        self.frm_Stock.pack_forget()
        self.frm_Vente.pack_forget()
        self.frm_Stat.pack(side = LEFT)



    def switchFrameV(self):
        self.frm_Stock.frmButton.pack_forget()
        self.frm_Stat.frmButton.pack_forget()
        self.frm_Vente.frmButton.pack()

        self.btV.config(bg = CouleurGris)
        self.btS.config(bg = CouleurBlanc)
        self.btStat.config(bg = CouleurBlanc)

        self.frm_Stock.pack_forget()
        self.frm_Stat.pack_forget()
        self.frm_Vente.pack(side = LEFT)
    
    def switchFrameS(self):
        self.frm_Vente.frmButton.pack_forget()
        self.frm_Stat.frmButton.pack_forget()
        self.frm_Stock.frmButton.pack()

        self.btS.config(bg = CouleurGris)
        self.btV.config(bg = CouleurBlanc)
        self.btStat.config(bg = CouleurBlanc)

        self.frm_Vente.pack_forget()
        self.frm_Stat.pack_forget()
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


    
    for i in range(20):
         _stock + Ensemble("AA{}".format(i),"Ensemble Ete",[])
         _stock.lstEnsemble[-1].addVet(_stock.lstVetement[randrange(0,len(_stock.lstVetement))])
         _stock.lstEnsemble[-1].addVet(_stock.lstVetement[randrange(0,len(_stock.lstVetement))])
         _stock.lstEnsemble[-1].addVet(_stock.lstVetement[randrange(0,len(_stock.lstVetement))])

    

  
        
    
    
    for i,v in enumerate(_stock.lstVetement[0:2]):
        v.lstAssorti.append(_stock.lstVetement[i])
    
    jeans = Vetement(1110,"jeans","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
    pull = Vetement(1111,"pull","adidas","vert","haut",28.0,21.0,15.0,"xs",100)
    blouse = Vetement(2222,"blouse","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
    pantalon = Vetement(3333,"pantalon","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
    robe = Vetement(4444,"robe","adidas","vert","haut",28.0,21.0,15.0,"xs",200)

    jupe = Vetement(5555,"jupe","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
    chemise = Vetement(6666,"chemise","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)
    sweat = Vetement(7777,"sweat","adidas","vert","haut",28.0,21.0,15.0,"xs",200)
    costume = Vetement(8888,"costume","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)
    cravate = Vetement(9999,"cravate","nike","bleu","bas",50.0,21.0,25.0,"xxl",100)

    tailleur = Vetement(1010,"tailleur","adidas","vert","haut",28.0,21.0,15.0,"xs",200)
    uniforme = Vetement(1011,"uniforme","tachini","rouge","manteau",70.0,21.0,30.0,"m",500)


    _stock+jeans
    _stock+pull
    _stock+blouse
    _stock+pantalon
    _stock+robe

    _stock+jupe
    _stock+chemise
    _stock+sweat
    _stock+costume
    _stock+cravate

    _stock+tailleur
    _stock+uniforme


    _Historique.Out(blouse,10)
    _Historique.Out(pull)
    _Historique.Out(pull)
    _Historique.Out(pull)
    _Historique.Out(pull)
    _Historique.Out(blouse,40)
       
    

    mainFen = baseRoot(_stock, _Historique, _emp)

    mainFen.mainloop() 
    