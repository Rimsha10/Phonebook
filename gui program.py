from tkinter import Tk, Frame, Label, Entry, Radiobutton, Button, IntVar, StringVar, BooleanVar
from tkinter import *


class window(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(400, 500)
        self.maxsize(700, 900)
        self.title('PhoneBook')
        imge = PhotoImage(file='y.png')
        #bg_Image = Label(self, image=imge).place(x=0, y=0, relwidth=1, relheight=1)
        self.config(bg='#00688B')

        def convert():
           proceed.set(True)
        la=Label(self,text='Welcome To PhoneBook ',font=('Georgia',20,'bold'),fg='white',bg='#00688B')
        la.pack(pady=5)
        label = Label(self,image=imge)
        label.pack()
        f=Frame(self,bg='#00688B')

        lb=Label(f,text='SELECT AN OPTION',font=('Georgia',20,'bold'),fg='#FFC125',bg='#00688B')#fg='#00868B')
        lb.pack(pady=25)
        radio_selection = IntVar(f, 0)
        rb1 = Radiobutton(f, text='Search Contacts', font=('Verdana', 18), variable=radio_selection, value=1, bg='#00688B',fg='white')
        rb1.pack(pady=30)
        rb2 = Radiobutton(f, text='Add Contacts', font=('Verdana', 16), variable=radio_selection, value=2,
                          bg='#00688B',fg='white',activeforeground='black',command='sel')#bg='#B0E0E6')
        rb2.pack(pady=31)
        rb3 = Radiobutton(f, text='Delete Contacts', font=('Verdana', 16), variable=radio_selection, value=3,bg='#00688B',fg='white')
                          #bg='#B0E0E6')
        rb3.pack(pady=32)
        b1 = Button(f, text='OK', font=('Anton',14,'bold'),bg='white',command=convert,fg='#00688B',width='15')
        b1.pack(pady=34)
        f.pack(pady=10)
        proceed = BooleanVar(f, False)
        f.wait_variable(proceed)
        if radio_selection.get() == 2:
            root2 = Tk()
            root2.title('Add Contacts')
            root2.minsize(500, 500)
            root2.maxsize(550, 650)
            root2.config(bg='#B0E0E6')
            def save():
                proceed.set(True)
                l=Label(root2,text='Contact successfully added to phonebook!',font=('Verdana',15),fg='#00868B')
                l.pack(pady=25)
            l1a=Label(root2,text='Contact Details',font=('Georgia',18,'bold'),bg='#B0E0E6',fg='#00868B')
            l1a.pack(pady=10)
            f2 = Frame(root2, bg='#B0E0E6')
            l1b=Label(f2,text='Name',font=('Verdana',15),bg='#B0E0E6')
            l1b.grid(row=1,column=1,pady=20,sticky='ns')
            e1b= Entry(f2,bd=5,width=28)
            e1b.grid(row=1,column=2,pady=20 )
            l1c = Label(f2, text='Contact Number ',font=('Verdana',15),bg='#B0E0E6')
            l1c.grid(row=2, column=1,pady=22)
            e1c = Entry(f2, bd=5, width=28)
            e1c.grid(row=2, column=2,pady=22)
            l1d = Label(f2, text='Email Address ',font=('Verdana',15),bg='#B0E0E6')
            l1d.grid(row=3, column=1,pady=24)
            e1d = Entry(f2, bd=5, width=25)
            e1d.grid(row=3, column=2,pady=24)
            b1 = Button(f2, text='SAVE', font=('Anton',14,'bold'),bg='#E0EEEE', command=save,fg='#00868B')
            b1.grid(row=1000,column=2)
            f2.pack(fill='both',pady=15)
            proceed = BooleanVar(f2, False)
            f2.wait_variable(proceed)
            contact = list((e1b.get(), e1c.get(), e1d.get()))
            w = Write()
            w.write((str(contact)+'\n'))
            root2.mainloop()
            #self.entry = e1.get()
            #self.flag = 0
        if radio_selection.get() == 3:
            root= Tk()
            root.title('Delete Contacts')
            root.minsize(400, 500)
            root.config(bg='#B0E0E6')
            l1a = Label(root, text='Select A Contact', font=('Georgia', 16, 'bold'),fg='#00868B', bg='#B0E0E6')
            l1a.pack(pady=10)
            def delete():
                proceed.set(True)
                l = Label(root, text='Contact successfully deleted from phonebook!', font=('Verdana', 15),
                          fg='#00868B')
                l.pack(pady=25)
            #self.flag = 0
          #  for item in self.contact:
           #     self.flag += 1
            contacts = Read.read(self, 'Phonebook.txt')
            f2b=Frame(root,bg='#B0E0E6')
            flag=0
            if len(contacts) != 0:
                head = f"\n{'Name':<30}{'Contact':<30}{'Email':<20}\n"
                l1 = Label(f2b, text=head, bg='#B0E0E6',fg='black',font=('Verdana', 15, 'bold'))
                l1.pack()
                radio_selection1 = IntVar(f, 0)

                for item in contacts:
                    ind=contacts.index(item)+1
                    head2= f'\n{item[0]:30}{item[1]:30}{item[2]:20}'
                    rb = Radiobutton(f2b, text=head2, font=('Verdana', 15), variable=radio_selection1, value=ind,
                                      bg='#B0E0E6')
                    print(head2)
                    rb.pack(pady=19+ind)
                b1a = Button(f2b, text='DELETE', font=('Anton', 14, 'bold'), bg='#E0EEEE', command=delete,
                                fg='#00868B',
                                width='15')
                b1a.pack(pady=24)
                flag+=1
            else:
                l1bb = Label(f2b, text='Contacts not found', font=('Verdana',12), fg='#CD3333', bg='#B0E0E6')
                l1bb.pack()
            f2b.pack()

            proceed = BooleanVar(f2b, False)
            f2b.wait_variable(proceed)
            if flag!=0:
              for i in range(len(contacts)+1):
                if radio_selection1.get() == i:
                        contacts.pop(i-1)
                        w = open('Phonebook.txt','w')
                        for item in contacts:
                          w.write((str(item)+'\n'))
            root.mainloop()

        if radio_selection.get() == 1:
            f1 = Frame1()
            f1.frame1()
            self.mainloop()
            #self.entry = e1.get()
            self.flag = 2



class Frame1:
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.minsize(500, 600)
        self.root.maxsize(550, 650)
        self.root.title('Search Contacts')
        # imge = PhotoImage(file='unnamed.png')
        # bg_Image = Label(self, image=imge).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.config(bg='#B0E0E6')
    def frame1(self):
        def convert():
           proceed.set(True)
        f1 = Frame(self.root,bg='#B0E0E6')
        l1 = Label(f1, text='SELECT FILTER\n',font=('Georgia',16,'bold'),fg='#00868B',bg='#B0E0E6')
        l1.pack()
        radio_selection = IntVar(f1, 0)
        rb1 = Radiobutton(f1, text='Name',font=('Verdana',14), variable=radio_selection, value=1,bg='#B0E0E6')
        rb1.pack()
        rb2 = Radiobutton(f1, text='Contact Number',font=('Verdana',14), variable=radio_selection, value=2,bg='#B0E0E6')
        rb2.pack()
        rb3 = Radiobutton(f1, text='Email Address',font=('Verdana',14), variable=radio_selection, value=3,bg='#B0E0E6')
        rb3.pack()
        l2 = Label(f1, text='\nENTER IN SEARCH FIELD\n',font=('Verdana',14),bg='#B0E0E6')
        l2.pack ()
        e1 = Entry(f1,bd=5,width=28)
        e1.pack()
        b1 = Button(f1, text='SHOW RESULTS',font=('Anton',14,'bold'),bg='#E0EEEE',command=convert,fg='#00868B' )
        b1.pack(pady=20)
        f1.pack()
        proceed = BooleanVar(f1, False)
        f1.wait_variable(proceed)
        if radio_selection.get() == 1:
            self.entry = e1.get()
            self.flag = 0
        if radio_selection.get() == 2:
            self.entry = e1.get()
            self.flag = 1
        if radio_selection.get() == 3:
            self.entry = e1.get()
            self.flag = 2
        self.frame2()
    def showresult(self):

        self.contact = Read.read(self,'Phonebook.txt')
        #print(self.contact)
        self.contacts_found = []
        for item in self.contact:
            if self.entry in item[self.flag]:

                self.contacts_found.append(item)
        #print(self.contacts_found)
        return self.contacts_found
    def getcontacts(self):
        return self.contacts_found

    def frame2(self):
        self.root2=Tk()
        self.root2.title('Search Results')
        self.root2.minsize(400, 500)
        self.root2.config(bg='#B0E0E6')
        f2 = Frame(self.root2,bg='#C6E2FF')
        self.contacts = self.showresult()
        if len(self.contacts) != 0:
           head = f"\n{'Name':<30}{'Contact':<30}{'Email':<20}\n"
           for item in self.contacts:
               head += f'\n{item[0]:30}{item[1]:30}{item[2]:20}'
           l1 = Label(f2, text=head,font=('Verdana',12),bg='#B0E0E6')
           l1.pack()
        else:
            l1=Label(f2,text='Contacts not found',font=('Verdana',12),fg='#CD3333',bg='#B0E0E6')
            l1.pack()
        f2.pack()
        self.root2.mainloop()
class Read:
    def read(self, fn):
        r = open(fn, 'a+')
        r.seek(0)
        l=[]
        for item in r:
            l.append(eval(item))
        r.close()
        return l
class Write:
    def write(self,contact):
      f = open('Phonebook.txt','a')
      f.write(contact)
      f.close()
#class Frame2:
   # def __init__(self, root):
      #  self.root = root
       ##self.frame2()
    #def frame2(self):
        #f2 = Frame(self.root)
        #self.contacts=Frame1.getcontacts(self)
       # if len(self.contacts) != 0:
       #     l1 = Label(f2, text=self.contacts_found,bg='#B0E0E6')
        #    l1.pack()
        #f2.pack()
       # self.root.mainloop()



w1 = window()
