def city_country(city,country,famoussite=''):
    if famoussite:
        describe = city.title() + ", " + country.title() + " - famous sites: " + famoussite.title()
    else:
        describe = city.title() + ", " + country.title()
    return describe