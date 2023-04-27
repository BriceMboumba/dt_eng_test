#!/usr/bin/env python
import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    user='user_dteng', password='cirilgroupt', host='localhost', port="3306", database='db_dteng')

# define your own path
paths = ["/home/brice/dt_eng_test/data/people.csv",
         "/home/brice/dt_eng_test/data/places.csv"]


def reader_csv_file(paths: list):
    for index, path in enumerate(paths):
        try:
            if index == 0:
                # enter to the first file (people)
                df = pd.read_csv(path)
                # Create a list of tuples from the dataframe values
                tuples = list(set([tuple(x) for x in df.to_numpy()]))
                # SQL query to execute
                if connection and tuples:
                    print("DB connected")
                    cursor = connection.cursor()
                    for i in range(1, len(tuples) + 1):
                        query = """ INSERT INTO people(id, given_name, family_name, date_of_birth, place_of_birth) VALUES (%s, %s, %s, %s, %s) """
                        cursor.execute(query, (i,) + tuples[i])
                        print("progressing: {}/{}".format(i, len(tuples)))
                        connection.commit()
            else:
                # enter to the second file (places)
                df = pd.read_csv(path)
                # Create a list of tuples from the dataframe values
                tuples = list(set([tuple(x) for x in df.to_numpy()]))
                # SQL query to execute
                if connection and tuples:
                    print("DB connected")
                    cursor = connection.cursor()
                    for i in range(1, len(tuples) + 1):
                        query = """ INSERT INTO places(id, city, county, country) VALUES (%s, %s, %s, %s) """
                        cursor.execute(query, (i,) + tuples[i])
                        print("progressing: {}/{}".format(i, len(tuples)))
                        connection.commit()
        except IndexError:
            pass


reader_csv_file(paths)
