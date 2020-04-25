"""
TSS Package
--------------------------
Documentation Générale
"""


# -*- coding: utf-8 -*-
## author : Rochez Justin

########Import##########
from common import CouleurBlanc,CouleurBleu, widthSpinBox ,widthEntry, widthLabel, widthCombo


#toAdd on common 
from tkinter import Tk,Toplevel,Frame,LabelFrame,GROOVE,Label,Button,StringVar
from tkinter import messagebox, ttk


#importTest
from random import choice,randrange
########Global########## 

########Class###########

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
        self.FrFond.pack (ipadx = 42, ipady =5)

        self.frmRecherche = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmAjout = Frame(self.FrFond, bg =CouleurBlanc)
        self.frmModif =Frame(self.FrFond, bg =CouleurBlanc)

        self.key = ["Numéro d'article","Libéllé","Marque","Quantité","PrixHTVA","Tva","Taille","Catégorie","Couleur"]
        
        self.tree = ttk.Treeview(self.l, columns = [k for k in self.key[1:None]],height=10)
        for i,k in enumerate(self.key):
            self.tree.heading('#%s' %(i),text = k)
            if k[0] not in ["T","P","Q"]:
                self.tree.column('#%s' %(i), minwidth=130,width=130)
            else:
                self.tree.column('#%s' %(i), minwidth=63,width=63)  
       
        self.frmrecherche()
        self.tree.pack()
        self.updateStock()
        self.frmButton = Frame(self, bg = CouleurBlanc, relief = GROOVE, border = 2)
        self.frmButton.grid(row = 0, column = 0, ipadx = 30 , ipady = 23)
        Frame(self.frmButton,height = 30,bg = CouleurBlanc).pack()
        ttk.Button(self.frmButton, text = "Rechercher", command = self.frmrecherche, width = 15).pack()
        ttk.Button(self.frmButton, text = "Ajouter", command = self.frmajout,width = 15).pack()
        ttk.Button(self.frmButton, text = "Modifier", command = self.frmmodif,width = 15).pack()
        ttk.Button(self.frmButton, text = "Supprimer", command = self.Supprimer,width = 15).pack()
        ttk.Button(self.frmButton, text = "exporter en Excel", command = self.test,width = 15).pack()
        #*************end Frame button*******
        #************Frame des bouton de Menu******
        self.frmMenu = Frame(self, bg = "#33b8ff", relief = GROOVE, border = 2)
        self.frmMenu.grid(row = 1, column = 0, ipadx = 5 , ipady = 13)
        Frame(self.frmMenu,height = 30,bg = CouleurBleu).pack()
        Button(self.frmMenu,text = "Vente",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_Stock",command = self.test, bg = "#989898", relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Statistique",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        Button(self.frmMenu,text = "Gestion_employé",command = self.test, bg = CouleurBlanc, relief = GROOVE, width = 20).pack(pady= 2)
        #************end bouton de menu************
        self.info = StringVar()
        self.info.set("Aucune action effectuée")
        self.labInfo = Label(self.l,textvariable = self.info, bg = CouleurBlanc,width = 128,  anchor="w")
        self.labInfo.pack()
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
            if int(i/2) == i/2:
                self.tree.insert('', 'end', i , text=vetm.idVet,values = [vetm.libelle,vetm.marque, vetm.quantite,vetm.prixHTVA, vetm.tauxTVA, vetm.taille,vetm.categorie, vetm.couleur]\
                    ,tags = 'pair')   
            else:
                self.tree.insert('', 'end', i , text=vetm.idVet,values = [vetm.libelle,vetm.marque, vetm.quantite,vetm.prixHTVA, vetm.tauxTVA, vetm.taille,vetm.categorie, vetm.couleur])


    def changeFrame(self,frameToOpen):
        """Fonction qui ferme toutes les Frames pour n'ouvrir que la FrameToOpen
        """
        self.frmAjout.pack_forget()
        self.frmModif.pack_forget()
        self.frmRecherche.pack_forget()
        frameToOpen.pack()

    def frmajout(self, event = None):
        """Creation de la Frame D'ajout
        """
        self.dctAjout = {}
        self.entreeAj = {}
        try:
            self.changeFrame(self.frmAjout)
            Label(self.frmAjout,text = "article à ajouter: ",bg =CouleurBlanc, width =widthLabel, anchor="w").grid(row= 0, column = 0)
            Label(self.frmAjout,text= ("%s :" %("Prix achat")),bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 5, column = 2, padx = 20, pady = 1)
            for i,s in enumerate(self.key):
                self.dctAjout[s]= StringVar()
                try:
                    if len(self.tree.focus()) != 0:
                        self.dctAjout[s].set(self.parent.stock.lstVetement[int(self.tree.focus())].lstAllElement[i])
                except :
                    self.dctAjout[s].set('')  
            self.dctAjout["Prix achat"] = StringVar()
            if len(self.tree.focus()) != 0:
                self.dctAjout["Prix d'achat"].set(self.parent.stock.lstVetement[int(self.tree.focus())].prixAchat)
            
            for Row,s in enumerate(self.dctAjout.keys()):
                self.entreeAj[s]=ttk.Entry(self.frmAjout,textvariable = self.dctAjout[s] ,width = widthEntry)
                if s == "Quantité" or s == "PrixHTVA" or s =="Tva" or s == "Prix achat":
                    self.entreeAj[s]= ttk.Spinbox(self.frmAjout ,textvariable = self.dctAjout[s],from_=0, to=999999,width = widthSpinBox)
                if Row <= 4 :
                    Label(self.frmAjout, text = ("%s :" %(s)),bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = Row+1, column = 0, padx = 20, pady = 1)
                    self.entreeAj[s].grid(row = Row+1, column = 1, padx = 20, pady = 1)
                else:
                    Label(self.frmAjout, text = ("%s :" %(s)),bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = Row-4, column = 2, padx = 20, pady = 1)
                    self.entreeAj[s].grid(row = Row-4, column = 3, padx = 20, pady = 1)

            ttk.Button(self.frmAjout, text ="Confirmer" , command = self.ajouter).grid(row = 0, rowspan = 6, column = 4)
            ttk.Button(self.frmAjout, text ="In Stock" , command = self.InStock).grid(row = 3, rowspan = 9, column = 4)
            self.tree.bind("<Button-1>", self.frmajout)
            for w in self.entreeAj.values(): 
                w.bind("<Return>", self.ajouter)
            
        except:
            messagebox.showerror(title="Error", message="l'ajout à échoué!")

    def ajouter(self,event = None):
        try:
           valeur = [v.get()for v in self.entreeAj.values()]
           if int(valeur[0]) not in [int(v.idVet) for v in self.parent.stock.lstVetement]:
                self.parent.stock + Vetement(valeur[0],valeur[1],valeur[2],valeur[8],valeur[7],valeur[4],valeur[5],valeur[9], valeur[6],valeur[3])
                self.parent.Historique.In( self.parent.stock.lstVetement[-1])
                messagebox.showinfo(title="Article ajouté", message="L'article %s a été ajouté avec succès" %(self.parent.stock.lstVetement[-1].idVet) )
                self.info.set("Ajout de l'article %s au stock" %(self.parent.stock.lstVetement[-1].idVet))
           else: 
               messagebox.showinfo(title="en stock", message="Le numéro de vêtement que vous avez utilisé est déjà dans le stock. Pour modifier veuillez allez dans l'option Modifier")
        except :
            messagebox.showerror(title="Error", message="l'ajout à échoué!\nToutes les cases doivent être remplie")

    def InStock(self):
        """Fonction de modification de la quantité d'un article Vetement se trouvant déja dans le stock.
        La fonction n'éffectue qu'un In dans le stock. Les fonctions Out Stock sont prévue pour la fenetre de vente.
        """

        def changeQuant(event = None):
            """change la quantité de stock en effectuant un In, adapte aussi l'historique
            """
            try:
                if int(quantite.get()) > 0:
                    temp = self.parent.stock.lstVetement[int(self.tree.focus())].quantite
                    self.info.set("Ajout de %s quantité(s) de l'article %s" %(int(quantite.get()),self.parent.stock.lstVetement[int(self.tree.focus())].idVet))
                    messagebox.showinfo(title="Entrée en stock",message ="Ajout de %s quantité(s) pour:\n%s" \
                        %(int(quantite.get()),self.parent.stock.lstVetement[int(self.tree.focus())]))
                    self.parent.stock.lstVetement[int(self.tree.focus())].quantite = int(quantite.get())
                    self.parent.Historique.In(self.parent.stock.lstVetement[int(self.tree.focus())])
                    self.parent.stock.lstVetement[int(self.tree.focus())].quantite = temp  + int(quantite.get())
                    self.tree.bind("<Button-1>", self.frmajout)
                    self.recherche()
                    rootIn.destroy()
                else:
                    messagebox.showinfo(title= "Attention", message=" La quantité doit être plus grande que 0.")
            except:
                messagebox.showerror(title="Error", message="Une Erreur est survenue dans l'entrée en stock")   
   
        rootIn = Toplevel(self.parent)
        quantite = StringVar()
        if len(self.tree.focus()) != 0:
            self.tree.unbind("<Button-1>")  
            rootIn.title("TSS : Entrée en stock")
            rootIn.minsize(300,220)
            frameLabel = Frame(rootIn, bg= CouleurBlanc)
            Label(frameLabel,text= self.parent.stock.lstVetement[int(self.tree.focus())], bg = CouleurBlanc,width =widthLabel).pack()
            spin = ttk.Spinbox(frameLabel ,textvariable = quantite,from_=0, to=999999,width = widthSpinBox)
            spin.pack()
            spin.bind("<Return>", changeQuant)
            ttk.Button(frameLabel, text ="Confirmer" , command = changeQuant).pack()
            ttk.Button(frameLabel, text ="quitter" , command = rootIn.destroy).pack()
            frameLabel.pack()
            rootIn.mainloop()
        else:
            messagebox.showwarning(title="Selectionner Article.", message="Vous devez selectionner un article!")

    def frmmodif(self, event = None):
        """Fonction de création de la Frame de modification
        """
        try:
            self.changeFrame(self.frmModif)
            self.tree.bind("<Button-1>", self.frmmodif)
            Label(self.frmModif,text = "article à modifier: ",bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row= 0, column = 0)
            self.dctStvModif = {}
            for i,s in enumerate(self.key):
                self.dctStvModif[s]= StringVar()
                try:
                    if len(self.tree.focus()) != 0:
                        self.dctStvModif[s].set(self.parent.stock.lstVetement[int(self.tree.focus())].lstAllElement[i])
                except :
                    self.dctStvModif[s].set('')  

            self.entree = {}
            lenColn =int(len(self.dctStvModif)/2)
            for Row,s in enumerate(self.dctStvModif.keys()):
                self.entree[s]=ttk.Entry(self.frmModif, textvariable = self.dctStvModif[s], width = widthEntry)
                if s == "Quantité" or s == "PrixHTVA" or s =="Tva":
                    self.entree[s]= ttk.Spinbox(self.frmModif ,textvariable = self.dctStvModif[s],from_=0, to=999999,width = widthSpinBox)
                if Row +1 <= lenColn :
                    Label(self.frmModif, text = ("%s :" %(s)),bg =CouleurBlanc, width =widthLabel, anchor="w").grid(row = Row+1, column = 0, padx = 20, pady = 1)
                    self.entree[s].grid(row = Row+1, column = 1, padx = 20, pady = 1)
                else:
                    Label(self.frmModif, text = ("%s :" %(s)),bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = Row-lenColn+1, column = 2, padx = 20, pady = 1)
                    self.entree[s].grid(row = Row-lenColn+1, column = 3, padx = 20, pady = 1)
            Label(self.frmModif, text = ("%s :" %("Assorti avec")),bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 5, column = 0, padx = 20, pady = 1)
            if len(self.tree.focus()) == 0:
                self.assortModif = ttk.Combobox(self.frmModif,width = widthCombo)
            else :
                self.assortModif = ttk.Combobox(self.frmModif,width = widthCombo,values = [v.idVet for v in self.parent.stock.lstVetement[int(self.tree.focus())].lstAssorti])
            self.assortModif.grid(row = 5, column = 1, padx = 20, pady = 1)
            ttk.Button(self.frmModif, text ="Confirmer" , command = self.Modifier).grid(row = 0, rowspan = 6, column = 4)
            ttk.Button(self.frmModif, text ="Réassortir" , command = self.reassortir).grid(row = 3, rowspan = 9, column = 4)
            
            for w in self.entree.values(): 
                w.bind("<Return>", self.Modifier)  
            
        except:
            messagebox.showerror(title="Error", message="Aucun vetement n'as été selectionné!")

    def reassortir(self):
        """Fonction qui va permettre à l'utilisateur d'assortir un vetement avec plusieurs autre vetement.
        """
        def addAssorti(event = None):
            """ Fonction qui change l'assortiment d'un vetement. 
            On reprend la selection de l'utilisateur et on l'ajoute à l'assortiment du vetement. 
            si l'utilisateur ne selectionne qu'une ligne dans la treeview, la lstAssorti ne sera que de longueur 1
            """
            self.tree.selection_add(self.tree.focus())
            if len(self.tree.selection()) == 1:
                if messagebox.askyesno(title= "Assortiment", message= "voulez vous assortir %s avec\n%s" %(vetAAssortir.libelle,self.parent.stock.lstVetement[int(self.tree.focus())])):
                    vetAAssortir.addVetAssort(self.parent.stock.lstVetement[int(self.tree.focus())])
                    self.info.set("Ajout du Vetement %s à la liste d'assortiment de %s" %(self.parent.stock.lstVetement[int(self.tree.focus())].idVet,vetAAssortir.libelle))
            else: 
                message = "Le vêtement %s est assorti avec :" %(vetAAssortir.libelle)
                for i in self.tree.selection():
                    
                    if messagebox.askyesno(title= "Assortiment", message= "voulez vous assortir %s avec\n%s" %(vetAAssortir.libelle,self.parent.stock.lstVetement[int(i)])):
                        vetAAssortir.addVetAssort(self.parent.stock.lstVetement[int(i)])
                        message += "%s ," %(self.parent.stock.lstVetement[int(i)].idVet)
                        self.info.set("%s" %(message[0:-1]))
            self.assortModif.config(values =[v.idVet for v in vetAAssortir.lstAssorti])
            self.tree.selection_set()
            self.frmmodif()


        try:
            try:
                self.frmmodif()
                vetAAssortir=self.parent.stock.lstVetement[int(self.tree.focus())]
                messagebox.showinfo(title="Réassortir", message="Selectionnez plusieurs vêtement assorti avec %s\nCliquez sur un vetement ensuite sur Enter \
                    \nOu selectionnez plusieurs vetement avec CTRL+ click ensuite Enter pour valider."\
                     %(self.parent.stock.lstVetement[int(self.tree.focus())].libelle))
                vetAAssortir.lstAssorti = []
                self.tree.unbind("<Button-1>")
                self.tree.bind("<Return>", addAssorti)
            except:
                messagebox.showerror(title="Error", message="Vous devez selectionner un vêtement pour le réassortiment") 
        except:
           messagebox.showerror(title="Error", message="Aucun vetement n'as été selectionné pour le réassortiment!") 
    
        

    def Modifier (self, event= None):
        """Fonction de confirmation de modification d'un vetement. 
        Si l'idVet du vetement existe déjà, la modification se fera. 
        Si les Quantités de l'article change, les modifications seront prises en compte dans l'historique
        """
        try:
            messageInfo = "Aucune modification effectuée"
            if str(self.dctStvModif["Numéro d'article"].get()) == str(self.parent.stock.lstVetement[int(self.tree.focus())].idVet):
                messagebox.showinfo(title="Attention !", message="Toute modification des quantités entrainera un flux de stock!")
                if messagebox.askyesno(title="Modification", message="Voulez-vous modifier ?\n%s" %(self.parent.stock.lstVetement[int(self.tree.focus())])):
                    if self.parent.stock.lstVetement[int(self.tree.focus())].quantite-int(self.dctStvModif["Quantité"].get()) > 0:
                        messageInfo = "Modification: sortie de stock de l'article %s" %(self.parent.stock.lstVetement[int(self.tree.focus())].idVet)
                        self.parent.stock.lstVetement[int(self.tree.focus())].quantite -= int(self.dctStvModif["Quantité"].get())
                        self.parent.Historique.Out(self.parent.stock.lstVetement[int(self.tree.focus())])
                    elif self.parent.stock.lstVetement[int(self.tree.focus())].quantite-int(self.dctStvModif["Quantité"].get()) < 0:
                        messageInfo = "Modification: entrée en stock de l'article %s" %(self.parent.stock.lstVetement[int(self.tree.focus())].idVet)
                        self.parent.stock.lstVetement[int(self.tree.focus())].quantite = int(self.dctStvModif["Quantité"].get())-self.parent.stock.lstVetement[int(self.tree.focus())].quantite
                        self.parent.Historique.In(self.parent.stock.lstVetement[int(self.tree.focus())])
                    try:
                        self.parent.stock.lstVetement[int(self.tree.focus())]= Vetement(self.dctStvModif["Numéro d'article"].get(),self.dctStvModif["Libéllé"].get(),\
                            self.dctStvModif["Marque"].get(),self.dctStvModif["Couleur"].get(),self.dctStvModif["Catégorie"].get(),self.dctStvModif["PrixHTVA"].get(),self.dctStvModif["Tva"].get(),\
                                self.parent.stock.lstVetement[int(self.tree.focus())].prixAchat,self.dctStvModif["Taille"].get(),self.dctStvModif["Quantité"].get(),\
                                    self.parent.stock.lstVetement[int(self.tree.focus())].lstAssorti)
                        messageInfo = "Modification de l'article %s effectuée avec succès" %(self.parent.stock.lstVetement[int(self.tree.focus())].idVet)
                    except:
                        messagebox.showerror(title="Error", message="Erreur dans la modification de l'article")
                    self.info.set(messageInfo)
                    for e in self.dctStvModif.values():
                        e.set('')
                    self.recherche()
                
        except :
            messagebox.showerror(title="Error", message="Vous devez selectionner un vetement")
    
    def Supprimer(self):
        """
        Fonction de suppression d'un vetement avec messages de confirmation utilisateur
        """
        try:
            if (messagebox.askyesno(title="Confirmer Suppression ?",message="%s" %(self.parent.stock.lstVetement[int(self.tree.focus())]))):
                self.info.set("Suppression de l'article %s" %(self.parent.stock.lstVetement[int(self.tree.focus())].idVet))
                del(self.parent.stock.lstVetement[int(self.tree.focus())])
                self.recherche()
            else:
                self.info.set("Aucune Suppression effectuée")      
        except:
            messagebox.showerror(title="Error", message="Erreur dans la suppression de l'article!")

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
            self.info.set("recherche effectuée avec succès")
        except :
            messagebox.showerror(title="Error", message="Erreur d'encodage!") 
            self.updateStock() 
                    
    def frmrecherche(self): # à améliorer
            """Fonction de création de la Frame de Recherche
            """
            self.tree.unbind("<Button-1>")
            self.changeFrame(self.frmRecherche)
            Label(self.frmRecherche, text = "rechercher par:" ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 0, column = 0)          
            for i,k in enumerate(self.key):
                if k != "PrixHTVA":
                    if i < int(len(self.key)/2):
                        Label(self.frmRecherche, text = "%s :" %(k) ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = i+1, column = 0, padx = 20, pady = 1)
                    else:
                        Label(self.frmRecherche, text = "%s :" %(k) ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = i-int(len(self.key)/2), column = 2, padx = 20, pady = 1)
                else:
                    Label(self.frmRecherche, text = "PrixMin :" ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 5, column = 0, padx = 20, pady = 1)
                    Label(self.frmRecherche, text = "PrixMax :" ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 5, column = 2, padx = 20, pady = 1)
                    self.minPrixfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = widthSpinBox)
                    self.maxPrixfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = widthSpinBox)  
            self.idVetfrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = [vetm.idVet for vetm in self.parent.stock.lstVetement])     
            self.tvafrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = sorted(self.parent.stock.lstNonRep()["tva"]))
            self.libfrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = [vetm.libelle for vetm in self.parent.stock.lstVetement])
            self.quantfrRech =ttk.Spinbox(self.frmRecherche,from_=0, to=999999,width = widthSpinBox)
            self.MarquefrRech =ttk.Combobox(self.frmRecherche,width = widthCombo, values = self.parent.stock.lstNonRep()["marque"])
            self.taillefrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = self.parent.stock.lstNonRep()["taille"])
            self.catfrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = self.parent.stock.lstNonRep()["cat"])
            self.couleurfrRech =ttk.Combobox(self.frmRecherche,width = widthCombo,values = self.parent.stock.lstNonRep()["color"])
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
    pass