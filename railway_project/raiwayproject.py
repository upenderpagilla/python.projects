import random
import pickle
import sys

logged_in = False
uid=0
pwd=""

class train:
    def __init__(self, name='',num=0,arr_time='',dep_time='',src='',des='',day_of_travel='',seat_available_in_1ac=0,seat_available_in_2ac=0,seat_available_in_SL=0,fare_1ac=0,fare_2ac=0,fare_sl=0):
        self.name=name
        self.num=num
        self.arr_time=arr_time
        self.dep_time=dep_time
        self.src=src
        self.des=des
        self.day_of_travel=day_of_travel
        self.seats={'1AC':seat_available_in_1ac,'2AC':seat_available_in_2ac,'SL':seat_available_in_SL}
        self.fare={'1AC':fare_1ac,'2ac':fare_2ac,'SL':fare_sl}

    def print_seat_availability(self):
        print("no.of seats available in 1AC:-"+str(self.seats['1AC']))
        print("no.of seats available in 2AC:-"+str(self.seats['2AC']))
        print("no.of seats available in SL:-"+str(self.seats['SL']))

    def check_availability(self,coach='',ticket_num=0):
        coach=coach.upper()
        if coach not in ('SL','1AC','2AC'):
            train.print_seat_availability()
            coach=input("Enter the coach(1ac/2ac/sl):-")
        else:
            if self.seats[coach]==0:
                return False
            elif self.seats[coach]>=ticket_num:
                return True
            else:
                return False

    def book_ticket(self, coach='',no_of_tickets=0):
        self.seats[coach]-=no_of_tickets
        return True

class ticket:
    def __init__(self,train,user,ticket_num,coach,ticket_dict):
        self.pnr=str(train.num)+str(user.uid)+str(random.randint(1000,9999))
        self.train_num=train.num
        self.coach=coach
        self.uid=user.uid
        self.train_name=train.name
        self.user_name=user.name
        self.ticket_num=ticket_num
        ticket_dict=0
        user.history.update({self.pnr:self})
        ticket_dict.update({self.pnr:self})

class user:
    def __init__(self,uid=0,name='',hometown='',cell_num='',pwd=''):
        self.uid=uid
        self.name=name
        self.hometown=''
        self.cell_num=''
        self.pwd=pwd
        self.history={}

class acceptors:
    '''class containing functions for accepting and validating values properly'''
    def accept_uid():
        uid=0
        try:
            uid=int(input("Enter the userid:-"))
        except ValueError:
            print("Please enter userid properly")
            return acceptors.accept_uid()
        else:
            return uid
    def accept_pwd():
        pwd=input("Enter your password:-")
        return pwd
    def accept_train_number():
        train_num=0
        try:
            train_num=int(input("Enter the train number:-"))
        except ValueError:
            print("Please enter train number properly.")
            return acceptors.accept_train_number()
        else:
            if train_num not in trains:
                print("please enter a valid train number")
                return acceptors.accept_train_number()
            else:
                return train_num
    def accept_menu_option():
        option=input("Enter your option:")
        if option not in ('1','2','3','4','5','6','7','8'):
            print("Please enter a valid option!")
            return acceptors.accept_menu_option()
        else:
            return int(option)
    def  accept_coach():
        coach=input("Enter the coach:")
        coach=coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print("Please enter coach properly!")
            return acceptors.accept_coach()
        else:
            return coach
    def accept_prompt():
        prompt=input("confirm?(y/n):-")
        if prompt not in ('y','n'):
            print("Please enter proper choice")
            return acceptors.accept_prompt()
        return prompt
    def accept_ticket_num():
        ticket_num=0
        try:
            ticket_num=int(input("Enter the number of tickets:"))
            if ticket_num<0:
                raise ValueError
        except ValueError:
            print("Enter proper ticket number")
            return acceptors.accept_ticket_num()
        else:
            return ticket_num
    def accept_pnr():
        pnr=input("Enter your pnr number:")
        if pnr not in ticket_dict:
            print("Please enter proper pnr number")
            return acceptors.accept_pnr()
        else:
            return pnr
def book_ticket():
    if not logged_in:
        login('p')
    check_seat_availability('p')
    choice=acceptors.accept_train_number()
    trains[choice].print_seat_availability()
    coach=acceptors.accept_ticket_num()
    ticket_num=acceptors.accept_ticket_num()
    if trains[choice].check_availability(coach,ticket_num):
        print("You have to pay:-",trains[choice].fare[coach]*ticket_num)
        prompt=acceptors.accept_prompt()
        if prompt=='y':
            trains[choice].book_ticket(coach,ticket_num)
            print("Booking successful!\n\n")
            tick=ticket(trains[choice],users[uid],ticket_num,coach)
            print("Please note PNR number:-",tick.pnr,"\n\n")
            menu()
        else:
            print("Exiting.....\n\n")
            menu()
    else:
        print(ticket_num,"tickets not available")
        menu()

