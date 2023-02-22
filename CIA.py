from tkinter import *
import tkinter.scrolledtext as st
import wikipedia

wikipedia.set_lang('th')
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

f1 = ('tahoma', 30)
f2 = (None, 18)
f3 = ('Angsana Upc', 18)
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
def Search(event):
    keyword = v_search.get()
    try:
        text = wikipedia.summary(keyword)
        v_experience.set('')
        v_experience.set(text)
        experience.delete(1.0, END)
        experience.insert(INSERT, v_experience.get())
    except:
        text = wikipedia.summary('')
        v_experience.set('--No result----')
        experience.delete(1.0, END)
        experience.insert(INSERT, v_experience.get())
E1.bind('<Return>', Search)

####### โซนด้านซ้าย #######
# main #

FrameRect(50, 100, 900, 30)  # Header bar
FixedText(400, 102, 'USER INFO')

FrameRect(50, 100, 900, 800)  # ห่างจากบน ซ้าย และมุม

# in-right
FrameRect(500, 150, 420, 200)

photo = PhotoImage(file="./photo/user1.png").subsample(2)
userphoto = Label(GUI, image=photo, bd=0, relief='ridge', highlightthickness=0, width=300, height=400)
userphoto.place(x=80, y=150)

### in botton ###

v_experience = StringVar()
v_experience.set('---- ข้อความจากหน้าเว็บ ----')
# text = wikipedia.summary('albert einstein')
# v_experience.set(text)

######### กรอบ หรือ Fram จะใช้ F ตัวใหญ่  #######

F1 = Frame(GUI, width=900)
F1.place(x=70, y=600)
# experience = Label(GUI, textvariable=v_experience, fg=fg, bg=bg, font=f2)
# experience.place(x=70, y=600)
experience = st.ScrolledText(F1, width=85, height=12, bg=bg, fg=fg, font=('tahoma', 18))
experience.pack()

experience.insert(INSERT, v_experience.get())

### โซนด้านขวา ###

FrameRect(1000, 100, 900, 20)  # Header bar
FrameRect(1000, 100, 900, 800)  # ห่างจากบน ซ้าย และมุม

GUI.mainloop()
