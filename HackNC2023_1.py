#!/usr/bin/env python
# coding: utf-8

# # This is the code for each submission of a patient medical error report.
# ## Note: the UI will make each question multiple-choice, however, for the Python code, a short answer is expected, requiring answers to follow example syntax notes (ie. capital letters for start of words, etc) 

# In[ ]:


med_list: list = ["Diagnosis", "Medicine", "Patient Care", "Procedure", "Infection"]
selected_item = input(f"Select which error you would like to focus on in this report {med_list}: ")
print(selected_item)

ur_gency: list = ["Immediate Medical Action Required", "Non-Urgent Medical Action Required", "No Medical Attention Required"]
time_day: list = ["Morning", "Afternoon", "Evening", "Night"]

occurence_med_list = [0] * 5
occurence_urgency = [0] * 3
occurence_time = [0] * 4
occurence_diagnosis = [0] * 2
occurence_medicine = [0] * 3
occurence_patient = [0] * 3
occurence_procedure = [0] * 3
occurence_infection = [0] * 3

for i in range (0, len(med_list)):
    if selected_item == med_list[i]:
        occurence_med_list[i] += 1 

if selected_item == "Diagnosis":
    diagnos: list = ["Incorrect Diagnosis", "Refusal to Give Diagnosis"]
    diagnos_1 = input(f"Which of the following occurred?{diagnos}")
    for i in range (0, len(diagnos)):
        if diagnos_1 == diagnos[i]:
            occurence_diagnosis[i] += 1
    diagnos_2 = input(f"State time of day incidence occurred {time_day}:")
    for i in range (0, len(time_day)):
        if diagnos_2 == time_day[i]:
            occurence_time[i] += 1
    diagnos_3 = input(f"Select the level of urgency {ur_gency}:")
    for i in range (0, len(ur_gency)):
        if diagnos_3 == ur_gency[i]:
            occurence_urgency[i] += 1

if selected_item == "Medicine":
    occur: list = ["Wrong Medication Prescribed" , "Wrong Medication Given", "Wrong Dose Given"]
    occur_1 = input(f"Which of the following occurred?{occur}")
    for i in range (0, len(occur)):
        if occur_1 == occur[i]:
            occurence_medicine[i] += 1
    occur_2 = input(f"State time of day incidence occurred {time_day}:")
    for i in range (0, len(time_day)):
        if occur_2 == time_day[i]:
            occurence_time[i] += 1
    occur_3 = input(f"Select the level of urgency {ur_gency}:")
    for i in range (0, len(ur_gency)):
        if occur_3 == ur_gency[i]:
            occurence_urgency[i] += 1

if selected_item == "Patient Care":
    care: list = ["Lack of Attention to Patient", "Internal Injury", "External Injury" ]
    care_1 = input(f"Which of the following occurred?:{care} ")
    for i in range (0, len(care)):
        if care_1 == care[i]:
            occurence_patient[i] += 1
    care_2 = input(f"State time of day incidence occurred {time_day}:")
    for i in range (0, len(time_day)):
        if care_2 == time_day[i]:
            occurence_time[i] += 1
    care_3 = input(f"Select the level of urgency {ur_gency}:")
    if care_3 == ur_gency[i]:
        occurence_urgency[i] += 1

if selected_item == "Procedure":
    prop: list = ["Inncorrect Sutturing", "No Patient Check-in", "Incorrect Surgical Prodecure"]
    prop_1 = input(f"Which of the following occured?:{prop} ")
    for i in range (0, len(prop)):
        if prop_1 == prop[i]:
            occurence_procedure[i] += 1
    prop_2 = input(f"State time of day incidence occurenced {time_day}:")
    for i in range (0, len(time_day)):
        if prop_2 == time_day[i]:
            occurence_time[i] += 1
    prop_3 = input(f"Select the level of urgency {ur_gency}:")
    if prop_3 == ur_gency[i]:
        occurence_urgency[i] += 1

if selected_item == "Infection":
    infection: list = ["Inncorrect IV setup", "Unsanitary Tools Used", "Internal Infection"]
    infection_1 = input(f"Which of the following occured?:{infection} ")
    for i in range (0, len(infection)):
        if infection_1 == infection[i]:
            occurence_infection[i] += 1
    infection_2 = input(f"State time of day incidence occurenced {time_day}:")
    for i in range (0, len(time_day)):
        if infection_2 == time_day[i]:
            occurence_time[i] += 1
    infection_3 = input(f"Select the level of urgency {ur_gency}:")
    for i in range (0, len(ur_gency)):
        if infection_3 == ur_gency[i]:
            occurence_urgency[i] += 1


# # This is representative of the data analytics/statistics that would be generated based on the submitted patient medical error reports.
# ## Note: using a random built-in function/generator, 5 sample responses were analyzed
# ### 0 means that the choice was NOT selected in the report, 1 means that the choice was selected in the report

# In[ ]:


import numpy as np
import random
possible_numbers = [0, 1]

