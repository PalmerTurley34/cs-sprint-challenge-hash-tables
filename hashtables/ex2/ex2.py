#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {ticket.source: ticket.destination for ticket in tickets}
    curr = 'NONE'
    route = [flights[curr]]
    while flights[curr] != 'NONE':
        curr = flights[curr]
        route.append(flights[curr])
    return route
