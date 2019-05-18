from urllib import request
from datetime import datetime
import json


class Search:
    """This class used for searching flights from given city to final
    and back."""
    URL = "https://api.skypicker.com/flights?flyFrom\
={}&to={}&dateFrom={}&dateTo={}&partner=picky"

    def __init__(self, u_from, u_to, d_from, d_to):
        """This method initializes."""
        self.u_from = u_from.replace(" ", "-")
        self.u_to = u_to.replace(" ", "-")
        self.d_from = d_from
        self.d_to = d_to

    def url_request(self):
        """This method gets data from kiwi.com."""
        url_param = Search.URL.\
        format(self.u_from, self.u_to, self.d_from, self.d_to)
        url1 = request.urlopen(url_param)
        content = url1.read().decode(url1.info().\
        get_param('charset') or 'utf-8')
        data = json.loads(content)
        return data

    def data_extract(self):
        """This method extract data about flight: date, price, duration,
        link ex."""
        flight = []
        m = self.url_request()['data'][0]
        flight.append(m['price'])
        flight.append(m['fly_duration'])
        flight.append(len(m['route']))
        link = m['deep_link']
        full_route = []
        for i in m['route']:
            lst = []
            lst.append(str(datetime.fromtimestamp(i['aTimeUTC'])))
            lst.append(str(datetime.fromtimestamp(i['dTimeUTC'])))
            lst.append(i['cityFrom'].replace("ó", "o"))
            lst.append(i['cityTo'].replace("ó", "o"))
            full_route.append(lst)
        flight.append(full_route)
        return flight, link
