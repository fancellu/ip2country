# ip2Country

Uses MaxMind GeoLite2 Country free database to do bulk IP address country lookups

## To run

Download ```GeoLite2-Country.mmdb``` to the local directory

```pip install -r requirements.txt```

```python main.py ipfile.txt```

## Outputs

line_number, IP, iso_code, country_name

Then the count of IP addresses for each country, ordered by most common