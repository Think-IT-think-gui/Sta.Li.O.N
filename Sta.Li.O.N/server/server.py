from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Style
from tkinter import ttk
import threading
from tkinter import messagebox
from tkinter import filedialog
import tkinter.scrolledtext
import socket
import threading
import sqlite3
import random
from time import *
import time
import ast


#================================================BACK END=====================================================

#==============================================server language================================================
HEADER = 64
PATH = os.path.dirname(os.path.realpath(__file__))
FORMAT = 'utf-8'
DISCONNECT = "fdtr&^*246*"
LOGIN = "df422=r53@"
SIGN_IN = "df83#$%1=244"
NA = "24fsd71`21"
YA = "34&*#$%^%$"
END_SEND = "*%^dgrt43%4"
REJECTED  = "#$^$%HGFHG^%$"
ACCEPTED = "454$#%$#768"
USER_EXIST = "#$%$#rw22r"
AVAILIABLE = "rewr23432r"
ADD_CHAT = "2382%$sf"
BROAD = "erw0e223"
RECIEVED = "43eert435"
GET_DATA = "#@#@dsew"
COVER_DATA = "fWER3@@#"
OUT_DATA = "323^&%DF"
REFRESH = "W#!erw@!F("
IMG_SEND = "wr@##!^$&%#$"
IMG_SEEK = "&)$DF#@#%@@$#%"
WHO_IS_HERE = "erW@#@!&Ghgh*($%"
FIND_PATH = "q#!^FDt$%@*Dfdg$#"
DATA_BACK = "@#YR&%^FG^&*^"
#==============================================server language================================================

#==========================================log saving function================================================
def save_logs(log):
    conn1 = sqlite3.connect(PATH+'\\main_database.db')
    c = conn1.cursor()
    c.execute("INSERT INTO Logs VALUES (:ALL_logs, :log)",
               {   'ALL_logs': "all",
                   'log': log,  
               })      
    conn1.commit()
    conn1.close()
#==========================================log saving function================================================

#==========================================delete client function=============================================
def Delete_Client():
 if messagebox.askyesno(title="Client Manager" , message="Do You Want To Remove This Client?",icon="warning"):
  info = client_Username.get()
  print(info)
  conn2 = sqlite3.connect(PATH+'\\main_database.db')
  c = conn2.cursor()
  c.execute(f"SELECT * FROM Client_Info WHERE  Username='{info}'")
  info3 = c.fetchone()
  conn2.commit()
  conn2.close()
  os.remove(f'{PATH}\\Chat_Data\\Rcv_profile\\{info}.db')
  os.remove(f'{PATH}\\Data_Files\\Client_profile\\{info3[8]}.png')
  conn2 = sqlite3.connect(PATH+'\\main_database.db')
  c = conn2.cursor()
  c.execute(f"DELETE  FROM Client_Info WHERE Username='{info}'")
  conn2.commit()
  conn2.close() 
  clients_to_server()
  current_date = strftime("%d/%b/%Y")
  current_time = strftime("%I:%M %p")
  text_area.insert(END, current_date+"-"+current_time+" > "+info+" has been removed from the server"+'\n')
  save_logs(current_date+"-"+current_time+" > "+info+" has been removed from the server"+'\n')
  client_name.delete(0,"end")
  client_ip.delete(0,"end")
  client_Location.delete(0,"end")
  client_password.delete(0,"end")
  client_Username.delete(0,"end")
  messagebox.showinfo(title='Client Manager',message='The Operation Completed Successfully!')
 else:
   messagebox.showinfo(title='Client Manager',message='The Operation Was Canciled!')
#===========================================delete client function============================================

#===============================================info preview function=========================================
def client_extract(f_name):
  global base3
  print(f_name)
  conn2 = sqlite3.connect(PATH+'\\main_database.db')
  c = conn2.cursor()
  c.execute(f"SELECT * FROM Client_Info WHERE Info_key='{f_name}'")
  info3 = c.fetchall()
  conn2.commit()
  conn2.close() 
  client_name.delete(0,"end")
  client_ip.delete(0,"end")
  client_Location.delete(0,"end")
  client_password.delete(0,"end")
  client_Username.delete(0,"end")
  client_name.insert(0,str(info3[0][1]).capitalize()+" "+str(info3[0][2]).capitalize())
  client_ip.insert(0,info3[0][7])
  client_Location.insert(0,str(info3[0][3]).capitalize())
  client_password.insert(0,info3[0][6])
  client_Username.insert(0,info3[0][5])
  image6 = Image.open(PATH+f'\\Data_Files\\Client_profile\\{f_name}.png')
  new_image6 = image6.resize((200,200))
  base3 = ImageTk.PhotoImage(new_image6)
  image_hold.config(image=base3)
