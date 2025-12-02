import pandas as pd
import sqlite3

conection = sqlite3.connect("data\sql-murder-mystery.db")
cursor = conection.cursor()

person = pd.read_sql("SELECT * FROM person", conection)
print("person:")
print(person)
print("\n\n")

get_fit_now_member = pd.read_sql("SELECT * FROM get_fit_now_member", conection)
print("get_fit_now_member:")
print(get_fit_now_member)
print("\n\n")

interview = pd.read_sql("SELECT * FROM interview", conection)
print("interview:")
print(interview)
print("\n\n")

get_fit_now_check_in = pd.read_sql("SELECT * FROM get_fit_now_check_in", conection)
print("get_fit_now_check_in:")
print(get_fit_now_check_in)
print("\n\n")

facebook_event_checkin = pd.read_sql("SELECT * FROM facebook_event_checkin", conection)
print("facebook_event_checkin:")
print(facebook_event_checkin)
print("\n\n")

drivers_license= pd.read_sql("SELECT * FROM drivers_license", conection)
print("drivers_license:")
print(drivers_license)
print("\n\n")

crime_scene_report = pd.read_sql("SELECT * FROM crime_scene_report", conection)
print("crime_scene_report:")
print(crime_scene_report)
print("\n\n")

income = pd.read_sql("SELECT * FROM income", conection)
print("income:")
print(income)
print("\n\n")

solution = pd.read_sql("SELECT * FROM solution", conection)
print("solution:")
print(solution)
print("\n\n")

query = '''
SELECT description 
FROM crime_scene_report
WHERE city = 'SQL City' and date = 20180115 and type = 'murder'
'''
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)
