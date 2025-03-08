from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

def process_life_expectancy(year, region):
    all_region_of_interest = []
    all_year_of_interest = []
    bigData = []
    valid_regions = []

    # Read the CSV file
    with open("life-e.csv") as all_data:
        all_data.readline()
        for line in all_data:
            data = line.split(",")
            valid_regions.append(data[0].strip())

    if region not in valid_regions:
        return {"error": "Invalid region"}

    # Helper function
    def min_max_avg(compound_list):
        lowest, highest = float('inf'), float('-inf')
        lowest_info, highest_info = [], []
        count, total = 0, 0
        for entry in compound_list:
            life_e = float(entry[3].strip())
            count += 1
            total += life_e
            if life_e < lowest:
                lowest, lowest_info = life_e, entry
            if life_e > highest:
                highest, highest_info = life_e, entry
        avg = total / count if count else 0
        return [lowest_info[0], lowest_info[2], lowest_info[3], highest_info[0], highest_info[2], highest_info[3], avg]

    with open("life-e.csv") as all_data:
        all_data.readline()
        for line in all_data:
            data = line.split(",")
            if data[0] == region:
                all_region_of_interest.append(data)
            if int(data[2].strip()) == year:
                all_year_of_interest.append(data)
            bigData.append(data)

    return {
        "overall": min_max_avg(bigData),
        "year": min_max_avg(all_year_of_interest),
        "region": min_max_avg(all_region_of_interest)
    }

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    year = int(request.form["year"])
    region = request.form["region"]
    result = process_life_expectancy(year, region)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
