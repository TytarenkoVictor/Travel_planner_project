from date_estimation import CheckDate
from flights import Search
from time_counting import Time
from data_block import TravelPlan



def main(u_from, u_to, d_from, d_to):
    """This function creates html string and save
    html file with all data."""
    try:
        check = CheckDate(d_from, d_to)
    except:
        er = "Please, enter correct dates."
        ht = """
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
      <div style="border:1px solid black;">\
      <p style="text-align:center;">{}</p></div>
      {}
    </body>
</html>
            """.format(er, "<br>")
        with open("templates/file.html", "w", encoding="utf-8") as file:
            file.write(ht)

    if check.check_two() is True:
        d_from = d_from[0:-2] + "20" + d_from[-2:]
        d_to = d_to[0:-2] + "20" + d_to[-2:]
        try:
            r = Search(u_from, u_to, d_from, d_from)
            dd = r.data_extract()
            m = Search(u_to, u_from, d_to, d_to)
            tt = m.data_extract()
            summary = [dd[0][0] + tt[0][0], dd[1], tt[1]]
        except:
            er = "Sorry there are no flights on your route..."
            ht = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
        </head>
        <body>
          <div style="border:1px solid black;">\
          <p style="text-align:center;">{}</p></div>
          {}
        </body>
    </html>
                """.format(er, "<br>")
            with open("templates/file.html", "w", encoding="utf-8") as file:
                file.write(ht)
        try:
            time = Time(dd, tt)
            data1 = dd[0][3] + tt[0][3]
            data2 = time.final_route()
            travel = TravelPlan(data1, data2, summary)
            cities = travel.city_block()
            route = "Your route:  " + "  ==>  ".join(cities[1])
            st = ""
            while not cities[0].isEmpty():
                st += '''<div style="border:1px solid black;">\
                <p style="text-align:center;">{}</p></div>'''.\
                format(cities[0].pop()[1:].replace("\n", "<br><br>"))
                st += "\n"
            ht = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
        </head>
        <body>
          <div style="border:1px solid black;">\
          <p style="text-align:center;">{}</p></div>
          {}
          <div style="border:1px solid black;"><center><img src="{}">\
          </center></div>
        </body>
    </html>
                """.format(route, st, "static/visual.png")
            ht.format(route, st)
            with open("templates/file.html", "w", encoding="utf-8") as file:
                file.write(ht)
        except:
            er = "Your date are too short to visit this city."
            ht = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
        </head>
        <body>
          <div style="border:1px solid black;">\
          <p style="text-align:center;">{}</p></div>
          {}
        </body>
    </html>
                """.format(er, "<br>")
            with open("templates/file.html", "w", encoding="utf-8") as file:
                file.write(ht)
    else:
        er = check.check_two()
        ht = """
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
      <div style="border:1px solid black;">\
      <p style="text-align:center;">{}</p></div>
      {}
    </body>
</html>
            """.format(er, "<br>")
        with open("templates/file.html", "w", encoding="utf-8") as file:
            file.write(ht)
