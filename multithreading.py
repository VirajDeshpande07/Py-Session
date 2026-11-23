from threading import Thread
def task():
    print("Thread is running")

#create thread
t = Thread(target = task)

#start.thread
t.start()

#waiting for completion
t.join()

print("Main program ends.")