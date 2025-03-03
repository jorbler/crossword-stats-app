from datetime import datetime
import pandas as pd
import numpy as np
import os

index_order = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def load_daily_data() -> pd.DataFrame:
    '''Loads daily data for graphing/table view.'''
    data_files = os.listdir("data/")
    daily_data = pd.read_csv("data/" + [file for file in data_files if file.startswith("daily")][0])[["seconds_spent_solving", "print_date", "star", "day"]]
    return daily_data

def daily_gold_days() -> pd.DataFrame:
    '''Gets DataFrame with only puzzles that were completed with a Gold Star.'''
    daily_data = load_daily_data()
    gold_all_days = daily_data[daily_data["star"] == "Gold"].reset_index(drop = True)
    return gold_all_days

def load_bonus_data() -> pd.DataFrame:
    '''Loads bonus data for graphing/table view.'''
    data_files = os.listdir("data/")
    bonus_data = pd.read_csv("data/" + [file for file in data_files if file.startswith("bonus")][0])[["seconds_spent_solving", "title", "print_date"]]
    bonus_data = bonus_data.dropna()
    return bonus_data

def load_mini_data() -> pd.DataFrame:
    '''Loads mini data for graphing/table view.'''
    data_files = os.listdir("data/")
    mini_data = pd.read_csv("data/" + [file for file in data_files if file.startswith("mini")][0])[["seconds_spent_solving", "print_date", "solved", "day"]]
    return mini_data



def get_day_frame(day: str) -> pd.DataFrame:
    '''Preps data for individual day histograms.'''
    daily_data = daily_gold_days()
    day_frame = daily_data[daily_data["day"] == day].reset_index(drop = True)
    day_frame = day_frame[["seconds_spent_solving", "print_date"]]

    datetime_date = []
    for i in range(len(day_frame)):
        datetime_date += [datetime.strptime(day_frame["print_date"].iloc[i], "%Y-%m-%d")]
    day_frame["datetime_date"] = datetime_date
    
    return day_frame

def prep_bar_chart_all_days() -> pd.Series:
    '''Preps data for bar chart containing average times for each day.'''
    gold_all_days = daily_gold_days()
    ave_by_day = gold_all_days.groupby("day")["seconds_spent_solving"].mean()
    present_days = list(ave_by_day.index)
    not_present_days = [day for day in index_order if day not in present_days]
    for day in not_present_days:
        ave_by_day.loc[day] = 0

    ave_by_day = pd.Series([ave_by_day[index_order[0]],
                            ave_by_day[index_order[1]],
                            ave_by_day[index_order[2]],
                            ave_by_day[index_order[3]],
                            ave_by_day[index_order[4]],
                            ave_by_day[index_order[5]],
                            ave_by_day[index_order[6]]],
                            index_order)
    return ave_by_day

def prep_box_plot_all_days() -> pd.DataFrame: # Not yet in app
    '''Preps data for boxplot graph with each day's stats.'''
    gold_all_days = daily_gold_days()
    day_vals_list = [gold_all_days[gold_all_days["day"] == "Monday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Tuesday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Wednesday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Thursday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Friday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Saturday"]["seconds_spent_solving"].values,
                     gold_all_days[gold_all_days["day"] == "Sunday"]["seconds_spent_solving"].values]
    return day_vals_list

def prep_mini_hist_box(num_days: int) -> pd.DataFrame:
    '''Preps data for the histogram/boxplot graph.'''
    mini_data = load_mini_data()
    mini_hist_box_data = mini_data[mini_data["day"] != "Saturday"]
    mini_hist_box_data = mini_hist_box_data[-(num_days):]["seconds_spent_solving"].values
    return mini_hist_box_data



def bonus_table() -> pd.DataFrame:
    '''Preps bonus data for table view.'''
    bonus_data = load_bonus_data()
    bonus_data["seconds_spent_solving"] = bonus_data["seconds_spent_solving"].apply(lambda x: f"{round(x//60)}m {round(x%60)}s")
    return bonus_data.sort_values("print_date")

def daily_table() -> pd.DataFrame:
    '''Preps daily data for table view.'''
    gold_all_days = daily_gold_days()
    daily_table_var = gold_all_days
    daily_table_var["seconds_spent_solving"] = daily_table_var["seconds_spent_solving"].apply(lambda x: f"{round(x//60)}m {round(x%60)}s")
    daily_table_var = daily_table_var[["seconds_spent_solving","print_date","day"]]
    return daily_table_var.sort_values("print_date")

def mini_table() -> pd.DataFrame:
    '''Preps mini data for table view.'''
    mini_table_var = load_mini_data()
    mini_table_var = mini_table_var[mini_table_var["solved"] == True]
    mini_table_var["seconds_spent_solving"] = mini_table_var["seconds_spent_solving"].apply(lambda x: f"{round(x//60)}m {round(x%60)}s")
    mini_table_var = mini_table_var[["seconds_spent_solving","print_date","day"]]
    return mini_table_var.sort_values("print_date")
