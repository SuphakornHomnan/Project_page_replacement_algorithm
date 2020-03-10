def FIFO(str, frameSize):
    keep_list = []
    checkHit = False
    index = 0
    pagefault_count=0
    for i in range(len(str)):
        #check string with frame keep[]
        if(len(keep_list)>0):
            for j in range(len(keep_list)):
                if keep_list[j] == str[i]:
                    checkHit = True
                    break
                else:
                    continue

        if(len(keep_list)==frameSize):
            del keep_list[index]
        if(checkHit==False):
            keep_list.append(str[i])
            pagefault_count += 1
        if(checkHit == True):
            checkHit = False
            continue

    return pagefault_count



