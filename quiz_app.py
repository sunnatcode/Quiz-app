from tkinter import *
import json
from PIL import Image, ImageTk
bioo = {
    "Register": {},
    "Score": {}
}







def register():
    registerr = Tk()
    registerr.geometry("300x300")
    registerr.title("Tkinter widgets ! ")
    registerr.config(bg='#34eb9b')
    registerr.resizable(0, 0)

    def ochir():
        global bioo
        name = entry1.get()
        surname = entry4.get()
        phone_number = entry6.get()
        email = entry8.get()
        bio = {
            'name': name,
            'surname': surname,
            'phone_number': phone_number,
            'email': email
        }

        bioo['Register'] = bio
        print(bioo)


        registerr.destroy()
        first_quiz()
        


    label1 = Label(registerr, text="Registration", bg='#34eb9b', foreground='black', font=('Helvatica', 15, 'bold'))
    label1.pack()

    label2 = Label(registerr, text="First Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label2.pack(padx=4)

    entry1 = Entry(registerr)
    entry1.pack(padx=5)

    label3 = Label(registerr, text="Last Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label3.pack(padx=6)

    entry4 = Entry(registerr)
    entry4.pack(padx=7)

    label5 = Label(registerr, text="Phone Number", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label5.pack(padx=8)

    entry6 = Entry(registerr)
    entry6.pack(padx=9)

    label7 = Label(registerr, text='E-Mail', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label7.pack(padx=10)

    entry8 = Entry(registerr)
    entry8.pack(padx=11)

    btn = Button(registerr,text="Next",font=('Helvatica',15,'normal'), command=ochir)
    btn.pack(pady=10)
    registerr.mainloop()
    

def first_quiz():
    first = Tk()
    first.geometry('600x400')
    first.title('Quiz app')
    first.resizable(width=False, height=False)


    def next1_func():
        global bioo
        a = var.get()
        bioo['Score']["1"] = a
        print(bioo)
        first.destroy()
        second_quiz()


    label_top = Label(first, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    label_top.pack()

    var = StringVar()
    var.set(0)

    quiz1 = Label(first, text='Hamma harfni kattalawtiribyoziladigan funksiya nima?',
    font=('Arial', 15, 'bold'))
    quiz1.place(x=70, y=100)

    radio1 = Radiobutton(first, text='upper()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radio1.place(x=70, y=140)

    radio2 = Radiobutton(first, text='lower()', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radio2.place(x=70, y=180)

    radio3 = Radiobutton(first, text='capitalize()', value="False", variable=var, font=('Arial', 15, 'normal'))
    radio3.place(x=70, y=220)

    radio4 = Radiobutton(first, text='print()', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radio4.place(x=70, y=260)

    next = Button(first, text='Next', bg='blue', fg='white', width=13, height=2, command=next1_func)
    next.place(x=260, y=330)

    first.mainloop()
    first_quiz()


def second_quiz():
    second = Tk()
    second.geometry('600x400')
    second.title('Quiz app')
    second.resizable(width=False, height=False)


    def next2_func():
        global bioo
        a = var.get()
        bioo['Score']["2"] = a
        print(bioo)
        second.destroy()
        third_quiz()


    labell_top = Label(second, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(second, text='Quydagilardan float qiymatdagi sonlarni toping?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(second, text='6876.0', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(second, text='3578', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(second, text='3.14', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(second, text='A va C javoblar togri', value="Tog'ri", variable=var, font=(

'Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(second, text='Next', bg='blue', fg='white', width=13, height=2, command=next2_func)
    nextt.place(x=260, y=330)

    second.mainloop()


def third_quiz():
    third = Tk()
    third.geometry('600x400')
    third.title('Quiz app')
    third.resizable(width=False, height=False)

    def next3_func():
        global bioo
        a = var.get()
        bioo['Score']["3"] = a
        print(bioo)
        third.destroy()
        fourth_quiz()
    

    labell_top = Label(third, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(third, text='else , elif , if shu shartlardan foydalanishimiz uchun. Uning ketma ketligini topib bering?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(third, text='elif , if , else', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(third, text='if , else , elif', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(third, text='else , elif , if', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(third, text='if , elif, else', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(third, text='Next', bg='blue', fg='white', width=13, height=2, command=next3_func)
    nextt.place(x=260, y=330)

    third.mainloop()


def fourth_quiz():
    fourth = Tk()
    fourth.geometry('600x400')
    fourth.title('Quiz app')
    fourth.resizable(width=False, height=False)

    def next4_func():
        global bioo
        a = var.get()
        bioo['Score']["4"] = a
        print(bioo)
        fourth.destroy()
        fiveth_quiz()


    labell_top = Label(fourth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(fourth, text='Listga malumot qoshish?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(fourth, text='remove()', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(fourth, text='[]', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(fourth, text='append()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(fourth, text='2 va 3 chi tori', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(fourth, text='Next', bg='blue', fg='white', width=13, height=2, command=next4_func)
    nextt.place(x=260, y=330)

    fourth.mainloop()



def fiveth_quiz():
    fiveth = Tk()
    fiveth.geometry('600x400')
    fiveth.title('Quiz app')
    fiveth.resizable(width=False, height=False)

    def next5_func():
        global bioo
        a = var.get()
        bioo['Score']["5"] = a
        print(bioo)
        fiveth.destroy()
        sixth_quiz()


    labell_top = Label(fiveth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(fiveth, text='Listdan malumot ochirish?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(fiveth, text='remove()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(fiveth, text='[]', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(fiveth, text='append()', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(fiveth, text='2 va 3 chi tori', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(fiveth, text='Next', bg='blue', fg='white', width=13, height=2, command=next5_func)
    nextt.place(x=260, y=330)

    fiveth.mainloop()


def sixth_quiz():
    sixth = Tk()
    sixth.geometry('600x400')
    sixth.title('Quiz app')
    sixth.resizable(width=False, height=False)

    def next6_func():
        global bioo
        a = var.get()
        bioo['Score']["6"] = a
        print(bioo)
        sixth.destroy()
        seventh_quiz()


    labell_top = Label(sixth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(sixth, text='fg nima qiladi?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(sixth, text='oynaning rangini ozgartiradi', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(sixth, text='yozuvni rangini ozgartiradi', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(sixth, text='ekranga obzats beradi', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(sixth, text='hammasi togri', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(sixth, text='Next', bg='blue', fg='white', width=13, height=2, command=next6_func)
    nextt.place(x=260, y=330)

    sixth.mainloop()



def seventh_quiz():
    seventh = Tk()
    seventh.geometry('600x400')
    seventh.title('Quiz app')
    seventh.resizable(width=False, height=False)

    def next7_func():
        global bioo
        a = var.get()
        bioo['Score']["7"] = a
        print(bioo)
        seventh.destroy()
        eightth_quiz()

    labell_top = Label(seventh, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(seventh, text='Sarlavha beradigan funksiya?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(seventh, text='geometry', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(seventh, text='resizable', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(seventh, text='Tk()', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(seventh, text='title', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(seventh, text='Next', bg='blue', fg='white', width=13, height=2, command=next7_func)
    nextt.place(x=260, y=330)

    seventh.mainloop() 



def eightth_quiz():
    eightth = Tk()
    eightth.geometry('600x400')
    eightth.title('Quiz app')
    eightth.resizable(width=False, height=False)

    def next8_func():
        global bioo
        a = var.get()
        bioo['Score']["8"] = a
        print(bioo)
        eightth.destroy()
        nineth_quiz()


    labell_top = Label(eightth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(eightth, text='Celsiy formulasi?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(eightth, text='5/9(150+32)', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(eightth, text='9/5(150+32)', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(eightth, text='5*9(150-32)', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(eightth, text='5/9*(150-32)', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(eightth, text='Next', bg='blue', fg='white', width=13, height=2, command=next8_func)
    nextt.place(x=260, y=330)

    eightth.mainloop()



def nineth_quiz():
    nineth = Tk()
    nineth.geometry('600x400')
    nineth.title('Quiz app')
    nineth.resizable(width=False, height=False)

    def next9_func():
        global bioo
        a = var.get()
        bioo['Score']["9"] = a
        print(bioo)
        nineth.destroy()
        tenth_quiz()


    labell_top = Label(nineth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(nineth, text='Texnologiya bu nima?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(nineth, text='yangi narsalar', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(nineth, text='tosh', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(nineth, text='computer', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(nineth, text='noutbuk', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(nineth, text='Next', bg='blue', fg='white', width=13, height=2, command=next9_func)
    nextt.place(x=260, y=330)

    nineth.mainloop()



def tenth_quiz():
    tenth = Tk()
    tenth.geometry('600x400')
    tenth.title('Quiz app')
    tenth.resizable(width=False, height=False)


    def next10_func():
        global bioo
        a = var.get()
        bioo['Score']["10"] = a
        print(bioo)
        tenth.destroy()
        score_page()

        

    labell_top = Label(tenth, bg='green', width=90, height=2, fg='white',
        text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
    labell_top.pack()

    var = StringVar()
    var.set(0)

    quizz1 = Label(tenth, text='font() ga nechta argument bersa boladi?',
    font=('Arial', 15, 'bold'))
    quizz1.place(x=70, y=100)

    radioo1 = Radiobutton(tenth, text='3', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo1.place(x=70, y=140)

    radioo2 = Radiobutton(tenth, text='2', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
    radioo2.place(x=70, y=180)

    radioo3 = Radiobutton(tenth, text='4', value="False", variable=var, font=('Arial', 15, 'normal'))
    radioo3.place(x=70, y=220)

    radioo4 = Radiobutton(tenth, text='5', value="Error", variable=var, font=('Arial', 15, 'normal'))
    radioo4.place(x=70, y=260)

    nextt = Button(tenth, text='Next', bg='blue', fg='white', width=13, height=2, command=next10_func)
    nextt.place(x=260, y=330)

    tenth.mainloop()


def  score_page():
    score = Tk()
    score.geometry('600x400')
    togri_javoblar = 0
    notogri_javoblar = 0

    for k,v in bioo['Score'].items():
        if v == "Tog'ri":
            togri_javoblar = togri_javoblar +  1
        else:
            notogri_javoblar = notogri_javoblar +  1

    with open('register.json', 'w') as a:
        json.dump(bioo,a)

    frame1 = Frame(score, width=300, height=400, bg='red')
    frame1.place(x=0, y=0)

    rasm = Image.open('download.png').resize((200, 250))
    image = ImageTk.PhotoImage(rasm)
    label = Label(frame1, image=image)
    label.place(x=50, y=70)

    frame2 = Frame(score, width=300, height=400, bg='green')
    frame2.place(x=300, y=0)

    namee = bioo['Register']['name']
    surname = bioo['Register']['surname']
    phone = bioo['Register']['phone_number']
    email = bioo['Register']['email']

    label1 = Label(frame2, text=f"Name: {namee}", bg='green', fg='white')
    label1.place(x=25, y=30)

    label2 = Label(frame2, text=f"Surname: {surname}", bg='green', fg='white')
    label2.place(x=25, y=60)

    label3 = Label(frame2, text=f"Phone number: {phone}", bg='green', fg='white')
    label3.place(x=25, y=90)

    label4 = Label(frame2, text=f"Email: {email}", bg='green', fg='white')
    label4.place(x=25, y=120)

    label5 = Label(frame2, text=f"Togri javoblar: {togri_javoblar}", bg='green', fg='white')
    label5.place(x=25, y=150)

    label6 = Label(frame2, text=f"Notogri javoblar: {notogri_javoblar}", bg='green', fg='white')
    label6.place(x=25, y=180)

    score.mainloop()



register()




