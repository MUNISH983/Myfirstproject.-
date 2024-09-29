class theater:
    def __init__(self,movies):
        self.ticket = movies

    def moviesToWatch(self):
        print("these are the movie which is running")
        for ticket in self.ticket:
           print(" " + ticket)

    def borrowTicket(self,ticketname):
        if ticketname in self.ticket:
            print(f"your ticket has been book for {ticketname} enjoy the movie")     
            self.ticket.remove(ticketname)  
            return True
        else:
            print("sorry your ticket is either not avilable or has been soldout to some one")
            return False
        
    def returnTicket(self,ticketname):
        self.ticket.append(ticketname)
        print("thanks for purchasing the ticket ")

class watchers:
    def requestTicket(self):
        self.ticket = input("enter the name of the movie:  ")
        return self.ticket
    def returnticket(self):
        self.ticket = input("enter the name of the ticket which you want to return:  ")
        return self.ticket
    
if __name__ == "__main__":
    centre = theater(["gorzilla", "krish 5","o my god","kgf 3"])   
    watchers = watchers()
    centre.moviesToWatch()
    while(True):
        welcomemsg = '''welcome to theater
        here are your options:
        1 for list of movies
        2 for request ticket
        3 for return ticket
        4 for exit the ticket'''
        a = int(input("enter a choice: "))
        if a == 1:
            centre.moviesToWatch()
        elif a == 2:
            centre.borrowTicket(watchers.requestTicket())    
        elif a == 3:
            centre.returnTicket(watchers.returnticket())    
        elif a == 4:
            print("thanks for watching the movie")
            exit()
        else:
            print("invalid choice") 
        print(welcomemsg)   

