
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk, ImageFile, ImageDraw, ImageOps
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
import os
import ast
ImageFile.LOAD_TRUNCATED_IMAGES = True

#================================================BACK END=====================================================

#==============================================server language================================================
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
PATH = os.path.dirname(os.path.realpath(__file__))
#==============================================server language================================================

#======================================back end connection function===========================================  
def connect():
  global ADDR
  ADDR = (ip_in.get(), int(port_in.get()))
  ip_win.destroy()
try:
   conn1 = sqlite3.connect(PATH+'\\Data_Files\\Connections\\Conn_File.db')
   c = conn1.cursor()
   c.execute("""CREATE TABLE connections (
      ALL_conns text,
      ip text,
      port text
      )""")
   conn1.commit()
   conn1.close()
except:
  pass 
def save_connect():
  conn1 = sqlite3.connect(PATH+'\\Data_Files\\Connections\\Conn_File.db')
  c = conn1.cursor()
  c.execute("INSERT INTO connections VALUES (:ALL_conns, :ip, :port)",
    {   'ALL_conns': "all",
        'ip': ip_in.get(),
        'port': port_in.get()
    })  
  list_of_connections.delete(0,"end")  
  conn1.commit()
  c.execute(f"SELECT * FROM connections WHERE ALL_conns='all'")
  info_val = c.fetchall() 
  conn1.commit()
  conn1.close()
  for i in info_val:
    list_of_connections.insert("end",f"{i[1]}-{i[2]}") 
def fill_data(e):
  info = list_of_connections.get(ACTIVE)
  text1 = info.split("-")
  port = (repr(text1[-1])).replace("'","")
  int(port)
  info = list_of_connections.get(ACTIVE)
  text = info.split("-")
  adr = (repr(text[0])).strip(" ").replace("'","")
  ip_in.delete(0,"end")
  port_in.delete(0,"end")
  ip_in.insert(0,adr)
  port_in.insert(0,port)
#======================================back end connection function===========================================  

#======================================front end connection function==========================================  
ip_win = CTk()
ip_win.geometry("400x220")
ip_win.resizable(False,False)
list_of_connections = Listbox(ip_win,width=18,height=12,border=0,font=("arial",11),bg="#333333",
                                         highlightcolor="#333333",highlightbackground="#333333")
list_of_connections.place(x=0,y=0)
ip_in = CTkEntry(ip_win,width=200,placeholder_text="Server_Address")
ip_in.place(x=183,y=35) 
list_of_connections.bind("<Button-1>",fill_data)
port_in = CTkEntry(ip_win,width=90,placeholder_text="Port")
port_in.place(x=183,y=70)
save_button= CTkButton(ip_win,text="Save Connection",command=save_connect)
save_button.place(x=225,y=130)
conn_button= CTkButton(ip_win,text="Connect",command=connect)
conn_button.place(x=225,y=170)
conn1 = sqlite3.connect(PATH+'\\Data_Files\\Connections\\Conn_File.db')
c = conn1.cursor()
c.execute(f"SELECT * FROM connections WHERE ALL_conns='all'")
info_val = c.fetchall() 
conn1.commit()
conn1.close()
for i in info_val:
  list_of_connections.insert("end",f"{i[1]}-{i[2]}") 
ip_win.mainloop()
try:
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect(ADDR)
except:
 print("couldn't make a connection with the listed ip")
 quit()
#======================================front end connection function==========================================  

def chat_main():
#======================================image link proccessing function========================================  
  global message_listener
  def img_start():
    global img_id_out
    os.startfile(f"{PATH}\\Data_Files\\Chat_data_files\\{img_id_out}.png")  
  def open_img(img_id):
    global img_id_out
    img_id_out = img_id
    x = threading.Thread(target=img_start)
    x.start()
  def img_start_for_main():
    global img_id_in
    os.startfile(img_id_in)  
  def open_img_for_main(id_img):
    global img_id_in
    img_id_in = id_img
    x = threading.Thread(target=img_start_for_main)
    x.start()
  def image_assiner(Data_info):
    global image_post_img
    image_post_img.config(command= lambda : open_img(Data_info))
#======================================image link proccessing function========================================  

