from urllib import request
from linkedqueue import LinkedQueue
import json


class Search:
    """ """
    URL = "https://api.skypicker.com/flights?flyFrom={}&to={}&dateFrom={}&partner=picky"

    def __init__(self, u_from, u_to, d_from):
        """ """
        self.u_from = u_from
        self.u_to = u_to
        self.d_from = d_from

    def url_request(self):
        """ """
        url_param = Search.URL.format(self.u_from, self.u_to, self.d_from)
        url1 = request.urlopen(url_param)
        content = url1.read().decode(url1.info().get_param('charset') or 'utf-8')
        data = json.loads(content)
        return data

    def data_extract(self):
        """ """
        flights = LinkedQueue()
        for i in self.url_request()['data']:
            lst = []
            lst.append(i['price'])
            lst.append(i['fly_duration'])
            lst.append(len(i['route']))
            flights.push(lst)


if __name__ == "__main__":
    u_from = "kiev"
    u_to = "paris"
    d_from = "15/08/2019"
    d_to = "18/08/2019"
    # u_from = input("from :")
    # u_to = input("to :")
    # d_from = input("date from :")
    # d_to = input("date to :")
    r = Search(u_from, u_to, d_from)
    print(r.data_extract())
    r = Search(u_to, u_from, d_to)
    print(r.data_extract())





# r.url_request()['data'][0]
# id-
# countryFrom
# countryTo
# bags_price
# baglimit
# dTime
# aTime
# dTimeUTC
# p1
# p2
# p3
# aTimeUTC
# price+
# flyFrom
# mapIdfrom
# mapIdto
# flyTo
# distance
# cityFrom+
# cityTo+
# route
# routes
# airlines
# nightsInDest
# pnr_count
# transfers
# has_airport_change
# fly_duration+
# duration
# facilitated_booking_available
# type_flights
# found_on
# conversion
# booking_token
# quality
# deep_link+
# search_id+
# data!!!!!!!!
# connections-
# time+1
# currency+
# currency_rate+1
# refresh-
# del+??
# ref_tasks-
# search_params
# all_stopover_airports-
# all_airlines-
