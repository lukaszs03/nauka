import requests
import json 

r = requests.get("https://jsonplaceholder.typicode.com/todos")
a = requests.get("https://jsonplaceholder.typicode.com/users")

def count_task_frequency(tasks): 
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1

    return completedTasksFrequencyByUser

def users_with_top_completed_tasks(completedTasksFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTasks = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTasksFrequencyByUser.items():
        if numberOfCompletedTask == maxAmountOfCompletedTasks:
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks

def naming_users(usersWithTopCompletedTasks):
    for user in users: 
        if(user["id"] in usersWithTopCompletedTasks):
            print("The cookie award is going to users:", user["name"])
    return usersWithTopCompletedTasks

try:
    tasks = r.json()
    users = a.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = users_with_top_completed_tasks(completedTasksFrequencyByUser)
    naming_users(usersWithTopCompletedTasks)
    #print("The cookie award is going to users with ID:", users_with_top_completed_tasks)