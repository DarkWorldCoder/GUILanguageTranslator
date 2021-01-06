from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import myModule
import pyperclip
# from pydub import AudioSegment
from tkinter import ttk
from translate import Translator
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
LANGUAGES = myModule.LANGUAGES
tk = Tk()
engine.setProperty('rate',120)
langCon = ""


lan= ""
## Functions

def Convert():
    translator = Translator(from_lang="ko",to_lang=langCon)
    text2.delete("1.0","end-1c")
    global lan
    text = text1.get("1.0","end-1c")

    lan = translator.translate(text)
    text2.insert(INSERT,lan)
    
def ReadFile():
    try:
        text1.delete("1.0","end")
        file =filedialog.askopenfilename(initialdir="/User/lenovo/Desktop",
                                            title= "Select Text Files",
                                            filetypes=(("Text files","*.txt"),("All files","*.*") ))
        with open(file,"r") as f:
            j = f.read()
            text1.insert(INSERT,j)
    except Exception:
        pass
def SaveFIle():
    global lan
    file =filedialog.asksaveasfilename(initialdir="/User/lenovo/Desktop",
                                            title= "Select Text Files",
                                            filetypes=(("Text files","*.txt"),("All files","*.*") ))
    with open(file,"w") as f:
        f.write(lan)

                
def callback(selection):
    global langCon
    select = selection
    values = list(LANGUAGES.values())
    position = values.index(select)
    
    key = list(LANGUAGES.keys())
    langCon = key[position]
def copy():
    pyperclip.copy(lan)
def Speak():
    engine.say(text1.get("1.0","end-1c"))
    engine.runAndWait()
def ReadSound():
    file =filedialog.askopenfilename(initialdir="/User/lenovo/Desktop",
                                            title= "Select Text Files",
                                            filetype=(("WAV Files","*.WAV"),("WAV Files","*.wav")))
    r = sr.Recognizer()
    
    
    harvard = sr.AudioFile(file)
    
    with harvard as source:
        audio = r.record(source)
    text1.insert(INSERT,r.recognize_google(audio))
    
    
tk.title("Speech Recoginizer")
tk.geometry(("1200x500"))

varList1 = StringVar(tk)
varList1.set("Auto Detect")

values = list(LANGUAGES.values())
varList2 = StringVar(tk)
varList2.set("Languages")

values1 = list(LANGUAGES.values())
    

om = OptionMenu(tk, varList1,"Auto Detect")
om.grid(row=0,column=0)


om = OptionMenu(tk, varList2,*values1,command =callback)
om.grid(row = 0,column=2)
text1 = Text(tk,font=("Courier",20),width=25,height=10)
text1.grid(row = 1,column=0,padx = 10)
frame = Frame(tk,width=450,height=305,bg="white")
frame2 = Frame(frame,width=500,height=305,bg="white")
frame.grid(row=1,column = 2)
frame2.pack()
frame2.pack_propagate(False)
frame3 = Frame(tk)
frame3.grid(row=1,column=1)
w = Label(frame2, text ='Translation',font=("Courier",20),bg = "White")  
w.pack() 
text2 = Text(frame2,font=("Courier",20),bg = "White",)
# text2.insert(0,"Translation")
text2.pack()
ButtonFrame = Frame(tk)
ButtonFrame.grid(row =3,column =0,padx = 10,pady = 10)
width = 30
height = 30
img = Image.open(".\\assests\\sound.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)

openFIle = Button(ButtonFrame,text="Read",command = ReadFile)
openFIle.grid(row = 0,column = 0,ipadx = 10,ipady = 6,padx = 10,pady = 10)
button = Button(ButtonFrame,text=">>",image = photoImg,command=Speak)
button.grid(row = 0,column = 1,padx = 10,pady = 10)
img1 = Image.open(".\\assests\\addaudio.png")
img1 = img1.resize((width,height), Image.ANTIALIAS)
photoImg1 =  ImageTk.PhotoImage(img1)

button1= Button(ButtonFrame,text=">>",image = photoImg1,command = ReadSound)
button1.grid(row = 0,column = 2,padx = 20,pady = 10)
ButtonFrame1 = Frame(tk)
ButtonFrame1.grid(row = 3,column=2)
img = Image.open(".\\assests\\copy.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg2 =  ImageTk.PhotoImage(img)
button2 = Button(ButtonFrame1,image = photoImg2,command = copy)
button2.grid(row = 0,column = 2,padx = 20,pady = 10)
# button3 = Button(ButtonFrame1,image=photoImg,command=Speak1)
# button3.grid(row = 0,column = 3,padx = 20,pady = 10)
saveFile = Button(ButtonFrame1,text="Save",command = SaveFIle)
saveFile.grid(row = 0,column = 4,ipadx = 10,ipady = 6,padx = 10,pady = 10)
frame4 = Frame(tk)
frame4.grid(row=3,column=1)
button4 = Button(frame4,text="Convert",bg = "#1f9eff",font=("Courier"),command=Convert)
button4.grid(row = 0,column=0,padx = 30,pady = 10,ipadx = 10,ipady=10)





tk.mainloop()