#==========================================data listener function=============================================  
  def message_listener():
   global Database_chat_new
   global target_client
   global image_post_img
   global image_post
   global address_input 
   global new_frame
   while True:
     try:  
      msg = client.recv(1024).decode(FORMAT)
     except:
      pass 
#=============================================================================================================    
     if msg == main_user:
      info_msg = client.recv(1024).decode(FORMAT)
      info_msg = ast.literal_eval(info_msg)
      if info_msg[0] == COVER_DATA+target_client:
       test_frame = Frame(new_frame,bg="#f2f2f2")
       test_frame.pack(fill=X,expand=1)
       other_frame =CTkFrame(test_frame)
       other_frame.pack(side=LEFT,padx=5,pady=5)
       current_time = strftime("%I:%M %p")
       time_sent2 = Label(master=other_frame,text=current_time,bg="#dbdbdb",font=("arial",6))
       time_sent2.place(x=0,y=0)
       test1 = CTkLabel(master=other_frame,text=info_msg[1],justify=LEFT)
       test1.pack(padx=5,pady=13)
       range_list1 = random.randint(1, 100)
       canvas.config(width=range_list1)
       list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
       from_list2 = random.choice(list2)
       canvas.config(width=from_list2) 
      else:
       data = [REFRESH,main_user] 
       client.send(str(data).encode(FORMAT))
       file_size = client.recv(1024).decode(FORMAT)
       Database_client_list = client.recv(int(file_size)).decode(FORMAT)
       Database_client_list = ast.literal_eval(Database_client_list)
       try:
        for i in second_frame.winfo_children():
            i.destroy()
        for i in Database_client_list:
            assigner(i[1],i[2])
       except:
           pass
       notification.config(compound=LEFT,text=f"  Message from {i[1]}")
#=============================================================================================================    
     elif msg == WHO_IS_HERE:      
        clients_avl = client.recv(5000).decode(FORMAT)
        clients_avl = ast.literal_eval(clients_avl)
        select["menu"].delete(0,"end")
        for i in clients_avl:
          select["menu"].add_command(label=i,command=lambda value=i: insert_val(value))
          option.append(str(i)) 
#=============================================================================================================    
     elif msg == f"##**{main_user}":
       Data_info = client.recv(1024).decode(FORMAT)
       Data_info = ast.literal_eval(Data_info)
       if Data_info[0] == COVER_DATA+target_client:
        filename = (f"{PATH}\\Data_Files\\Chat_data_files\\{Data_info[2]}.png")
        new_file = open (filename, "wb")
        Data = client.recv(int(Data_info[1])) 
        new_file.write(Data)
        time.sleep(1)
        new_file.close()         
        test_frame2 = Frame(new_frame,bg="#f2f2f2")
        test_frame2.pack(fill=X,expand=1)
        other_frame2 =CTkFrame(test_frame2)
        other_frame2.pack(side=LEFT,padx=5,pady=5)
        current_time = strftime("%I:%M %p")
        time_sent3 = Label(master=other_frame2,text=current_time,bg="#dbdbdb",font=("arial",6))
        time_sent3.place(x=0,y=0)
        image1 = Image.open(f"{PATH}\\Data_Files\\Chat_data_files\\{Data_info[2]}.png")
        new_image1 = image1.resize((400,450))
        base_img_file = ImageTk.PhotoImage(new_image1) 
        image_post_img = CTkButton(master=other_frame2,text="",image=base_img_file)
        image_post_img.pack(padx=5,pady=13)
        image_assiner(Data_info[2])        
       else:
         Data = client.recv(int(Data_info[1]))
         data = [REFRESH,main_user] 
         client.send(str(data).encode(FORMAT))
         file_size = client.recv(1024).decode(FORMAT)
         Database_client_list = client.recv(int(file_size)).decode(FORMAT)
         Database_client_list = ast.literal_eval(Database_client_list)
         for i in second_frame.winfo_children():
            i.destroy()
         try:    
          for i in Database_client_list:
            assigner(i[1],i[2])
         except:
            pass
         notification.config(compound=LEFT,text=f"  {i[1]} sent an image")  
       range_list1 = random.randint(1, 100)
       canvas.config(width=range_list1)
       list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
       from_list2 = random.choice(list2)
       canvas.config(width=from_list2) 
