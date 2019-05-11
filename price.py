from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


class CostOfLiving:
    """This class is for cost of living determination."""
    URL = "https://www.numbeo.com/cost-of-living/in/{}?displayCurrency=EUR"

    def __init__(self, city):
        """This method initializes."""
        self.city = city
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
        lst = []
        for i in self.table.text.split("\n")[3:]:
            if i != "" and bool(re.search(r'\d', i)):
                lst.append(i.replace(u'\xa0', ''))
        single = lst.pop(-3)
        lst = [i+" "+j for i, j in zip(lst[::2], lst[1::2])]
        lst.append(single)
        return lst

    def estimate_food_expences(self, days):
        """Recommended minimum amount of money for food
        (2400 calories, Western food types)"""
        portions_per_day = [0.25, 0.25, 0.10, 0.2, 0.10, 0.15,
        0.15, 0.30, 0.25, 0.30, 0.20, 0.20, 0.10, 0.20, 1]
        total = 0
        for i, e in enumerate(self.extract_data()[8:23]):
            total += float(e.split()[-2][0:-1]) * portions_per_day[i]
        home = round(total, 2) * days
        inexpensive = float(self.extract_data()[0].split()[-2][0:-1]) * 3 * days
        mid = float(self.extract_data()[1].split()[-2][0:-1]) * 1.5 * days
        mac = float(self.extract_data()[2].split()[-2][0:-1]) * 3 * days
        return home, mac, inexpensive, mid

    def estimate_transport_expences(self, days):
        """Recommended minimum amount of money for transport
        (3 trips per day, public transport)"""
        transport = float(self.extract_data()[27].split()[-2][0:-1]) * 3 * days
        return transport


if __name__ == "__main__":
    city = "Lisbon"
    c = CostOfLiving(city)
    c.parse()
    c.extract_data()
    print(c.estimate_food_expences(3))
    print(c.estimate_transport_expences(3))










# site = "https://www.numbeo.com/cost-of-living/in/Lviv?displayCurrency=EUR"
#
# # site = "https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Ukraine&country2=Ukraine&city1=Kiev&city2=Lviv&tracking=getDispatchComparison"
#
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(site, headers=hdr)
# page = urlopen(req)
# soup = BeautifulSoup(page, "html.parser")
# # summary = soup.find("div", attrs={"class": "seeding-call limit_size_ad_right padding_lower other_highlight_color"})
# # print(summary.text)
# # di = soup.find("div", attrs={"class": "column mod-main"})
# table = soup.find("table", attrs={"class": "data_wide_table"})
# print(table.text)




# def cost_of_living(city, comp):
#     if comp == "-":
#         site = "https://www.numbeo.com/cost-of-living/in/{}?displayCurrency=EUR".format(city)
#     else:
#         site = "https://www.numbeo.com/cost-of-living/compare_cities.jsp?\
#         &city1={}&city2={}&\
#         tracking=getDispatchComparison".format(comp, city)
#
#     hdr = {'User-Agent': 'Mozilla/5.0'}
#     req = Request(site, headers=hdr)
#     page = urlopen(req)
#     soup = BeautifulSoup(page, "html.parser")
#     if comp == "-":
#         summary = soup.find("div", attrs={"class": "seeding-call limit_size_ad_right padding_lower other_highlight_color"})
#         table = soup.find("table", attrs={"class": "data_wide_table"})
#         return summary.text, table.text
    # else:


# if __name__ == "__main__":
#     user1 = input("Enter city :")
#     compare = input("Do you want to caompare with other city?(+/-)")
#     if compare == "+":
#         comp = input("Enter city, which you want compare to :")
#     elif compare == "-":
#         comp = "-"
#     print(cost_of_living(user1, comp))
