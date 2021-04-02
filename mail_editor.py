"""
Ce programme a été entièrement développé par Kuntz Loïc dans le cadre d'un projet de fin de semestre.
Date de rendu de ce projet : 20/01/2021
"""
from tkinter import *
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import eel
import threading
import tkinter.font as tkFont
from tkinter import font
import tkinter.ttk as ttk
import tkinter.messagebox

isEELInit = False
currentOutput = ""
outCount = 0

def lcnwb():
    global isEELInit
    if isEELInit == False: #Initialise le navigateur web
        isEELInit = True
        print("#First Launch!")
        eel.init("web")
        eel.start('email.html', block=False)
    else: #Lance à nouveau une fenêtre de navigateur
        eel.show("email.html")
    print("#Update")
    while True:
        eel.sleep(10)

def appercu():
    zm = zonemail.get("1.0", END)
    htmlcode = '<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<title>Visualisation de ' \
               'l\'email</title>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' \
               '</head>\n<body>\n'+zm+'\n</body>\n</html>'

    if os.path.exists("web"):
        pass
    else:
        os.mkdir("web")
    f = open("web/email.html", "w", encoding="UTF-8")
    f.write(htmlcode)
    f.close()

    x = threading.Thread(target=lcnwb)
    x.start()

def mainwind():
    global fen, senderemailent, zonemail, receiveremailent, senderemailpassword, objectent
    fen = Tk()
    fen.title("Editeur de mails")
    width = 580
    height = 431

    idFrameBGColor = '#FAA207'
    idFrameMailColor = '#F29C07'
    contentFrameMailColor = '#FDD405'

    screenwidth = fen.winfo_screenwidth()
    screenheight = fen.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    fen.geometry(alignstr)
    fen.resizable(width=False, height=False)
    #Fin de la partie création plus centrage de la fenêtre
    #Début de la définition de la zone de login
    globalFrame = Frame(fen, bg="#FAA207", bd=1) #Frame avec tout
    globalInfosFrame = Frame(globalFrame, bg=idFrameBGColor, bd=1) #Partie contenant toutes les entry concernant l'envoi
    globalIdFrame = Frame(globalInfosFrame, bg=idFrameBGColor, bd=1)
    idFrame = Frame(globalIdFrame, bg=idFrameBGColor, bd=1) #Partie id sender
    previeewAndSendMailFrame = Frame(globalFrame, bg="#000000", bd=1)
    zoneMailFrame = Frame(globalInfosFrame, bg=idFrameMailColor, bd=1) #Partie infos mail to send(email, obj)
    infoMailContentFrame = Frame(zoneMailFrame, bg=idFrameMailColor, bd=1)
    codeAndButtonsMailFrame = Frame(globalFrame, bg="#E29206", bd=1)
    codeMailFrame = Frame(codeAndButtonsMailFrame, bg=contentFrameMailColor, bd=1)
    buttonMailFrame = Frame(codeAndButtonsMailFrame, bg="#000000", bd=1)

    ft = tkFont.Font(family='Times', size=13)
    ExpIDLBL = Label(globalIdFrame, bg=idFrameBGColor, text="Identifiants de l'expéditeur", justify="left", fg="#333333", font=ft)

    ft = tkFont.Font(family='Times', size=12)
    SenderIDLBL = Label(idFrame, bg=idFrameBGColor, text="E-mail :", justify="left", fg="#333333", font=ft)

    file = open("identifiants.txt", "r")

    senderemailent = Entry(idFrame, highlightthickness=1)
    senderemailent.config(highlightbackground="#000000", highlightcolor="#1E8DB2", relief="flat", text="Email", justify="left", fg="#333333", font=ft, borderwidth="1px")

    #Préremplis le champ email de l'expéditeur
    senderemailent.insert(0, file.readlines()[0])
    file.close()

    SenderPWLBL = Label(idFrame, bg=idFrameBGColor, text="Mot de passe :", justify="left", fg="#333333", font=ft)

    senderemailpassword = Entry(idFrame, highlightthickness=1, relief="flat", text="Password", justify="left", fg="#333333", font=ft, borderwidth="1px", highlightcolor="#1E8DB2",highlightbackground="#000000", show="•")

    ExpIDLBL.pack()
    SenderIDLBL.grid(row=1, column=0, sticky=W)
    senderemailent.grid(row=1, column=1, sticky=W)
    SenderPWLBL.grid(row=2, column=0, sticky=W)
    senderemailpassword.grid(row=2, column=1, sticky=W)

    idFrame.pack()
    # Fin de la définition de la zone de login
    # Début de la définition de la zone d'infos du mail

    ft = tkFont.Font(family='Times', size=13)
    TitleMailInfosLBL = Label(zoneMailFrame, bg=idFrameMailColor, font=ft, fg="#333333", justify="left", text="Informations sur le mail")

    ft = tkFont.Font(family='Times', size=12)
    ReceiverEmailLBL = Label(infoMailContentFrame, bg=idFrameMailColor, text = "E-mail du destinataire :", font=ft, fg="#333333", justify="left")

    receiveremailent = Entry(infoMailContentFrame, highlightthickness=1, relief="flat", text="Email Destinataire", justify="left", fg="#333333", font=ft, borderwidth="1px", highlightbackground="#000000", highlightcolor="#1E8DB2")

    ObjectLBL = Label(infoMailContentFrame, bg=idFrameMailColor, text="Objet :", font=ft, justify="left", fg="#333333")

    objectent = Entry(infoMailContentFrame, highlightthickness=1, relief="flat", text="Objet du mail", justify="left", fg="#333333", font=ft, borderwidth="1px", highlightbackground="#000000", highlightcolor="#1E8DB2")

    ReceiverEmailLBL.grid(row=0, column=0, sticky=W)
    receiveremailent.grid(row=0, column=1, sticky=E)
    ObjectLBL.grid(row=1, column=0, sticky=W)
    objectent.grid(row=1, column=1, sticky=E)

    TitleMailInfosLBL.pack()
    infoMailContentFrame.pack()

    globalIdFrame.grid(row=0, column=0, sticky=W)
    zoneMailFrame.grid(row=0, column=1, sticky=E)
    globalInfosFrame.pack()

    ZoneMailLBL = Label(codeMailFrame, bg=contentFrameMailColor, text="Code du mail :", justify="left", font=ft, fg="#333333")

    zonemail = Text(codeMailFrame, width=54, height=18, relief="flat")
    ZoneMailLBL.pack()
    zonemail.pack()

    style = ttk.Style()
    style.configure('TButton', font=('calibri', 10))

    newTitleButton = ttk.Button(buttonMailFrame, style = 'TButton', text="Titre", width=18, command=addTitle)
    newTitleButton.pack()

    newParagraphButton = ttk.Button(buttonMailFrame, style = 'TButton', text="Paragraphe", width=18, command=addParagraph)
    newParagraphButton.pack()

    newParagraphButton = ttk.Button(buttonMailFrame, style = 'TButton', text="Barre de séparation", width=18, command=addSeparator)
    newParagraphButton.pack()

    codeMailFrame.grid(row=0, column=0, sticky=W)
    buttonMailFrame.grid(row=0, column=1, sticky=W)
    codeAndButtonsMailFrame.pack()

    previewButton = ttk.Button(previeewAndSendMailFrame, style = 'TButton', text="Prévisualiser le mail", width=18, command=appercu)
    previewButton.grid(row=0, column=0, sticky=W)

    sendMailButton = ttk.Button(previeewAndSendMailFrame, style = 'TButton', text="Envoyer le mail", width=18, command=sendmailctnt)
    sendMailButton.grid(row=0, column=1, sticky=W)

    previeewAndSendMailFrame.pack()
    globalFrame.pack()

