def getClenString(originString,problemNumber):

    #originString = "A354597	Cat	2014-05-02 12:16:00	Normal	Ariel	Spayed Female A362707	Dog	2016-01-27 12:27:00	Sick	Girly Girl	Spayed Female A370507	Cat	2014-10-27 14:43:00	Normal	Emily	Spayed Female A414513	Dog	2016-06-07 09:17:00	Normal	Rocky	Neutered Male"
    spltList=originString.split("\t")
    addList = []
    addString = ""
    cnt = 0

    for x in spltList:
        if cnt==problemNumber:
            tmp = x.split(" ")
            if(len(tmp)>2):
                addString+=tmp[0]+" "+tmp[1]
                addList.append(addString)
                addString=tmp[2]+","
            else:
                addString+=x
                addList.append(addString)
            cnt = 1
            continue
        addString+=x+","
        cnt+=1
    return addList





        
    




    