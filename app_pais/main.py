import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv(
        '/Users/imagemaker/Desktop/Python/PIP/app_pais/data.csv')
    country = input('Type Contry => ')
    data = list(filter(lambda x: x['Continent'] == 'South America', data))

    # country = list(map(lambda x: x['Country'], data))
    # percent = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_pie_chart(country, percent)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        lavels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], lavels, values)


if __name__ == '__main__':
    run()
