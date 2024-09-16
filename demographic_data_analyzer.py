import pandas as pd

# race_count:
# get all the race labels/indices
# count for each
# insert count for each to race indices
# done.

# avr_age_men:
# get all the ages of men (How? get indices that are male through boolean values, filter age column through those values)
# get average
# done.

# percentage_bachelors
# get number of people
# get number of people with bachelors
# calculate percentage
# round percentage to the nearest tenth
#

# highest_earning_country_percentage
# get the number of rich people for each country
# take the max of that number and retrieve the country associated with it.
# output that country
#

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # DF breakdown:
    bachelors = df.loc[df['education']=='Bachelors']
    masters = df.loc[df['education']=='Masters']
    doctorate = df.loc[df['education']=='Doctorate']
    hi_educ = df[(df['education']=='Bachelors') & (df['education']=='Masters') & (df['education']=='Doctorate')]
    lo_educ = df[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]

    bachelors_rich = bachelors[bachelors['salary']=='>50K']
    masters_rich = masters[masters['salary']=='>50K']
    doctorate_rich = doctorate[doctorate['salary']=='>50K']
    lo_educ_rich = lo_educ[lo_educ['salary']=='>50K']

    one_hour_people = df[df['hours-per-week']==1]
    one_hour_50Kplus_people = one_hour_people[one_hour_people['salary']=='>50K']

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex']=='Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100*len(bachelors)/len(df), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # percentage with salary > 50K
    higher_education_rich = round(100*(len(bachelors_rich)+len(masters_rich)+len(doctorate_rich)) / (len(bachelors)+len(masters)+len(doctorate)), 1)
    lower_education_rich = round(100*len(lo_educ_rich)/len(lo_educ), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # num_min_workers = None
    rich_percentage = round(100*len(one_hour_50Kplus_people)/len(one_hour_people), 1)

    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df['salary']=='>50K']
    countries = df['native-country'].unique()
    rich_people_per_country = dict()
    for country in countries:
        rich_people_per_country[country] = [len(rich_people[rich_people['native-country']==country]), len(df[df['native-country']==country])]

    highest_earning_country = None
    greatest_percentage = float('-inf')
    for country, values in rich_people_per_country.items():
        curr_percentage = values[0]/values[1] 
        if highest_earning_country == None:
            greatest_percentage = curr_percentage
            highest_earning_country = country
        elif curr_percentage > greatest_percentage:
            greatest_percentage = curr_percentage
            highest_earning_country = country

    highest_earning_country_percentage = round(100*rich_people_per_country[highest_earning_country][0]/rich_people_per_country[highest_earning_country][1], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indians = df[df['native-country']=='India']
    rich_indians = indians[indians['salary']=='>50K']
    rich_indian_occupations = rich_indians['occupation'].unique()
    rich_indian_per_occupation = dict()

    for occ in rich_indian_occupations:
        rich_indian_per_occupation[occ] = len(rich_indians[rich_indians['occupation']==occ])

    top_IN_occupation = None 
    greatest_n_people = float('-inf')
    for occ, n_people in rich_indian_per_occupation.items():
        curr_n_people = n_people
        if top_IN_occupation == None:
            greatest_n_people = curr_n_people
            top_IN_occupation = occ
        elif curr_n_people > greatest_n_people:
            greatest_n_people = curr_n_people
            top_IN_occupation = occ

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# temp
# calculate_demographic_data(print_data=True)