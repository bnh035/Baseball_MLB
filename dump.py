import numpy as np

p_dtype = {
        'px':float,
        'pz':float,
        'start_speed':float,
        'end_speed':float,
        'spin_rate':float,
        'spin_dir':float,
        'break_angle':float,
        'break_length':float,
        'break_y':float,
        'ax':float,
        'ay':float,
        'az':float,
        'sz_bot':float,
        'sz_top':float,
        'type_confidence':float,
        'vx0':float,
        'vy0':float,
        'vz0':float,
        'x':float,
        'x0':float,
        'y':float,
        'y0':float,
        'z0':float,
        'pfx_x':float,
        'pfx_z':float,
        'nasty':int,
        'zone':int,
        'code':str,
        'type':str,
        'pitch_type':str,
        'event_num':int,
        'b_score':int,
        'ab_id':int,
        'b_count':int,
        's_count':int,
        'outs':int,
        'pitch_num':int,
        'on_1b':int,
        'on_2b':int,
        'on_3b':int
}

ab_dtype = {
        'ab_id':int,
        'batter_id':int,
        'event':str,
        'g_id':int,
        'inning':int,
        'o':int,
        'p_score':int,
        'p_throws':str,
        'pitcher_id':int,
        'stand':str,
        'top':bool
        }

a = np.zeros(3, 3)
b = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
