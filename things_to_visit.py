from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class ThingsToVisit:
    """This class determines which things tourist should visit in city."""
    def __init__(self, city):
        """This method initializes."""
        self.city = city
        self.url = "https://wikitravel.org/en/{}#See".format(self.city)

    def find_attractions(self):
        """This methods parse site and determines main things to do
        or attractions in given city."""
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(self.url, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        index_start = soup.text.find("See[edit]")
        index_end = soup.text.find("Do[edit]")
        main = soup.text[index_start:index_end]
        lst = main.split("\n")
        lst_header = []
        for e in lst:
            if "[edit]" in e:
                lst_header.append(e[0:-6])
        if len(lst_header) == 1:
            lst_header.append("Explore city")
            lst_header.append("Sightseeing")
        return lst_header[1:]

    def link(self):
        """This method returns link on more detail info about things to visit
        in given city."""
        return "Things to see in " + self.city + ": " + self.url
