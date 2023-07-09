import sys

import geoip2.database
import collections


def handle_ips(file_name):
    '''
        Reads in each IP, lookup for country, print out iso_code and country name
        Useful for later processing in Excel etc
        Print out all countries ordered by most_common
    :param file_name:
    :return:
    '''
    country_count = collections.Counter()

    with geoip2.database.Reader('GeoLite2-Country.mmdb') as reader:
        with open(file_name, "r") as f:
            for line_number, line in enumerate(f):
                line = line.rstrip()
                response = reader.country(line)
                print(f"{line_number},{line},{response.country.iso_code},{response.country.name}")
                country_count[response.country.name] += 1
    print("-" * 10)

    for country, count in country_count.most_common():
        print(f"{country}:{count}")


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("please supply a file with the ip addresses")
        sys.exit(1)
    handle_ips(sys.argv[1])
