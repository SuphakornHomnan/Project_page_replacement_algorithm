def maxDistance(dictForward,frameSize):
    temp = 0
    index = 0
    for i in range(frameSize):
        if dictForward[i] > temp:
            temp = dictForward[i]
            index = i
        else:
            continue
    return index

def Optimal(str,frameSize):
    keep_list = []
    checkHit = False
    pagefault_count=0
    index = 0
    for i in range(len(str)):
        if(len(keep_list)>0):
            for j in range(len(keep_list)):
                # ถ้าpage hit
                if keep_list[j] == str[i]:
                    checkHit = True
                    break
                else:
                    continue

        if checkHit == False:
                if(len(keep_list)==frameSize):
                    keepForward_list = []
                    dictForward = {}
                    indexDelete = 0
                    if index < len(str)-1:
                        for j in range(index+1,len(str)):
                            keepForward_list.append(str[j])

                        #เช็คระยะของค่าในkeep_list ว่าในkeepForward_listแต่ละค่ามีระยะเท่าไหร่
                        for id in range(len(keep_list)):
                            found = False
                            for temp in range(len(keepForward_list)):
                                if keep_list[id] == keepForward_list[temp]:
                                    dictForward[id] = temp
                                    found = True
                                    break
                            if found == False:
                                dictForward[id] = 99999999999999
                            else:
                                continue
                        indexDelete = maxDistance(dictForward,frameSize)
                        del keep_list[indexDelete]
                keep_list.append(str[i])
                index += 1
                pagefault_count += 1

        if checkHit == True:
            checkHit = 0
            index += 1
            continue
    return pagefault_count