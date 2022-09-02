#Question_4:

class Phonebook(list):

    '''Allows to keep track of given contacts in phonebook'''

# method for search field filter
    def search_menu(self):
        option = int(input('Filters for search field:\n1. Name\n2. Contact Number\n3. Email\nSelect option: '))
        self.contacts_found = Phonebook()
        if option == 1:
                flag=0
        elif option==2:
                flag=1
        elif option==3:
                flag=2
        s=str(input('Search contacts by filter option '+str(flag+1 )))
        for item in self:
             if s in item[flag]:
                    self.contacts_found.append(item)
        return self.contacts_found

# method for print format
    def __str__(self):
        if len(self) != 0:
            head = f"\n{'Name':<30}{'Contact':<30}{'Email':<20}\n"
            for item in self:
                head += f'\n{item[0]:30}{item[1]:30}{item[2]:20}'
            return head
        else:
            return 'Contacts Not Found..'

#childclass

class ProtectedPhonebook(Phonebook):

    '''Child class of Phonebook, with the functionality to refuse deletion of stored contacts'''

#methods to stop deletion of contacts
    def pop(self,p):
        print('Contacts cannot be deleted...')

    def remove(self,r):
        print('Contacts cannot be deleted...')

#instance1
pb1=Phonebook()
pb1.append(['Jake Peralta','34562357962','dake@gmail.com'])
pb1.append(['Gina Linneti','0332879079','ginad@gcom.com'])
pb1.append(['Sally Fernandez','0123457865','sf.12@hotmail.com'])
pb1.append(['Harry Linneti','0123878650','hd@hotmail.com'])
print(pb1.search_menu())
pb1.sort()
pb1.remove(['Jake Peralta','34562357962','dake@gmail.com'])
print(pb1)

#instance2
pb2=ProtectedPhonebook()
pb2.append(['Lilly Fernandez','0213457965','sf.23@gmail.com'])
pb2.append(['John Ferndinand','0123467365','js.67@hotmail.com'])
pb2.pop(0)
pb2.remove(['Jake Peralta','34562357962','dake@gmail.com'])
print(pb2)