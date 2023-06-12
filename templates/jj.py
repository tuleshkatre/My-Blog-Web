# import threading
# import time
# exitFlag = 0


# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name, self.counter, 4)
#         print("Exiting " + self.name)


# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#           threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1


# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# # Start new Threads
# thread1.start()
# # thread2.start()
# # thread1.join()
# # thread2.join()
# # print("Exiting Main Thread")

# vi = (1,2,3,4,5,6)
# vi1 = (7,8,9,)
# li = []
# for i in vi :
#     li.append(i)
# print(li)
# print(list(vi))
# print(vi+vi1)






















