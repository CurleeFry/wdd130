# import requests

# # Replace with your actual access token
# ACCESS_TOKEN = ""
# API_URL = 'https://byui.instructure.com/api/v1/'

# # Set up the headers with the access token
# headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

# # Get the list of courses
# courses_response = requests.get(f'{API_URL}courses', headers=headers)

# if courses_response.status_code == 200:
#     courses = courses_response.json()
#     print("\nYour Grades:")

#     for course in courses:
#         course_id = course.get('id')
#         course_name = course.get('name')

#         # Get the grades for the course
#         grades_response = requests.get(f'{API_URL}courses/{course_id}/enrollments', headers=headers)

#         if grades_response.status_code == 200:
#             enrollments = grades_response.json()

#             for enrollment in enrollments:
#                 if enrollment.get('type') == 'StudentEnrollment':
#                     grades = enrollment.get('grades', {})
#                     current_score = grades.get('current_score')
#                     final_score = grades.get('final_score')

#                     print(f"\nCourse: {course_name}")
#                     print(f"  - Current Score: {current_score if current_score is not None else 'N/A'}")
#                     print(f"  - Final Score: {final_score if final_score is not None else 'N/A'}")

#         else:
#             print(f"\nFailed to retrieve grades for {course_name} (Error {grades_response.status_code})")

# else:
#     print("Failed to retrieve courses (Error", courses_response.status_code, ")")

import requests

# Replace with your actual access token
ACCESS_TOKEN = 
API_URL = 'https://byui.instructure.com/api/v1/'

# Set up headers
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

# Get the list of all courses (including completed ones)
courses_response = requests.get(f'{API_URL}courses?state[]=completed&state[]=available', headers=headers)

# Initialize a list to store course grades
grades_list = []

if courses_response.status_code == 200:
    courses = courses_response.json()
    unique_courses = {}  # Dictionary to track unique courses

    for course in courses:
        course_id = course.get('id')
        course_name = course.get('name')

        # Avoid duplicate course entries
        if course_id not in unique_courses:
            unique_courses[course_id] = course_name

            # Get the grades for this course
            grades_response = requests.get(f'{API_URL}courses/{course_id}/enrollments', headers=headers)

            if grades_response.status_code == 200:
                enrollments = grades_response.json()

                for enrollment in enrollments:
                    if enrollment.get('type') == 'StudentEnrollment':
                        grades = enrollment.get('grades', {})
                        current_score = grades.get('current_score')
                        final_score = grades.get('final_score')

                        # Only store if at least one score exists
                        if current_score is not None or final_score is not None:
                            grades_list.append((course_name, current_score, final_score))

# Print the final list if it contains any data
if grades_list:
    print("\nGrades List:")
    for course, current, final in grades_list:
        print(f"{course} - Current Score: {current if current is not None else 'N/A'}, Final Score: {final if final is not None else 'N/A'}")
else:
    print("\nNo grades found.")
