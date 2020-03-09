from FIFO import FIFO
from LRU import min,LRU
from Optimal_algorithm import max,Optimal
# importing the required module
import matplotlib.pyplot as plt

#Reference string
ref_str1 = 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10
ref_str2 = 1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10
ref_str3 = 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1
frameSize = 2
frame_list =[]
page_fault_FIFO = []
page_fault_Opti = []
page_fault_LRU = []
#show page fault case 1
# while frameSize < 11 :
#     print("frameSize : {}".format(frameSize))
#     print("---------------------------")
#     print("Page fault of FIFO :{}".format(FIFO(ref_str1,frameSize)))
#     print("Page fault of Optimal :{}".format(Optimal(ref_str1,frameSize)))
#     print("Page fault of LRU:{}".format(LRU(ref_str1,frameSize)))
#     print("---------------------------")
#     page_fault_FIFO.append(FIFO(ref_str1,frameSize))
#     page_fault_Opti.append(Optimal(ref_str1,frameSize))
#     page_fault_LRU.append(LRU(ref_str1,frameSize))
#     frame_list.append(frameSize)
#     frameSize +=1

#show page fault case 2
# while frameSize < 11 :
#     print("frameSize : {}".format(frameSize))
#     print("---------------------------")
#     print("Page fault of FIFO :{}".format(FIFO(ref_str2,frameSize)))
#     print("Page fault of Optimal :{}".format(Optimal(ref_str2,frameSize)))
#     print("Page fault of LRU:{}".format(LRU(ref_str2,frameSize)))
#     print("---------------------------")
#     page_fault_FIFO.append(FIFO(ref_str2,frameSize))
#     page_fault_Opti.append(Optimal(ref_str2,frameSize))
#     page_fault_LRU.append(LRU(ref_str2,frameSize))
#     frame_list.append(frameSize)
#     frameSize +=1

#show page fault case 3
while frameSize < 7 :
    print("frameSize : {}".format(frameSize))
    print("---------------------------")
    print("Page fault of FIFO :{}".format(FIFO(ref_str3,frameSize)))
    print("Page fault of Optimal :{}".format(Optimal(ref_str3,frameSize)))
    print("Page fault of LRU:{}".format(LRU(ref_str3,frameSize)))
    print("---------------------------")
    page_fault_FIFO.append(FIFO(ref_str3,frameSize))
    page_fault_Opti.append(Optimal(ref_str3,frameSize))
    page_fault_LRU.append(LRU(ref_str3,frameSize))
    frame_list.append(frameSize)
    frameSize +=1

# #plot graph
#FIFO graph
plt.plot(frame_list,page_fault_FIFO)
# naming the x axis
plt.xlabel('#frame')
# naming the y axis
plt.ylabel('#page_fault')

# giving a title to my graph
plt.title('FIFO graph!')

# function to show the plot
plt.show()

#Optimal graph
plt.plot(frame_list,page_fault_Opti)
# naming the x axis
plt.xlabel('#frame')
# naming the y axis
plt.ylabel('#page_fault')

# giving a title to my graph
plt.title('Optimal graph!')

# function to show the plot
plt.show()

#LRU graph
plt.plot(frame_list,page_fault_LRU)
# naming the x axis
plt.xlabel('#frame')
# naming the y axis
plt.ylabel('#page_fault')

# giving a title to my graph
plt.title('LRU graph!')

# function to show the plot
plt.show()
