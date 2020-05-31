# -*- coding: utf-8 -*-
## author :Becquet Emilien

"""
Frame de connexion
--------------------------
Documentation Générale
"""
from tkinter import LabelFrame,Frame,Label,Pack,Entry,messagebox,RIGHT,StringVar
from tkinter import ttk
from common import Admin,User

from pathlib import Path
########Global########## 
CouleurBlanc = "#FFFFFF"
CouleurBleu ="#33b8ff"
directory = Path(__file__).parent
widthSpinBox = 21
widthEntry = 23
widthLabel = 20
widthCombo = 20


class FrmAcceuil(Frame):
    """Classe servant pour l'interface graphique TK"""

    def __init__(self,parent):     #Création du Frame Accueil
        Frame.__init__(self)
        self.root = parent
        #Frame(self).pack(pady = 50)
        self.frame_connex = LabelFrame(self,text='Connexion', relief="groove", bd=2, height=600, width=500)
        self.frame_inscri = LabelFrame(self,text='inscription', relief="groove", bd=2, height=600, width=500)
        self.frame_acc = LabelFrame(self,text='Login', relief="groove", bd=2, height=600, width=500)
        self.frame_acc.pack(ipadx= 25, ipady = 10)
        ######FrameAcceuil###########
        self.label_acc = Label(self.frame_acc, text="Bienvenue sur le TSS !")
        self.label_acc.pack()
        #Bouton qui envoie sur le frame Connex
        self.button_connex = ttk.Button(self.frame_acc, text="Connexion", command=self.FrameConnex, width = 15)
        self.button_connex.pack()
        #Bouton qui envoie sur le frame Inscription
        self.button_inscri = ttk.Button(self.frame_acc, text="Inscription", command=self.FrameInscription, width = 15)
        self.button_inscri.pack()
        self.button_quit = ttk.Button(self.frame_acc, text="Quitter", command=quit, width = 15)
        self.button_quit.pack()
        ######end FrameAcceuil######
        ######FrameConnection#######
        self.label_user = Label(self.frame_connex, text="Nom d'utilisateur :")
        self.label_user.pack()
        self.entry_user = Entry(self.frame_connex)
        self.entry_user.pack()
        self.label_password = Label(self.frame_connex, text="Mot de passe :")
        self.label_password.pack()
        self.entry_password = Entry(self.frame_connex, show="*")
        self.entry_password.pack()
        self.button_connex = ttk.Button(self.frame_connex, text="Connexion",width = 15,command = self.login) #Ajouter la commande permettant d'accéder au menu d'utilisateur
        self.button_connex.pack()
        self.button_annuler = ttk.Button(self.frame_connex, text="Annuler", command=self.AnnulerConnex,width = 15)
        self.button_annuler.pack()
        ######end FrameConnection###
        ######FrameInscription######
        self.label_name=Label(self.frame_inscri, text="Nom : ")
        self.label_name.pack()
        self.entry_name=Entry(self.frame_inscri)
        self.entry_name.pack()
        self.label_username=Label(self.frame_inscri, text="Nom d'utilisateur : ")
        self.label_username.pack()
        self.entry_username=Entry(self.frame_inscri)
        self.entry_username.pack()
        self.label_newPW=Label(self.frame_inscri, text="Mot de passe : ")
        self.label_newPW.pack()
        self.entry_newPW=Entry(self.frame_inscri, show="*")
        self.entry_newPW.pack()
        self.label_confirmPW=Label(self.frame_inscri, text="Confirmez votre mot de passe : ")
        self.label_confirmPW.pack()
        self.entry_confirmPW=Entry(self.frame_inscri, show="*")
        self.entry_confirmPW.pack()
        self.button_valider=ttk.Button(self.frame_inscri, text="Valider", command=self.ConfirmInscri,width = 15)
        self.button_valider.pack()
        self.button_annuler=ttk.Button(self.frame_inscri, text="Annuler", command=self.AnnulerConnex,width = 15)
        self.button_annuler.pack()
        ######end FrameInscription##
    def changeFrame(self,frmToOpen):
        self.frame_acc.pack_forget()    #Cache le frame d'accueil
        self.frame_inscri.pack_forget()
        self.frame_connex.pack_forget()
        frmToOpen.pack(ipadx= 25 , ipady = 10)

    def FrameConnex(self):      #Création du Frame Connexion
        self.changeFrame(self.frame_connex)       

    def AnnulerConnex(self):      # Optimisation du bouton annuler
        self.changeFrame(self.frame_acc)   #Cache le frame de connexion
        #self.FrameAccueil()     #Renvoie au frame d'accueil
        
    def FrameInscription(self):     #Création du Frame Inscription
        self.changeFrame(self.frame_inscri)

    def ConfirmInscri(self): #Confirme l'inscription
        self.root.user=[]
        self.name=self.entry_name.get()
        self.username=self.entry_username.get()
        self.pw1=self.entry_newPW.get()
        self.pw2=self.entry_confirmPW.get()
        if self.pw1 == self.pw2:
            self.AjoutList()
            messagebox.showinfo("Inscription", "Bienvenue Utilisateur %s" %(self.root.user[-1].name))
            self.root.userActif = self.root.user[-1]
            self.frame_inscri.pack_forget()
            self.entry_name.delete(0,'end')
            self.entry_username.delete(0,'end')
            self.entry_newPW.delete(0,'end')
            self.entry_confirmPW.delete(0,'end')
            #self.FrameAccueil()
            self.frame_acc.pack()
            self.connect()
        else:
            #Affiche un message d'erreur sur la confirmation du mot de passe. Doit être optimisée
            messagebox.showinfo("Inscription", "Les Passwords doivent correspondre")
            #print("les mots de passes ne correspondent pas")

    def login(self):
        acces = False
        for u in self.root.user:
            if str(u.userName) == str(self.entry_user.get()) and str(u.password) == str(self.entry_password.get()):
                self.root.userActif = u
                self.entry_user.delete(0,'end')
                self.entry_password.delete(0,'end')
                self.connect()
                acces = True
                break
        if not acces:
            self.entry_user.delete(0,'end')
            self.entry_password.delete(0,'end')
            messagebox.showinfo("Login", "Utilisateur introuvable veuillez vous inscrire")


    def connect(self):
        self.pack_forget()   
        self.frmUser= Frame(self.root)
        self.InfoUser = LabelFrame(self.frmUser,text='Utilisateur', relief="groove", bd=2, height=600, width=500,bg =CouleurBlanc)
        self.InfoUser.pack(side= RIGHT)
        self.userName =StringVar()
        self.userName.set("User Name: %s" %(self.root.userActif.userName))
        Label(self.InfoUser, textvariable = self.userName  ,bg =CouleurBlanc,width =widthLabel, anchor="w").grid(row = 0, column = 0, columnspan = 2)
        ttk.Button(self.InfoUser,text = "LogOut", command = self.logOut).grid(row = 1, column = 0)
        ttk.Button(self.InfoUser,text = "Quitter", command = self.Quitter).grid(row = 1, column = 1)
        self.frmUser.pack(ipadx = 350)
        self.root.openTSS()

    

    def logOut(self):
        self.root.userActif = None
        self.frmUser.pack_forget()
        self.root.closeTSS()

    def Quitter(self):
        self.root.quit()

    def AjoutList(self): #Crée et ajoute une liste avec les instructions d'inscription
        self.root.user.append(User(self.name, self.username, self.pw1))

if __name__ == "__main__":
    pass   
    

