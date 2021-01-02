#!/usr/bin/env python

from open_data import import_clean_data
from process_data import get_metadata, create_test_data, low_spin, high_spin, split_df_pitch, add_proj_line
from plot_data import plot_data, plot_grid, heatmap, data_surface, kde
import math
from pybaseball import statcast

#TODO: finish updating packages to python3.8. currently up to scipy in terminal
p_data = pitching_stats(2012, 2016)
print(data.head())
#data = statcast(start_dt='2017-06-24', end_dt='2017-06-27')
#data.head(2)
"""
data_file = 'cleaned_pitches.csv'
test_data_file = 'test_pitches.csv'

# Import Data
# ===========
# Full data
data = import_clean_data(data_file)

# Test data -> NOTE: test set must be created first
#data = import_clean_data(test_data_file)

# Creates the test data set [NOTE: Comment out if not needed]
#test_data = create_test_data(data, 100, 'test_pitches.csv')

# Process Data
# ============
# NOTES:
# - There is a lot of data to process so it would be more efficient to filter
#   the data before doing any calcs or 'improvements'.
# Split the data by what hand the pitcher throws with.
handed = 'X'
handed_col = '???' #merge the handed data from the  AB data
if handed == 'R' or handed == 'L':
    data = data.loc[data[handed_col]==handed]

# Remove excessive break_length values
data = data.loc[data['break_length']<100]

# Split the data by pitch type
data = split_df_pitch(data, 'FF')

data = add_proj_line(data)


#data['mov_dir'] = math.atan()
print(data)

#Split by high and low spin pitches
"""
"""
low_thresh = 0.5
hi_thresh = 0.5
angle_cut = 10
speed_cut = 90
low_spin(data, low_thresh, speed_cut)
high_spin(data, hi_thresh, angle_cut)
"""
"""

# Plot Data
# =========
# Kernel plot
#kde(data)

# Scatter plot
#plot_data(data)

# Plot grid of scatter plots
plot_grid(data)
"""
