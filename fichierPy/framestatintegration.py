# -- coding : utf-8 --
## author : Dif Nassim
""" Package de la fentre des statistiques.
"""
## Import 
from tkinter import Tk,Toplevel,Frame,LabelFrame,GROOVE,Label,Button,StringVar,X,IntVar,Radiobutton,RIGHT
from tkinter import messagebox, ttk
from datetime import datetime,timedelta

########Global########## 
CouleurBlanc = "#FFFFFF"
CouleurBleu ="#33b8ff"

widthSpinBox = 21
widthEntry = 23
widthLabel = 20
widthCombo = 20



class FrmStat(Frame):
    """
    """
    def __init__ (self,parent):
        Frame.__init__(self)
        self.parent = parent
        self.l = LabelFrame(self, text="Statistiques", padx=10, pady=5)

        self.FrFond = Frame(self.l,relief = GROOVE, border = 2,  bg =CouleurBlanc)
        self.FrFond.pack (ipadx = 47, ipady =7)

        self.FrameE=Frame(self.FrFond, bg =CouleurBlanc)
        self.FrameE.pack(fill = X, expand = 1)
        self.construtFrameE()

        self.tree = ttk.Treeview(self.l,height=8)
        self.tree.pack()
        self.affichageFrameG()
        ######################################### Frame des boutons ##################################################
        self.frmButton = Frame(self.parent.frmButton, bg = CouleurBlanc)
        Frame(self.frmButton,height = 30,bg = CouleurBlanc).pack()
        ttk.Button(self.frmButton, text = "Exporter en Excel", command = self.test, width = 15).pack()
        ttk.Button(self.frmButton, text = "Daily Report", command = self.remplirTreeviewDailyReport,width = 15).pack() #command=lambda: remplirTreeviewDailyReport(stockVet, historiqueVente)
        ttk.Button(self.frmButton, text = "Top 10", command = self.remplirTreeviewTop10,width = 15).pack() #command=lambda: remplirTreeviewTop10(stockVet, historiqueVente)
        ttk.Button(self.frmButton, text = "Stock", command = self.remplirTreeviewStock,width = 15).pack() #lambda: remplirTreeviewStock(stockVet))
        ########################################Fin Frame des boutons ##############################################
        Frame(self.l, bg =CouleurBlanc).pack()
        self.valHtvaTotal =StringVar()
        self.valHtvaTotal.set("0.0")
        self.benefTotal=StringVar()
        self.benefTotal.set("0.0")
        self.depLabelTot=StringVar()
        self.depLabelTot.set("0.0")

        self.frameH=Frame(self.l, bg =CouleurBlanc,relief = GROOVE, border = 2)
        self.frameH.pack(side = RIGHT)
        self.affichageFrameH()

        self.remplirTreeview()

        self.l.grid(row = 0, rowspan =2, column = 1)
        #####################################Fin Interface########################################################

    def comparaisonString(self,chaineA,chaineB):
        try:
            chaineA = str.lower(chaineA)
            chaineB = str.lower(chaineB)
        except:
            pass
        caraB = 0
        try:
            for caraA in chaineA:
                if not (caraA == chaineB[caraB]):
                    return False
                caraB += 1
            return True
        except:
            if int(chaineA) != int(chaineB):
                return False
            else:
                return True

    def remplirTreeviewSearch(self):
        self.viderTreeview()
        lstSearch = self.rechercheVet()
        inout= None
        i = 1

        valHtvaTotal = 0.0
        benefTotal = 0.0
        depenseTotal = 0.0

        for ligne in lstSearch:
            if ligne.InOut == True:
                inout = "In"
            else:
                inout = "Out"
            self.tree.insert("", "end", text = inout, values=(ligne.vetement.idVet,ligne.vetement.libelle, ligne.vetement.quantite\
                , ligne.vetement.prixAchat,ligne.vetement.prixHTVA,  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
            valHtvaTotal += (ligne.vetement.prixHTVA*ligne.vetement.quantite)
            benefTotal += (((ligne.vetement.prixHTVA) - (ligne.vetement.prixAchat))*ligne.vetement.quantite)
            depenseTotal += (ligne.vetement.prixAchat*ligne.vetement.quantite)
            i += 1

        self.valHtvaTotal.set(valHtvaTotal)
        self.benefTotal.set(benefTotal)
        self.depLabelTot.set(depenseTotal)
        self.affichageFrameH()

    def rechercheVet(self):#listStock,listHisto,numArt,libelle,dateDebut,dateFin,taille,couleur,categorie,inOut
        listRech =[]

        numArt = self.entreeNumArt.get()
        libelle = self.entreeLibelle.get()
        dateDebut = str(self.entreeDateDeb.get())
        dateFin = str(self.entreeDateFin.get())
        taille = self.entreeTaille.get()
        couleur = self.entreeCouleur.get()
        categorie = self.entreeCategorie.get()

        #print(numArt)

        if self.inOutRadioButton.get() == 0:
            inOut=True
        else:
            inOut=False

        for ligneVet in self.parent.Historique.lstInOutStock:
            if ligneVet.InOut == inOut:
                if dateDebut =="" or dateFin=="" or (ligneVet.dateTime >= dateDebut and ligneVet.dateTime <= dateFin):
                    if (self.comparaisonString(numArt,ligneVet.vetement.idVet)) and self.comparaisonString(libelle,ligneVet.vetement.libelle)  \
                            and self.comparaisonString(taille,ligneVet.vetement.taille) \
                            and self.comparaisonString(couleur,ligneVet.vetement.couleur)\
                            and self.comparaisonString(categorie,ligneVet.vetement.categorie):

                        listRech.append(ligneVet)

        return listRech

    def remplirTreeviewStock(self):
        self.viderTreeview()
        i = 1
        inout = None
        valHtvaTotal = 0.0
        benefTotal = 0.0
        depenseTotal = 0.0

        for vet in self.parent.Historique.lstInOutStock:
            if vet.InOut == True:
                inout = "In"
            else:
                inout = "Out"
            self.tree.insert("", "end", text = inout, values=(vet.vetement.idVet,vet.vetement.libelle, vet.vetement.quantite, vet.vetement.prixAchat,\
                vet.vetement.prixHTVA,  vet.vetement.prixTVAC(), vet.dateTime))
            valHtvaTotal += (vet.vetement.prixHTVA*vet.vetement.quantite)
            benefTotal += (((vet.vetement.prixHTVA) - (vet.vetement.prixAchat))*vet.vetement.quantite)
            depenseTotal += (vet.vetement.prixAchat*vet.vetement.quantite)
            i += 1

        self.valHtvaTotal.set(valHtvaTotal)
        self.benefTotal.set(benefTotal)
        self.depLabelTot.set(depenseTotal)
        self.affichageFrameH()

    def dailyReport(self):
        listDaily = []
        dateToday = datetime.now()

        for ligne in self.parent.Historique.lstInOutStock:
            dateCommande = ligne.dateTime
            if dateCommande <= dateToday and dateCommande > (dateToday - timedelta(days=7)) and ligne.InOut==False:
                listDaily.append(ligne)

        return listDaily

    def remplirTreeviewDailyReport(self):
        self.viderTreeview()
        lstReport = self.dailyReport()
        i = 1
        valHtvaTotal = 0.0
        benefTotal = 0.0
        depenseTotal = 0.0

        for ligne in lstReport:
            self.tree.insert("", "end", text = i, values=(ligne.vetement.idVet ,ligne.vetement.libelle, ligne.vetement.quantite, ligne.vetement.prixAchat,\
                ligne.vetement.prixHTVA,  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
            valHtvaTotal += ligne.vetement.prixHTVA*ligne.vetement.quantite
            benefTotal += ((ligne.vetement.prixHTVA)-(ligne.vetement.prixAchat))*ligne.vetement.quantite
            depenseTotal += ligne.vetement.prixAchat*ligne.vetement.quantite
            i += 1

        self.valHtvaTotal.set(valHtvaTotal)
        self.benefTotal.set(benefTotal)
        self.depLabelTot.set(depenseTotal)
        self.affichageFrameH()


    def idVetLst(self,inOrOut):#stock,histo,inOrOut
        listIdVet =[]
        for vet in self.parent.stock.lstVetement:
            listIdVet.append([(vet),0])
        #print(listIdVet)

        for tupl in listIdVet:
            #print(tupl)
            for instInOut in self.parent.Historique.lstInOutStock:
            #   print(tupl[0])
                if instInOut.InOut == inOrOut and tupl[0].idVet == (instInOut.vetement).idVet:
                        tupl[1] += instInOut.vetement.quantite # à verifier
                        #print(tupl[1])

        return listIdVet
    
    def top10Vet(self):
        
        listClassement = self.idVetLst(False)
        i = 1

        while i < len(listClassement):
            k = i
            while k > 0 and listClassement[k][1] > listClassement[k - 1][1]:
                tuplTempo = listClassement[k]
                listClassement[k] = listClassement[k - 1]
                listClassement[k - 1] = tuplTempo
                k = k-1
            i = i+1


        if len(listClassement)<10:
            return listClassement[:len(listClassement)]

        else:
            return listClassement[:10]
    
    def remplirTreeviewTop10(self):
        self.viderTreeview()
        lstTop10 = self.top10Vet()
        #print(lstTop10)
        valHtvaTotal = 0.0
        benefTotal = 0.0
        depenseTotal = 0.0

        i = 1
        for tupl in lstTop10:
            self.tree.insert("", "end", text = i, values=(tupl[0].idVet,tupl[0].libelle, tupl[1], tupl[0].prixAchat,tupl[0].prixHTVA,  tupl[0].prixTVAC(), ""))
            valHtvaTotal += tupl[0].prixHTVA * tupl[1]
            benefTotal += ((tupl[0].prixHTVA)-(tupl[0].prixAchat)) * tupl[1]
            depenseTotal += tupl[0].prixAchat * tupl[1]
            i += 1

        self.valHtvaTotal.set(valHtvaTotal)
        self.benefTotal.set(benefTotal)
        self.depLabelTot.set(depenseTotal)
        self.affichageFrameH()


    def remplirTreeview(self):
        self.viderTreeview()

        i = 1

        valHtvaTotal = 0.0
        benefTotal = 0.0
        depenseTotal = 0.0

        for ligne in self.parent.Historique.lstInOutStock:
            self.tree.insert("", "end", text = i, values=(ligne.vetement.idVet ,ligne.vetement.libelle, ligne.vetement.quantite, ligne.vetement.prixAchat,ligne.vetement.prixHTVA,\
                  ligne.vetement.prixTVAC(), ligne.dateTime.strftime("%x")))
            valHtvaTotal += ligne.vetement.prixHTVA*ligne.vetement.quantite
            benefTotal += ((ligne.vetement.prixHTVA)-(ligne.vetement.prixAchat))*ligne.vetement.quantite
            depenseTotal += ligne.vetement.prixAchat*ligne.vetement.quantite
            i += 1

        self.valHtvaTotal.set(valHtvaTotal)
        self.benefTotal.set(benefTotal)
        self.depLabelTot.set(depenseTotal)
        self.affichageFrameH()
    
    def viderTreeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

       

    def affichageFrameH(self):
        self.frameH.pack()
        self.valTotalHTVA = Label(self.frameH, text="Valeur HTVA: %s" %(self.valHtvaTotal.get()),bg= CouleurBlanc, width= widthLabel)
        self.valTotalHTVA.grid(row=0, column=0, padx=20, pady=1)
        self.beneficeTotal = Label(self.frameH, text="Bénéfice total: %s" %(self.benefTotal.get()),bg= CouleurBlanc, width= widthLabel)
        self.beneficeTotal.grid(row=1, column=0, padx=20, pady=1)
        self.depenseTotal = Label(self.frameH, text="Dépenses: %s" %(self.depLabelTot.get()),bg= CouleurBlanc, width= widthLabel)
        self.depenseTotal.grid(row=2, column=0, padx=20, pady=1)

    def affichageFrameG(self):
        self.tree.pack()
        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        self.tree.column('#0' , minwidth=55,width=55)
        self.tree.column("1", width=122)
        self.tree.column("2", width=120)
        self.tree.column("3", width=122)
        self.tree.column("4", width=122)
        self.tree.column("5", width=117)
        self.tree.column("6", width=97)
        self.tree.column("7", width=155)

        self.tree.heading("1", text="idVet")
        self.tree.heading("2", text="Libellé")
        self.tree.heading("3", text="Quantité")
        self.tree.heading("4", text="PrixAchat")
        self.tree.heading("5", text="PrixHTVA")
        self.tree.heading("6", text="Prix de vente")
        self.tree.heading("7", text="Date")
        #treeScroll = ttk.Scrollbar()
        #treeScroll.configure(command=tree.yview)
        #tree.configure(yscrollcommand=treeScroll.set)
        #treeScroll.pack(side=LEFT, pady=100)
        #treeScroll.place(x=150, y=200)

    def construtFrameE(self):
        self.recherche = Label(self.FrameE, text="Rechercher par:",width = widthLabel,bg= CouleurBlanc)
        self.recherche.grid(row=0, column=0, padx = 20, pady = 1)
        self.num = Label(self.FrameE, text="Numéro d'article:",width = widthLabel,bg= CouleurBlanc)
        self.num.grid(row=1, column=0, padx = 20, pady = 1)
        self.entreeNumArt = ttk.Entry(self.FrameE, textvariable="valnum", width=widthEntry)
        self.entreeNumArt.grid(row=1, column=1, padx = 20, pady = 1)
        self.libelle = Label(self.FrameE, text="Libellé:",width = widthLabel,bg= CouleurBlanc)
        self.libelle.grid(row=2, column=0, padx=20, pady=1)
        self.vallib = StringVar()
        self.entreeLibelle = ttk.Entry(self.FrameE, textvariable=self.vallib, width=widthEntry)
        self.entreeLibelle.grid(row=2, column=1, padx=20, pady=1)
        self.dateDeb = Label(self.FrameE, text="Date début:",width = widthLabel,bg= CouleurBlanc)
        self.dateDeb.grid(row=3, column=0, padx=20, pady=1)
        self.valDeb = StringVar()
        self.entreeDateDeb = ttk.Entry(self.FrameE, textvariable=self.valDeb, width=widthEntry)
        self.entreeDateDeb.grid(row=3, column=1, padx=20, pady=1)
        self.dateFin = Label(self.FrameE, text="Date fin:",width = widthLabel,bg= CouleurBlanc)
        self.dateFin.grid(row=4, column=0, padx=20, pady=1)
        self.valFin = StringVar()
        self.entreeDateFin = ttk.Entry(self.FrameE, textvariable=self.valFin, width=widthEntry)
        self.entreeDateFin.grid(row=4, column=1, padx=20, pady=1)
        ############# col 2 #############
        self.tailleV = Label(self.FrameE, text="Taille:",width = widthLabel,bg= CouleurBlanc)
        self.tailleV.grid(row=1, column=2, padx=20, pady=1)
        self.valTaille = StringVar()
        self.entreeTaille = ttk.Entry(self.FrameE, textvariable=self.valTaille, width=widthEntry)
        self.entreeTaille.grid(row=1, column=3, padx=20, pady=1)
        self.couleurV = Label(self.FrameE, text="Couleur:",width = widthLabel,bg= CouleurBlanc)
        self.couleurV.grid(row=2, column=2, padx=20, pady=1)
        self.entreeCouleur = ttk.Entry(self.FrameE, textvariable="valCouleur", width=widthEntry)
        self.entreeCouleur.grid(row=2, column=3, padx=20, pady=1)
        self.categorieV = Label(self.FrameE, text="Catégorie:",width = widthLabel,bg= CouleurBlanc)
        self.categorieV.grid(row=3, column=2, padx=20, pady=1)
        self.valCat = StringVar()
        self.entreeCategorie = ttk.Entry(self.FrameE, textvariable= self.valCat, width=widthEntry)
        self.entreeCategorie.grid(row=3, column=3, padx=20, pady=1)
        self.entrSort = Label(self.FrameE, text="Entrée/sortie:",width = widthLabel,bg= CouleurBlanc)
        self.entrSort.grid(row=4, column=2, padx=20, pady=1)
        self.inOutRadioButton = IntVar()
        self.boutonEnt = Radiobutton(self.FrameE, text="in", variable=self.inOutRadioButton, value=0,bg= CouleurBlanc)
        self.boutonEnt.grid(row=4, column=3, padx=1, pady=1)
        self.boutonSort = Radiobutton(self.FrameE, text="out", variable=self.inOutRadioButton, value=1,bg= CouleurBlanc)
        self.boutonSort.grid(row=4, column=4, padx=1, pady=1)

        ##self.searchButton ajouter la commande remplirTreevieuw
        self.searchButton = ttk.Button(self.FrameE, text="rechercher", command= self.remplirTreeviewSearch)
        self.searchButton.grid(row=0,rowspan=4, column=4)

    def test(self):
        messagebox.showinfo("TSS", "application en construction")