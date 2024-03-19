from tkinter import *
from functools import partial
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
from PIL import ImageTk, Image


# style
bgColor = '#165263'
bgColor2 = '#336877'
bgColor3 = '#8BA9B1'
bgColor4 = '#3E636E'
font = "Bahnschrift"




def validateLogin(usernameEntry, passwordEntry):
    username = 'kevin'
    password = '123'
    if usernameEntry.get() == username and passwordEntry.get() == password:
        messagebox.showinfo(title='State', message = 'Successful login', command=openMainMenu())
    else:
        messagebox.showerror(title='Error!', message='Invalid Login. Try again')


def _quit():
   tkWindow.destroy()

def openMainMenu():
    # Toplevel object which will
    # be treated as a new window
    menu = Toplevel(tkWindow)

    #sets the menu to always be on top (not technically necessary as it's the only window open)
    #menu.attributes("-topmost", True)

    #hides the login window
    tkWindow.withdraw()

    mainMenuWindow(menu)

    # Create Menu Bar

    #menuBar = Menu(menu)
    #menu.config(menu=menuBar)
    # File Menu
    #fileMenu = Menu(menuBar, tearoff=0)
    #fileMenu.add_command(label="View Files", command=filesWindow)
    #fileMenu.add_command(label="Upload", command=uploadWindow)
    #fileMenu.add_separator()
    #fileMenu.add_command(label="Exit", command=_quit)
    #menuBar.add_cascade(label="File", menu=fileMenu)
    # Help Menu
    #helpMenu = Menu(menuBar, tearoff=0)
    #helpMenu.add_command(label="Tutorial", command=helpWindow)
    #menuBar.add_cascade(label="Help", menu=helpMenu)

def mainMenuWindow(menu):
    # sets the title of the
    # Toplevel widget


    menu.title("Main Menu")
    menu.configure(bg=bgColor)
    # sets the geometry of toplevel
    menu.geometry("1920x1080")

    # A Label widget to show in toplevel
    Frame(menu, bg=bgColor).place(relx=0.0, rely=0.0, relwidth=1, relheight=0.15)
    Label(menu, text="MedDocs", bg=bgColor, fg='white', font=(font, 30, "bold")).place(x=960, y=40, anchor="center")
    Frame(menu, bg=bgColor2).place(relx=0.0, rely=0.09, relwidth=1, relheight=0.06)

    Button(menu, text="HOME", command=mainMenuWindow, bg=bgColor2 ,fg='white', borderwidth=0, font=(font, 12, 'bold')).place(x=720,y=110, anchor="n")
    Button(menu, text="UPLOAD DOCUMENTS", command=uploadWindow, bg=bgColor2,fg='white', borderwidth=0, font=(font, 12, 'bold')).place(x=960,y=110,anchor="n")
    Button(menu, text="HELP", command=helpWindow, bg=bgColor2,fg='white',borderwidth=0, font=(font, 12,'bold')).place(x=1152, y=110, anchor="n")

    Button(menu, text="PROFILE", command=profileWindow, bg=bgColor, fg='white', borderwidth=0,font=(font, 12, 'bold')).place(x=1850, y=30, anchor="n")


    Label(menu, text="Welcome to MedDocs", bg=bgColor,fg=bgColor3,font=(font, 40, "bold")).place(x=100, y=400, anchor="nw")
    Label(menu, text="A place to upload, organize, and share your medical documents with medical professionals", bg=bgColor,fg=bgColor3, font=(font, 15)).place(x=100, y=460, anchor="nw")
    Frame(menu, bg=bgColor3).place(relx=0.0, rely=0.7, relwidth=1, relheight=0.4)

    Frame(menu, bg=bgColor4).place(relx=0.1, rely=0.65, relwidth=0.157, relheight=0.3)
    Frame(menu, bg=bgColor4).place(relx=0.3, rely=0.65, relwidth=0.157, relheight=0.3)
    Frame(menu, bg=bgColor4).place(relx=0.5, rely=0.65, relwidth=0.157, relheight=0.3)
    Frame(menu, bg=bgColor4).place(relx=0.7, rely=0.65, relwidth=0.157, relheight=0.3)

    Label(menu, text="UPLOAD", bg='#3E636E',fg=bgColor3,font=(font, 20, "bold")).place(x=280, y=790, anchor="nw")
    Label(menu, text="STORE", bg='#3E636E',fg=bgColor3,font=(font, 20, "bold")).place(x=680, y=790, anchor="nw")
    Label(menu, text="ORGANIZE", bg='#3E636E',fg=bgColor3,font=(font, 20, "bold")).place(x=1040, y=790, anchor="nw")
    Label(menu, text="SHARE", bg='#3E636E',fg=bgColor3,font=(font, 20, "bold")).place(x=1440, y=790, anchor="nw")

