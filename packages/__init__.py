import xlwings as xw
import pandas as pd
import openpyxl
from flask import Flask, render_template
from flask_login import  login_required, current_user
from datetime import datetime

def reset_parts_count():
    # Get the current date and time
    now = datetime.datetime.now()
    wb = xw.Book("Excel/HBH.xlsm")
    for sheet_name in ["474", "471", "424", "429","458"]:
        sheet = wb.sheets[sheet_name]
        sheet.range("B2:Y8").value = 0
        
        # Save and close the workbook
        wb.save()
       

def l474_df():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    file_path = "Excel/HBH.xlsm"
    parts_df = pd.read_excel(file_path, usecols="A:Y", nrows=8, engine='openpyxl')
    starved_474df = pd.read_excel(file_path, sheet_name="474StarvedBlocked", usecols="M:N", nrows=9, engine='openpyxl')
    blocked_474df = pd.read_excel(file_path, sheet_name="474StarvedBlocked", usecols="M:N", nrows=9, skiprows=10, engine='openpyxl')

    # Calculate row totals and add to dataframe
    parts_df['Part Totals'] = parts_df.select_dtypes(include='number').sum(axis=1)
    starved_columns = starved_474df.columns.tolist()
    blocked_columns = blocked_474df.columns.tolist()

    # Calculate column totals and add to dataframe
    col_total = parts_df.select_dtypes(include='number').sum(axis=0, min_count=1).tolist()
    col_total_labels = parts_df.columns.tolist()
    starved_row_total = starved_474df.select_dtypes(include='number').sum(axis=0).tolist()
    blocked_row_totals = blocked_474df.select_dtypes(include='number').sum(axis=0).tolist()
    
    # Calculate weekday totals and add to list
    weekday_total = parts_df.groupby(['Week Day']).sum().sum(axis=1).tolist()

    # Convert dataframe into a dictionary
    data = parts_df.to_dict('records')

    # Create a list of weekday-part pairs for the table in the HTML template
    weekday_parts = [(weekday, parts_df.loc[parts_df['Week Day'] == weekday, 'Part Totals'].tolist()[0]) for weekday in parts_df['Week Day'].unique()]
    weekday_starved = [(weekdays, starved_474df.loc[starved_474df['Week Day'] == weekdays, 'Total'].tolist()[0]) for weekdays in starved_474df['Week Day'].unique()]
    weekday_blocked = [(weekdayb, blocked_474df.loc[blocked_474df['Week Day'] == weekdayb, 'Total'].tolist()[0]) for weekdayb in blocked_474df['Week Day'].unique()]
    intialize = render_template('474.html',
        weekday_parts=weekday_parts, data=data, col_total=col_total, 
        col_total_labels=col_total_labels, weekday_total=weekday_total, starved_df=starved_474df, starved_columns=starved_columns,
        starved_row_total=starved_row_total, weekday_starved=weekday_starved,weekday_blocked=weekday_blocked, blocked_row_totals=blocked_row_totals,
        blocked_columns=blocked_columns,user=current_user
    )
    return intialize

import warnings

