from tkinter import *
from pygame import mixer
mixer.init()

def play(audio):
    mixer.music.load(audio)
    mixer.music.play(-1)

#create a window
root=Tk()
root.title("tkinter course")
root.geometry("600x700")
root.config(bg="#262626")
root.resizable(False,False)

lbl_title = Label(root,text="Please Choose the song",font=('arial',35,'bold'),bg='yellow',fg='red').pack(fill=X,pady=15,padx=10)

btn1=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="ghamand kar",bg="orange",command=lambda:play('ghamand.mpeg')).pack(pady=10,padx=10,)

btn2=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="chandigarh me",bg="orange",command=lambda:play('ghar.mpeg')).pack(pady=10,padx=10,)

btn3=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="hanuman chalisa",bg="orange",command=lambda:play('hanuman.mp3')).pack(pady=10,padx=10,)

btn4=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="achutam",bg="orange",command=lambda:play('achutam.mpeg')).pack(pady=10,padx=10,)

btn5=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="delhi de diya",bg="orange",command=lambda:play('mumbai.mpeg')).pack(pady=10,padx=10,)

btn6=Button(root,padx=16,pady=16,fg="black", font=('Times New Roman', 15 ,'bold'),text="shankara",bg="orange",command=lambda:play('shankara.mpeg')).pack(pady=10,padx=10,)


root.mainloop()