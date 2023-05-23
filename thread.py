import threading
import time

# Define a function that will be executed in a separate thread
def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i, "Timestamp:", time.time())
        time.sleep(1)  # Simulate some work being done

# Define another function that will be executed in a separate thread
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("print letter fun Thread 2:", letter, "Timestamp:", time.time())
        time.sleep(1)  # Simulate some work being done

# Create thread objects for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
print()
# # Start the threads
thread1.start()
thread2.start()

# # Wait for the threads to finish before proceeding
thread1.join()
thread2.join()

print("Main thread exiting.")
# 1684496513
print_letters()
print_numbers()