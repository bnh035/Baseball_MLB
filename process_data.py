#!/usr/bin/env python

def get_metadata(df):
    data_dict = {}
    data_dict['shape'] = df.shape()

    return data_dict

def add_proj_line(df):
    # Check point, time, and velocity is valid
    df['avg_speed'] = (df['start_speed'] + df['end_speed']) * 1.47 / 2
    df['dist'] = 60.5
    df['time'] = df['dist'] / df['avg_speed']
    df['proj_x'] = df['x0'] + df['vx0'] * df['time']
    #df['proj_y'] = df['y0'] + df['vy0'] * df['time'] - 40
    df['proj_z'] = df['z0'] + df['vz0'] * df['time']
    df['diff_x'] = (df['proj_x'] - df['px']) * 12
    df['diff_z'] = (df['proj_z'] - df['pz']) * 12
    df['total_mov'] = (df['diff_x'] ** 2 + df['diff_z'] ** 2) **0.5
    return df

def create_test_data(df, num_of_rows, output_file_name):
    clipped_data = df[:num_of_rows]
    clipped_data.to_csv(output_file_name, index=False)
    return clipped_data

def low_spin(df, cut_off, speed_limit):
    df = df.loc[df['start_speed']>=speed_limit]
    max_spin = df['spin_rate'].max()
    min_spin = df['spin_rate'].min()
    rate_cut_off = min_spin + (max_spin - min_spin) * cut_off
    ls_df = df.loc[df['spin_rate'] < rate_cut_off]
    ls_drop_avg = ls_df['break_length'].mean()
    print(ls_drop_avg)

def high_spin(df, cut_off, angle_cut):
    df = df.loc[(df['break_angle'] <= angle_cut) & (df['break_angle'] >= -angle_cut)]
    max_spin = df['spin_rate'].max()
    min_spin = df['spin_rate'].min()
    rate_cut_off = max_spin - (max_spin - min_spin) * cut_off
    hi_df = df.loc[df['spin_rate'] > rate_cut_off]
    hi_drop_avg = hi_df['break_length'].mean()
    print(hi_drop_avg)

def split_df_pitch(df, pitch_opt):
    pitch_types = {
    'FF':'Four-seam',
    'SL':'Slider',
    'FT':'Two-seam',
    'CH':'Changeup',
    'SI':'Sinker',
    'CU':'Curveball',
    'FC':'Cutter',
    'KC':'Knuckle-curve',
    'FS':'Splitter',
    'KN':'Knuckleball',
    'SC':'Screwball'
    }
    """
    if pitch_opt in df['pitch_type']:
        pitch_df = df.loc[df['pitch_type']==pitch_opt]
    else:
        pitch_df = 'Error: No such pitch.'
    """
    pitch_df = df.loc[df['pitch_type'] == pitch_opt]
    return pitch_df