practice_one = [(random.choices (possible_numbers, k = 5)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 4)), (random.choices (possible_numbers, k = 2)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3))]
practice_two = [(random.choices (possible_numbers, k = 5)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 4)), (random.choices (possible_numbers, k = 2)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3))]
practice_three = [(random.choices (possible_numbers, k = 5)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 4)), (random.choices (possible_numbers, k = 2)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3))]
practice_four = [(random.choices (possible_numbers, k = 5)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 4)), (random.choices (possible_numbers, k = 2)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3))]
practice_five = [(random.choices (possible_numbers, k = 5)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 4)), (random.choices (possible_numbers, k = 2)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3)), (random.choices (possible_numbers, k = 3))]

total_practice = [practice_one, practice_two, practice_three, practice_four, practice_five]

random_occurence_med_list = [0] * 5
random_occurence_urgency = [0] * 3
random_occurence_time = [0] * 4
random_occurence_diagnosis = [0] * 2
random_occurence_medicine = [0] * 3
random_occurence_patient = [0] * 3
random_occurence_procedure = [0] * 3
random_occurence_infection = [0] * 3

med_list: list = ["Diagnosis", "Medicine", "Patient Care", "Procedure", "Infection"]
ur_gency: list = ["Immediate Medical Action Required", "Non-Urgent Medical Action Required", "No Medical Attention Required"]
time_day: list = ["Morning", "Afternoon", "Evening", "Night"]
diagnos: list = ["Incorrect Diagnosis", "Refusal to Give Diagnosis"]
occur: list = ["Wrong Medication Prescribed" , "Wrong Medication Given", "Wrong Dose Given"]
care: list = ["Lack of Attention to Patient", "Internal Injury", "External Injury" ]
prop: list = ["Inncorrect Sutturing", "No Patient Check-in", "Incorrect Surgical Prodecure"]
infection: list = ["Inncorrect IV setup", "Unsanitary Tools Used", "Internal Infection"]

for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_med_list)):
        if total_practice[i][0][j] == 1:
            random_occurence_med_list[j] += 1

for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_urgency)):
        if total_practice[i][1][j] == 1:
            random_occurence_urgency[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_time)):
        if total_practice[i][2][j] == 1:
            random_occurence_time[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_diagnosis)):
        if total_practice[i][3][j] == 1:
            random_occurence_diagnosis[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_medicine)):
        if total_practice[i][4][j] == 1:
            random_occurence_medicine[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_patient)):
        if total_practice[i][5][j] == 1:
            random_occurence_patient[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_procedure)):
        if total_practice[i][6][j] == 1:
            random_occurence_procedure[j] += 1
            
for i in range (0, len(total_practice)):
    for j in range (0, len(random_occurence_infection)):
        if total_practice[i][7][j] == 1:
            random_occurence_infection[j] += 1
        
stats_button = input("To View the Data Analytics Based on Patient Medical Error Reports, Type in 'Statistics'")
if stats_button == "statistics":
    print (f"The type of error with the most occurrences, {np.max(random_occurence_med_list)}, is {med_list[np.argmax(random_occurence_med_list)]} ")
    print (f"The type of urgency with the most occurrences, {np.max(random_occurence_urgency)}, is {ur_gency[np.argmax(random_occurence_urgency)]} ")
    print (f"The time of error with the most occurrences, {np.max(random_occurence_time)}, is {time_day[np.argmax(random_occurence_time)]} ")
    print (f"The type of diagnosis-related error with the most occurrences, {np.max(random_occurence_diagnosis)}, is {diagnos[np.argmax(random_occurence_diagnosis)]} ")
    print (f"The type of medicine-related error with the most occurrences, {np.max(random_occurence_medicine)}, is {occur[np.argmax(random_occurence_medicine)]} ")
    print (f"The type of patient-related error with the most occurrences, {np.max(random_occurence_patient)}, is {care[np.argmax(random_occurence_patient)]} ")
    print (f"The type of procedure-related error with the most occurrences, {np.max(random_occurence_procedure)}, is {prop[np.argmax(random_occurence_procedure)]} ")
    print (f"The type of infection-related error with the most occurrences, {np.max(random_occurence_infection)}, is {infection[np.argmax(random_occurence_infection)]} ")
else:
    print (f"The type of error with the most occurrences, {np.max(random_occurence_med_list)}, is {med_list[np.argmax(random_occurence_med_list)]} ")
    print (f"The type of urgency with the most occurrences, {np.max(random_occurence_urgency)}, is {ur_gency[np.argmax(random_occurence_urgency)]} ")
    print (f"The time of error with the most occurrences, {np.max(random_occurence_time)}, is {time_day[np.argmax(random_occurence_time)]} ")
    print (f"The type of diagnosis-related error with the most occurrences, {np.max(random_occurence_diagnosis)}, is {diagnos[np.argmax(random_occurence_diagnosis)]} ")
    print (f"The type of medicine-related error with the most occurrences, {np.max(random_occurence_medicine)}, is {occur[np.argmax(random_occurence_medicine)]} ")
    print (f"The type of patient-related error with the most occurrences, {np.max(random_occurence_patient)}, is {care[np.argmax(random_occurence_patient)]} ")
    print (f"The type of procedure-related error with the most occurrences, {np.max(random_occurence_procedure)}, is {prop[np.argmax(random_occurence_procedure)]} ")
    print (f"The type of infection-related error with the most occurrences, {np.max(random_occurence_infection)}, is {infection[np.argmax(random_occurence_infection)]} ")

