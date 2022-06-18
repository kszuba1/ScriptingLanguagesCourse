from datetime import datetime

all_cases=[]
by_date={}
by_country={}
by_date_c={}
by_country_c={}
def load_data():
    with open('C:\\Users\\K\\Desktop\\studia\\skryptLab\\Covid.txt', 'r',encoding="utf-8") as file:
        for line in file:
            row = line.strip().split()
            row[3] = int(row[3])
            row[2] = int(row[2])
            row[1] = int(row[1])
            row[5] = int(row[5])
            row[4] = int(row[4])
            all_cases.append((row[6],row[3],row[2],row[1],row[5],row[4]))

            if (len(row) >= 10):

                if ((row[3], row[2], row[1]) in by_date_c):
                    by_date_c[(row[3], row[2], row[1])].append((row[10], row[5], row[4]))
                else:
                    by_date_c[(row[3], row[2], row[1])] = [(row[10], row[5], row[4])]

                if (row[10] in by_country_c):
                    by_country_c[row[10]].append((row[3], row[2], row[1], row[5], row[4]))
                else:
                    by_country_c[row[10]] = [(row[3], row[2], row[1], row[5], row[4])]

            if((row[3],row[2],row[1]) in  by_date):
                by_date[(row[3],row[2],row[1])].append((row[6],row[5],row[4]))
            else:
                by_date[(row[3],row[2],row[1])]=[(row[6],row[5],row[4])]

            if(row[6] in  by_country):
                by_country[row[6]].append((row[3],row[2],row[1],row[5],row[4]))
            else:
                by_country[row[6]]=[(row[3],row[2],row[1],row[5],row[4])]

    file.close()


class App:

    def __init__(self):
        load_data()

    def findByDayAndCountry(self, day, month, year, country, criterion):

        date = (year, month, day)

        deathTotal = 0
        casesTotal = 0

        for (c, deaths, cases) in by_date[date]:
            if c == country:
                deathTotal += deaths
                casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal,"by day and country", day, month, year, country, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by day and country", day, month, year, country, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by day and country", day, month, year, country, criterion)
            return 'Błędnę kryterium!'

    def findByDayAndContinent(self, day, month, year, continent, criterion):

        date = (year, month, day)

        deathTotal = 0

        casesTotal = 0

        for (c, deaths, cases) in by_date_c[date]:
            if c == continent:
                deathTotal += deaths
                casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal, "by day and continent", day, month, year, continent, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by day and continent", day, month, year, continent, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by day and continent", day, month, year, continent, criterion)
            return 'Błędnę kryterium!'

    def findByRangeAndCountry(self, dayS, monthS, yearS, dayE, monthE, yearE, country, criterion):

        deathTotal = 0
        casesTotal = 0

        for (y, m, d, deaths, cases) in by_country[country]:
            if (y==yearS and y==yearE):
                if (m>=monthS and m<=monthE):
                    if ((m==monthS and d>=dayS) or (m==monthE and d<=dayE and d>=dayS) or (m!=monthS and m!=monthE) ):
                        deathTotal += deaths
                        casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal, "by range and country", dayS, monthS, yearS, dayE, monthE, yearE, country, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by range and country", dayS, monthS, yearS, dayE, monthE, yearE, country, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by range and country", dayS, monthS, yearS, dayE, monthE, yearE, country, criterion)
            return 'Błędnę kryterium!'

    def findByRangeAndContinent(self, dayS, monthS, yearS, dayE, monthE, yearE, continent, criterion):

        deathTotal = 0
        casesTotal = 0

        for (y, m, d, deaths, cases) in by_country_c[continent]:
            if (y==yearS and y==yearE):
                if (m>=monthS and m<=monthE):
                    if ((m==monthS and d>=dayS) or (m==monthE and d<=dayE and d>=dayS) or (m!=monthS and m!=monthE) ):
                        deathTotal += deaths
                        casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal, "by range and continent", dayS, monthS, yearS, dayE, monthE, yearE, continent, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by range and continent", dayS, monthS, yearS, dayE, monthE, yearE, continent, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by range and continent", dayS, monthS, yearS, dayE, monthE, yearE, continent, criterion)
            return 'Błędnę kryterium!'

    def findByMonthAndCountry(self, month, country, criterion):

        deathTotal = 0
        casesTotal = 0

        for (y, m, d, deaths, cases) in by_country[country]:
            if (m == month):
                deathTotal += deaths
                casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal, "by month and country",  month, country, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by month and country",  month, country, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by month and country", month, country, criterion)
            return 'Błędnę kryterium!'

    def findByMonthAndContinent(self, month, continent, criterion):

        deathTotal = 0
        casesTotal = 0

        for (y, m, d, deaths, cases) in by_country_c[continent]:
            if (m == month):
                deathTotal += deaths
                casesTotal += cases

        if criterion == 'przypadki':
            self.writeInFile(casesTotal, "by month and continent",  month, continent, criterion)
            return casesTotal

        elif criterion == 'zgony':
            self.writeInFile(deathTotal, "by month and continent",  month, continent, criterion)
            return deathTotal
        else:
            self.writeInFile("Błąd", "by month and continent", month, continent, criterion)
            return 'Błędnę kryterium!'

    def writeInFile(self, response, *request):

        file = open("C:\\Users\\K\\Desktop\\studia\\skryptLab\\logs.txt", "a")

        now = datetime.now()

        time_now = now.strftime("%d/%m/%Y %H:%M:%S")

        file.write(time_now)
        file.write("\n")

        file.write(str(request))
        file.write("\n")

        file.write(str(response))

        file.write("\n-----------------------------------\n")
        file.close()

