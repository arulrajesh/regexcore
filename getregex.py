import pandas as pd
from typing import List
import os
from os.path import dirname, abspath
from regex_core import regex_core

def generate(insight_query, limit) -> List:
    regex_pattern = list()

    for iq in insight_query:
        # print(row[-1])
        regx = compose(text='''%s''' % (str(iq)), limit=limit)
        # print(regx)
        regex_pattern.append(regx)

    return regex_pattern


def start(tenant):
    df = pd.read_excel(dirname(
        abspath(__file__)) + os.sep + 'data' + os.sep + tenant + '.xlsx')
    # df = df.dropna(axis=0)

    regex_pattern = generate(insight_query=df["UserEntry"], limit=30)

    df['regex'] = regex_pattern

    df.to_excel(dirname(
        abspath(
            __file__)) + os.sep + 'data' + os.sep + 'Regex_rules' + '.xlsx',
                index=False)


if __name__ == '__main__':
    #start('callminer_cats')
    print (regex_core.compose('''"test* exit"''',limit=30))
