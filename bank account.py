# -*- coding: utf-8 -*-

import pickle
import os
import pathlib
class User :
    code_cli=0
    nom = ""
    prenom = ""   
    def createUser(self):
        x=""
        
        while x != "true" :           
            self.code_cli= int(input("Entrer le code clien :"))
            
            with open('users.data', 'rb') as f:
                
                content = f.read()
                
                if self.code_cli in content:
                    
                    print("Code de client deja exist")

                else:
                      
                    self.nom = str(input("Entrer le nom de client :" ))
                    self.prenom = str(input("Entrer le prenom de client :" ))
                    print("\n\n\nLe utilisateur a été crée") 
                    break
               
            
class Account :
   
   code_cpt = 0
   code_cli=0
 
   deposit=0
   d_cpt = 0        
   def createAccount(self):
       x=""
       f = open("users.data","rb")
       fcc = open("accounts.data","rb")
       self.code_cli= int(input("Entrer le code clien :"))
       
       with open('users.data', 'rb') as f:
           
           content = f.read()
           
           if self.code_cli not in content:
               
               print("Code de client n'existe pas ")
              

           else:
              
              self.code_cpt = int(input("Entrer le code de compte :"))
              with open('accounts.data', 'rb') as fcc:
                  content = fcc.read()
                  
                  if self.code_cpt in content:
                      
                      print("Code de client existe deja  ")
                     

                  else:
                      nom = input("Entrer le nom de client :" )
                      prenom = input("Entrer le prenom de client :" )
                      print("compte crée")
                  
              
              
       
           
           
                  
              
                   
                            
       
                 
       
       
       
       
       

           
       
                   
                   
           
               
           
           
           
    

                
       
           
           
       
               
                   
               
          
      
       
       
      
          
              
              
                      
                  
                  
                      
                  
              
                     
                  
                  
                   
                  
                  
              
                  
          
      
      
              
              
              
              
              
             
                     
                        
              
              
                  
      
          
              
                  
                  
                  
         
                            
                  
                  
              
                             
                             
                         
                                 
                             
                                 
                             
                         
                         
                                
          
          
                 
                          
                         
                         
                     
                     
                     
                         
              
                  
                  
                  
                      
                   
                      
                       
                  
                  
              
              
          
           
               
          
                         
                     
                
                
                    
          
          
                   
          
                      
                   
               
           
                   
                   
                            
         
   
     
         
   def modifyUser(self):
       t=""
       while t != "true" : 
           self.code_cli = int(input("Entrer le code de client :" ))
           with open('users.data', 'rb') as f:
               content = f.read()
               if self.code_cli not in content:
                   print("Code de client n'existe pas")
                   t == "true"
               else :
                       break
       print("Numero de compte : ",self.code_cli)
       self.nom = input("Modifier le nom :")
       self.prenom = input("Modifier lr ptrnom :")    
   def modifyAccount(self):
       print("Account Number : ",self.code_cpt)

       self.name = input("Modify Account Holder Name :")

       self.type = input("Modify type of Account :")

       self.deposit = int(input("Modify Balance :"))

   def depositAmount(self,amount):

       self.deposit += amount  

   def withdrawAmount(self,amount):

       self.deposit -= amount  

   def report(self):

       print(self.code_cpt, " ",self.nameCode_cli ," ",self.d_cpt,"", self.deposit)  

   def getAccountcode_cpt(self):
       return self.code_cpt
   def getAccountCode_cli(self):
       return self.code_cli
   def getAcccountHolderD_cpt(self):
       return self.d_cpt  
   def getDeposit(self):
       return self.deposit 
   
   def getUsertCode_cli(self):
       return self.code_cli
   def getUsertHolderNon(self):
       return self.nom
   def getUserHolderPrenom(self):
       return self.prenom

def intro():

   print("\t\t\t\t**********************")

   print("\t\t\t\tGESTION COMPTE BANCAIRE")

   print("\t\t\t\t**********************")
   print("\t\t\tTaper une touche pour commencer")

   

  

   input()
   

def writeUser():

   user = User()

   user.createUser()

   writeUsersFile(user)

def writeAccount():

   account = Account()

   account.createAccount()

   writeAccountsFile(account)
   

def displayAlluser():

   file = pathlib.Path("users.data")
   

   if file.exists ():

       infile = open('users.data','rb') 
       
       

       mylist = pickle.load(infile)
       
       for item in mylist :
           
 
           print("-Code Client: ", item.code_cli,"|Nom de client: ", item.nom, "|Prenom de client: ",item.prenom  )
           

       infile.close()

   else :

       print("No records to display")
       
def displayAllaccount():

   file = pathlib.Path("accounts.data")
   

   if file.exists ():

       infile = open('accounts.data','rb')
       

       mylist = pickle.load(infile)

       for item in mylist :

           
           print("-Code compte: ",item.code_cpt,"|Code client: ", item.code_cli, "|Date creation: ",item.d_cpt, "|solde: ",item.d_cpt  )

       infile.close()

   else :

       print("No records to display")

def displaySp(num):

   file = pathlib.Path("accounts.data")

   if file.exists ():

       infile = open('accounts.data','rb')

       mylist = pickle.load(infile)

       infile.close()

       found = False

       for item in mylist :

           if item.code_cpt == num :

               print("Your account Balance is = ",item.deposit)

               found = True

   else :

       print("No records to Search")

   if not found :

       print("No existing record with this number")