#===============================================info preview function=========================================

#=============================================client assigner function========================================
def assigner(first,last,link):
   global base5
   image2 = Image.open(PATH+f'\\Data_Files\\Client_profile\\{link}.png')
   new_image1 = image2.resize((150,150))
   base5 = ImageTk.PhotoImage(new_image1)
   client_tab = CTkButton(master=second_frame,image=base5,compound=TOP,border=0,
             text=str(first).capitalize()+" "+str(last).capitalize(),command= lambda : client_extract(link))
   client_tab.pack(padx=120,pady=10)
#=============================================client assigner function========================================

   
 
#========================================import clients to pannel function====================================

def clients_to_server(): 
  for i in second_frame.winfo_children():
                   i.destroy()
  conn2 = sqlite3.connect(PATH+'\\main_database.db')
  c = conn2.cursor()
  c.execute(f"SELECT * FROM Client_Info WHERE All_clients='all'")
  info2 = c.fetchall()
  conn2.commit()
  conn2.close() 
  count = 0
  for i in info2:
    assigner(info2[count][1],info2[count][2],info2[count][8])
    count+=1         
  range_list = random.randint(1, 100)
  my_canvas.config(width=range_list)
  list1 = [400,396,397,403,401,399,402]
  from_list1 = random.choice(list1)
  my_canvas.config(width=from_list1)
#========================================import clients to pannel function====================================

#================================================creating database============================================
current_date = strftime("%d/%b/%Y")
current_time = strftime("%I:%M %p")
try:
 conn1 = sqlite3.connect(PATH+'\\main_database.db')
 c = conn1.cursor()
 c.execute("""CREATE TABLE Client_Info (
    ALL_clients,
    First_name text,
    Last_name text,
    Location text,
    Date text,
    Username text,
    Password text,
    Client_ip text,
    Info_key text
 )""")
 conn1.commit()
 conn1.close()
except sqlite3.OperationalError:
    pass 
try:
   conn1 = sqlite3.connect(PATH+'\\main_database.db')
   c = conn1.cursor()
   c.execute("""CREATE TABLE Logs (
      ALL_logs text,
      log text
      )""")
   conn1.commit()
   conn1.close()
except:
  pass   
#================================================creating database============================================

#=============================================stop server function============================================
def Stop():
    global connected
    global server
    connected = False
    server.close()
    Stop_server.config(state=DISABLED)
    Start_server.config(state=NORMAL)
    print("server has stopped!")
    current_date = strftime("%d/%b/%Y")
    current_time = strftime("%I:%M %p")
    text_area.insert(END, current_date+"-"+current_time+" > The server has Stop all operations!"+'\n')
    save_logs(current_date+"-"+current_time+" > The server has Stop all operations!"+'\n')
#=============================================stop server function============================================


#================================================handle client================================================
def Handle_client(conn, addr):
  global clients  
  try: 
    while connected:
        print("boby")
        Data_type = conn.recv(1024).decode(FORMAT)
        print(Data_type)
        Data_type = ast.literal_eval(Data_type)
        print(Data_type)