#image (doesnt work help)
    #PhotoImage(file=r'greys.jpg')
    #img = PhotoImage(file='greys.jpg')
    #Label(menu,image=img).pack()
    #Label(menu,image=img).pack(side="bottom",fill="both",expand="yes")
    #frame = Frame(win, width=600, height=400)
    #frame.pack()
    #frame.place(anchor='center', relx=0.5, rely=0.5)
    #img = ImageTk.PhotoImage(Image.open("greys.jpg"))

    # Create a Label Widget to display the text or Image
    #label = Label(frame, image=img)
    #label.pack()

#profile window

def profileWindow():
    profile = Toplevel(tkWindow)
    tkWindow.withdraw()

    # sets the title of the
    # Toplevel widget
    profile.title("Profile")

    # sets the geometry of toplevel
    profile.geometry("1920x1080")

    profile.configure(bg=bgColor)

    # top menu
    Frame(profile, bg=bgColor).place(relx=0.0, rely=0.0, relwidth=1, relheight=0.15)
    Label(profile, text="MedDocs", bg=bgColor, fg='white', font=(font, 30, "bold")).place(x=960, y=40, anchor="center")
    Frame(profile, bg=bgColor2).place(relx=0.0, rely=0.09, relwidth=1, relheight=0.06)
    Button(profile, text="HOME", command=mainMenuWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=720, y=110, anchor="n")
    Button(profile, text="UPLOAD DOCUMENTS", command=uploadWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=960, y=110, anchor="n")
    Button(profile, text="HELP", command=helpWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=1152, y=110, anchor="n")
    Button(profile, text="PROFILE", command=profileWindow, bg=bgColor, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=1850, y=30, anchor="n")

    #body
    Frame(profile, bg=bgColor3).place(relx=0.330, rely=0.25, relwidth=0.3, relheight=0.6)
    Label(profile, text="Profile", bg=bgColor3, fg=bgColor, font=(font, 25, "bold")).place(x=935, y=300, anchor="center")

    Label(profile, text="Username: ", bg=bgColor3, fg=bgColor, font=(font, 20, "bold")).place(x=730, y=400,
                                                                                           anchor="center")
    Label(profile, text="kevin                        ", bg='white', fg=bgColor, font=(font, 15)).place(x=900, y=400,
                                                                                              anchor="center")

    Label(profile, text="Email: ", bg=bgColor3, fg=bgColor, font=(font, 20, "bold")).place(x=700, y=450,
                                                                                              anchor="center")
    Label(profile, text="kevin@kevin.com  ", bg='white', fg=bgColor, font=(font, 15)).place(x=900, y=450,
                                                                                                    anchor="center")

    Label(profile, text="Password: ", bg=bgColor3, fg=bgColor, font=(font, 20, "bold")).place(x=730, y=500,
                                                                                           anchor="center")
    Label(profile, text="***********              ", bg='white', fg=bgColor, font=(font, 15)).place(x=900, y=500,
                                                                                                    anchor="center")
    Button(profile, text="LOGOUT", command=_quit, bg=bgColor, fg='white', font=(font, 12, 'bold')).place(
        x=960, y=750, anchor="ne")

def uploadWindow():
    # creates new window
    upload = Toplevel(tkWindow)

    # upload menu always on top
    #upload.attributes("-topmost", True)

    tkWindow.withdraw()

    # sets the title of the
    # Toplevel widget
    upload.title("Upload Menu")

    # sets the geometry of toplevel
    upload.geometry("1920x1080")
    upload.configure(bg=bgColor)

    # top menu
    Frame(upload, bg=bgColor).place(relx=0.0, rely=0.0, relwidth=1, relheight=0.15)
    Label(upload, text="MedDocs", bg=bgColor, fg='white', font=(font, 30, "bold")).place(x=960, y=40, anchor="center")
    Frame(upload, bg=bgColor2).place(relx=0.0, rely=0.09, relwidth=1, relheight=0.06)

    Button(upload, text="HOME", command=mainMenuWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=720, y=110, anchor="n")
    Button(upload, text="UPLOAD DOCUMENTS", command=uploadWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=960, y=110, anchor="n")
    Button(upload, text="HELP", command=helpWindow, bg=bgColor2, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=1152, y=110, anchor="n")
    Button(upload, text="PROFILE", command=profileWindow, bg=bgColor, fg='white', borderwidth=0,
           font=(font, 12, 'bold')).place(x=1890, y=25, anchor="ne")

    Button(upload, text="RETURN", command=upload.withdraw, bg=bgColor2, fg='white', borderwidth=0, font=(font, 12, 'bold')).place(x=30, y=110, anchor="nw")

    #Entry(upload, textvariable=password, show='*', font=(font, 15), bg=bgColor3, borderwidth=0,fg="#000000").place(x=300, y=210, anchor="center")



    Frame(upload, bg=bgColor3).place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.5)

    #label_file_explorer

    Label(upload, text="Documents",bg=bgColor, fg='white', font=(font, 30, "bold", )).place(x=960, y=40, anchor="center")

    Button(upload, text="Upload Files", command=img, bg=bgColor3, fg='white', borderwidth=0, font=(font, 20, 'bold')).place(x=150, y=300, anchor="nw")
    Button(upload, text="View Documents", command=filesWindow, bg=bgColor3, fg='white', borderwidth=0,font=(font, 20, 'bold')).place(x=150,y=500,anchor="nw")