def depositAndWithdraw(num1,num2):

   file = pathlib.Path("accounts.data")

   if file.exists ():

       infile = open('accounts.data','rb')

       mylist = pickle.load(infile)

       infile.close()

       os.remove('accounts.data')

       for item in mylist :

           if item.code_cpt == num1 :

               if num2 == 1 :

                   amount = int(input("Enter the amount to deposit : "))

                   item.deposit += amount

                   print("Your account is updted")
                   

               elif num2 == 2 :

                   amount = int(input("Enter the amount to withdraw : "))

                   if amount <= item.deposit :

                       item.deposit -=amount

                   else :

                       print("You cannot withdraw larger amount")              

   else :

       print("No records to Search")

   outfile = open('newaccounts.data','wb')

   pickle.dump(mylist, outfile)

   outfile.close()

   os.rename('newaccounts.data', 'accounts.data') 
   
def deleteUser(num):

   file = pathlib.Path("users.data")

   if file.exists ():

       infile = open('users.data','rb')

       oldlist = pickle.load(infile)

       infile.close()

       newlist = []

       for item in oldlist :

           if item.code_cli != num :

               newlist.append(item)

       os.remove('users.data')

       outfile = open('newusers.data','wb')

       pickle.dump(newlist, outfile)

       outfile.close()

       os.rename('newusers.data', 'users.data')
 
def modifyUser(num):

   file = pathlib.Path("users.data")

   if file.exists ():

       infile = open('users.data','rb')

       oldlist = pickle.load(infile)

       infile.close()

       os.remove('users.data')

       for item in oldlist :

           if item.code_cli != num :
                                       print("existe pas")
           else:
           
           

               item.nom = input("Entre le nom de client : ")

               item.prenom = input("Enter le prenom de client : ")
       outfile = open('newusers.data','wb')

       pickle.dump(oldlist, outfile)

       outfile.close()

       os.rename('newusers.data', 'users.data')

       
def modifyAccount(num):

   file = pathlib.Path("accounts.data")

   if file.exists ():

       infile = open('accounts.data','rb')

       oldlist = pickle.load(infile)

       infile.close()

       os.remove('accounts.data')

       for item in oldlist :

           if item.code_cpt == num :

               item.named_cpt = input("Enter the account holder name : ")

               item.typed_cpt = input("Enter the account Type : ")

               item.deposit = int(input("Enter the Amount : "))      

       outfile = open('newaccounts.data','wb')

       pickle.dump(oldlist, outfile)

       outfile.close()

       os.rename('newaccounts.data', 'accounts.data')

def writeAccountsFile(account) :  

   file = pathlib.Path("accounts.data")

   if file.exists ():

       infile = open('accounts.data','rb')

       oldlist = pickle.load(infile)

       oldlist.append(account)

       infile.close()

       os.remove('accounts.data')

   else :

       oldlist = [account]

   outfile = open('newaccounts.data','wb')

   pickle.dump(oldlist, outfile)

   outfile.close()

   os.rename('newaccounts.data', 'accounts.data')

def writeUsersFile(user) : 
    file = pathlib.Path("users.data")

    if file.exists ():

        infile = open('users.data','rb')

        oldlist = pickle.load(infile)

        oldlist.append(user)

        infile.close()

        os.remove('users.data')

    else :

        oldlist = [user]

    outfile = open('newusers.data','wb')

    pickle.dump(oldlist, outfile)

    outfile.close()

    os.rename('newusers.data', 'users.data')  

   

# start of the program

ch=""

num1=0

intro()

while ch != 6:

  

   print("\tMAIN MENU")

  
   print("\t\t\t\t1. GESTION DE CLIENT")

   print("\t\t\t\t2. GESTION DE COMPTE")

   print("\t\t\t\t3. GESTION OPERATION")

 

   print("\t\t\t\t4. EXIT")

   print("\t\t\t\tChoisr entre (1-4) ")

   ch = input()



   if ch == '1':
       ch1=""
       num=0
       while ch1 != 6:
           print('\tGestion des Clients!!!')
           print("\t\t\t\t1-afficher liste de client")
           print("\t\t\t\t2-ajouter client")
           print("\t\t\t\t3-modifier clientt")
           print("\t\t\t\t4-supp client")
           print("\t\t\t\t5. EXIT")
           ch1 = input()
           if ch1 == '1':
               displayAlluser();       
           elif ch1 == '2':
               writeUser()
           elif ch1 == '3':
               num = int(input("\tEntrer le numero de client : "))
               modifyUser(num)
           elif ch1 == '4':
               num =int(input("\tEntrer le numero de client : "))
               deleteUser(num)              
           elif ch1 == '5':          
              intro()     
           break

 

   elif ch =='2':
       ch2=0
       num=0
       while ch2 != 3:
           print('\tGestion des Comptes!!!')
           print("\t\t\t\t1-afficher liste des Comptes")
           print("\t\t\t\t2-ajouter nouveau compte")
           #print("\t\t\t\t3-Supprimer compte")
           print("\t\t\t\t3. EXIT")
           ch1 = input()
           if ch1 == '1':
               displayAllaccount(); 
           elif ch1 == '2':
               writeAccount();
           elif ch1=='3':
               
               
               intro()    
               
               break
   elif ch == '3':
       ch3=0
       num=0
       while ch3 != 3:
           print('\tGestion des operations!!!')
           print("\t\t\t\t1-retirer argent")
           print("\t\t\t\t2-versement argent")
           print("\t\t\t\t3. EXIT")
           ch1 = input()
           if ch1 == '1':
               num = int(input("\tEnter The account No. : "))
               depositAndWithdraw(num, 2) 
               print("historique: ")
               print("numero de compteest:")
               print("le somme retiré est:")
               print("le nouveau solde est: ")
           elif ch1 == '2':
               num = int(input("\tEnter The account No. : "))
               depositAndWithdraw(num, 1)
                                  
           elif ch1 == '3':
               intro()     
           break                                           

       break

   else :

       print("Invalid choice")  

   