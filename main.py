#TODO Έχει την δυνατότητα να φορτώσει ήδη υπάρχον αρχείο με λέξεις /done
#TODO Να τερματίζει χωρίς error το πρόγραμμα μόλις τελειώσουν οι λέξεις
#TODO scrollbar stin lista
#TODO επιλογή πολλαπλών στοιχείων για διαγραφή
#TODO δεν αποθηκεύει με ελληνικά ονόματα (UTF-8?)
from tkinter import *
import random
#from datetime import date
#from os.path import exists
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile


lista = []
examList = []   #einai i lista stin opoia antigrafetai to dic gia na pairnei tuxees lekseis kai na rotaei

#se autin ti lista apothikeuontai oi tyxaies epiloges gia na mporei na tis sugkrinei giati se kathe patima toy koumpiou
#allazei i leksi pou rotaei kai den mporei na bgei pote sosti
askList = []

global file
global myLabel

root = Tk()
root.title("Taliana ορθογραφία")
root.geometry("500x500")

e = Entry(root, width=50)
e.pack(pady=20)
word = e.get()

lb = Listbox(root, width=60, height=10)
lb.pack(pady=10)


#--------------Menu bar--------------------------------------|
def browseFile():
    filename = filedialog.askopenfilename(initialdir = "D:\Documents\Python\pythonProject",
                                          title = "Select a file",
                                          filetypes = (("Text files", "*.txt*"),
                                                       ("All files", "*.*")))
    with open(filename, "r") as file:
        for words in file:
             #tempList.append(words.rstrip("\n").split("\t"))
             lb.insert(END, words.rstrip("\n").split(":"))
        file.close()

def saveAs():
    files = [("Text Files", "*.txt")]
    file = asksaveasfile(filetypes = files, defaultextension= ".txt")
    for words in lb.get(0, END):
        file.write(":".join(words) +"\n")


menubar = Menu(root)
root.config(menu=menubar)
#Βγάζει την διακεκομμένη γραμμή
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label="Open", command=browseFile)
file_menu.add_command(label="Save as", command=saveAs)
menubar.add_cascade(label = "File", menu=file_menu, underline=0)

#-------------------------------------------------------------|

def insWord():
    lista = e.get().title().split()
    lb.insert(END, lista)
    for i in range(lb.size()):  #tha kanei auto tin douleia molis patisei o xristis to less begin
        examList.append(lb.get(i))
    e.delete(0, END)

def delWord():
    lb.delete(ANCHOR)

def saveToFile():
    file = open("Test Taliano spelling.txt", "w+")
    for words in lb.get(0, END):
        file.write(":".join(words) +"\n")
    file.close()

def readFile(): #to be deleted
    file = open("Test Taliano spelling.txt", "r")
    for words in file:
        print(words.split(None, 1)[0])    #diavazei tin proti leksi apo to arxeio - idk how it works!
#readBtn = Button(root, text="Read", command = readFile).pack()
    file.close()

#TODO αυτή η συνάρτηση θα λειτουργεί με το κουμπί open από το menu
#TODO θα έχει save as και θα βάζει ο χρήστης το όνομα που θέλει στο αρχείο /done
#
#def fileCheck():
#     currentDate = date.today().strftime("%d-%m-%Y") + ".txt"
#     fileExists = exists(currentDate)
#     if fileExists:
#         file = open(currentDate, "r")
#
#         for words in file:
#             lb.insert(END, words.split(None, 1))
#         file.close()
#     else:
#         with open(currentDate, "w") as file:
#             for words in lb.get(0, END):
#                 file.write(":".join(words) + "\n")
#         file.close()




#TODO να κλείνει το αρχείο όταν δεν χρειάζεται άλλο, αλλά πρέπει να υπάρχει ανοικτό για να κάνει απλό save
def popUpWin():
    examList = []

    #file = open("Test Taliano spelling.txt", "r")

    top = Toplevel(root)
    top.geometry("300x300")
    top.title("Η ώρα της κρίσης")

    #COMMENTED TO BE DELETED!!!!
    #Debugging can be deleted
    # for words in file:
    #     examList.append(list(words.split()))
    #     print("Appended: ", list(words.split()))

    for words in lb.get(0, END):
        examList.append(list(words))

    print("Examlist: ", examList)

    #An den mpei edo bgainei to label kato apo to koumpi
    askWordLabel = Label(top, text="Hello man")
    askWordLabel.pack()

    answerInp = Entry(top, width=30)
    answerInp.pack(pady=20)

    #An den mpei edo bgainei kato apo to koumpi kai den ginetai overwrite (correct/wrong)
    ansLabel = Label(top, text="Hello")
    ansLabel.pack()

    def checkAns():
        #Ρωτάει λέξεις που έχουν ήδη αφαιρεθεί
        sample = random.choice(examList)

        askWordLabel.config(text=sample[0])

        askList.append(sample)

        answer = answerInp.get().title()

        print("sample1 = ", sample[1])
        print("Answer: ", answer)
        print("Length = ", len(examList))
        print("asklist:",askList[len(askList)-2][1])
        print("askList whole: ", askList)

        # if len(examList) <= 0:
        #     Label(top, text="Telos").pack()
        # else:
        #     if askList[len(askList)-2][1] == answer:
        #         ansLabel.config(text="Correct")
        #         examList.pop(examList.index(sample))
        #     else:
        #         ansLabel.config(text="Wrong")

        answerInp.delete(0, END)
        #TODO θέλει πείραγμα γιατί δεν βγάζει τα σωστά στοιχεία από την λίστα
        if askList[len(askList) - 2][1] == answer:
            ansLabel.config(text="Correct")
            popped = examList.pop(examList.index(askList[len(askList)-2]))
            print("Popped: ", popped)
            print("Exam list: ", examList)
        else:
            ansLabel.config(text="Wrong")
        if len(examList) <= 0:
            ansLabel.config(text="The End")

    insBtn = Button(top, text="Submit", command = lambda:[checkAns()]).pack(pady=10)

testBtn = Button(root, text= "Tset", command= saveToFile).pack()
popUpBtn = Button(root, text="Less Go", command= lambda: [popUpWin()]).pack()
#popUpBtn = Button(root, text="Less Go", command= lambda: [saveToFile(),popUpWin()]).pack()
insBtn = Button(root, text="Insert ", command=insWord).pack(pady=20)
delBtn = Button(root, text="Delete", command=delWord).pack(pady=10)

root.mainloop()