# Single upload. trying to figure out how to separate actions and make it better.

# def browseFiles():
#     filename = filedialog.askopenfilename(initialdir="/",
#                                           title="Select a File",
#                                           filetypes=(("Text files",
#                                                       "*.txt*"),('PNG', "*.png"),("JPEG", "*.jpg"),
#                                                      ("all files",
#                                                       "*.*")))




def filesWindow():
    files = Toplevel(tkWindow)

    #files.attributes("-topmost", True)

    tkWindow.withdraw()
    # sets the title of the
    # Toplevel widget
    files.title("Files Menu")

    # sets the geometry of toplevel
    files.geometry("600x400")

    # A Label widget to show in toplevel
    Label(files,
          text="Here are your uploaded files.").pack()

    Button(files, text='button', command=img).pack()

def img():
    path = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(('PNG', "*.png"),("JPEG", "*.jpg"),
                                                     ("all files",
                                                      "*.*")))

    if path == '':
        return
    else:
        img = Toplevel(tkWindow)
        tkWindow.title('File Upload View')
        im = Image.open(path)
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(img, image=tkimage)
        myvar.image = tkimage
        myvar.pack()

def helpWindow():
    help = Toplevel(tkWindow)
    help.configure(bg=bgColor4)

    help.attributes("-topmost", True)

    help.geometry("800x400+560+300")
    help.title("How to Use MedDocs")

    Label(help, text="First, Welcome to MedDocs! We hope that this program will be able to help you get more \n"
                          "organized and keep your 'docs' in a row! ", font=(font,12)).place(x=100,y=40,anchor="w")
    Label(help, text="How to Upload a File:", font=(font,15,"bold","italic")).place(x=400,y=95,anchor="center")
    Label(help, text="First, select the upload button. A new window should appear with the options 'browse files' \n"
                          "and 'return'. Click on browse files, and a file explorer will come up, and you can navigate \n"
                          "to the file you'd like to upload. Once you pick your file and hit the upload button on the \n"
                          "bottom right, your file will be uploaded to our server!",
                           font=(font,12)).place(x=100,y=155,anchor="w")
    Label(help, text="How to View Your Files:", font=(font,15,"bold","italic")).place(x=400, y=220,anchor="center")
    Label(help, text="To view your uploaded files, select the 'view documents' button. This button allows you \n"
                     "to view every file you have uploaded to our system.", font=(font,12)).place(x=400,y=260,anchor='center')

# window
tkWindow = Tk()
tkWindow.configure(bg=bgColor)
tkWindow.geometry('600x400+660+340')
tkWindow.title('MedDocs Login')
tkWindow.resizable(False, False)
welcome = Label(tkWindow, text="MedDocs", bg=bgColor, fg='white', font=(font, 30, "bold", "italic")).place(x=300, y=70, anchor="center")

# username label and text entry box
usernameLabel = Label(tkWindow, text="Username", bg=bgColor, fg='white', font=(font, 15)).place(x=130, y=160, anchor="center")
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username,  font=(font, 15), bg=bgColor3, borderwidth=0, fg="#000000").place(x=300, y=160, anchor="center")

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password", bg=bgColor, fg='white', font=(font, 15)).place(x=130, y=210, anchor="center")
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', font=(font, 15), bg=bgColor3, borderwidth=0, fg="#000000").place(x=300, y=210, anchor="center")

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin, borderwidth=0, font=(font, 15), bg=bgColor3).place(x=300, y=300, anchor="center")



tkWindow.mainloop()