def cancel_ticket():
    pnr=acceptors.accept_pnr()
    if pnr in ticket_dict:
        check_pnr(pnr)
        print("cancel the tickets?")
        prompt=acceptors.accept_prompt()
        if prompt=='y':
            if logged_in:
                print("Ticket cancelled.\n")
                trains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach]
                del users[ticket_dict[pnr].uid].history[pnr]
                del ticket_dict[pnr]
            else:
                login('p')
                print("Ticket Cancelled\n")
                trains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach]
                del users[ticket_dict[pnr].uid].history[pnr]
                del ticket_dict[pnr]
        else:
            print("\nTicket not cancelled\n")
    menu()
def check_seat_availability(flag=''):
    src=input("Enter the source station:-")
    des=input("Enter the destination station:-")
    flag_2=0
    for i in trains:
        if trains[i].src==src and trains[i].des==des:
            print("Train name:-",trains[i].name," ","number:-",trains[i])
            flag_2+=1
        if flag_2==0:
            print("\nNo trains found between stations you entered are not found")
            menu()
        if flag=='':
            train_num=acceptors.accept_train_number()
            trains[train_num].print_seat_availability()
            menu()
        else:
            pass
def check_pnr(pnr=''):
    if pnr=='':
        pnr=acceptors.accept_pnr()
        print()
        print("user name:",ticket_dict[pnr].user_name)
        print("Train name:",ticket_dict[pnr].train_name)
        print("Train number:",ticket_dict[pnr].train_num,"source:",ticket_dict[pnr].src,"destination:",ticket_dict[pnr].des)
        print("No of tickets booked:",ticket_dict[pnr].ticket)
        print()
        menu()
    else:
        print()
        print("user name:",ticket_dict[pnr].user_name)
        print("Train name:",ticket_dict[pnr].train_name)
        print("Train number:",ticket_dict[pnr].train_num,"source:",ticket_dict[pnr].src,"destination:",ticket_dict[pnr].des)
        print("No of tickets booked:",ticket_dict[pnr].ticket)
        print()
        menu()        

def create_new_acc():
    user_name=input("Enter your username:-")
    pwd=input("Enter your password:-")
    uid=random.randint(1000,9999)
    hometown=input("Enter your hometown:")
    cell_num=input("Enter your phone number:")
    u=user(uid,user_name,hometown,cell_num,pwd)
    print("Your userID is:",uid)
    users.update({u.uid:u})
    menu()

def login(flag=''):
    global uid
    global pwd
    uid=acceptors.accept_uid()
    pwd=acceptors.accept_pwd()
    if uid in users and users[uid].pwd==pwd:
        print("\nWelcome ",users[uid].name,"!\n")
        global logged_in
        logged_in=True
    else:
        print("\n No such userID/wrong password!\n")
        return login()
    if flag=='':
        menu()
    else:
        pass

def check_prev_bookings():
    if not logged_in:
        login('p')
    for i in users[uid].history:
        print("\nPNR number= ",i)
        check_pnr(i)
    menu()

def end():
    #s()
    print("----------------------Thank you----------------------")
    print("-----------------------------------------------------")
    sys.exit()

t1=train('hyderabad',12706,'06:00','12:00','vjw','hyd','Mon',30,23,43,290,250,239)
t2=train('tirupati',12598,'09:05','04:00','vjw','tpt','tue',23,56,89,350,310,220)
t3=train('banglore',22353,'11:56','03:12','ctc','ban','fri',60,45,42,2200,1000,500)
trains={t1.num:t1,t2.num:t2,t3.num:t3}

u1=user(1111,'sharanya','vijayawada','7956475963','sharanya')
u2=user(2358,'alex parrish','newyork','7563218964','alexparrish')
users={u1.uid:u1,u2.uid:u2}
ticket_dict={}

def load():
   with open('data.pkl', 'rb') as f:
       trains=pickle.load(f)
       users=pickle.load(f)
       ticket_dict=pickle.load(f)

def s():
   with open('data.pkl', 'wb') as f:
       pickle.dump(trains,f)
       pickle.dump(users,f)
       pickle.dump(ticket_dict,f)
        
print("------------------------WELCOME TO RAILWAY RESERVATION PORTAL------------------------")
print("-------------------------------------------------------------------------------------")
#load()

def menu():
    print("Choose one of the following option:-")
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.check PNR")
    print("4.check seat availability")
    print("5.Create new account")
    print("6.check previous bookings")
    print("7.Login")
    print("8.Exit")
    func={1:book_ticket,2:cancel_ticket,3:check_pnr,4:check_seat_availability,5:create_new_acc,6:check_prev_bookings,7:login,8:exit}
    option=acceptors.accept_menu_option()
    func[option]()
menu()