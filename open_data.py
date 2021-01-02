#!/usr/bin/env python

""" open_data.py
    ==================
Date Started: 13 December 2020
"""

import pandas as pd
import numpy as np
import math
from datetime import datetime
import os.path


def conv(val):
    """Converter function to change NaN to 0.

    Parameters
    ----------
    val : Series entry
        Description of parameter `val`.

    Returns
    -------
    float
        Returns either the original value or 0 if NaN.

    """
    if val == np.nan:
        ret_val = 0
    else:
        ret_val = val
    return ret_val


def conv_time(total_seconds):
    """Converts seconds to minutes and seconds.

    Parameters
    ----------
    total_seconds : int
        The number of seconds to be converted.

    Returns
    -------
    list of ints
        First list value is the number of minutes, the second is the seconds.

    """
    minutes = int(math.floor(total_seconds/60.0))
    seconds = int(total_seconds - minutes * 60)
    return [minutes, seconds]


def check_csv(file_name):
    """Determines if a csv filename is valid.

    Parameters
    ----------
    file_name : string
        The csv filename to be checked.

    Returns
    -------
    boolean
        Returns True if the filename is valid.

    """
    if file_name[-4:] == '.csv' and os.path.isfile(file_name):
        ret_val =  True
    elif not os.path.isfile(file_name):
        print('Error: No such file "' + file_name + '".')
        ret_val = False
    else:
        print('Error: Not a valid CSV.')
        ret_val = False
    return ret_val


def check_chunksize(num):
    """Check chunksize is valid.

    Parameters
    ----------
    num : int
        The chunksize to be checked.

    Returns
    -------
    type : bool
        True if chunksize is valid.

    """
    if isinstance(num, int) and (num > 0):
        ret_val = True
    elif not isinstance(num, int):
        print('Error: Chunk Size is not an integer.')
    else:
        print('Error: Chunk Size is less than zero.')
        ret_val = False
    return ret_val


def import_data(file_name, chunk_size, cols, clean_data):
    """Short summary.

    Parameters
    ----------
    file_name : string
        Name of the file containing the data to be imported.
    chunk_size : int
        Determines the size of the chunks that the data will be imported in.
    cols : list
        List of columns to check for NaN values.
    clean_data : boolean
        Determines if a cleaned data file is to be output.

    Returns
    -------
    DataFrame
        DataFrame containing the imported data.

    """
    if check_csv(file_name) and check_chunksize(chunk_size) and isinstance(cols, list) and isinstance(clean_data, bool):
        # Import csv in chunks
        print("Importing Data...")
        imported_data = pd.DataFrame()
        df = pd.read_csv(file_name, chunksize=chunk_size)

        # Process parameter
        chunk_num = 0
        num_of_chunks = math.ceil(sum(1 for row in open(file_name, 'r'))/chunk_size)
        char_count = 20
        now = datetime.now()
        time_rem = [0, 0]
        time_passed = [0, 0]

        for chunk in df:
            # Process chunk
            chunk.dropna(axis=0, inplace=True)

            for i in cols:
                chunk[i] = chunk[i].astype(np.uint32)

            imported_data = imported_data.append(chunk)

            # Calc process
            chunk_num = chunk_num + 1
            perc_comp = int(math.ceil(100 * chunk_num / num_of_chunks))
            comp_count = int(math.ceil(perc_comp * char_count / 100))

            if chunk_num % 20 == 0:
                secs_rem = int(100*(datetime.now() - now).total_seconds()/perc_comp)
                secs_passed = int((datetime.now() - now).total_seconds())
                time_rem = conv_time(secs_rem)
                time_passed = conv_time(secs_passed)

            # Output process details
            chunk_line = 'Chunk: ' + str(chunk_num) + '/' + str(num_of_chunks)
            perc_line = ' (' +  str(perc_comp) + '%)'
            perc_bar = '[' + '=' * (comp_count - 1) + '>' + ' ' * (char_count - comp_count) + ']'
            time_passed_line = ' Time: ' + str(time_passed[0]) + 'm ' + str(time_passed[1]) + 's'
            time_rem_line = ', Est. time: ' + str(time_rem[0]) + 'm ' + str(time_rem[1]) + 's'
            print('\r' + chunk_line + perc_line + perc_bar + time_passed_line + time_rem_line, end='\r')

        # Export data
        if clean_data:
            print('\n' + 'Writing Data ...')
            imported_data.to_csv('pitch_out.csv', index=False)
            print('Done')
        ret_val = imported_data
    else:
        if not isinstance(cols, list):
            print('Error: Columns given are not in a list.')
        elif not isinstance(clean_data, bool):
            print('Error: clean_data was expecting a boolean value.')
        ret_val = 0
    return ret_val


def import_clean_data(file_name):
    print('Importing data...')
    now = datetime.now()
    imported_data = pd.read_csv(file_name)
    fin_time = datetime.now()
    print('Done in: ' + str(fin_time - now) + 's')
    return imported_data


def export_data(df, file_name):
    # Not really necessary at the moment
    if isinstance(df, pd.DataFrame):
        df.to_csv(file_name, index=False)
    else:
        print('Error: Input is not a dataFrame')
        return 0


# in_data = import_data('pitches.csv', 50000, ['nasty', 'zone'], True)
#in_data = import_clean_data('cleaned_pitches.csv')
#print(in_data)
# export_data(in_data, 'cleaned_pitches.csv')
