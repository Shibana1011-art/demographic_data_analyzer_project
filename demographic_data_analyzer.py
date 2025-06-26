

import pandas as pd

def calculate_demographic_data():
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]

    df = pd.read_csv("adult.data", names=column_names, skipinitialspace=True)

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    bachelors_percentage = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[~higher_education]['salary'] == '>50K').mean() * 100, 1)

    min_hours = df['hours-per-week'].min()
    rich_min_workers = df[df['hours-per-week'] == min_hours]
    rich_percentage = round((rich_min_workers['salary'] == '>50K').mean() * 100, 1)

    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_country = country_rich.idxmax()
    highest_country_percentage = round(country_rich.max(), 1)

    india_rich_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'bachelors_percentage': bachelors_percentage,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage': rich_percentage,
        'highest_country': highest_country,
        'highest_country_percentage': highest_country_percentage,
        'top_IN_occupation': india_rich_occupation
    }
