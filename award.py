import requests
import json 

r = requests.get("https://jsonplaceholder.typicode.com/todos")

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

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    users_with_top_completed_tasks = users_with_top_completed_tasks(completedTasksFrequencyByUser)
    print("The cookie award is going to users with ID:", users_with_top_completed_tasks)