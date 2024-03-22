# შექმენით რამდენიმე json ფაილი, დაწერეთ მოცემული json ფაილების პარსინგი რომელიც ფაილის სახელთან ერთად დაბეჭდავს json-ში არსებულ მონაცემებს და თითოეული ფაილისთვის გაუშვით ცალცალკე ნაკადი(thread)

import threading
import json


def handling_json(file_path):
    
    with open(file_path, "r") as file:
        json_data = json.load(file)

        for data in json_data:
            print(f"{file_path}, Name: {data['name']}, Age: {data['age']}\n")

json_file_paths = ["json1.json", "json2.json"]

threads = []

for file in json_file_paths:
    thread = threading.Thread(target = handling_json, args=(file,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Task is done.")