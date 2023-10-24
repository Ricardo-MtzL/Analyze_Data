#The following Function and Test cases correspond to my application for the QA Engineer position at cart.com
 

import datetime
import unittest

def analyze_data(*data):    # Function "ANALYZE DATA" with data inputted as a tuple
    inputList = list(data)  # converts Tuple "data" and converts it in a list
    processedList = []      # list used to process data
    outputList = []         # list to save data once it's processed
    maximum = None          # variable that saves the  Max nr
    minimum = None          # variable that saves the Min nr
    average = None          # variable that saves the Avg nr
    uniqueValueCount = None # variable that saves the unique value count
    median = None           # variable that saves the median nr

    for x in inputList:                                                 #for every element in the input list
        if type(x) == int or type(x) == float :                         #if such element is INT or FLOAT
         processedList.append(x)                                        #add such element to the last position of the processed list
         processedList.sort()                                           #order such list
         maximum = max(processedList)                                   #get the maximum number of such list
         minimum = min(processedList)                                   #get the minimum number of such list
         average = sum(processedList) / len (processedList)             #get the avg number of such list
         uniqueValueCount = len(set(processedList))                     #get the UVC

         n=len(processedList)                                           #variable that saves de length of the list
         if n % 2 == 0:                                                 #if the length is even
            middle1 = processedList[n // 2]                             #first middle vaalue
            middle2 = processedList[n // 2 - 1]                         #second middle value
            median = (middle1 + middle2) / 2                            #get the median nr
         else:                                                          #if the length is odd
          median = processedList[n // 2]                                #get the median nr
    
    outputList =[minimum, maximum, average, uniqueValueCount, median]   #saves previous results on an ouput List
   

    #print("Data entered by user:" ,processedList)   
    #print("minimum:" , minimum)
    #print("maximum:" , maximum)
    #print("average:", average)
    #print("unique value count:", uniqueValueCount)
    #print("median:", median)
   
    return outputList                                                   #Deliver processed data

integersTest=[1, 5, -2, 8, 0, -2, 5, 1, 10, -5]
floatsTest=[2.5,3.5,1.5,2.5,2.5]
mixedDataTest=[1, 3.5, "apple", 2.5, 1, 3, "banana"]
datesTest=[datetime.date(2022, 1, 1), datetime.date(2021, 1, 1),datetime.date(2022, 1, 1)]
emptyList=[]

class TestAnalyzeData(unittest.TestCase):   #Using unittest to automatically compare the results of each cases.
    result_floats = None                            
    def test_integers(self):
        result = analyze_data(*integersTest)
        self.assertEqual(result, [-5, 10, 2.1, 7, 1])

    def test_floats(self):
        result = analyze_data(*floatsTest)
        self.assertEqual(result, [1.5,3.5,2.6,3,2.5])
    
    def test_mixed_data(self):
        result = analyze_data(*mixedDataTest)
        self.assertEqual(result, [1, 3.5, 2.2, 4, 2.5])
        TestAnalyzeData.result_floats = result

    def test_dates(self):
        result = analyze_data(*datesTest)
        self.assertEqual(result, [None, None, None, 0, None])

    def test_empty_list(self):
        result = analyze_data(emptyList)
        self.assertEqual(result, [ ])

#Results
print()
print("Below are shown the results of the Test Cases. Showing only the Input/Output.")
print("Case 1")
print("Input:", integersTest)
print("Output:", analyze_data(*integersTest))
print()
print("Case 2")
print("Input:", floatsTest)
print("Output:", analyze_data(*floatsTest))
print()
print("Case 3")
print("Input:", mixedDataTest)
print("Output:", analyze_data(*mixedDataTest))
print()
print("Case 4")
print("Input:", datesTest)
print("Output:", analyze_data(*datesTest))
print()
print("Case 5")
print("Input:", emptyList)
print("Output:", analyze_data(*emptyList))
print()
print("And now the same Test Cases are run by using unittest. Showing the exact location of the error/discrepancy.")

unittest.main() #Execution of the Unittest


