import pandas as pd

class TransForm():

    def __init__(self, timeTable):
        self.timeTable = timeTable

    def saveJson(self, i):
        column = [0,1,2,3,6,7]
        count = 0
        data = {}
        for d in range(len(self.timeTable[i])):
            if d == column[count]:
                data[self.timeTable[0][d]] = self.timeTable[i][d]
                count+=1
                if count == len(column):
                    break
        return data

    def convert(self):
        # list to dict 
        data_many_dict = []
        for i in range(1, len(self.timeTable)):
            data_many_dict.append(self.saveJson(i))

        return data_many_dict
