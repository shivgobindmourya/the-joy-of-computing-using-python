import csv
from gmplot import gmplot

# Step 1: Create map (center point + zoom)
gmap = gmplot.GoogleMapPlotter(28.7041, 77.1025, 13)


# Step 2: Read CSV file
latitudes = []
longitudes = []

with open('c:/Users/techn/Downloads/Python OEC/Week 7/route.csv','r') as f:
    reader = csv.reader(f)

    for row in reader:
        lat = float(row[0])
        lon = float(row[1])

        latitudes.append(lat)
        longitudes.append(lon)


# Step 3: Mark starting point (yellow)
gmap.marker(latitudes[0], longitudes[0], color='yellow')

# Step 4: Mark ending point (red)
gmap.marker(latitudes[-1], longitudes[-1], color='red')

# Step 5: Plot route line (blue)
gmap.plot(latitudes, longitudes, color='blue', edge_width=3)

# Step 6: Generate HTML file
gmap.draw("my_map.html")

print("Map created successfully! Open my_map.html")