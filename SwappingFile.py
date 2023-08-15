def swapFileData():
    file1 = "SampleText1.txt"
    file2 = "SampleText2.txt"
    with open(file1,"r")as f:
        data_1 = f.read()
    with open(file2,"r")as h:
        data_2 = h.read()
    with open(file1,"w")as q:
        q.write(data_2)
    with open(file2,"w")as j:
        j.write(data_1)

swapFileData()