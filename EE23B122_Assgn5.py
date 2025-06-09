# The code asks for text input when run
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import math
import copy

# Import the layout from the file given by sir
from qwerty_layout import keys, characters

# Create a copy of the layout, to not tamper with the original
kbd_copy = copy.deepcopy(keys)

# Calculating the total distance for a given text on a specific layout
# The distance is our cost here
def find_cost(text, layout_data, current_layout):
    total_cost = 0  # Total cost is set to 0
    
    # going throuhg every character of the text
    for c in text:
        # If character has only 1 key 
        # Basically the general case
        if len(layout_data.characters[c]) == 1:
            if c == ' ':  # Handle space character
                space_key = layout_data.characters[c]
                # checking for space key in the layout
                if space_key[0] in current_layout:
                    x1, y1 = current_layout[space_key[0]]['pos']
                    # finding the start position in the layout
                    if current_layout[space_key[0]]['start'] in current_layout:
                        start_key = current_layout[space_key[0]]['start']
                        x2, y2 = current_layout[start_key]['pos']
                        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Total euclidean distance
            else:  # For all other characters
                if c in current_layout:
                    x1, y1 = current_layout[c]['pos']
                    if current_layout[c]['start'] in current_layout:
                        start_key = current_layout[c]['start']
                        x2, y2 = current_layout[start_key]['pos']
                        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
                total_cost += cost1 + cost2
    
    return total_cost  # Return the total typing cost


# optimizing the layout using simulated annealing
# Setting the temperature and cooling rate accordingly
def sim_aneal(text, layout, layout_data, temperature=1000, cooling=0.99, end_temp=0.0001):
    # Working with a copy of the layout
    current_layout = copy.deepcopy(layout)
    
    # Finding the initial cost on the current layout
    current_cost = find_cost(text, layout_data, current_layout)
    
    best_layout = current_layout  # best layout = current layout
    best_cost = current_cost  # best cost = current cost
    
    # Storing the cost over each iteration
    cost_over_time = [current_cost]
    
    # Running the loop time the temperature is low enough
    while temperature > end_temp:
        # Swap two keys in the layout
        new_layout = copy.deepcopy(current_layout)  # Create a new layout by copying the current layout
        key1, key2 = random.sample(list(new_layout.keys()), 2)  # Select two random keys
        
        # Updating the start positions of the swapped keys
        for key in layout:
            if new_layout[key]['start'] == key1:
                new_layout[key]['start'] = key2
            elif new_layout[key]['start'] == key2:
                new_layout[key]['start'] = key1
        
        # Swap the positions of the two keys
        new_layout[key1], new_layout[key2] = new_layout[key2], new_layout[key1]
        
        # new typing cost after the swap
        new_cost = calc_typing_cost(text, layout_data, new_layout)
        
        # Check if the new layout is better 
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_layout = new_layout
            current_cost = new_cost
            # Update if all ok
            if new_cost < best_cost:
                best_layout = current_layout
                best_cost = current_cost
        
        # Adding up all the costs
        cost_over_time.append(current_cost)
        
        # updating the temperature for the next iteration
        temperature *= cooling
    
    # Return the suitable parameters
    return best_layout, best_cost, cost_over_time, current_cost


# Plotting the cost (distance) over time
def plot_cost(costs):
    plt.plot(costs)
    plt.xlabel('Time')
    plt.ylabel('Cost')
    plt.title('Cost Over Time')
    plt.show()


# Plotting the keyboard layout
# The idea for this function was provided by sir
def plot_kbd(best_layout):
    fig, ax = plt.subplots(figsize=(15, 6)) 
    
    for key, data in best_layout.items():
        x, y = data['pos']  # Get the position of the key
        rect = Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=False)  # Draw the key as a rectangle
        ax.add_patch(rect)  # Add the rectangle to the plot
        ax.text(x, y, key, ha='center', va='center', fontsize=12)  # Add the key label
    
    # Set the limits and appearance of the plot
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')  # Remove axes for a clean look
    plt.title('Final Layout (Optimized)')
    plt.tight_layout()
    plt.show()


# Main function to execute the optimization and plotting
def main():
    # Getting user input
    text = input("Enter the text you want to optimize typing for: ")
    
    # Object that holds character and key info
    layout_info = type('', (), {'characters': characters, 'keys': keys})()
    
    # simulated annealing optimization
    best_layout, best_cost, costs, current_cost = sim_aneal(text, layout_copy, layout_info)
    
    # Plotting the cost
    plot_cost(costs)
    
    # Show the optimized kbd
    plot_kbd(best_layout)
    
# Running the main function
if __name__ == "__main__":
    main()