#=============================================================================================================              
        if Data_type[0] == REFRESH:
              conn3 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              c = conn3.cursor() 
              c.execute(f"SELECT * FROM Client_Chat_List WHERE ALL_clients='all'")
              info3 = c.fetchall()
              conn3.commit()
              conn3.close()
              print("hhhhhhhwwereh")
              file_size = os.path.getsize(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              conn.send(str(file_size).encode(FORMAT))
              time.sleep(1)
              conn.send(str(info3).encode(FORMAT))
#=============================================================================================================              
        if Data_type[0] == IMG_SEEK:
          print('hayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
          file2 = open(f"{PATH}\\Chat_Data\\Image_files\\{Data_type[1]}.png",'rb')
          data2 = file2.read()
          file2.close() 
          file_size = os.path.getsize(f"{PATH}\\Chat_Data\\Image_files\\{Data_type[1]}.png")
          conn.send(str(file_size).encode(FORMAT))
          time.sleep(1)
          conn.sendall(data2)
          print('hayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
#=============================================================================================================              
        if Data_type[0] == IMG_SEND:            
             rand1 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand2 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand3 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand4 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand5 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand6 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand7 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand8 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand9 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand10 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             key_val = str(random.choice(rand1)+random.choice(rand2)+random.choice(rand3)+random.choice(rand4)+random.choice(rand5)
                   +random.choice(rand6)+random.choice(rand7)+random.choice(rand8)+random.choice(rand9)+random.choice(rand10))         
             filename = (f"{PATH}\\Chat_Data\\Image_files\\{key_val}.png")
             new_file = open (filename, "wb")
             chat_size = conn.recv(1024).decode(FORMAT)
             Data = conn.recv(int(chat_size))
             new_file.write(Data)
             time.sleep(1)
             new_file.close()
             new_name_target = f"##**{Data_type[1]}"
             newsender = COVER_DATA+Data_type[2]
             data_info = [newsender,chat_size,key_val]
             for i in clients:
              i.send(new_name_target.encode(FORMAT))
              i.send(str(data_info).encode(FORMAT)) 
              time.sleep(1)          
              i.sendall(Data)
             current_time = strftime("%I:%M %p")
             conn2 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[2]}.db')
             c = conn2.cursor()
             c.execute(f"SELECT * FROM Client_Chat_List WHERE user_name='{Data_type[1]}'")
             info_val = c.fetchone() 
             conn2.commit()
             conn2.close() 
             hashed_data = f"#@#@#{Data_type[2]}"
             conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Data_Rcv\\{info_val[2]}.db')
             c = conn1.cursor()
             c.execute("INSERT INTO Client_Chat VALUES (:ALL_clients, :Message, :Tag, :Time)",
                    {   'ALL_clients': "all",
                        'Message': key_val,
                        'Tag': hashed_data,
                        'Time' : current_time
                    })      
             conn1.commit()
             conn1.close()             
#=============================================================================================================              
        if Data_type[0] == WHO_IS_HERE:
           conn2 = sqlite3.connect(PATH+'\\main_database.db')
           c = conn2.cursor()
           c.execute(f"SELECT * FROM Client_Info WHERE All_clients='all'")
           info = c.fetchall()
           info_out = []
           for i in info:
              info_out.append(i[5])
           print(info_out)
           conn.send(WHO_IS_HERE.encode(FORMAT))
           time.sleep(1)
           conn.send(str(info_out).encode(FORMAT))
#=============================================================================================================                      
        if Data_type[0] == ADD_CHAT:
         conn2 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
         c = conn2.cursor()
         c.execute(f"SELECT * FROM Client_Chat_List WHERE user_name='{Data_type[2]}'")
         first_info = c.fetchone() 
         conn2.commit()
         conn2.close()
         if first_info == None:
             rand1 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand2 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand3 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand4 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand5 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand6 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand7 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand8 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand9 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             rand10 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
             key_val = str(random.choice(rand1)+random.choice(rand2)+random.choice(rand3)+random.choice(rand4)+random.choice(rand5)
                   +random.choice(rand6)+random.choice(rand7)+random.choice(rand8)+random.choice(rand9)+random.choice(rand10))
             conn2 = sqlite3.connect(PATH+'\\main_database.db')
             c = conn2.cursor()
             c.execute(f"SELECT * FROM Client_Info WHERE Username='{Data_type[2]}'")
             info = c.fetchone()
             conn2.commit()
             conn2.close() 
             current_date = strftime("%d/%b/%Y")
             current_time = strftime("%I:%M %p")
             if info == None:
              conn.send(NA.encode(FORMAT))
              text_area.insert(END, current_date+"-"+current_time+" > A client failed to add {} to their chats!".format(Data_type[2])+'\n')
              save_logs(current_date+"-"+current_time+" > A client failed to add {} to their chats!".format(Data_type[2])+'\n') 
             else:
              conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Data_Rcv\\{key_val}.db')
              c = conn1.cursor()
              c.execute("""CREATE TABLE Client_Chat (
              ALL_clients,
              Message,
              Tag,
              Time
              )""")
              conn1.commit()
              conn1.close()
              conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[2]}.db')
              c = conn1.cursor()
              c.execute("INSERT INTO  Client_Chat_List VALUES (:ALL_clients, :user_name, :chat_file_name)",
                    {   'ALL_clients': "all",
                        'user_name': Data_type[1],
                        'chat_file_name' : key_val
                    })      
              conn1.commit()
              conn1.close()
              conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              c = conn1.cursor()
              c.execute("INSERT INTO  Client_Chat_List VALUES (:ALL_clients, :user_name, :chat_file_name)",
                    {   'ALL_clients': "all",
                        'user_name': Data_type[2],
                        'chat_file_name' : key_val
                    })   
              conn1.commit()
              conn1.close()
              text_area.insert(END, current_date+"-"+current_time+" > A client added {} to their chats!".format(Data_type[2])+'\n')
              save_logs(current_date+"-"+current_time+" > A client added {} to their chats!".format(Data_type[2])+'\n')
              conn.send(YA.encode(FORMAT))
              conn3 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              c = conn3.cursor() 
              c.execute(f"SELECT * FROM Client_Chat_List WHERE ALL_clients='all'")
              info3 = c.fetchall()
              conn3.commit()
              conn3.close()
              file_size = os.path.getsize(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              conn.send(str(file_size).encode(FORMAT))
              time.sleep(1)
              conn.send(str(info3).encode(FORMAT))      
         else:
              conn.send(NA.encode(FORMAT))
              text_area.insert(END, current_date+"-"+current_time+" > A client failed to add {} to their chats!".format(Data_type[2])+'\n')
              save_logs(current_date+"-"+current_time+" > A client failed to add {} to their chats!".format(Data_type[2])+'\n')  
#=============================================================================================================                    
        while Data_type[0] == GET_DATA:            
          data3 = []
          conn3 = sqlite3.connect(f'{PATH}\\Chat_Data\\Data_Rcv\\{Data_type[1]}.db')
          c = conn3.cursor() 
          c.execute(f"SELECT * FROM Client_Chat WHERE ALL_clients='all'")
          info3 = c.fetchall()
          conn3.commit()
          conn3.close()
          for i in info3:
              data3.append(i)
          chat_size = os.path.getsize(f'{PATH}\\Chat_Data\\Data_Rcv\\{Data_type[1]}.db')
          conn.send(OUT_DATA.encode(FORMAT))
          conn.send(str(chat_size).encode(FORMAT))
          time.sleep(1)
          conn.send(str(data3).encode(FORMAT)) 
          break
#=============================================================================================================              
        while Data_type[0] == LOGIN:       
          conn2 = sqlite3.connect(PATH+'\\main_database.db')
          c = conn2.cursor()
          c.execute(f"SELECT * FROM Client_Info WHERE Username='{Data_type[1]}'")
          info = c.fetchone()
          current_date = strftime("%d/%b/%Y")
          current_time = strftime("%I:%M %p")
          try:
            if Data_type[2] == info[6]:
              text_area.insert(END, current_date+"-"+current_time+" > "+Data_type[1]+", logged is sucessfully!"+'\n')
              conn.send(YA.encode(FORMAT)) 
              pic_file_size = os.path.getsize(f'{PATH}\\Data_Files\\Client_profile\\{info[8]}.png')
              file2 = open(f"{PATH}\\Data_Files\\Client_profile\\{info[8]}.png",'rb')
              data5 = file2.read()
              file2.close()         
              conn.send(str(pic_file_size).encode(FORMAT))
              time.sleep(1)
              conn.sendall(data5)                     
              data2 = []       
              conn2 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
              c = conn2.cursor()
              c.execute(f"SELECT * FROM Client_Chat_List WHERE ALL_clients='all'")
              info2 = c.fetchall()
              for i in info2:
                data2.append(i)            
              time.sleep(1)
              conn.sendall(str(data2).encode(FORMAT)) 
              save_logs(current_date+"-"+current_time+" > "+Data_type[1]+", logged is sucessfully!"+'\n')
            else:
              conn.send(NA.encode(FORMAT))
              text_area.insert(END, current_date+"-"+current_time+" > "+Data_type[1]+", had an error logging in"+'\n')
              save_logs(current_date+"-"+current_time+" > "+Data_type[1]+", had an error logging in"+'\n')               
          except:
              conn.send(NA.encode(FORMAT))        
              text_area.insert(END, current_date+"-"+current_time+" > "+Data_type[1]+", had an error logging in"+'\n') 
              save_logs(current_date+"-"+current_time+" > "+Data_type[1]+", had an error logging in"+'\n')   
          conn2.commit()
          conn2.close()
          break
#=============================================================================================================              
        while Data_type[0] == BROAD:
            newsender = COVER_DATA+Data_type[1]
            msg_data = [newsender,Data_type[3]]
            for i in clients:
             i.send(Data_type[2].encode(FORMAT))           
             i.send(str(msg_data).encode(FORMAT))
            conn2 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{Data_type[1]}.db')
            c = conn2.cursor()
            c.execute(f"SELECT * FROM Client_Chat_List WHERE user_name='{Data_type[2]}'")
            info_val = c.fetchone() 
            conn2.commit()
            conn2.close()
            conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Data_Rcv\\{info_val[2]}.db')
            c = conn1.cursor()
            c.execute("INSERT INTO Client_Chat VALUES (:ALL_clients, :Message, :Tag, :Time)",
                    {   'ALL_clients': "all",
                        'Message': Data_type[3],
                        'Tag': Data_type[1],
                        'Time' : current_time
                    })      
            conn1.commit()
            conn1.close()
            break  
#=============================================================================================================              
        while Data_type[0] == SIGN_IN:
         size_img = conn.recv(1024).decode(FORMAT)
         data = conn.recv(int(size_img))
         try:  
             ent1 = Data_type[1]
             ent2 =  Data_type[2]
             ent3 = Data_type[3]
             ent4 =  Data_type[4]
             ent5 =  Data_type[5]
             conn2 = sqlite3.connect(PATH+'\\main_database.db')
             c = conn2.cursor()
             c.execute(f"SELECT * FROM Client_Info WHERE Username='{ent4}'")
             info = c.fetchone()
             if info == None:  
                conn.send(AVAILIABLE.encode(FORMAT))
                rand1 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand2 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand3 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand4 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand5 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand6 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand7 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand8 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand9 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                rand10 = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                key_val = str(random.choice(rand1)+random.choice(rand2)+random.choice(rand3)+random.choice(rand4)+random.choice(rand5)
                +random.choice(rand6)+random.choice(rand7)+random.choice(rand8)+random.choice(rand9)+random.choice(rand10))
                file2 = open(f"{PATH}\\Data_Files\\Client_profile\\{key_val}.png",'wb')
                file2.write(data)
                time.sleep(1)
                file2.close()
                conn1 = sqlite3.connect(PATH+'\\main_database.db')
                c = conn1.cursor()
                current_date = strftime("%d/%b/%Y")
                current_time = strftime("%I:%M %p")  
                c.execute("INSERT INTO Client_Info VALUES (:ALL_clients, :First_name, :Last_name, :Location, :Date, :Username, :Password, :Client_ip, :Info_key)",
                {   'ALL_clients': "all",
                   'First_name': ent1,
                   'Last_name' :ent2,
                   'Location': ent3,
                   'Username': ent4,
                   'Password' : ent5,
                   'Date' : current_date,
                   'Client_ip' : addr[0],
                   'Info_key' : key_val
                })    
                conn1.commit()
                conn1.close()
                conn1 = sqlite3.connect(f'{PATH}\\Chat_Data\\Rcv_profile\\{ent4}.db')
                c = conn1.cursor()
                c.execute("""CREATE TABLE Client_Chat_List (
                ALL_clients,
                user_name text,
                chat_file_name text
                )""")
                conn1.commit()
                conn1.close()
                text_area.insert(END, current_date+"-"+current_time+" > A new client has been added"+'\n')
                text_area.insert(END, current_date+"-"+current_time+" > Client's Name "+ent1+" "+ent2+'\n')
                save_logs(current_date+"-"+current_time+" > A new client has been added"+'\n')
                save_logs(current_date+"-"+current_time+" > Client's Name "+ent1+" "+ent2+'\n')
                clients_to_server() 
                time.sleep(1)
                clients_to_server()
             else:
                text_area.insert(END, current_date+"-"+current_time+" > There was a sign up error"+'\n')
                save_logs(current_date+"-"+current_time+" > There was a sign up error"+'\n')
                text_area.insert(END, current_date+"-"+current_time+" > Error = User Name Exist's"+'\n')
                save_logs(current_date+"-"+current_time+" > Error = User Name Exist's"+'\n')
                text_area.insert(END, current_date+"-"+current_time+" > Attempted user name = "+ent4+'\n')
                save_logs(current_date+"-"+current_time+" > Attempted user name = "+ent4+'\n')
                conn.send(USER_EXIST.encode(FORMAT))  
             conn2.commit()
             conn2.close()
             break
         except FileNotFoundError:
             break
#=============================================================================================================              
  except:
    conn.close()
    clients.remove(conn)
#================================================handle client================================================

#=======================================applying new address functio==========================================              
def apply_ip():
  global ADDR
  server_value = ip_ent.get()
  port_value = port_ent.get()
  ADDR = (server_value,int(port_value))
  ip_ent.delete(0,"end")
  port_ent.delete(0,"end")
#=======================================applying new address functio==========================================              

#==========================================default address functio============================================              
def start_up_ip():
  global ADDR
  server_value = socket.gethostbyname(socket.gethostname())
  port_value = 5050
  ADDR = (server_value,port_value)
#==========================================default address functio============================================              

#===========================================change address functio============================================              
def settings():
  global ip_ent
  global port_ent
  win2 = CTkToplevel()
  ip_ent = CTkEntry(win2,placeholder_text="Ip Address")
  ip_ent.pack(pady=10,padx=10)
  port_ent = CTkEntry(win2,placeholder_text="Port")
  port_ent.pack(pady=10,padx=10)
  submit = CTkButton(win2,text="Apply",command=apply_ip)
  submit.pack(pady=10,padx=10)

  mainloop()
def start():
    global clients
    global server
    global connected
    connected = True
    clients = []
    current_date = strftime("%d/%b/%Y")
    current_time = strftime("%I:%M %p")
    print(ADDR)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("server is running!")
    text_area.insert(END, current_date+"-"+current_time+" > The server is running!"+'\n')
    save_logs(current_date+"-"+current_time+" > The server is running!"+'\n')
    server.listen()
    try: 
     while True:
        conn, addr = server.accept()
        clients.append(conn)
        client_thread = threading.Thread(target=Handle_client, args=(conn, addr))
        client_thread.start()
    except:
        pass    
#===========================================change address functio============================================              

#===========================================initialize server functio=========================================              
def intialize():
    global connected
    Stop_server.config(state=NORMAL)
    Start_server.config(state=DISABLED)
    start_thread = threading.Thread(target=start)
    start_thread.start()
connected = True
start_up_ip()
#===========================================initialize server functio=========================================              

#================================================BACK END=====================================================

#==================================================FRONT END==================================================

count = 0
win = CTk()
win.geometry("800x800")

#==============================================image imports==================================================
image1 = Image.open(PATH+'\\Data_Files\\IMG\\1.png')
new_image1 = image1.resize((200,200))
base1 = ImageTk.PhotoImage(new_image1)
imagea = Image.open(PATH+'\\Data_Files\\IMG\\4.png')
new_imagea = imagea.resize((40,40))
basea = ImageTk.PhotoImage(new_imagea)
#==============================================image imports==================================================

#================================================left panel===================================================
set_appearance_mode("Light") 
set_default_color_theme("dark-blue") 
win.grid_columnconfigure(1, weight=1)
win.grid_rowconfigure(0, weight=1)
frame_left = CTkFrame(master=win,width=310,corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")
s = Style()
s.theme_use('alt')
s.configure("TScrollbar",troughcolor="#dedede")
main_frame = CTkFrame(master=frame_left,width=80,corner_radius=30)
main_frame.pack(padx=5,side=LEFT,fill=Y)
my_canvas = Canvas(main_frame,borderwidth=0,bg="#f0f0f0")
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame,command=my_canvas.yview,style="TScrollbar")
my_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure
                   (scrollregion = my_canvas.bbox("all")))
second_frame = Frame(my_canvas,bg="#f0f0f0")
my_canvas.create_window((0,0), window=second_frame, anchor="nw")
#================================================left panel===================================================

#===============================================right top panel===============================================
frame_right = CTkFrame(master=win)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
frame_right.grid_columnconfigure(0, weight=1)
frame_right.grid_rowconfigure(2, weight=1)
Display = CTkFrame(master=frame_right,height=600)
Display.grid(row=1, column=0,sticky="wesn", padx=20, pady=20)
settings_buttons = Button(Display,image=basea,border=0,activebackground="#dedede",
                                                    bg="#dedede",command=settings)
settings_buttons.place(x=5,y=5)
Display.grid_columnconfigure(0, weight=1)
Display.grid_rowconfigure(2, weight=1)
image_hold = CTkLabel(master=Display,image=base1)
image_hold.grid(row=0,column=1,pady=40)
space1 = CTkLabel(master=Display,text="")
space1.grid(row=1,column=0,)
client_name = CTkEntry(master=Display,width=250,placeholder_text="Client Name")
client_name.grid(row=2,column=0,pady=20,padx=20,columnspan=2,sticky="we")
client_ip = CTkEntry(master=Display,width=250,placeholder_text="Client IP address")
client_ip.grid(row=2,column=2,pady=20,padx=20)
client_Location = CTkEntry(master=Display,width=250,placeholder_text="Client Location")
client_Location.grid(row=3,column=0,pady=20,padx=20)
client_Username = CTkEntry(master=Display,width=250,placeholder_text="Client Username")
client_Username.grid(row=3,column=1,pady=20,padx=20)
client_password = CTkEntry(master=Display,width=250,placeholder_text="Client Password")
client_password.grid(row=3,column=2,pady=20,padx=20)
Delete_Client = CTkButton(master=Display,text="Delete Client",command=Delete_Client)
Delete_Client.grid(row=4,column=1,sticky="we")
space1 = CTkLabel(master=Display,text="")
space1.grid(row=5,column=0,)
#===============================================right top panel===============================================

#============================================right buttom panel===============================================
Menu_frame = CTkFrame(master=frame_right)
Menu_frame.grid(row=2, column=0,sticky="wesn", padx=20, pady=20)
Menu_frame.grid_columnconfigure(1, weight=1)
Menu_frame.grid_rowconfigure(0, weight=0)
space2 = CTkLabel(master=Menu_frame,width=140,text="")
space2.grid(row=0, column=0, padx=20, pady=20,sticky="ewns")
controll_menu = CTkFrame(master=Menu_frame)
controll_menu.place(x=20,y=20)
controll_menu.grid_columnconfigure(1, weight=1)
controll_menu.grid_rowconfigure(2, weight=0)
Start_server = CTkButton(master=controll_menu,text="Start Server",command=intialize)
Start_server.grid(row=0,column=0,sticky="we",padx=20, pady=10)
Stop_server = CTkButton(master=controll_menu,text="Stop Server",command=Stop,state=DISABLED)
Stop_server.grid(row=1,column=0,sticky="we",padx=20, pady=10)
controll_info = CTkFrame(master=Menu_frame)
controll_info.grid(row=0, column=1,sticky="ewns", padx=20, pady=20)
controll_info.grid_columnconfigure(2, weight=1)
controll_info.grid_rowconfigure(1, weight=1)
space3 = CTkFrame(master=controll_info)
space3.grid(row=0, column=2,sticky="ewns", padx=20, pady=20)
text_area = tkinter.scrolledtext.ScrolledText(controll_info,border=0,bg="#ebebeb",width=40,height=18)
text_area.grid(row=0, column=0,sticky="ewns",padx=5,pady=5,columnspan=3)
#============================================right buttom panel===============================================
try:
 conn2 = sqlite3.connect(f'{PATH}\\main_database.db')
 c = conn2.cursor()
 c.execute("SELECT * FROM Logs WHERE ALL_logs='all'")
 logs_info = c.fetchall()
 for i in logs_info:
  text_area.insert("end",i[1])
 conn2.commit()
 conn2.close()
except:
  pass
clients_to_server()
win.mainloop()
#==================================================FRONT END==================================================
