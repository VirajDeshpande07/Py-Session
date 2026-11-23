#Thread lifcycle:
#New: A thread is created but not yet started. It has been allocated resources but it is not executing.

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



#lock : a lock is a synchronization provided by the threading module that allows only one thread to access q shared resource at a time.
#it prevents race condition and eusures data consistency when multiple threads work on a same data.

# create lock                    acquire()                                                release()
  #lock = threading.lock()       lock aquire()                                           lock.release() other waiting threads
                                #if the lock is free thread aquires it.                  can now aquire the lock.
                                #if the another thread is holding the lock 
                                # thread waits.