def l471_df():
    # ignore FutureWarnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

    file_path = "Excel/HBH.xlsm"
    parts_df = pd.read_excel(file_path, usecols="A:Y", nrows=8, engine='openpyxl', sheet_name="471")
    starved_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, engine='openpyxl')
    blocked_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, skiprows=10, engine='openpyxl')

    # Calculate row totals and add to dataframe
    parts_df['Part Totals'] = parts_df.iloc[:, :25].sum(axis=1, numeric_only=True)

    # Calculate column totals and add to dataframe
    col_total = parts_df.iloc[:, :25].sum(axis=0, numeric_only=True).tolist()
    col_total_labels = parts_df.columns.tolist()
    starved_row_total = starved_471df.sum(axis=0, numeric_only=True).tolist()
    blocked_row_totals = blocked_471df.sum(axis=0, numeric_only=True).tolist()

    # Calculate weekday totals and add to list
    weekday_total = parts_df.groupby(['Week Day'])['Part Totals'].sum(numeric_only=True).tolist()

    # Convert dataframe into a dictionary
    data = parts_df.to_dict('records')

    # Create a list of weekday-part pairs for the table in the HTML template
    weekday_parts = [(weekday, parts_df.loc[parts_df['Week Day'] == weekday, 'Part Totals'].tolist()[0]) for weekday in parts_df['Week Day'].unique()]
    weekday_starved = [(weekdays, starved_471df.loc[starved_471df['Week Day'] == weekdays, 'Total'].tolist()[0]) for weekdays in starved_471df['Week Day'].unique()]
    weekday_blocked = [(weekdayb, blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()[0]) for weekdayb in blocked_471df['Week Day'].unique() 
                       if len(blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()) > 0]

    # Pass data to template
    intialize = render_template('471.html',
        weekday_parts=weekday_parts, data=data, col_total=col_total, 
        col_total_labels=col_total_labels, weekday_total=weekday_total, starved_df=starved_471df, starved_columns=starved_471df.columns.tolist(),
        starved_row_total=starved_row_total, weekday_starved=weekday_starved, weekday_blocked=weekday_blocked, blocked_row_totals=blocked_row_totals,
        blocked_columns=blocked_471df.columns.tolist(), user=current_user
    )
    return intialize



def l424_df():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    file_path = "Excel/HBH.xlsm"
    parts_df = pd.read_excel(file_path, usecols="A:Y", nrows=8, engine='openpyxl', sheet_name="424")
    starved_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, engine='openpyxl')
    blocked_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, skiprows=10, engine='openpyxl')


    # Calculate row totals and add to dataframe
    parts_df['Part Totals'] = parts_df.sum(axis=1)
    starved_columns = starved_471df.columns.tolist()
    blocked_columns = blocked_471df.columns.tolist()


    # Calculate column totals and add to dataframe
    col_total = parts_df.sum(axis=0, min_count=1).tolist()
    col_total_labels = parts_df.columns.tolist()
    starved_row_total = starved_471df.sum(0).tolist()
    blocked_row_totals = blocked_471df.sum(0).tolist()
    
    
    # Calculate weekday totals and add to list
    weekday_total = parts_df.groupby(['Week Day']).sum().sum(axis=1).tolist()

    # Convert dataframe into a dictionary
    data = parts_df.to_dict('records')

    # Create a list of weekday-part pairs for the table in the HTML template
    weekday_parts = [(weekday, parts_df.loc[parts_df['Week Day'] == weekday, 'Part Totals'].tolist()[0]) for weekday in parts_df['Week Day'].unique()]
    weekday_starved = [(weekdays, starved_471df.loc[starved_471df['Week Day'] == weekdays, 'Total'].tolist()[0]) for weekdays in starved_471df['Week Day'].unique()]
    weekday_blocked = [(weekdayb, blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()[0]) for weekdayb in blocked_471df['Week Day'].unique() 
                       if len(blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()) > 0]

    # Pass data to template
    intialize = render_template('424.html',
        weekday_parts=weekday_parts, data=data, col_total=col_total, 
        col_total_labels=col_total_labels, weekday_total=weekday_total, starved_df=starved_471df, starved_columns=starved_columns,
        starved_row_total=starved_row_total, weekday_starved=weekday_starved,weekday_blocked=weekday_blocked, blocked_row_totals=blocked_row_totals,
        blocked_columns=blocked_columns,user=current_user
    )
    return intialize


