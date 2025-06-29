# Joel Atkinson Assignment 7.2 Function File Advanced Python CSD-325

def city_country(city, country, population=None, language=None):
    if population is None:
        return f'{city}, {country}'
    if language is None:
        return f'{city}, {country}, {population}'
    return f'{city}, {country}, {population}, {language}'

def main():
    # Call the function three times
    print(city_country('Vancouver', 'Canada'))
    print(city_country('Los Angeles', 'USA', 'Population: 3,821,000'))
    print(city_country('Tokyo', 'Japan', 'Population: 9,700,000', 'Japanese'))

main()