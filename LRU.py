def minDesitance(dictBackward,frameSize):
    temp = 999
    index =0
    for i in range(frameSize):
        if temp>dictBackward[i]:
            temp = dictBackward[i]
            index = i
    return index

def LRU(str,frameSize):
    keep_list = []
    checkHit = FALSE
    pagefault_count=0
    index = 0
    for i in range(len(str)):
        if(len(keep_list)>0):
            for j in range(len(keep_list)):
                #Page Hit!!
                if keep_list[j] == str[i]:
                    checkHit = TRUE
                    break
                else:
                    continue

        if checkHit == FALSE:
            if(len(keep_list)==frameSize):
                keepBackward_list = []
                dictBackward = {}
                indexDelete = 0
                if index < len(str):
                    for j in range(index):
                        keepBackward_list.append(str[j])

                    #เช็คระยะของค่าในkeep_list ว่าในkeepForward_list แต่ละค่ามีระยะเท่าไหร่
                    for id in range(len(keep_list)):
                        found = FALSE
                        for temp in range(len(keepBackward_list)):
                            if keep_list[id] == keepBackward_list[temp]:
                                dictBackward[id] = temp
                                found = TRUE
                    indexDelete = minDesitance(dictBackward,frameSize)
                    del keep_list[indexDelete]
            keep_list.append(str[i])
            index += 1
            pagefault_count += 1

        if checkHit == TRUE:
            checkHit = FALSE
            index += 1
            continue

    return pagefault_count