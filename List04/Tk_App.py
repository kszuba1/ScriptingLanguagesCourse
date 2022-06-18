from tkinter import *
from tkinter import messagebox
from C_App import App

def start():
    app = App()
    window = Tk()

    window.title("Aplikacja tkinter")
    window.geometry('1200x600')

    label1 = Label(window, text='Dzień ', font=("Arial Bold", 30))
    label1.grid(column=0, row=0)

    label2 = Label(window, text='Wybierz przypadki/zgony : ')
    label2.grid(column=0, row=1)
    criterion = Entry(window, width=60)
    criterion.grid(column=1, row=1)

    label3 = Label(window, text='Wybierz kraj/kontynent : ')
    label3.grid(column=0, row=2)
    country_or_continent = Entry(window, width=60)
    country_or_continent.grid(column=1, row=2)

    label4 = Label(window, text="Wpisz lokalizacje: ")
    label4.grid(column=0, row=3)
    location = Entry(window, width=60)
    location.grid(column=1, row=3)

    label5 = Label(window, text="Wpisz numer miesiaca: ")
    label5.grid(column=0, row=4)
    month = Entry(window, width=60)
    month.grid(column=1, row=4)

    label6 = Label(window, text="Wpisz dzien: ")
    label6.grid(column=0, row=5)
    day = Entry(window, width=60)
    day.grid(column=1, row=5)

    def byDay():
        result = "Błędne kryterium!"
        criterion_txt = criterion.get()
        country_or_continent_txt = country_or_continent.get()
        location_txt = location.get()
        day_int = int(day.get())
        month_int = int(month.get())
        year = 2020


        if (criterion_txt=="przypadki" or criterion_txt=="zgony"):
            if (country_or_continent_txt=="kraj"):
                result = app.findByDayAndCountry(day_int, month_int, year, location_txt, criterion_txt)

            elif (country_or_continent_txt == "kontynent"):
                result = app.findByDayAndContinent(day_int, month_int, year, location_txt, criterion_txt)

            else:
                result = "Błędny wybór lokalizacji!"

        else:
            result = "Błędny wybór kryterium!"

        messagebox.showinfo('Informacja', result)

    btn = Button(window, text="Potwierdź",command=byDay)
    btn.grid(column=1, row=6)

    label7 = Label(window, text='Miesiąc', font=("Arial Bold", 30))
    label7.grid(column=0, row=7)

    label8 = Label(window, text='Wybierz przypadki/zgony : ')
    label8.grid(column=0, row=8)
    criterion2 = Entry(window, width=60)
    criterion2.grid(column=1, row=8)

    label9 = Label(window, text='Wybierz kraj/kontynent : ')
    label9.grid(column=0, row=9)
    country_or_continent2 = Entry(window, width=60)
    country_or_continent2.grid(column=1, row=9)

    label10 = Label(window, text="Wpisz lokalizacje: ")
    label10.grid(column=0, row=10)
    location2 = Entry(window, width=60)
    location2.grid(column=1, row=10)

    label11 = Label(window, text="Wpisz numer miesiaca: ")
    label11.grid(column=0, row=11)
    month2 = Entry(window, width=60)
    month2.grid(column=1, row=11)

    def byMonth():
        result = "Błędne kryterium!"
        criterion_txt = criterion2.get()
        country_or_continent_txt = country_or_continent2.get()
        location_txt = location2.get()
        month_int = int(month2.get())
        year = 2020

        if (criterion_txt=="przypadki" or criterion_txt=="zgony"):
            if (country_or_continent_txt=="kraj"):
                result = app.findByMonthAndCountry(month_int, location_txt, criterion_txt)

            elif (country_or_continent_txt == "kontynent"):
                result = app.findByMonthAndContinent(month_int, location_txt, criterion_txt)

            else:
                result = "Błędny wybór lokalizacji!"

        else:
            result = "Błędny wybór kryterium!"

        messagebox.showinfo('Informacja', result)

    btn2 = Button(window, text="Potwierdź",command=byMonth)
    btn2.grid(column=1, row=12)

    label12 = Label(window, text='Zakres', font=("Arial Bold", 30))
    label12.grid(column=0, row=13)

    label13 = Label(window, text='Wybierz przypadki/zgony : ')
    label13.grid(column=0, row=14)
    criterion3 = Entry(window, width=60)
    criterion3.grid(column=1, row=14)

    label14 = Label(window, text='Wybierz kraj/kontynent : ')
    label14.grid(column=0, row=15)
    country_or_continent3 = Entry(window, width=60)
    country_or_continent3.grid(column=1, row=15)

    label15 = Label(window, text="Wpisz lokalizacje: ")
    label15.grid(column=0, row=16)
    location3 = Entry(window, width=60)
    location3.grid(column=1, row=16)

    label16 = Label(window, text="Wpisz datę początkową: ")
    label16.grid(column=0, row=17)
    date_start = Entry(window, width=60)
    date_start.grid(column=1, row=17)

    label16 = Label(window, text="Wpisz datę końcową: ")
    label16.grid(column=0, row=18)
    date_end = Entry(window, width=60)
    date_end.grid(column=1, row=18)

    def byRange():
        result = "Błędne kryterium!"
        criterion_txt = criterion3.get()
        country_or_continent_txt = country_or_continent3.get()
        location_txt = location3.get()
        date_start_txt = date_start.get()
        date_end_txt = date_end.get()
        year = 2020

        date_start_txt = date_start_txt.split('.')
        date_end_txt = date_end_txt.split('.')

        for i in range(3):
            date_start_txt[i] = int(date_start_txt[i])
            date_end_txt[i] = int(date_end_txt[i])

        if (date_start_txt[1] > date_end_txt[1]):
            result = 'Błędny zakres!'

        elif (date_start_txt[1] == date_end_txt[1] and (date_start_txt[0] >= date_end_txt[0])):
            result = 'Błędny zakres!'

        else:
            if (criterion_txt=="przypadki" or criterion_txt=="zgony"):
                if (country_or_continent_txt=="kraj"):
                    result = app.findByRangeAndCountry(date_start_txt[0], date_start_txt[1], date_start_txt[2],
                                                  date_end_txt[0], date_end_txt[1], date_end_txt[2], location_txt, criterion_txt)

                elif (country_or_continent_txt == "kontynent"):
                    result = app.findByRangeAndContinent(date_start_txt[0], date_start_txt[1], date_start_txt[2],
                                                  date_end_txt[0], date_end_txt[1], date_end_txt[2], location_txt, criterion_txt)

                else:
                    result = "Błędny wybór lokalizacji!"

            else:
                result = "Błędny wybór kryterium!"

        messagebox.showinfo('Informacja', result)

    btn3 = Button(window, text="Potwierdź",command=byRange)
    btn3.grid(column=1, row=19)


    window.mainloop()


if __name__ == '__main__':
    start()