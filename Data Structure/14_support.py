import queue

class Visit :
    def __init__(self, arrival, id, remaining) :
        self.arrival = arrival
        self.id = id
        self.remaining = remaining

    def __lt__(self, other) :
        if(self.remaining != other.remaining) :
            return self.remaining > other.remaining
        else :
            return self.arrival < other.arrival
        
        
def main() :
    numClient = int(input())
    clients = f_makeOrder(numClient)
    result = f_consulting(clients)
    f_displayResult(result)
    

def f_makeOrder(numClient) :
    clients = list()
    for i in range(numClient) :
        arrival, id, remaining = map(int, input().split())
        clients.append(Visit(arrival, id, remaining))

    return clients

def f_consulting(clients) :
    order = queue.PriorityQueue()
    now = 30
            
    exit = queue.Queue()

    while(clients or order.qsize()) : 
        if(clients) :
            now, order, clients = f_remainingsort(order, now, clients)

        temp = order.get()
        
        if(temp.remaining <= 10) :
            exit.put(temp)
            now += temp.remaining
        else :
            consultedTime = temp.remaining//2
            now += consultedTime
            temp.arrival = now
            temp.remaining -= consultedTime
            order.put(temp)

    return exit

def f_remainingsort(order, now, clients) :
    while(clients) :
        if(clients[0].arrival <= now) : 
            order.put(clients[0])
            del clients[0]
        else :
            break

    if(order.empty()) :
        order.put(clients[0])
        now = clients[0].arrival
        del clients[0]
    
    return now, order, clients

def f_displayResult(result) :
    while(result.qsize()) :
        print(result.get().id)

main()