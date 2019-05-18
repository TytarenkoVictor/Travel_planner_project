from datetime import datetime


class Time:
    """This class estimates time."""
    def __init__(self, data1, data2):
        """This method initializes."""
        self.data1 = data1
        self.data2 = data2

    @staticmethod
    def plane_transfer(data):
        """This method determine numbers of transit and returns flight data:
        all arrive and departues time, all cities and transit."""
        if data[0][2] > 0:
            time_list = []
            city = []
            for i in data[0][3]:
                city.append(i[-1])
                time_list.append(i[1])
                time_list.append(i[0])
            fmt = '%Y-%m-%d %H:%M:%S'
            ss = [str(datetime.strptime(time_list[i + 1], fmt) - \
            datetime.strptime(time_list[i], fmt)) for i in \
            range(1, len(time_list) - 1, 2)]
            transit = []
            for time in range(0, len(time_list[1:-1]), 2):
                transit.append((time_list[1:-1][time], \
                time_list[1:-1][time + 1]))
            return ss, transit, city
        else:
            return False

    @staticmethod
    def visit_another(data):
        """This method determines is it enough time to visit transit city.
        If total time in airport - time to get to city and back to airport
        bigger that 4 hours returns True."""
        if not data:
            return False
        else:
            fmt = '%H:%M:%S'
            result = []
            for time in data:
                time_difference = datetime.strptime(time, fmt) - \
                datetime.strptime('04:00:00', fmt)
                if str(time_difference)[1] == ":":
                    diff = int("0" + str(time_difference)[0:1])
                else:
                    diff = int(str(time_difference)[0:2])
                if diff >= 4:
                    result.append(True)
                else:
                    result.append(False)
            return result

    @staticmethod
    def combine_results(data):
        """This method combines all results about all transit cities."""
        results = []
        time_data = Time.plane_transfer(data)
        stay = Time.visit_another(time_data[0])
        for i in range(len(time_data[0])):
            results.append((time_data[2][i], time_data[1][i], time_data[0][i],\
             stay[i], int(time_data[0][i].split(":")[0]) + \
             round(int(time_data[0][i].split(":")[1]) / 60, 2)))
        return results

    def total_time_in_city(self):
        """This method determines total time in visited city, time of arrival
        and departue and total time in hours."""
        arrive = self.data1[0][3][-1][0]
        departue = self.data2[0][3][0][1]
        fmt = '%Y-%m-%d %H:%M:%S'
        total_time = str(datetime.strptime(departue, fmt) - \
        datetime.strptime(arrive, fmt))
        divide = total_time.split()
        if len(divide) == 1:
            return False
        elif divide[-1][1] == ":":
            divide[-1] = "0" + divide[-1]
        hours1 = int(divide[0]) * 24
        hours2 = int(divide[-1][0:2])
        hours3 = round(int(divide[-1][3:5]) / 60, 1)
        hours_total = hours1 + hours2 + hours3
        results = [(self.data1[0][3][-1][-1], (arrive, departue), \
        total_time, True, hours_total)]
        return results

    def final_route(self):
        """This method combines results about all transit cities and main
        cities and returns route."""
        arrive = Time.combine_results(self.data1)
        city = self.total_time_in_city()
        departue = Time.combine_results(self.data2)
        return arrive + city + departue
