import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
d_min = 99999999999
for i in range(n):
    no, nom, adresse, tel, lon_b, lat_b = input().split(";")
    lat_b = lat_b.replace(",", ".")
    lon_b = lon_b.replace(",", ".")
    lat = lat.replace(",", ".")
    lon = lon.replace(",", ".")
    x = (float(lon_b) - float(lon)) * math.cos((float(lat) + float(lat_b))/2)
    y = (float(lat_b) - float(lat))
    d = math.sqrt(x*x + y*y) * 6371
    if d < d_min:
        answer = nom
        d_min = d

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(answer)
