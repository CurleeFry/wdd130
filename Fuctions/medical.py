lowest = 9999
lowest_info = []
highest = 0
highest_info = []
count = 0
sum = 0
lowest_i = 9999
lowest_info_i = []
highest_i = 0
highest_info_i = []
lowest_r = 9999
lowest_info_r = []
highest_r = 0
highest_info_r = []
sum_r = 0

with open("life-expectancy.csv") as all_data:
    all_data.readline()
    interest = int(input("Enter the year of interest: "))
    regionOfInterest = input("please enter the country/ region of interest: ")
    while 1542 > interest or interest > 2020:
        interest = int(input("Sorry, your entry is not within the data. Enter the year of interest: "))
    for line in all_data:
        data = line.split(",")
        region = data[0]
        year = int(data[2].strip())
        life_e = float(data[3].strip())
        if life_e < lowest:
            lowest = life_e
            lowest_info = data
        if life_e > highest:
            highest = life_e
            highest_info = data
        if year == interest:
            count +=1
            sum += life_e
            avg = sum / count
            if life_e < lowest_i:
                lowest_i = life_e
                lowest_info_i = data
            if life_e > highest_i:
                highest_i = life_e
                highest_info_i = data
        # if region == regionOfInterest.title():
        #     count +=1
        #     sum_r += life_e
        #     avg_r = sum / count
        #     if life_e < lowest_r:
        #         lowest_r = life_e
        #         lowest_info_r = data
        #     if life_e > highest_r:
        #         highest_r = life_e
        #         highest_info_r = data


print(f"The overall max life expectancy is: {highest_info[3].strip()} from {highest_info[0]} in 2019\nThe overall min life expectancy is: {lowest_info[3].strip()} from {lowest_info[0]} in 1882")
print(f"\nFor the year {interest}:\nThe average life expectancy across all countries was{avg: .2f}\nThe max life expectancy was in {highest_info_i[0]} with {highest_info_i[3].strip()}\nThe max life expectancy was in {lowest_info_i[0]} with {lowest_info_i[3].strip()}")
# print(f"{lowest_info_r} {highest_info_r} {avg_r}")