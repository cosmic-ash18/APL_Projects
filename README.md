# EE2703 Assignment 4 & 5

## Assignment 4: Keyboard Usage Heatmap and Distance Calculation

### Introduction
This part of the assignment analyzes keyboard usage for a given input text. The goal is to:
- Generate a heatmap showing frequency of key usage.
- Calculate the total distance fingers move while typing the text.

### Functions Used
1. **`calculate_distance(start, end, layout)`**  
   Calculates Euclidean distance between two keys based on their coordinates.

2. **`total_distance(text, layout)`**  
   Computes the total distance fingers travel when typing the input text.

3. **`heatmap(text, layout)`**  
   Visualizes key usage as a heatmap.

### Assumptions
- Only standard English letters and numbers are considered.
- Input text does not contain unsupported special characters.

### Key Findings
- The code calculates total typing distance.
- Frequently used keys are easily identified using the heatmap.
- Visualization helps understand typing patterns.

### Output Examples
- The program shows visual heatmaps and numeric total distances for given text inputs.

### Extra Work
- Also tried to plot key usage as contours using `seaborn.kdeplot`.

---

## Assignment 5: Keyboard Layout Optimization using Simulated Annealing

### Introduction
This part aims to optimize keyboard layout using simulated annealing to minimize finger movement while typing.

### Problem Description
The goal is to rearrange keys so that the total typing distance for a given input text is minimized. The optimization uses random key swaps and a probabilistic acceptance function.

### Steps Followed

1. **Input**  
   - Takes text input from user.
   - Uses `qwerty_layout.py` for initial layout.

2. **Cost Calculation**  
   - Calculates distance between consecutive keys using 2D Euclidean formula.

3. **Simulated Annealing**  
   - Starts with an initial temperature and layout.
   - Repeatedly swaps two keys.
   - Accepts new layout based on cost and temperature.
   - Returns best layout and cost.

4. **Plotting**  
   - Shows cost reduction over iterations.
   - Displays optimized keyboard layout.

5. **Main Function**  
   - Integrates input, optimization, and plotting.

### Resources and Notes
- Simulated annealing was the most challenging part.
- `seaborn` and discussions with classmates and professor helped.

---

## Conclusion
Both assignments provided practical insights into keyboard analysis and optimization. The heatmap helped visualize key usage, and simulated annealing provided an effective way to reduce typing effort.
