import pandas as pd
import numpy as np

planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]

# TO DO: Create a Pandas Series "dist_planets" using the lists above, representing the distance of the planet from the Sun.
# Use the `distance_from_sun` as your data, and `planets` as your index.
dist_planets = pd.Series(distance_from_sun, planets)
print("Planets and their distance to the sun: \n",dist_planets, '\n')

# TO DO: Calculate the time (minutes) it takes light from the Sun to reach each planet. 
# You can do this by dividing each planet's distance from the Sun by the speed of light.
# Use the speed of light, c = 18, since light travels 18 x 10^6 km/minute.
c = 18 #18 x 10^6 km/minute
time_light = np.divide(dist_planets, c)
print("Time (in mins) it takes for sunlight to reach a planet: \n", time_light, '\n')

# TO DO: Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[time_light<40.0]
print("Planets where that time is under 40 mins: \n", close_planets, '\n')