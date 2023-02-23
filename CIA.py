from tkinter import *
import tkinter.scrolledtext as st
import wikipedia
from PIL import Image, ImageTk
from tkinter import filedialog
wikipedia.set_lang('th')

######. ฐานข้อมูล  ##########
import sqlite3

conn = sqlite3.connect('user.sqlite3')
c = conn.cursor()

#create table
c.execute("""CREATE TABLE IF NOT EXISTS userinfo(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        first_name TEXT,
        last_name TEXT,
        tel TEXT,
        address TEXT,
        points INT,
        skill TEXT,
        experience TEXT,
        photo TEXT
    )""")



def insert_userinfo(datadict):
    ID=None
    code = datadict['code']
    first_name = datadict['first_name']
    last_name = datadict['last_name']
    tel = datadict['tel']
    address = datadict['address']
    points = datadict['points']
    skill = datadict['skill']
    experience = datadict['experience']
    photo = datadict['photo']
    with conn:
        command = 'INSERT INTO userinfo VALUES (?,?,?,?,?,?,?,?,?,?)'
        c.execute(command,(ID,code,first_name,last_name,tel,address,points,skill,experience,photo))
    conn.commit() #save
    print('success')


def view_userinfo():
    with conn:
        command = "SELECT * FROM userinfo"
        c.execute(command)
        result = c.fetchall()
    return result

def search_userinfo(field,data,fetchall=True):
    with conn:
        command = "SELECT * FROM userinfo WHERE code=(?)"
        command = 'SELECT * FROM userinfo WHERE {}=(?)'.format(field)
        c.execute(command,([data]))
        if fetchall:
            result = c.fetchall()
        else:
            result = c.fetchone()
    return result


def update_userinfo(ID,field,data):
    with conn:
        command = 'UPDATE userinfo SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,([data,ID]))
    conn.commit()
    print('success')


def delete_userinfo(ID):
    with conn:
        command = 'DELETE FROM userinfo WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('deleted')


data = {'code':'US-1002',
        'first_name':'Somchai',
        'last_name':'Engineer',
        'tel':'0801234567',
        'address':'99 Siam Bangkok',
        'points':0,
        'skill':'1. Python\n2. IoT\n3. 3D Model',
        'experience':'-Submarine\n-Jet Engine',
        'photo':'user1.png'}
######### สิ้นสุดฐานข้อมูล ###############
# color
bg = '#1c1c1c'
fg = 'white'
GUI = Tk()
GUI.geometry('500x400+500+50')
GUI.configure(background='#1c1c1c')
GUI.state('zoomed')
WW = GUI.winfo_screenwidth()
WH = GUI.winfo_screenheight()
canvas = Canvas(GUI, width=WW, height=WH, background=bg)
canvas.configure(bd=0, relief='ridge', highlightthickness=0)
canvas.place(x=0, y=0)


# สร้างกรอบ เส้นสีเทา
def FrameRect(x, y, width=200, height=200, fill=False):
    if fill:
        frame1 = canvas.create_rectangle(0, 0, width, height, outline=fg, width=2, fill=fg)
    else:
        frame1 = canvas.create_rectangle(0, 0, width, height, outline=fg, width=2)
    canvas.move(frame1, x, y)  # เอาตำแหน่งสี่เหลี่ยมไปไว้ตรงไหน


##### ตัวอักษร ########

f1 = ('Tahoma', 30)
f2 = (None, 18)
f3 = ('Angsana New', 18)
##### โซนด้านบน #######

L1 = Label(GUI, text='FIRE MAN USER DATABASE', bg=bg, fg=fg, font=f1)
L1.place(x=50, y=30)


def FixedText(x, y, text='text=fixed text', font=f2, color=fg):
    L1 = Label(GUI, text=text, bg=bg, fg=color, font=font)
    L1.place(x=x, y=y)


#########  ช่อง ค้นหา Entry ###############
L1 = Label(GUI, text='พิมพ์คำที่ต้องการค้นหา', bg=bg, fg=fg, font=f3)
L1.place(x=600, y=10)


def FixedText2(x, y, text='text=fixed text', font=f2, color=fg):
    L1 = Label(GUI, text=text, bg=bg, fg=color, font=font)
    L1.place(x=x, y=y)


