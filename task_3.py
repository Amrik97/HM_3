def info(name, last_name, year, city, email, phone):
    print("%s %s %s года рождения, проживает в городе %s, \n"
          "email: %s, телефон: %s" % (name, last_name, year, city, email, phone))


if __name__ == '__main__':
    info(name="Олег", last_name="Змейкин", year="1996", city="Almaty", email="olezmey@example.com", phone="87775553344")
    exit(0)