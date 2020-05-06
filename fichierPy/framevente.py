# -*- coding: utf-8 -*-
## author : Rochez Justin
"""
Frame de caisse enregistreuse
================================
Documentation
"""


########Import##########
from tkinter import Tk,Toplevel,Frame,LabelFrame,GROOVE,Label,Button,StringVar,X
from tkinter import messagebox, ttk

########Global########## 
CouleurBlanc = "#FFFFFF"
CouleurBleu ="#33b8ff"

widthSpinBox = 21
widthEntry = 23
widthLabel = 20
widthCombo = 20

########Class###########

class FrmVente(Frame):
    """C'est la Frame qui contient la gestion des ventes.
    """
    def __init__ (self,parent):
        """
        :param Frame: Tkiner.Frame
        :type Frame:Frame()
        :param stockVetement: c'est un objet stock contenant des vetements 
        :type stockVetement: Stock()
        :params parent: C'est la fenetre parent Dans notre cas ici, nous utilisons le plus souvent baseRoot
        :type parent: baseRoot()
        """
        Frame.__init__(self)
        self.parent = parent
        
        self.l = LabelFrame(self, text="Gestion des ventes", padx=10, pady=5)

        self.FrFond = Frame(self.l,relief = GROOVE, border = 2,  bg =CouleurBlanc)
        self.FrFond.pack (ipadx = 42, ipady =20)

        self.frmScan = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmScan.pack(fill = X, expand = 1)
        #self.frmAjout = Frame(self.FrFond, bg =CouleurBlanc)
        #self.frmModif =Frame(self.FrFond, bg =CouleurBlanc)

        self.key = ["Numéro d'article","Libéllé","Marque","Taille","Catégorie","Couleur","Quantité","PrixTVAC","Tva"]
        
        self.tree = ttk.Treeview(self.l, columns = [k for k in self.key[1:None]],height=13)
        for i,k in enumerate(self.key):
            self.tree.heading('#%s' %(i),text = k)
            if k[0] not in ["T","P","Q"]:
                self.tree.column('#%s' %(i), minwidth=130,width=130)
            else:
                self.tree.column('#%s' %(i), minwidth=63,width=63)  
       
        
        self.tree.pack()
        
        self.frmButton = Frame(self.parent.frmButton, bg = CouleurBlanc)
        Frame(self.frmButton,height = 30,bg = CouleurBlanc).pack()
        ttk.Button(self.frmButton, text = "Payer", command = self.test, width = 15).pack()
        ttk.Button(self.frmButton, text = "Vider Panier", command = self.test,width = 15).pack()
        ttk.Button(self.frmButton, text = "Supprimer article", command = self.test,width = 15).pack()
        ttk.Button(self.frmButton, text = "imprimer Ticket", command = self.test,width = 15).pack()
        #*************end Frame button*******
        #************Frame des bouton de Menu******
       
        #************end bouton de menu************
        self.info = StringVar()
        self.info.set("Aucune action effectuée")
        self.labInfo = Label(self.l,textvariable = self.info, bg = CouleurBlanc,width = 128,  anchor="w")
        self.labInfo.pack()
        self.l.grid(row = 0, rowspan =2, column = 1)

        #***********Remplissage de la Frame frmScan****
        Label(self.frmScan,text= "Numéro d'article :",bg =CouleurBlanc,width =widthLabel, anchor="w").grid(column = 0, row = 0,padx = 20, pady = 1)
        Label(self.frmScan,text= "Quantité :",bg =CouleurBlanc,width =widthLabel, anchor="w").grid(column = 0, row = 1,padx = 20, pady = 1)
        self.idVetEntry = ttk.Combobox(self.frmScan,width = widthCombo,values = [vetm.idVet for vetm in self.parent.stock.lstVetement])
        self.idVetEntry.grid(column = 1, row = 0,padx = 20, pady = 1)
        self.quantEntry = ttk.Entry(self.frmScan,width = widthEntry)
        self.quantEntry.grid(column = 1, row = 1,padx = 20, pady = 1)
        ttk.Button(self.frmScan, text ="Scanner" , command = self.test).grid(row = 0, rowspan = 2, column = 2)

    def test(self):
        print("test ok")
    
    def openStock(self):
        self.pack_forget()
        self.parent.frm_Stock.pack()
        
if __name__ == "__main__":
    pass   