#=============================================================================================================    
     elif msg == YA:
       file_size = client.recv(1024).decode(FORMAT)
       time.sleep(1)
       Database_client_list = client.recv(int(file_size)).decode(FORMAT)
       Database_client_list = ast.literal_eval(Database_client_list)
       new_chat.delete(0,"end")
       get_client_avaliable()
       try:
        for i in second_frame.winfo_children():
            i.destroy()
        for i in Database_client_list:
            assigner(i[1],i[2])
       except:
           pass 
#=============================================================================================================    
     elif msg == NA:
       pass
#============================================================================================================= 
     elif msg == OUT_DATA:
       size = client.recv(1024).decode(FORMAT) 
       Database_chat_new = client.recv(int(size)).decode(FORMAT)
       msg = ast.literal_eval(Database_chat_new)
       message_input.config(state=NORMAL)
       send_button.config(state=NORMAL)
       for i in new_frame.winfo_children():
            i.destroy()
       test = CTkLabel(master=new_frame,text="Chats",width=new_size)
       test.pack()       
       try:
        for i in msg:
#===========================================chat assigner=====================================================    
         if i[2] == main_user:
           test_frame2 = Frame(new_frame,bg="#f2f2f2")
           test_frame2.pack(fill=X,expand=1)
           other_frame2 =CTkFrame(test_frame2)
           other_frame2.pack(side=RIGHT,padx=5,pady=5)
           test2 = CTkLabel(master=other_frame2,text=i[1],justify=LEFT)
           test2.pack(padx=5,pady=13)
           time_sent1 = Label(master=other_frame2,text=i[3],bg="#dbdbdb",font=("arial",6))
           time_sent1.place(x=0,y=0) 
