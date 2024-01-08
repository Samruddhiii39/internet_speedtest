from tkinter import *
import speedtest

def speeck():
    speed = speedtest.Speedtest()
    speed.get_servers()
    downl = str(speed.download()/((10**6),3))+"Mbps"
    uplo = str(speed.upload()/((10**6),3))+"Mbps"
    label_down.config(text=downl)
    label_up.config(text=uplo)

speed = Tk()
speed.title("Internet Speed Tester")
speed.geometry("500x500")
speed.config(bg="BLACK")

label = Label(speed,text="Internet Speed Test",font=("Time New Roman",30),fg="White",bg="Black")
label.place(x=80,y=50,height=40,width=350)

label = Label(speed,text="Downloading Speed",font=("Time New Roman",25),fg="White",bg="Black")
label.place(x=75,y=140,height=40,width=350)

label_down = Label(speed,text="00",font=("Time New Roman",25),fg="White",bg="Black")
label_down.place(x=75,y=190,height=40,width=350)

label = Label(speed,text="Uploading Speed",font=("Time New Roman",25),fg="White",bg="Black")
label.place(x=75,y=270,height=40,width=350)

label_up = Label(speed,text="00",font=("Time New Roman",25),fg="White",bg="Black")
label_up.place(x=75,y=320,height=40,width=350)

button = Button(speed,text="Check Speed",font=("times new roman",20),relief=RAISED,bg="yellow",command=speeck)
button.place(x=75,y=400,height=40,width=350)


speed.mainloop()
