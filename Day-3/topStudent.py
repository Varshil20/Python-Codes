def findTopStu(**kvls) :
    l = len(kvls)
    max = -1
    name = ""
    for key , val in kvls.items() :
        if val > max :
            max = val
            name = key
    
    return name


print(findTopStu(harsh=66 , varshil=90 , ronak=99 , amit=78 , zeel=87))