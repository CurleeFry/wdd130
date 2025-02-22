all_region_of_interest = []
all_year_of_interest = []
bigData = []
valid_regions = []

with open("life-expectancy.csv") as all_data:
    all_data.readline()
    for line in all_data:
        data = line.split(",")
        region = data[0].strip()
        if region not in valid_regions:
            valid_regions.append(region)

interest = int(input("Enter the year of interest: "))
while 1542 > interest or interest > 2020:
    interest = int(input("Sorry, that entry is not within the data. Please enter the year of interest: "))

regionOfInterest = input("Please enter the country/region of interest: ").title()
while regionOfInterest not in valid_regions:
    regionOfInterest = input("Sorry, that entry is not within the data. Please enter the country/region of interest: ").title()


def min_max_avg(compound_list):
    lowest = 9999
    lowest_info = []
    highest = 0
    highest_info = []
    count = 0
    sum = 0
    avg = 0
    for list in compound_list:
        life_e = float(list[3].strip())
        count += 1
        sum += life_e
        if life_e < lowest:
            lowest = life_e
            lowest_info = list
        if life_e > highest:
            highest = life_e
            highest_info = list
        avg = sum / count

    returns =  [lowest_info[0], lowest_info[2], lowest_info[3], highest_info[0], highest_info[2], highest_info[3], avg]
    return returns


with open("life-expectancy.csv") as all_data:
    all_data.readline()
    for line in all_data:
        data = line.split(",")
        region = data[0]
        year = int(data[2].strip())
        life_e = float(data[3].strip())
        if region == regionOfInterest.title():
            all_region_of_interest.append(data)
        if year == interest:
            all_year_of_interest.append(data)
        bigData.append(data)


everything = min_max_avg(bigData)
year_returns = min_max_avg(all_year_of_interest)
region_returns = min_max_avg(all_region_of_interest)


print(f"\nThe overall max life expectancy is:{float(everything[5]): .2f} from {everything[3]} in {everything[4]}.\
        \nThe overall min life expectancy is:{float(everything[2]): .2f} from {everything[0]} in {everything[1]}.\n")

print(f"In {interest}, the max life expectancy was:{float(year_returns[5]): .2f} from {year_returns[3]}.\
        \nThe min life expectancy was:{float(year_returns[2]): .2f} from {year_returns[0]}. The average lifespan was {float(year_returns[6]): .2f} years.\n")

print(f"In {regionOfInterest}, the max life expectancy was: {float(region_returns[5]): .2f} in {region_returns[4]}.\
        \nThe min life expectancy was:{float(region_returns[2]): .2f} in {region_returns[1]}. The average lifespan for this place is{float(region_returns[6]): .2f} years.")