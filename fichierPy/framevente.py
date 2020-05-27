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
from copy import deepcopy
from common import Stock,datetime
from os import path
import sys
from decimal import Decimal ,ROUND_HALF_UP
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
        self.ticket = Stock()
        
        self.l = LabelFrame(self, text="Gestion des ventes", padx=10, pady=5)

        self.FrFond = Frame(self.l,relief = GROOVE, border = 2,  bg =CouleurBlanc)
        self.FrFond.pack (ipadx = 223, ipady =20)

        self.frmScan = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmScan.pack(fill = X, expand = 1)
        #self.frmAjout = Frame(self.FrFond, bg =CouleurBlanc)
        #self.frmModif =Frame(self.FrFond, bg =CouleurBlanc)

        self.key = ["Numéro d'article","Libéllé","Marque","Taille","Catégorie","Couleur","Quantité","PrixTVAC","Tva"]
        
        
        self.tree = ttk.Treeview(self.l, columns = [k for k in self.key[1:None]],height=10)
        for i,k in enumerate(self.key):
            self.tree.heading('#%s' %(i),text = k)
            if k[0] not in ["T","P","Q","C"]:
                self.tree.column('#%s' %(i), minwidth=129,width=129)
            else:
                self.tree.column('#%s' %(i), minwidth=85,width=85)  
       
        
        self.tree.pack()
       
        
        self.frmButton = Frame(self.parent.frmButton, bg = CouleurBlanc)
        Frame(self.frmButton,height = 30,bg = CouleurBlanc).pack()
        ttk.Button(self.frmButton, text = "Payer", command = self.Payer, width = 15).pack()
        ttk.Button(self.frmButton, text = "Vider Panier", command = self.viderPanier,width = 15).pack()
        ttk.Button(self.frmButton, text = "Supprimer article", command = self.supprimerArticle,width = 15).pack()
        ttk.Button(self.frmButton, text = "imprimer Ticket", command = self.printTicket,width = 15).pack()
        #*************end Frame button*******
        #************Frame des bouton de Menu******
       
        #************end bouton de menu************
        self.info = StringVar()
        self.info.set("Aucune action effectuée")
        self.frmFooter = Frame(self.l)
        self.frmFooter.pack()
        self.labInfo = Label(self.frmFooter,textvariable = self.info, bg = CouleurBlanc,width = 89, relief = "ridge", height= 4)
        self.labInfo.grid(row = 0, column = 0)

        self.frmPrice = Frame(self.frmFooter, relief = GROOVE, border = 2)
        self.frmPrice.grid(row = 0, column = 1)

        self.FooterHTVA = StringVar()
        self.FooterHTVA.set("0.00")
        self.FooterTVAC = StringVar()
        self.FooterTVA = StringVar()

        
        for i,total in enumerate(["Total HTVA:","Total TVAC:","Coût TVA:"]):
            Label(self.frmPrice,text = total,bg = CouleurBlanc, width = 18).grid(row = i, column = 0)
        
        Label(self.frmPrice, textvariable = self.FooterHTVA,bg = CouleurBlanc, width = 13).grid(row = 0,column = 1)
        Label(self.frmPrice, textvariable = self.FooterTVAC,bg = CouleurBlanc, width = 13).grid(row = 1,column = 1)
        Label(self.frmPrice, textvariable = self.FooterTVA,bg = CouleurBlanc, width = 13).grid(row = 2,column = 1)
        for i in range(3):
            Label(self.frmPrice,text= "€",bg = CouleurBlanc, width = 3).grid(row = i, column = 2)
        
        
        self.l.grid(row = 0, rowspan =2, column = 1)

        #***********Remplissage de la Frame frmScan****
        Label(self.frmScan,text= "Numéro d'article :",bg =CouleurBlanc,width =widthLabel, anchor="w").grid(column = 0, row = 0,padx = 20, pady = 1)
        Label(self.frmScan,text= "Quantité :",bg =CouleurBlanc,width =widthLabel, anchor="w").grid(column = 0, row = 1,padx = 20, pady = 1)
        self.lstArticle =[vetm.idVet for vetm in self.parent.stock.lstVetement]
        for e in self.parent.stock.lstEnsemble:
            self.lstArticle.append(e.idEns)
        self.idVetEntry = ttk.Combobox(self.frmScan,width = widthCombo,values = self.lstArticle)
        self.idVetEntry.grid(column = 1, row = 0,padx = 20, pady = 1)
        self.idVetEntry.bind("<Return>",self.addObjet)
        self.quantEntry = ttk.Entry(self.frmScan,width = widthEntry)
        self.quantEntry.grid(column = 1, row = 1,padx = 20, pady = 1)
        self.quantEntry.bind("<Return>",self.addObjet)
        ttk.Button(self.frmScan, text ="Scanner" , command = self.addObjet).grid(row = 0, rowspan = 2, column = 2)

    def test(self):
        print("test ok")

    def supprimerArticle(self):
        """fonction de suppression d'un article de la treeview
        """
        #print(self.tree.item(self.tree.focus())["text"])
        try:
            obj = self.ticket.get(self.tree.item(self.tree.focus())["text"])
            if messagebox.askyesno(title= "Suppression",message= "Souhaitez vous supprimer {} du ticket?".format(obj.libelle)):
                self.ticket - obj
                self.showTicket()
        except:
            messagebox.showerror(title="Erreur",message="Erreur dans la suppression")
        

    def viderPanier(self):
        """Fonction de remise à zero du ticket et de la treeview, on recommence à Zero
        """
        self.ticket = Stock()
        self.showTicket()
        self.info.set("Panier Vidé à {}".format(datetime.now()))

    def addObjet(self, event = None):
        """Methode d'ajout d'un objet vetement ou ensemble dans le self.ticket, sans redondance et sans toucher au stock
        """
        obj = self.parent.stock.get(self.idVetEntry.get())
        try:
            if obj is not None:
                copyObj= deepcopy(obj)
                copyObj.quantite = int(self.quantEntry.get())
                quant = 0
                if self.ticket.get(0,copyObj) is not None:
                    quant = self.ticket.get(0,copyObj).quantite
                if obj.quantite >= quant and copyObj.quantite+quant <= obj.quantite:
                    self.ticket + copyObj
                    self.showTicket()
                    self.info.set("Dernier article encodé :{}\nPrix unitaire HTVA : {}\nQuantité :{}".format(copyObj.libelle,copyObj.prixHTVA,copyObj.quantite))
                else:
                    if obj.quantite == 0:
                        messagebox.showinfo(title="Stock à 0", message="rupture de stock pour {}.\nVeuillez en recommander.".format(obj.libelle))
                    else:
                        messagebox.showinfo(title="Pas assez de stock", message="Il reste {} {} en stock seulement.\nVeuillez changer votre quantité.".format(obj.quantite,obj.libelle))       
        except: 
            messagebox.showerror(title="Error", message="La quantité doit être un entier")    
       
            

    def showTicket(self):
        """Méthode pour remettre à jour le contenu de la Treeview self.tree par le contenu nouveau du ticket, et adaptation des self.FooterHTVA, self.FooterTVAC,self.FooterTVA
        """
        self.tree.delete(*self.tree.get_children())
        for v in self.ticket.lstVetement:
            self.tree.insert('', 'end' ,None, text=v.idVet,values = [v.libelle,v.marque, v.taille,v.categorie, \
                        v.couleur,v.quantite,v.prixTVAC(),v.tauxTVA])
        for v in self.ticket.lstEnsemble:
            ens = self.tree.insert('', 'end' ,None, text=v.idEns,values = [v.libelle,'','','','',v.quantite,v.prixTVAC(),v.tauxTVA])
            for o in v.lstVetement:
                self.tree.insert(ens, 'end' ,None, text=o.idVet,values = [o.libelle,o.marque, o.taille,o.categorie, o.couleur, o.quantite,o.prixTVAC(), o.tauxTVA])
        self.FooterHTVA.set(self.ticket.calculValeur())
        self.FooterTVAC.set(self.ticket.calculTVAC())
        self.FooterTVA.set(self.ticket.coutTVA())

    def Payer(self):
        """Méthode d'affichage d'un message d'alerte contenant une vue du ticket de caisse. Afin de faire payer le client. 
        Adaptation du Stock, et mise à jour de l'historique avec de nouvelle transaction, et vidange du panier
        """
        if messagebox.askyesno(title="imprimer?", message= "Voulez-vous imprimer le ticket?"):
            self.printTicket()
        messagebox.showinfo(title="Mon Ticket", message=self.StrTicket())
        for v in self.ticket.lstVetement:
            self.parent.stock.get(v.idVet).quantite -= v.quantite
            self.parent.Historique.Out(v,v.quantite)
        for e in self.ticket.lstEnsemble:
            self.parent.stock.get(e.idEns).quantite -= e.quantite
            self.parent.Historique.Out(e,e.quantite)
        self.viderPanier()
    
    def printTicket(self):
        """methode de creation d'un ticket de caisse dans la rubrique Ticket
        """
        pathTicket = path.dirname(sys.path[0])
        now = datetime.now().strftime("%Y %b_%d %Hh%Mm%Ss")
        fichier =open("{}\\Ticket\\{}.txt".format(pathTicket,now),"w")
        fichier.write(self.StrTicket())
        fichier.close

        

    def StrTicket(self):
        """Methode d'écriture du ticket de caisse

        :return: la chaine de caractère du ticket complet
        :rtype: String
        """
        now = datetime.now().strftime("%Y %b_%d %Hh%Mm%Ss")
        MonTicket += "\n%-70s" %(now)
        MonTicket += "\n%-3s%2s%-8s%2s%-37s%2s%7s%2s%7s" %("Qty"," ","Id"," ","Libelle"," ","P.U."," ",'Total')
        MonTicket += "\n%s" %("----------------------------------------------------------------------")
        for v in self.ticket.lstVetement:
            MonTicket += "\n%-3s%2s%-8s%2s%-37s%2s%7s%2s%7s" %(v.quantite," ",v.idVet," ",v.libelle," ",Decimal(v.prixHTVA).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)\
                ," ",Decimal(v.prixHTVA*v.quantite).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        for e in self.ticket.lstEnsemble:
            MonTicket += "\n%-3s%2s%-8s%2s%-37s%2s%7s%2s%7s" %(e.quantite," ",e.idEns," ",e.libelle," ",Decimal(e.prixHTVA).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)\
                ," ",Decimal(e.prixHTVA*e.quantite).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
            for v in e.lstVetement:
                MonTicket += "\n%3s%2s%8s%4s%-35s%2s%7s%2s%7s" %(v.quantite," ",v.idVet," ",v.libelle," ",Decimal(v.prixHTVA).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)\
                    ," ",Decimal(v.prixHTVA*v.quantite).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        MonTicket += "\n%s" %("----------------------------------------------------------------------")
        MonTicket += "\n%30s%40s" %("Total TVAC",self.ticket.calculTVAC())
        return MonTicket


    def openStock(self):
        self.pack_forget()
        self.parent.frm_Stock.pack()
        
if __name__ == "__main__":
    pass