#=================================================================================================            
         elif i[2] == f"#@#@#{main_user}":          
            info = [IMG_SEEK,i[1]]
            try:
              image4 = Image.open(f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
              new_image4 = image4.resize((400,450))
              base_image4 = ImageTk.PhotoImage(new_image4)             
            except:  
              client.send(str(info).encode(FORMAT))
              file_size = client.recv(1024).decode(FORMAT)
              filename = (f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
              new_file = open (filename, "wb")
              Data = client.recv(int(file_size)) 
              new_file.write(Data)
              time.sleep(1)
              new_file.close() 
              image4 = Image.open(f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
              new_image4 = image4.resize((400,450))
              base_image4 = ImageTk.PhotoImage(new_image4)
            test_frame4 = Frame(new_frame,bg="#f2f2f2")
            test_frame4.pack(fill=X,expand=1)
            other_frame4 =CTkFrame(test_frame4)
            other_frame4.pack(side=RIGHT,padx=5,pady=5)
            time_sent4 = Label(master=other_frame4,text=current_time,bg="#dbdbdb",font=("arial",6))
            time_sent4.place(x=0,y=0)
            image_post = CTkButton(master=other_frame4,text="",image=base_image4)
            image_post.pack(padx=5,pady=13)
            append_file(i[1])
            range_list1 = random.randint(1, 100)
            canvas.config(width=range_list1)
            list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
            from_list2 = random.choice(list2)
            canvas.config(width=from_list2) 
#=================================================================================================            
         elif i[2] == f"#@#@#{target_client}":
            info = [IMG_SEEK,i[1]]
            try:
             image4 = Image.open(f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
             new_image4 = image4.resize((400,450))
             base_image4 = ImageTk.PhotoImage(new_image4)
            except: 
             client.send(str(info).encode(FORMAT))
             file_size = client.recv(1024).decode(FORMAT)
             filename = (f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
             new_file = open (filename, "wb")
             Data = client.recv(int(file_size)) 
             new_file.write(Data)
             time.sleep(1)
             new_file.close()  
             image4 = Image.open(f"{PATH}\\Data_Files\\Chat_data_files\\{i[1]}.png")
             new_image4 = image4.resize((400,450))
             base_image4 = ImageTk.PhotoImage(new_image4)
            test_frame4 = Frame(new_frame,bg="#f2f2f2")
            test_frame4.pack(fill=X,expand=1)
            other_frame4 =CTkFrame(test_frame4)
            other_frame4.pack(side=LEFT,padx=5,pady=5)
            time_sent4 = Label(master=other_frame4,text=current_time,bg="#dbdbdb",font=("arial",6))
            time_sent4.place(x=0,y=0)
            image_post = CTkButton(master=other_frame4,text="",image=base_image4)
            image_post.pack(padx=5,pady=13)
            append_file(i[1])      
            range_list1 = random.randint(1, 100)
            canvas.config(width=range_list1)
            list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
            from_list2 = random.choice(list2)
            canvas.config(width=from_list2) 
         else:
#=================================================================================================            
           test_frame2 = Frame(new_frame,bg="#f2f2f2")
           test_frame2.pack(fill=X,expand=1)
           other_frame2 =CTkFrame(test_frame2)
           other_frame2.pack(side=LEFT,padx=5,pady=5)
           test2 = CTkLabel(master=other_frame2,text=i[1],justify=LEFT)
           test2.pack(padx=5,pady=13)
           time_sent1 = Label(master=other_frame2,text=i[3],bg="#dbdbdb",font=("arial",6))
           time_sent1.place(x=0,y=0) 
#===========================================chat assigner=====================================================    
       except:
         pass
       range_list1 = random.randint(1, 200)
       canvas.config(width=range_list1)
       list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
       from_list2 = random.choice(list2)
       canvas.config(width=from_list2) 
     else:
          pass
#==========================================data listener function=============================================  

#=========================================image link assigner function========================================  
  def append_file(id):
    global image_post
    image_post.config(command = lambda : open_img_for_main(f"{PATH}\\Data_Files\\Chat_data_files\\{id}.png"))
#=========================================image link assigner function========================================  

#============================================import clients function==========================================  
  def import_chat():
       global message_listener         
       Database_client_list = client.recv(5000).decode(FORMAT)     
       Database_client_list = ast.literal_eval(Database_client_list)
       try:
         for i in second_frame.winfo_children():
            i.destroy()
         for i in Database_client_list:
            assigner(i[1],i[2])
       except:
           pass
       x = threading.Thread(target=message_listener,daemon=True)
       x.start() 
       get_client_avaliable()
#=============================================import chat function============================================  

#==============================================initialize chat function=======================================  
  def start_chat(name,Database_key):
    global target_client
    global current_chat
    notification.config(compound=LEFT,text="")
    current_chat = name
    target_client = name
    data2 = [GET_DATA,Database_key]
    client.send(str(data2).encode(FORMAT))
    current_data = Database_key
#==============================================initialize chat function=======================================  

#==============================================availiable chat function=======================================    
  def get_client_avaliable():
    data = [WHO_IS_HERE]
    client.send(str(data).encode(FORMAT))
#==============================================availiable chat function=======================================  

#============================================send message (text) function=====================================  
  def send_new():
   while True: 
    message_out = message_input.get("1.0","end")
    message_input.delete("1.0","end")
    message_info = [BROAD,main_user,target_client,message_out]
    client.send(str(message_info).encode(FORMAT))
    break
  def send_message():
    global current_chat
    current_time = strftime("%I:%M %p")
    message_out = message_input.get("1.0","end")
    test_frame2 = Frame(new_frame,bg="#f2f2f2")
    test_frame2.pack(fill=X,expand=1)
    other_frame2 =CTkFrame(test_frame2)
    other_frame2.pack(side=RIGHT,padx=5,pady=5)
    test2 = CTkLabel(master=other_frame2,text=message_out,justify=LEFT)
    test2.pack(padx=5,pady=13)
    time_sent1 = Label(master=other_frame2,text=current_time,bg="#dbdbdb",font=("arial",6))
    time_sent1.place(x=0,y=0)
    range_list1 = random.randint(1, 100)
    canvas.config(width=range_list1)
    list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
    from_list2 = random.choice(list2)
    canvas.config(width=from_list2)
    range_list1 = random.randint(1, 100)
    canvas.config(width=range_list1)
    list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
    from_list2 = random.choice(list2)
    canvas.config(width=from_list2) 
    send_n = threading.Thread(target=send_new)
    send_n.start() 
#============================================send message (text) function=====================================  

#===========================================send message (image) function=====================================  
  def send_image_server(data,size):
     global target_client
     while True: 
      message_info = [IMG_SEND,target_client,main_user]
      client.send(str(message_info).encode(FORMAT))
      client.send(str(size).encode(FORMAT))
      time.sleep(1)
      client.send(data)
      range_list1 = random.randint(1, 100)
      canvas.config(width=range_list1)
      list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
      from_list2 = random.choice(list2)
      canvas.config(width=from_list2) 
      break
  def send_image():
    current_time = strftime("%I:%M %p")
    filepath = filedialog.askopenfilename()
    image = Image.open(filepath)
    image.resize((500,550), Image.ANTIALIAS)
    image.save(f"{PATH}\\Data_Files\\Temp\\Temp_img.png",quality=50)
    file_size = os.path.getsize(f"{PATH}\\Data_Files\\Temp\\Temp_img.png")
    file2 = open(f"{PATH}\\Data_Files\\Temp\\Temp_img.png",'rb')
    data2 = file2.read()
    file2.close()
    test_frame2 = Frame(new_frame,bg="#f2f2f2")
    test_frame2.pack(fill=X,expand=1)
    other_frame2 =CTkFrame(test_frame2)
    other_frame2.pack(side=RIGHT,padx=5,pady=5)
    image1 = Image.open(f"{PATH}\\Data_Files\\Temp\\Temp_img.png")
    new_image1 = image1.resize((400,450))
    base_image = ImageTk.PhotoImage(new_image1)
    time_sent1 = Label(master=other_frame2,text=current_time,bg="#dbdbdb",font=("arial",6))
    time_sent1.place(x=0,y=0)
    image_post = CTkButton(master=other_frame2,text="",image=base_image)
    image_post.pack(padx=5,pady=13)
    image_post.config(command = lambda : open_img_for_main(filepath))
    send_img_thread = threading.Thread(target=send_image_server, args=(data2,file_size))
    send_img_thread.start()
    range_list1 = random.randint(1, 100)
    canvas.config(width=range_list1)
    list2 = [new_size+1,new_size,new_size-1,new_size-2,new_size+2]
    from_list2 = random.choice(list2)
    canvas.config(width=from_list2) 
    mainloop()
#===========================================send message (image) function=====================================  
 
#=============================================chat list assigner function=====================================   
  def assigner(name,Database_key):
   global main_user
   global PATH
   try:
     id_name = CTkButton(master=second_frame,image=base2,border=0,text="3",bg_color="#e5e5e5")
     id_name.pack(padx=5,pady=10)
     id_name.config(command= lambda : start_chat(name,Database_key))   
     text_label= Label(id_name,text=str(name).capitalize(),font=("arial",16),bg="#e5e5e5")
     text_label.place(x=120,y=40)
     range_list = random.randint(1, 100)
     my_canvas.config(width=range_list)
     list1 = [370,371,372,373]
     from_list1 = random.choice(list1)
     my_canvas.config(width=from_list1)
   except:
    pass
#=============================================chat list assigner function=====================================   

#=============================================add new chat function===========================================   
  def add_client():
   global user_name_ent
   name = new_chat.get()
   if len(new_chat.get()) < 1 :
    pass
   elif new_chat.get() == main_user:
    pass
   else: 
     data = [ADD_CHAT,main_user,name]
     client.send(str(data).encode(FORMAT))

  def insert_val(info):    
    new_chat.delete(0,'end')
    new_chat.insert(0,info)   
#=============================================add new chat function===========================================   

#=============================================add new chat function===========================================   
 
#=============================================SECOND FRONT END================================================   
  global target_client   
  target_client = "none"
  current_data = "none"
  global win 
  global new_frame 
  global option
  win.destroy()
  win1 = CTk()
  win1.geometry("800x800")
  
#================================================image imports================================================   
  image1 = Image.open(PATH+'\\Data_Files\\IMG\\1.png')
  new_image1 = image1.resize((200,200))
  base1 = ImageTk.PhotoImage(new_image1)


  base2 = PhotoImage(file=PATH+'\\Data_Files\\IMG\\8.png')
  base6 = PhotoImage(file=PATH+'\\Data_Files\\IMG\\9.png')  
   
  image3 = Image.open(PATH+'\\Data_Files\\IMG\\4.png')
  new_image1 = image3.resize((60,60))
  base3 = ImageTk.PhotoImage(new_image1)
  
  image5 = Image.open(f"{PATH}\\Data_Files\\Temp\\profile_img.png")
  new_image1 = image5.resize((200,200))
  base5 = ImageTk.PhotoImage(new_image1)
#================================================image imports================================================   

  
#=================================================left panel==================================================   
  set_appearance_mode("Light") 
  set_default_color_theme("green") 
  win1.grid_columnconfigure(1, weight=1)
  win1.grid_rowconfigure(0, weight=1)
  frame_left = CTkFrame(master=win1,width=310,corner_radius=0)
  frame_left.grid(row=0, column=0, sticky="nswe")
  profile_picture = CTkLabel(master=frame_left,image=base5,
             text="")
  profile_picture.pack(pady=5)
  cover = CTkFrame(master=frame_left,)
  cover.pack(pady=5)
  option = ["dfdsf","werwr"]
  variable = StringVar(win)
  variable.set(option[0])
  select = OptionMenu(cover, variable, *option,command=insert_val)
  select.config(width=32,border=0,bg="#d1d1d1",borderwidth=0,highlightcolor="#d1d1d1",
                                                                 highlightthickness=0,)
  select.place(x=48,y=23)
  new_chat = CTkEntry(master=cover,width=240)
  new_chat.grid(row=0,column=1,pady=20,padx=15)
  button_2 = CTkButton(master=cover,text="Add Chat",command=add_client)
  button_2.grid(row=0,column=2,pady=20,padx=5)
  notification_cover = CTkFrame(master=frame_left,)
  notification_cover.pack(pady=5)
  spacing = CTkLabel(master=notification_cover,text="Notifications",width=400,height=1)
  spacing.pack()
  notification = Label(notification_cover,image=base6,bg="#d1d1d1",font=("arial",13),
                                                      compound=LEFT,border=0,text="")
  notification.pack(side=LEFT,pady=10,padx=10)
  s = Style()
  s.theme_use('alt')
  s.configure("TScrollbar",troughcolor="#dedede")
  main_frame = CTkFrame(master=frame_left,width=80,corner_radius=30)
  main_frame.pack(padx=5,side=LEFT,fill=Y)
  my_canvas = Canvas(main_frame,borderwidth=0,width=371,bg="#f0f0f0")
  my_canvas.pack(side=LEFT, fill=Y, expand=1)
  my_scrollbar = ttk.Scrollbar(main_frame,command=my_canvas.yview)
  my_scrollbar.pack(side=RIGHT,fill=Y)
  my_canvas.configure(yscrollcommand=my_scrollbar.set)
  my_canvas.bind('<Configure>', lambda e: my_canvas.configure
                   (scrollregion = my_canvas.bbox("all")))
  second_frame = Frame(my_canvas,bg="#f0f0f0")
  my_canvas.create_window((0,0), window=second_frame, anchor="nw")
#=================================================left panel==================================================   


#=================================================right panel=================================================   
  frame_right = CTkFrame(master=win1)
  frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
  frame_right.grid_columnconfigure(0, weight=1)
  frame_right.grid_rowconfigure(2, weight=1) 
  frame_message = CTkFrame(master=frame_right)
  frame_message.pack(padx=10,pady=10,fill=X,)
  frame_message.grid_columnconfigure(0, weight=1)
  frame_message.grid_rowconfigure(2, weight=1)
  message_input = Text(frame_message,height=1,font=("arial",10),state=DISABLED,border=0,bg="#dbdbdb")
  message_input.grid(row=0,column=0,sticky="snew",padx=5,pady=10)
  send_button = CTkButton(master=frame_message,text="Send",command=send_message,state=DISABLED)
  send_button.grid(row=0,column=1,sticky="new",padx=5,pady=10)
  send_img = CTkButton(master=frame_message,text="",image=base3,command=send_image)
  send_img.grid(row=1,column=0,padx=5,pady=10,sticky="w")
  m_frame = CTkFrame(master=frame_right,corner_radius=30,height=900000000)
  m_frame.pack(padx=5,pady=5,fill=BOTH,expand=1)
  canvas = Canvas(m_frame,borderwidth=0,height=900000000,bg="#f0f0f0")
  canvas.pack(side=LEFT, fill=X, expand=1)
  scrollbar = ttk.Scrollbar(m_frame,command=canvas.yview)
  scrollbar.pack(side=RIGHT,fill=Y)
  canvas.configure(yscrollcommand=scrollbar.set)
  canvas.bind('<Configure>', lambda e: canvas.configure
                   (scrollregion = canvas.bbox("all")))
  new_frame = Frame(canvas,bg="#f0f0f0")
  canvas.create_window((0,0), window=new_frame,anchor="nw")
  test = CTkLabel(master=new_frame,text="Chats",width=new_size)
  test.pack()
  new_frame.config(height=9000000)
#=================================================right panel=================================================   

  i = threading.Thread(target=import_chat,daemon=True)
  i.start()
  win1.mainloop()
#=============================================SECOND FRONT END================================================   

#=================================================BACK END====================================================   

#==============================================login function=================================================   
def log_in():
    global main_user
    main_user = user_name_ent.get()
    password_entry = user_password.get()
    if len(main_user) < 1:
      pass
    elif len(password_entry) < 1:
      pass
    else:  
      info = [LOGIN,user_name_ent.get(),user_password.get()]
      client.send(str(info).encode(FORMAT))     
      comfirmation = client.recv(1024).decode(FORMAT)
      print(comfirmation)
      if comfirmation == YA:
       filename = (f"{PATH}\\Data_Files\\Temp\\profile_img.png")
       new_file = open (filename, "wb")
       chat_size = client.recv(1024).decode(FORMAT)
       print(chat_size)
       Data = client.recv(int(chat_size))
       new_file.write(Data) 
       chat_main()
      else:
       statuse = Label(master=win,bg="#f0f0f0",text="Log In failed!")
       statuse.place(x=260,y=570)  
#==============================================login function=================================================   

#=============================================signup function=================================================   
def create_account():
    def set_image():
       file_img = filedialog.askopenfilename()
       im = Image.open(file_img)
       bigsize = (im.size[0]*3, im.size[1]*3)
       mask = Image.new("L", bigsize, 0)
       draw = ImageDraw.Draw(mask)
       draw.ellipse((0,0) + bigsize, fill=255)
       mask= mask.resize(im.size, Image.ANTIALIAS)
       im.putalpha(mask)
       im.save(f'{PATH}\\Data_Files\\Temp\\profile###1.png')
       img5 = Image.open(f'{PATH}\\Data_Files\\Temp\\profile###1.png')
       new_image5 = img5.resize((100,100))
       photo_img5 = ImageTk.PhotoImage(new_image5)
       photo.config(image=photo_img5) 
       mainloop()  
    def sign_up():   
     if len(f_user_name_ent.get()) < 2:
         statuse_info.config(text="Invalid First name")    
     elif len(l_user_name_ent.get()) < 2:
         statuse_info.config(text="Invalid Last name")
     elif len(location_ent.get()) < 2:
         statuse_info.config(text="Invalid Location")
     elif  len(user_name_ent.get()) < 2:
          statuse_info.config(text="Invalid Username")  
     elif  len(password_ent.get()) < 2:
         statuse_info.config(text="Invalid password")
     elif password_ent.get() == user_name_ent.get() :
          statuse_info.config(text="Use a another password") 
     else:
       data = [SIGN_IN,f_user_name_ent.get(),l_user_name_ent.get(),location_ent.get(),
                                                user_name_ent.get(),password_ent.get()]
       time.sleep(1)
       client.send(str(data).encode(FORMAT))
       file_size = os.path.getsize(f"{PATH}\\Data_Files\\Temp\\profile###1.png")
       file2 = open(f"{PATH}\\Data_Files\\Temp\\profile###1.png",'rb')
       data2 = file2.read()
       file2.close()
       client.send(str(file_size).encode(FORMAT))
       time.sleep(1)
       client.sendall(data2)
       
       user_state = client.recv(1024).decode(FORMAT)
       print(user_state)
       if user_state == AVAILIABLE:
          main_label1.destroy()
       else:
            statuse_info.config(text="Username Exists") 
#=============================================signup function================================================= 

#=================================================BACK END====================================================   

       
#=================================================FRONT END=================================================== 
    main_label1 = Label(win,image=background_img2)
    main_label1.place(x=-5,y=-5)
    photo = Button(main_label1,border=0,bg="#efefef",activebackground="#efefef",image=photo_img4,
                                                                               command=set_image)
    photo.place(x=260,y=90)
    f_user_name_ent = Entry(main_label1,width=14,font=("bell mt",17),bg="#efefef",border=0,fg="#212222")
    f_user_name_ent.place(x=250,y=245)
    l_user_name_ent = Entry(main_label1,width=14,font=("bell mt",17),bg="#efefef",border=0,fg="#212222")
    l_user_name_ent.place(x=250,y=287)
    location_ent = Entry(main_label1,width=11,font=("helvetica",17),bg="#efefef",border=0,fg="#212222")
    location_ent.place(x=184,y=335)
    user_name_ent = Entry(main_label1,width=20,font=("helvetica",16),bg="#efefef",border=0,fg="#212222")
    user_name_ent.place(x=185,y=396)
    password_ent = Entry(main_label1,width=20,font=("helvetica",16),bg="#efefef",border=0,fg="#212222")
    password_ent.place(x=185,y=460)
    login_button = CTkButton(main_label1,text="Sign Up",command=sign_up)
    login_button.place(x=246,y=510)
    statuse_info = Label(main_label1,bg="#efefef")
    statuse_info.place(x=250,y=570)    

#==============================================view password================================================== 
def capital_pasword():
    if(x.get()==1):
       user_password.config(show="")
    else:
      user_password.config(show="*") 
#==============================================view password================================================== 

set_appearance_mode("Light") 
set_default_color_theme("dark-blue") 
win = CTk()
win.title("Sign Up")
win.geometry("600x600")
win.resizable(False,False)
PATH = os.path.dirname(os.path.realpath(__file__))
wid = win.winfo_screenwidth()
new_size = int(wid - 470)

#===============================================image import================================================== 
img_1 = PhotoImage(file=PATH+'\\Data_Files\\IMG\\6.png')
img = Image.open(PATH+'\\Data_Files\\IMG\\3.jpg')
new_image1 = img.resize((610,605))
background_img = ImageTk.PhotoImage(new_image1)
img2 = Image.open(PATH+'\\Data_Files\\IMG\\7.png')
new_image2 = img2.resize((610,605))
background_img2 = ImageTk.PhotoImage(new_image2)
img4 = Image.open(PATH+'\\Data_Files\\IMG\\1.png')
new_image4 = img4.resize((70,70))
photo_img4 = ImageTk.PhotoImage(new_image4)
background_Label = Label(win,image=background_img)
background_Label.place(x=-5,y=-5)
image2 = Image.open(PATH+'\\Data_Files\\IMG\\2.png')
new_image1 = image2.resize((150,150))
base2 = ImageTk.PhotoImage(new_image1)
#===============================================image import================================================== 

user_name_ent = Entry(win,width=20,font=("bell mt",17),bg="#efefef",border=0,fg="#212222")
user_name_ent.place(x=182,y=245)
x = IntVar() 
ck_pass = Checkbutton(win,bg="#efefef",image=img_1,activebackground="#efefef",compound=TOP,
                 activeforeground="#172433",border=0,variable=x,command=capital_pasword)
ck_pass.place(x=382,y=320)
user_password = Entry(win,width=18,font=("bell mt",17),show="*",bg="#efefef",border=0)
user_password.place(x=182,y=312)
login_button = CTkButton(win,width=265,text="Log In",command=log_in,bg_color="#f0f0f0")
login_button.place(x=170,y=370)
sign_in_button = CTkButton(win,width=200,text="Sign Up",command=create_account,bg_color="#f0f0f0")
sign_in_button.place(x=203,y=420)
win.mainloop()
#=================================================FRONT END=================================================== 
