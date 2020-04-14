import re  
import pandas as pd

class TransForm():

    def __init__(self, timeTable):
        self.timeTable = timeTable

    def convert(self):
        # list to dict 
        data_many_dict = []
        for i in range(1, len(self.timeTable)):
            data = {self.timeTable[0][0]:self.timeTable[i][0], self.timeTable[0][1]:self.timeTable[i][1], self.timeTable[0][2]:self.timeTable[i][2], self.timeTable[0][3]:self.timeTable[i][3], self.timeTable[0][6]:self.timeTable[i][6], self.timeTable[0][7]:self.timeTable[i][7]}
            data_many_dict.append(data)

        return data_many_dict
