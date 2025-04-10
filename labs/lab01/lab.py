# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
     # mean 
    n = len(nums)
    mean = sum(nums) / n

    # median
    if n % 2 == 0: 
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n//2]
    
    return median <= mean


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    result = ''
    while n > 0:
        result += s[:n]
        n -= 1
    return result


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    results = []

    ints_len = max(len(str(abs(num))) for num in ints)
    
    for num in ints:
        # determines what the actual max length is after 'exploding' the values 
        # accounts for any length changes after exploding (9 exploded by 2 -> 7 8 9 10 11, accounts for length of 10 and 11)
        exploded_max = max(len(str(abs(num + n))), len(str(abs(num - n))))
        max_len = max(ints_len, exploded_max)
    
    for num in ints:
        # 'explode' the numbers by n values 
        exploded_vals = range(num - n, num + n + 1)
        
        # add the appropriate number of leading zeroes
        formatted_vals = []
        for val in exploded_vals:
            formatted_vals.append(f"{val:0{max_len}d}")
        
        # join all formatted values with spaces
        exploded_str = ' '.join(formatted_vals)
        results.append(exploded_str)

    return results   



# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    last_char = ''
    for line in fh: 
        line = line.strip()
        if line: 
            last_char += f'{line[-1]}'
    return last_char 


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    # get position of value within arr A without using a loop - range 
    positions = np.arange(len(A))
    
    #get the square root for each position 
    sqrt_positions = np.sqrt(positions)

    return A + sqrt_positions

def where_square(A):
    # perform sqrt on array passed in
    sqrt_A = np.sqrt(A)
    rounded = np.round(sqrt_A)

    # will return T/F depending on if the rounded sqrt ^2 
    # is equivalent to the passed in arr
    return np.abs(rounded ** 2 - A) == 0


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff): 
    cutoff_arr = []

    for col_index in range(len(matrix[0])): # gets the len of number of vals in 1 row 
                                            # to be used as a range of columns
        column = [row[col_index] for row in matrix] # gets the row and column val at each row in the matrix

        col_mean = sum(column) / len(column) # calculates mean of the column

        # appends cols that have col_mean > f 
        if col_mean > cutoff: 
            cutoff_arr.append(column) 
        
    return np.array(cutoff_arr)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    
    column_means = np.mean(matrix, axis = 0) # axis = 0 -> columns
    cutoff_arr = matrix[:, column_means > cutoff]

    return cutoff_arr


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):

    growth = (A[1:] - A[:-1]) / A[:-1]
    return np.array(np.round(growth, 2))

def with_leftover(A):
    stock_price = np.arange(len(A))
    money = 20

    n = money//stock_price # number of times you can purchase a stock without going over
    spent = n*stock_price # total amount of money spent 
    leftover = money - spent

    cum_leftover = np.cumsum(leftover) 

    # days when cumulative leftover >= next day's stock price
    valid_days = np.where(cum_leftover[:-1] >= stock_price[1:])[0]
    
    # return first valid day if exists, else -1
    if len(valid_days > 0): 
        return (valid_days[0] + 1)
    else: 
        return -1



# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    stats = pd.Series(dtype='object')
    
    # number of players
    stats['num_players'] = len(salary)
    
    # number of teams
    stats['num_teams'] = salary['Team'].nunique()
    
    # total salary 
    stats['total_salary'] = salary['Salary'].sum()
    
    # player with highest salary
    stats['highest_salary'] = salary.loc[salary['Salary'].idxmax(), 'Player']
    
    # average salary of Los Angeles Lakers
    lakers_avg = salary.loc[salary['Team'] == 'Los Angeles Lakers', 'Salary'].mean()
    stats['avg_los'] = round(lakers_avg, 2)
    
    # player with fifth lowest salary (name, team)
    fifth_lowest = salary.nsmallest(5, 'Salary').iloc[-1]
    stats['fifth_lowest'] = f"{fifth_lowest['Player']}, {fifth_lowest['Team']}"
    
    # check for duplicate last names (ignoring suffixes)
    last_names = salary['Player'].str.split().str[-1]  # Get last word of name
    stats['duplicates'] = last_names.duplicated().any()
    
    # total salary of team with highest paid player
    highest_team = salary.loc[salary['Salary'].idxmax(), 'Team']
    stats['total_highest'] = salary.loc[salary['Team'] == highest_team, 'Salary'].sum()
    
    return stats


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
