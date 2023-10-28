med_list: list = ["Diagnosis", "Medicine", "Patient Care", "Procedure", "Infection"]
selected_item = input(f"Pick which error you want to focus on {med_list}: ")
print(selected_item)

ur_gency: list = ["Immediate medical action required", "Non-urgent medical action required", "No medical attention required"]
time_day: list = ["Morning", "Afternoon", "Evening", "Night"]

if selected_item == "Diagnosis":
    diagnos: list = ["Incorrect Diagnosis", "Refusal to give diagnosis"]
    input(f"Which of the following occured?{diagnos}")
    input(f"State time of day of incidence occurence {time_day}:")
    input(f"Pick the urgency level {ur_gency}:")

if selected_item == "Medicine":
    occur: list = ["Wrong medication given", "Wrong dose given"]
    input(f"Which of the following occured?{occur}")
    input(f"State time of day of incidence{time_day}:")
    input(f"Pick the urgency level {ur_gency}:")

if selected_item == "Patient Care":
    care: list = ["Lack of attention to patient", "Injury" ]
    input(f"Which of the following occured?:{care} ")
    input(f"State time of day of incidence {time_day}:")
    input(f"Pick the urgency level {ur_gency}:")

if selected_item == "Procedure": 
    prop: list = ["Incorrect suturing", "No patient check-in", "Incorrect surgical prodecure done"]
    input(f"Which of the following occured?:{prop} ")
    input(f"State time of day incidence occurenced {time_day}:")
    input(f"Pick the urgency level {ur_gency}:")

if selected_item == "Infection":
    fection: list = ["Incorrect IV setup", "Unsanitary tools used"]
    input(f"Which of the following occured?:{fection} ")
    input(f"State time of day incidence occurenced {time_day}:")
    input(f"Pick the urgency level {ur_gency}:")





