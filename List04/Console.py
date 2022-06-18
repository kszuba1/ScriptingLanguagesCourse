from C_App import App


class _RangeError(Exception):
    pass


class Console:

    @staticmethod
    def get_string(message, name="string", default=None,
                   minimum_length=0, maximum_length=80,
                   force_lower=False):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line:
                    if default is not None:
                        return default
                    if minimum_length == 0:
                        return ""
                    else:
                        raise ValueError("{0} may not be empty".format(
                            name))
                if not (minimum_length <= len(line) <= maximum_length):
                    raise ValueError("{0} must have at least {1} and "
                                     "at most {2} characters".format(name, minimum_length, maximum_length))
                return line if not force_lower else line.lower()
            except ValueError as err:
                print("ERROR", err)

    @staticmethod
    def get_integer(message, name="integer", default=None, minimum=None,
                    maximum=None, allow_zero=True):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line and default is not None:
                    return default
                x = int(line)
                if x == 0:
                    if allow_zero:
                        return x
                    else:
                        raise _RangeError("{0} may not be 0".format(name))
                if ((minimum is not None and minimum > x) or
                        (maximum is not None and maximum < x)):
                    raise _RangeError("{0} must be between {1} and {2} "
                                      "inclusive{3}".format(name, minimum, maximum,
                                                            (" (or 0)" if allow_zero else "")))
                return x
            except _RangeError as err:
                print("ERROR", err)
            except ValueError as err:
                print("ERROR {0} must be an integer".format(name))

    def start(self):

        while True:
            command = Console.get_integer('Wybierz opcje:'
                                         '\n1 - dzień'
                                         '\n2 - zakres'
                                         '\n3 - miesiąc'
                                         '\n4 - wyjdź\n')

            if command == 1:
                app = App()
                date = Console.get_string('Podaj dokładny dzień (np. 23.10.2020)')
                date = date.split('.')
                criterion = Console.get_string('Podaj kryterium (przypadki/zgony)')
                country_or_continent = Console.get_string('Wybierz opcje:'
                                                          '\n1 - kraj'
                                                          '\n2 - kontynent\n')
                if country_or_continent == '1':
                    country = Console.get_string('Podaj kraj')
                    print(app.findByDayAndCountry(int(date[0]), int(date[1]), int(date[2]), country, criterion))
                elif country_or_continent == '2':
                    continent = Console.get_string('Podaj kontynent')
                    print(app.findByDayAndContinent(int(date[0]), int(date[1]), int(date[2]), continent, criterion))

                else:
                    print("Błędny wybór!")

            elif command == 2:
                app = App()
                date_start = Console.get_string('Podaj dokładny dzień początkowy (np. 23.10.2020)')
                date_end = Console.get_string('Podaj dokładny dzień końcowy (np. 27.10.2020)')

                date_start = date_start.split('.')
                date_end = date_end.split('.')

                for i in range(3):
                    date_start[i] = int(date_start[i])
                    date_end[i] = int(date_end[i])

                if (date_start[1] > date_end[1]):
                    print('Błędny zakres!')

                elif (date_start[1] == date_end[1] and (date_start[0] >= date_end[0])):
                    print('Błędny zakres!')

                else:

                    criterion = Console.get_string('Podaj kryterium (przypadki/zgony)')

                    country_or_continent = Console.get_string('Wybierz opcje:'
                                                              '\n1 - kraj'
                                                              '\n2 - kontynent\n')
                    if country_or_continent == '1':
                        country = Console.get_string('Podaj kraj')
                        print(app.findByRangeAndCountry(date_start[0], date_start[1], date_start[2],
                                                  date_end[0], date_end[1], date_end[2], country, criterion))
                    elif country_or_continent == '2':
                        continent = Console.get_string('Podaj kontynent')
                        print(app.findByRangeAndContinent(date_start[0], date_start[1], date_start[2],
                                                  date_end[0], date_end[1], date_end[2], continent, criterion))

                    else:
                        print("Błędny wybór!")



            elif command == 3:
                app = App()
                month = Console.get_integer('Podaj miesiąc (np. 5,10,11)')
                criterion = Console.get_string('Podaj kryterium (przypadki/zgony)')

                country_or_continent = Console.get_string('Wybierz opcje:'
                                                          '\n1 - kraj'
                                                          '\n2 - kontynent\n')

                if country_or_continent == '1':
                    country = Console.get_string('Podaj kraj')
                    print(app.findByMonthAndCountry(month,country,criterion))
                elif country_or_continent == '2':
                    continent = Console.get_string('Podaj kontynent')
                    print(app.findByMonthAndContinent(month,continent,criterion))

                else:
                    print("Błędny wybór!")

            elif command == 4:
                break

            else:
                print('Bledny wybór !')


if __name__ == '__main__':
    console = Console()
    console.start()