def validParag():
    output = getBalises()
    ctnt = "<p>"+output+"</p>"
    zonemail.insert("end", ctnt)

def hasRender(type, start, end):
    return type in get_tags(str(start) + "." + str(end), str(start) + "." + str(end))

def getBalises(currentLine=1, parag = ""):
    lastline = int(paragDesc.index('end').split('.')[0])

    renderToTest=["bold", "italic", "underline"]
    renderBalises=["b", "i", "u"]

    index = str(currentLine)+".end"
    charPerLines = int(paragDesc.index(index)[2:]) #Nombre de char per lines
    for j in range(charPerLines):
        charact = paragDesc.get(str(currentLine)+"."+str(j))
        if j == 0: #Cas du premier caractère de la ligne
            for k in range(len(renderToTest)):
                if hasRender(renderToTest[k], currentLine, j):
                    parag = parag + "<"+renderBalises[k]+">"
        parag = parag + charact

        if j == charPerLines-1 and currentLine != lastline:
            for k in range(len(renderToTest)):
                if hasRender(renderToTest[k], currentLine, j):
                    parag = parag + "</"+renderBalises[k]+">"

        if j+1 < charPerLines:
            for k in range(len(renderToTest)):
                if not hasRender(renderToTest[k], currentLine, j) and hasRender(renderToTest[k], currentLine, j+1):
                    parag = parag + "<"+renderBalises[k]+">"
                elif hasRender(renderToTest[k], currentLine, j) and not hasRender(renderToTest[k], currentLine, j+1):
                    parag = parag + "</" + renderBalises[k] + ">"

    if(currentLine != 0 and currentLine != lastline):
        parag = parag + "<br/>"

    if(currentLine != lastline):
        return getBalises(currentLine+1, parag)

    if(currentLine == lastline):
        return parag

def get_tags(start, end):
    index = start
    tags = []
    while paragDesc.compare(index, "<=", end):
        tags.extend(paragDesc.tag_names(index))
        index = paragDesc.index(f"{index}+1c")
    return set(tags)

def boldtxt(first="sel.first", last="sel.last"):
    bold_font = font.Font(paragDesc, paragDesc.cget("font"))
    bold_font.configure(weight="bold")
    paragDesc.tag_configure("bold", font=bold_font)
    current_tags = paragDesc.tag_names(first)
    if "bold" in current_tags:
        paragDesc.tag_remove("bold", first, last)
    else:
        paragDesc.tag_add("bold", first, last)

