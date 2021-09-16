import os
import csv
from citipy import citipy
import random
from config import number_of_cities

max_lat = 90
min_lat = -90
max_lng = 180
min_lng = -180
counter = 0

output_path = os.path.join("cities.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["City"])
    while counter < number_of_cities:
        rndLat = random.uniform(min_lat, max_lat)
        rndLng = random.uniform(min_lng, max_lng)
        city = citipy.nearest_city(rndLat, rndLng)
        cityName = city.city_name
        csvwriter.writerow([cityName])
        counter += 1
