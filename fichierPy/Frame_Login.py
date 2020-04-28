
from tkinter import LabelFrame,Frame,Label,Pack,Entry
from tkinter import ttk


class User: # Classe de User encore inutilisée. En Test
    right = ("Admin", "User")

    def __init__(self, name, userName, password):
        self.name=name
        self.userName=userName
        self.password=password

    def Rights(self, right):
        self.userRights = input("Droits de l'utilisateur : ")
        if self.userRights == 1:
            self.userRights = right[0]
        else:
            self.userRights = right[1]
        return self.userRights



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
        self.button_connex = ttk.Button(self.frame_connex, text="Connexion",width = 15) #Ajouter la commande permettant d'accéder au menu d'utilisateur
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
        self.user=[]
        self.name=self.entry_name.get()
        self.username=self.entry_username.get()
        self.pw1=self.entry_newPW.get()
        self.pw2=self.entry_confirmPW.get()
        if self.pw1 == self.pw2:
            self.AjoutList()
            self.frame_inscri.pack_forget()
            #self.FrameAccueil()
            self.frame_acc.pack()
            print(self.user)
        else:
            #Affiche un message d'erreur sur la confirmation du mot de passe. Doit être optimisée
            print("les mots de passes ne correspondent pas")

    def AjoutList(self): #Crée et ajoute une liste avec les instructions d'inscription
            self.newUser=[self.name, self.username, self.pw1]
            return self.user.append(self.newUser)

    
    

