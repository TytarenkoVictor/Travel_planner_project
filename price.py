from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


class CostOfLiving:
    """This class is for cost of living determination."""
    URL = "https://www.numbeo.com/cost-of-living/in/{}?displayCurrency=EUR"

    def __init__(self, city):
        """This method initializes."""
        self.city = city.replace(" ", "-")
        if self.city == "Krakow":
            self.city = "Krakow-Cracow"
        self.table = None

    def parse(self):
        """This method parse given url."""
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = CostOfLiving.URL.format(self.city)
        req = Request(url, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        self.table = soup.find("table", attrs={"class": "data_wide_table"})

    def extract_data(self):
        """This method extract data and creates list with it."""
        self.parse()
        lst = []
        for i in self.table.text.split("\n")[3:]:
            if i != "" and bool(re.search(r'\d', i)):
                lst.append(i.replace(u'\xa0', ''))
        single = lst.pop(-3)
        lst = [i + " " + j for i, j in zip(lst[::2], lst[1::2])]
        lst.append(single)
        return lst[0:28]

    def estimate_food_expences(self, hours):
        food = self.extract_data()
        """This method estimate food expences in given city during given period
        of time(in hours). Recommended minimum amount of money for food + water
        (2400 calories per day, Western food types). Milk - 0.25 liter,
        Bread - 125 g, Rice - 0.1 kg, Eggs - 2.4, Cheese - 0.1 kg,
        Chicken - 0.15 kg, Beef - 0.15 kg, Apples - 0.3 kg, Banana - 0.25 kg,
        Oranges - 0.3 kg, Tomato - 0.2 kg, Potato - 0.2 kg, Onion - 0.1 kg,
        Lettuce - 0.2 head, Water - 1.5 litter."""
        portions_per_day = [0.25, 0.25, 0.10, 0.2, 0.10, 0.15,
        0.15, 0.30, 0.25, 0.30, 0.20, 0.20, 0.10, 0.20, 1]
        total = 0
        for i, e in enumerate(food[8:-5]):
            total += float(e.split()[-2][0:-1]) * portions_per_day[i]
        home = round(round(total, 2) * round(hours/24, 2), 2)
        inexpensive = round(float(food[0].split()[-2][0:-1]) * \
        round(hours/8, 2), 2)
        mid = round(float(food[1].split()[-2][0:-1]) * round(hours/16, 2), 2)
        mac = round(float(food[2].split()[-2][0:-1]) * round(hours/8, 2), 2)
        return home, mac, inexpensive, mid

    def additional(self):
        """This method returns detail info about food + water prices
        in given city."""
        data = self.extract_data()
        st = ""
        for i in data[8:-5]:
            st += i + "\n"
        return st

    def estimate_transport_expences(self, hours):
        """This method estimate transport expences in given city during given
        period of time(in hours). Recommended minimum amount of money for
        transport (3 trips per day, public transport)"""
        pr = self.extract_data()[27]
        transport = round(float(pr.split()[-2][0:-1]) * round(hours/8, 2), 2)
        return transport