def l429_df():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    file_path = "Excel/HBH.xlsm"
    parts_df = pd.read_excel(file_path, usecols="A:Y", nrows=8, engine='openpyxl', sheet_name="429")
    starved_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, engine='openpyxl')
    blocked_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, skiprows=10, engine='openpyxl')


    # Calculate row totals and add to dataframe
    parts_df['Part Totals'] = parts_df.sum(axis=1)
    starved_columns = starved_471df.columns.tolist()
    blocked_columns = blocked_471df.columns.tolist()


    # Calculate column totals and add to dataframe
    col_total = parts_df.sum(axis=0, min_count=1).tolist()
    col_total_labels = parts_df.columns.tolist()
    starved_row_total = starved_471df.sum(0).tolist()
    blocked_row_totals = blocked_471df.sum(0).tolist()
    
    
    # Calculate weekday totals and add to list
    weekday_total = parts_df.groupby(['Week Day']).sum().sum(axis=1).tolist()

    # Convert dataframe into a dictionary
    data = parts_df.to_dict('records')

    # Create a list of weekday-part pairs for the table in the HTML template
    weekday_parts = [(weekday, parts_df.loc[parts_df['Week Day'] == weekday, 'Part Totals'].tolist()[0]) for weekday in parts_df['Week Day'].unique()]
    weekday_starved = [(weekdays, starved_471df.loc[starved_471df['Week Day'] == weekdays, 'Total'].tolist()[0]) for weekdays in starved_471df['Week Day'].unique()]
    weekday_blocked = [(weekdayb, blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()[0]) for weekdayb in blocked_471df['Week Day'].unique() 
                       if len(blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()) > 0]

    # Pass data to template
    intialize = render_template('429.html',
        weekday_parts=weekday_parts, data=data, col_total=col_total, 
        col_total_labels=col_total_labels, weekday_total=weekday_total, starved_df=starved_471df, starved_columns=starved_columns,
        starved_row_total=starved_row_total, weekday_starved=weekday_starved,weekday_blocked=weekday_blocked, blocked_row_totals=blocked_row_totals,
        blocked_columns=blocked_columns,user=current_user
    )
    return intialize


def l458_df():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    file_path = "Excel/HBH.xlsm"
    parts_df = pd.read_excel(file_path, usecols="A:Y", nrows=8, engine='openpyxl', sheet_name="458")
    starved_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, engine='openpyxl')
    blocked_471df = pd.read_excel(file_path, sheet_name="471StarvedBlocked", usecols="M:N", nrows=9, skiprows=10, engine='openpyxl')


    # Calculate row totals and add to dataframe
    parts_df['Part Totals'] = parts_df.sum(axis=1)
    starved_columns = starved_471df.columns.tolist()
    blocked_columns = blocked_471df.columns.tolist()


    # Calculate column totals and add to dataframe
    col_total = parts_df.sum(axis=0, min_count=1).tolist()
    col_total_labels = parts_df.columns.tolist()
    starved_row_total = starved_471df.sum(0).tolist()
    blocked_row_totals = blocked_471df.sum(0).tolist()
    
    
    # Calculate weekday totals and add to list
    weekday_total = parts_df.groupby(['Week Day']).sum().sum(axis=1).tolist()

    # Convert dataframe into a dictionary
    data = parts_df.to_dict('records')

    # Create a list of weekday-part pairs for the table in the HTML template
    weekday_parts = [(weekday, parts_df.loc[parts_df['Week Day'] == weekday, 'Part Totals'].tolist()[0]) for weekday in parts_df['Week Day'].unique()]
    weekday_starved = [(weekdays, starved_471df.loc[starved_471df['Week Day'] == weekdays, 'Total'].tolist()[0]) for weekdays in starved_471df['Week Day'].unique()]
    weekday_blocked = [(weekdayb, blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()[0]) for weekdayb in blocked_471df['Week Day'].unique() 
                       if len(blocked_471df.loc[blocked_471df['Week Day'] == weekdayb, 'Total'].tolist()) > 0]

    # Pass data to template
    intialize = render_template('458.html',
        weekday_parts=weekday_parts, data=data, col_total=col_total, 
        col_total_labels=col_total_labels, weekday_total=weekday_total, starved_df=starved_471df, starved_columns=starved_columns,
        starved_row_total=starved_row_total, weekday_starved=weekday_starved,weekday_blocked=weekday_blocked, blocked_row_totals=blocked_row_totals,
        blocked_columns=blocked_columns,user=current_user
    )
    return intialize