v_search = StringVar()
E1 = Entry(GUI, textvariable=v_search, font=('tahoma', 18), width=34, bg=bg, fg=fg)
E1.configure(insertbackground=fg)
E1.configure(highlightthickness=2, highlightbackground=fg, highlightcolor=fg)
E1.place(x=600, y=50)

def Search(events):
    keyword = v_search.get()
    result = search_userinfo ('code',keyword)[0]

    if len(result) != 0:
        r = result[:7]
        v_name.set('{} {}'.format(r[2].upper(),r[3].upper())) 
        userinfotext = 'CODE: {}\nTEL: {}\nADDRESS: {}'.format(r[1],r[4],r[5])
        view_userinfo.set(userinfotext)

        v_skill.set('')
        v_skill.set(result[7])
        skill.delete(1.0, END) 
        skill.insert(INSERT, v_skill.get())

        v_experience.set('') 
        v_experience.set(result[8])
        experience.delete(1.0, END)
        experience.insert(INSERT, v_experience.get())

    else:
        v_name.set('-----No result-----')
        v_userinfo.set('-----No result-----')
        v_skill.set('')
        v_skill.set('---No result---')
        skill.delete(1.0, END)
        skill.insert(INSERT, v_skill.get())

        v_experience.set('')
        v_experience.set('---No result---')
        experience.delete(1.0, END)
        experience.insert(INSERT, v_experience.get())


# #######. ค้นหา จาก wikipedia ##########
# def Search(event):
#     keyword = v_search.get()
#     try:
#         text = wikipedia.summary(keyword)
#         v_experience.set('')
#         v_experience.set(text)
#         experience.delete(1.0, END)
#         experience.insert(INSERT, v_experience.get())
#     except:
#         text = wikipedia.summary('')
#         v_experience.set('--No result----')
#         experience.delete(1.0, END)
#         experience.insert(INSERT, v_experience.get())

E1.bind('<Return>', Search)

####### โซนด้านซ้าย #######
# main #

FrameRect(50, 100, 900, 30)  # Header bar
FixedText(400, 102, 'USER INFO')

FrameRect(50, 100, 900, 800)  # ห่างจากบน ซ้าย และมุม

# in-right
FrameRect(500, 150, 420, 200)
# เปลี่ยนขนาดภาพ
photofile = Image.open("./photo/user1.png")
print('SIZE:', photofile.size)
img_w, img_h = photofile.size
ratio = img_h / img_w
resize_w = 200  # ขนาดเราที่ต้องการ
new_h = int(ratio * resize_w)
photofile = photofile.resize((resize_w, new_h))
photo = ImageTk.PhotoImage(photofile)
userphoto = Label(GUI, image=photo, bd=0, relief='ridge', highlightthickness=0)
userphoto.place(x=60, y=150)

# text = wikipedia.summary('albert einstein')
# v_experience.set(text)


# experience = Label(GUI, textvariable=v_experience, fg=fg, bg=bg, font=f2)
# experience.place(x=70, y=600)
# experience = st.ScrolledText(F1, width=85, height=12, bg=bg, fg=fg, font=('tahoma', 18)) #มีแถบสกรอ บาร์
# experience.pack()
######### กรอบ หรือ Fram จะใช้ F ตัวใหญ่  #######

F1 = Frame(GUI, )
F1.place(x=500, y=400)
F2 = Frame(GUI)
F2.place(x=500, y=600)
### in botton ###
v_skill = StringVar()
v_skill.set('-- skill --')
skill = st.Text(F1, width=40, height=7, bg=bg, fg=fg, font=f3)
skill.pack()
skill.insert(INSERT, v_skill.get())

v_experience = StringVar()
v_experience.set('-- experience --')
experience = st.Text(F2, width=40, height=7, bg=bg, fg=fg, font=f3)
experience.pack()
experience.insert(INSERT, v_experience.get())

### โซนด้านขวา ###

FrameRect(1000, 100, 900, 20)  # Header bar
FrameRect(1000, 100, 900, 800)  # ห่างจากบน ซ้าย และมุม





GUI.mainloop()