def italicstxt(first="sel.first", last="sel.last"):
    italics_font = font.Font(paragDesc, paragDesc.cget("font"))
    italics_font.configure(slant="italic")

    paragDesc.tag_configure("italic", font=italics_font)
    current_tags = paragDesc.tag_names(first)
    if "italic" in current_tags:
        paragDesc.tag_remove("italic", first, last)
    else:
        paragDesc.tag_add("italic", first, last)

def underlinetxt(first="sel.first", last="sel.last"):
    underline_font = font.Font(paragDesc, paragDesc.cget("font"))
    underline_font.configure(underline=True)

    paragDesc.tag_configure("underline", font=underline_font)
    current_tags = paragDesc.tag_names(first)
    if "underline" in current_tags:
        paragDesc.tag_remove("underline", first, last)
    else:
        paragDesc.tag_add("underline", first, last)

def validTitleCmd():
    toPaste = titleEntry.get()
    print(comboTitle.get())
    toPaste = "<"+comboTitle.get()+">"+toPaste+"</"+comboTitle.get()+">"
    zonemail.insert("end", toPaste)

def addTitle():
    global titleEntry
    global comboTitle
    aTitle = Tk()
    aTitle.title("Générer un titre")
    aTitle.geometry("290x114")

    ft = tkFont.Font(family='Times')
    titleFen = Label(aTitle, text="Veuillez entrer le contenu du titre", font=ft, fg="#333333")

    titleEntry = Entry(aTitle, highlightthickness=1, relief="flat", text="TitleTextEntry", justify="left"\
    , fg="#333333", font=ft, borderwidth = "1px", highlightbackground="#000000", highlightcolor="#1E8DB2")

    comboTitle = ttk.Combobox(aTitle,values=["h1","h2","h3","h4","h5","h6"], font=ft)
    comboTitle.current(0)

    style = ttk.Style()
    style.configure('TButton', font=('calibri', 10))

    validTitle = ttk.Button(aTitle, style = 'TButton', width=18, text="Valider", command=validTitleCmd)
    titleFen.pack()
    titleEntry.pack()
    comboTitle.pack()
    validTitle.pack()

def addSeparator():
    zonemail.insert("end", "<hr/>")

def addParagraph():
    global paragDesc
    aParag = Tk()
    buttonsAParagFrame = Frame(aParag, bg="#000000", bd=1)
    aParag.geometry("300x210")
    aParag.title("Générer un paragraphe")
    lblDesc = Label(aParag, text="Veuillez entrer le contenu du paragraphe")
    paragDesc = Text(aParag,width=35, height=8)
    validDescBtn = ttk.Button(aParag, style='TButton', text="Valider", command=validParag)

    bold_button = ttk.Button(buttonsAParagFrame, style='TButton', text="Gras", command=boldtxt)
    bold_button.grid(row=0, column=0)
    italic_button = ttk.Button(buttonsAParagFrame, style='TButton', text="Italique", command=italicstxt)
    italic_button.grid(row=0, column=1)
    underline_button = ttk.Button(buttonsAParagFrame, style='TButton', text="Souligné", command=underlinetxt)
    underline_button.grid(row=0, column=2)

    lblDesc.pack()
    paragDesc.pack()
    buttonsAParagFrame.pack()
    validDescBtn.pack()

def sendmailctnt():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        sender = senderemailent.get()
        receiver = receiveremailent.get()
        motdepasse = senderemailpassword.get()
        s.starttls()
        s.login(sender, motdepasse)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = objectent.get()
        msg['From'] = sender
        msg['To'] = receiver
        zm = zonemail.get("1.0", END)
        zm = zm.replace("\n", "<br/>")
        html = """\
           <html>
             <head></head>
             <body>
             """ + zm + """
             </body>
           </html>
           """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        idFile = open("identifiants.txt", "w")
        idFile.write(senderemailent.get())
        print(senderemailent.get())
        tkinter.messagebox.showinfo('Information', 'E-mail expédié avec succès!')
        print("Message envoyé!")
    except Exception as e:
        print("Erreur obtenue lors de l'envoi : ",e)
        tkinter.messagebox.showerror('Erreur', "Erreur obtenue lors de l'envoi : "+str(e))

def test(sendemail=False, email="exemple@exemple.fr"):
    senderemailpassword.insert(0, "Isfa_2021_tes")
    objectent.insert(0, "Lorem Ipsum")
    addTitle()
    titleEntry.insert(0, "Lorem Ipsum")
    addParagraph()
    paragDesc.insert("end", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In fringilla ipsum ut lectus auctor, eu euismod tortor suscipit")
    validTitleCmd()

    addSeparator()

    boldtxt("1.0", "1.26")
    italicstxt("1.28", "1.57")
    underlinetxt("1.57", "1.92")
    validParag()

    appercu()

    if(sendemail):
        receiveremailent.insert(0, email)
        sendmailctnt()

if __name__ == '__main__':
    mainwind()
    #test()
  #  test(True, "kuntz.loic57@gmail.com")
    fen.mainloop()