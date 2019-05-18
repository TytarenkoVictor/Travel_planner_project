from price import CostOfLiving
from linkedqueue import LinkedQueue
from things_to_visit import ThingsToVisit
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


class TravelPlan:
    """This class creates travel plan."""
    def __init__(self, data1, data2, summary):
        """This method initializes."""
        self.data1 = data1
        self.data2 = data2
        self.summary = summary
        self.queue = LinkedQueue()
        self.total_food = 0
        self.total_transport = 0
        self.extrainfo = ""
        self.see = ""

    def city_block(self):
        """This methods creates travel plan, including all flights, transit
        cities, final city, info about prices, transport and summary about
        travel total cost, links and ex. And add all of them to quque."""
        lst = []
        self.data2.append("Summary")
        print("Building your route...")
        print(self.data1[0][2])
        lst.append(self.data1[0][2])
        for i, city in zip(self.data1, self.data2):
            self.queue.add("\nfrom {} to {}\n{} ==> {}".\
            format(i[2], i[3], i[1], i[0]))
            st = ""
            if city == "Summary":
                print(self.data1[0][2])
                lst.append(self.data1[0][2])
                self.queue.add("\n" + city)
                self.summary_result()
                self.visualisation()
                return self.queue, lst
            print(city[0])
            lst.append(city[0])
            st = "\n" + city[0] + "\n" + city[1][0][0:-3] + " ==> " \
            + city[1][1][0:-3] + "\n" + "Total time: " + city[2][0:-3] + \
" hours"
            if city[3]:
                visit = ThingsToVisit(city[0])
                st += "\nMost popular things to do in " + city[0] + ":" + "\n" \
                + "\n".join(visit.find_attractions())
                self.see += visit.link() + "\n"
                cost0 = CostOfLiving(city[0])
                cost = cost0.estimate_food_expences(city[4])
                self.total_food += cost[0]
                st += "\nCost of food in " + city[0] + ":" + \
"\nPrice of products for cooking: " + str(cost[0]) + "€\n" + \
"Price in MacDonald's: " + str(cost[1]) + "€" + \
"\nPrice in inexpensive restaurants: " + str(cost[2]) + "€" + \
"\nPrice in mid range restaurants: " + str(cost[3]) + "€"
                self.extrainfo += "\nPrice list in " + city[0] + ":\n"+ \
                cost0.additional()
                tr = cost0.estimate_transport_expences(city[4])
                self.total_transport += tr
                st += "\nCost of transport: " + str(tr) + "€"
                st += "\nAccommodation: visit https://www.couchsurfing.com/ \
for free stay."
            else:
                st += "\nWaiting in airport, not enough time to visit \
this city."
            self.queue.add(st)

    def summary_result(self):
        """This method creates summary about trip."""
        sum_st = "\nMinimal budget for trip:\n1) Flights price: {}€\n2) Food \
expences: {}€\n3) Transport expences: {}€\n4) Accommodation expences: 0€\nTota\
l: {}€\n\nDetail food costs:\n{}\nThings to see links:\n{}\nFlight booking \
link1:\n{}\n\nFlight booking link2:\n{}".format(self.summary[0],\
round(self.total_food, 2), round(self.total_transport, 2), \
round(self.summary[0] + self.total_food + self.total_transport, 2),\
self.extrainfo, self.see, self.summary[1][0:62], self.summary[2][0:62])
        self.queue.add(sum_st)

    def visualisation(self):
        """This method creates total expenxes visualisation."""
        objects = ('Flights', 'Food', 'Transport', 'Accommodation')
        y_pos = np.arange(len(objects))
        performance = [self.summary[0], self.total_food, self.total_transport, 0]
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Price in €')
        plt.title('Minimal budget for trip')
        plt.savefig('static/visual.png')
