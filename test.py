
import requests
import json

# specify the url
url = 'http://localhost:8000/api/'

# create your list of dictionary data to be sent
data_list = [
    {"text": "75 mg/m2 by IV infusion or subcutaneous dosing rituximab"},
    {"text": "In visit 2, scheduled for week 4, participants will be administered a dose of 500mg of the experimental drug, Tricetinib, orally once daily for the subsequent 8 weeks until the next evaluation at visit 3."},
    {"text": "For visit 5, the dose of 200mg of Amlocid should be given intravenously every 2 weeks."},
    {"text": "During the sixth visit at week 12, participants are to receive a 10mg/kg dose of Sintacta administered subcutaneously, once every 4 weeks for the next 16 weeks."},
    {"text": "Participants will receive an initial dose of 400mg of Qulintab orally at the first visit, followed by 200mg twice daily in the subsequent visits."},
    {"text": "A single intravenous dose of 30 mg/kg Remdisivo will be administered on visit 3, followed by an evaluation on visit 4."},
    {"text": "Patients will take a daily 20mg oral dose of Zolorex starting from visit 1 for 4 weeks until visit 2."},
    {"text": "In visit 4, the participants will receive 5mg of Minacta intravenously over a period of one hour."},
    {"text": "Visit 5 will include the administration of 600mg of Bilinta, taken orally once every 12 hours."}
]


data_list = [
    {"text": "6 time each week injection with rituximab at 75 mg/m2"}
]

for data in data_list:
    # send a post request
    response = requests.post(url, json=data)

    # print the response
    print(response.json())
