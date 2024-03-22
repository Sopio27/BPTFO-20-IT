
# დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეცემა რიცხვებისგან შემდგარი Queue, ფუნქციამ უნდა დაბეჭდოს ნაკადის სახელი, რიგიდან ამოღებული მნიშვნელობა და არის თუ არა ეს რიცხვი ლუწი. გაუშვით სამი ნაკადი(thread) და მხოლოდ ამის შემდეგ შეავსეთ რიგი(queue). საბოლოოდ დააჯოინეთ და დაბეჭდეთ რომ ყველა ამოცანა შესრულებულია.

import queue
import threading

q_tasks = queue.Queue()
n_tasks = 3
n_threads = n_tasks
threads = []

def worker(q):

    while True:
        #Thread id
        print(f"Thread identification: {threading.current_thread()}\n")
        
        #Current value from queue
        item = q.get()

        if item is None:
            break

        print(f"Value: {item}\n")

        #Is even or odd
        if item%2 == 1:
            print("Current value is odd\n")
        else:
            print('Current value is even.\n')

        #End of task
        q.task_done()

for i in range(n_threads):
    thread = threading.Thread(target=worker, args=(q_tasks,) )
    thread.start()
    threads.append(thread)

for i in range(n_tasks):
    q_tasks.put(i)

for i in range(n_tasks):
    q_tasks.put(None)

for thread in threads:
    thread.join()
 
print("All tasks have been completed.")

