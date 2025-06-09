import math
import seaborn as sns  # To produce a heatmap
import matplotlib.pyplot as plt  # To show the plot finally
import numpy as np
from qwerty_layout import keys  # getting layout from the file

# to calculate distance between keys
def calculate_distance(start, end, layout):
    x1, y1 = layout[start]['pos']
    x2, y2 = layout[end]['pos']
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# to calculate total travel distance for a text
def total_distance(text, layout):
    total = 0
    for c in text:
        if c.isupper():  # if uppercase, include shift's distance
            # Use the closest shift key
            total += min(
                calculate_distance('Shift_L', c.lower(), layout),
                calculate_distance('Shift_R', c.lower(), layout)
            )
        elif c in layout:  # checking if char is in the layout dict 
            start = layout[c]['start']
            total += calculate_distance(start, c, layout)
    return total

# function to create heatmap
def heatmap(text, layout):
    # Counting freq of each key
    freq = {x: 0 for x in layout.keys()}
    for c in text.lower():  # Handling cases for upper and lower case
        if c in freq:
            freq[c] += 1

    # Transform freqs to a 2D array for heatmap generation
    max_row = int(max(p['pos'][0] for p in layout.values())) + 1  # Handling in int
    max_col = int(max(p['pos'][1] for p in layout.values())) + 1  
    heatmap_data = np.zeros((max_row, max_col))  # Converting the numpy

    # filling array with frequencies based upon key positions
    for k, p in layout.items():
        heatmap_data[int(p['pos'][0]), int(p['pos'][1])] = freq.get(k, 0) 
        # Using get to handle missing keys just in case

    # making heatmap using seaborn
    sns.heatmap(heatmap_data, cmap='coolwarm', annot=True)
    plt.show()