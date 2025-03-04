#  GOAL:
#     Help make labor costs more accurate and useful for management usage.
    
#  Inputs : 
#     Cafe labor files (currently unknown what type) that are updated near constantly

#  Desired outputs :
#     Labor split by morning, afternoon, and evening
#     Potentially have a weekly tracker that will combine the last weeks morning, afternoon, and evening (respectively) labor %
#     Potentially pass the data to excel to graph 
#     powerVI
#     Potentially predict labor and data for the current day (possibly to the hour)

#  Functions:
#     Scrape data from the input source and make it usable data
#     Sort data based on its relevancy (by morning afternoon and evening)
#     Potentially store old data a week out 
#     (Refresh/loop) the (data/program) to keep data relevant and also show active data
#     Pass data and information to a easily readable/understandable format

#For my work, I'm writing a python function that will 1. scrape labor cost data from the company's site, 2. potentially store up to a week's worth of data, 3. sort that data by relevancy (morning, afternoon, and evening labor percentages), and 4. refresh the 