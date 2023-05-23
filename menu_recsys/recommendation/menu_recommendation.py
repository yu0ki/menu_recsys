import pandas as pd
from itertools import combinations


def recommending(menus: pd.DataFrame, max_number=5, max_price=500, gender=0, momentum=2) -> list:
    results = list()
    for number in range(1, max_number + 1):
        temp_results = combinations(range(len(menus)), number)
        for temp_result in temp_results:
            results.append(list(temp_result))
    rec_menu = list()
    for result in results:  # result is a list of rows' ids
        result_price = menus.iloc[result, 1].sum()
        result_protein = menus.iloc[result, 2].sum()
        result_carbohydrates = menus.iloc[result, 3].sum()
        result_veg = menus.iloc[result, 4].sum()
        if result_price > int(max_price):
            continue
        if result_veg < 125:
            continue
        if gender == 1 or gender == 3:
            if momentum == 1:
                if result_protein < 10 or result_protein > 25:
                    continue
                if result_carbohydrates < 50 or result_carbohydrates > 100:
                    continue
            if momentum == 2:
                if result_protein < 15 or result_protein > 30:
                    continue
                if result_carbohydrates < 75 or result_carbohydrates > 125:
                    continue
            if momentum == 3:
                if result_protein < 20 or result_protein > 35:
                    continue
                if result_carbohydrates < 100 or result_carbohydrates > 150:
                    continue
        elif gender == 2:
            if momentum == 1:
                if result_protein < 5 or result_protein > 20:
                    continue
                if result_carbohydrates < 25 or result_carbohydrates > 75:
                    continue
            if momentum == 2:
                if result_protein < 10 or result_protein > 25:
                    continue
                if result_carbohydrates < 50 or result_carbohydrates > 100:
                    continue
            if momentum == 3:
                if result_protein < 15 or result_protein > 30:
                    continue
                if result_carbohydrates < 75 or result_carbohydrates > 125:
                    continue
        rec_menu.append((menus.iloc[result, 0].tolist(), result_price))
    if len(rec_menu) > 1:
        rec_menu = sorted(rec_menu, key=lambda x: (x[1], x[0]), reverse=True)
    rec_menu = [x[0] for x in rec_menu]
    for i in rec_menu:
        print(i)
    return rec_menu
