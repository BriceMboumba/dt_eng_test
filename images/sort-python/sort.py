#!/usr/bin/env python
import pandas as pd
import json

# define your own path
paths = ["/home/brice/dt_eng_test/data/people.csv",
         "/home/brice/dt_eng_test/data/places.csv"]


# take the number of born in each city
def mapping(paths):
    df = pd.read_csv(paths[0])
    # Create a list of tuples from the dataframe values
    tuples = list(set([tuple(x) for x in df.to_numpy()]))
    list_of_place_of_birth = []
    print("mapping...")
    for place_of_birth in tuples:
        list_of_place_of_birth.append(place_of_birth[3])

    print("mapping finished...")

    # count occurrence
    counts = dict()
    string = " ".join(list_of_place_of_birth)
    words = string.split(" ")

    print("counting...")
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print("counting finished...")
    return counts


# get city and country value
def listener(paths):
    get_df = pd.read_csv(paths[1])
    df = get_df.drop(['county'], axis=1)
    tuples = list(set([tuple(x) for x in df.to_numpy()]))

    return tuples


# sort and return definitely result
def sorting(map, tuples):
    result = []
    scotland_people = []
    northern_ireland = []
    for element in tuples:
        if element[0] in map:
            result.append((element[1], map.get(element[0])))

    for country in result:
        if country[0] == "Scotland":
            scotland_people.append(country[1])
        else:
            northern_ireland.append(country[1])

    output = {"Scotland": sum(scotland_people), "Northern Ireland": sum(northern_ireland)}

    with open("/home/brice/dt_eng_test/data/summary_output.json", "w") as f:
        json.dump(output, f)


sorting(mapping(paths), listener(paths))
