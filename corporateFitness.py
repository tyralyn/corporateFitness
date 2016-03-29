########################################################################################################################
#                                                                                                                      #
#   INPUT                                                                                                              #
#   [[date, miles run], [date 2, miles run 2], ...]                                                                    #                                                                 
#   [[4, 5], [12, 6], [16, 3]]                                                                                         #
#   start date: 10                                                                                                     #
#   end date: 20                                                                                                       #
#                                                                                                                      #
#   OUTPUT                                                                                                             #
#   [[start date, cumulative], [start date + 1, cumulative], ... [end date, cumulative]]                               #
#   [[10, 5], [11, 5], [12, 11], [13, 11], [14, 11], [15, 11], [16, 14], [17, 14], [18, 14], [19, 14], [20, 14]]       #
#   Input parameters: miles run (list of pairs ordered by date), start date (integer), end date (integer)              #
#   Return: cumulative miles run since date 0, inclusive and complete between start and end (list of pairs)            #
#                                                                                                                      #
########################################################################################################################

# simple solution that calculates cumulative record list
# and adds 0 date at beginning and end date entry at and of cumulative record list
# then creates new list that fills in the dates that dont exist
# does not work if input includes zero entry initially
def fitnessRecordBruteForce( startDate, endDate, recordList):
	cumulativeRecordList = [[0,0]]
	fullRecordList = []
	mileCounter = 0
	dateCounter = 0
	previousCount=0;
	for listIndex in range (0, len(recordList)): 
		mileCounter += recordList[listIndex][1]
		cumulativeRecordList.append([recordList[listIndex][0],mileCounter])
	cumulativeRecordList.append([endDate,cumulativeRecordList[-1][1]])

	for listIndex in range (0, len(cumulativeRecordList)):
		for i in range (dateCounter, cumulativeRecordList[listIndex][0]):
			fullRecordList.append([dateCounter, previousCount])
			dateCounter+=1
		fullRecordList.append(cumulativeRecordList[listIndex])
		previousCount=cumulativeRecordList[listIndex][1]
		dateCounter+=1
	return fullRecordList[startDate:endDate+1]

# more elegant solution that iterates through start date to end date
def fitnessRecord(startDate, endDate, recordList):
	fullRecordList = []
	mileCounter = 0
	listIndex = 0
	i = startDate
	while i < endDate+1: # i represents a "current day" -- the day of the next [day,miles] pair we need to add to the output list
		#if the item encountered in the input list is a later date than the current
		if (listIndex < len(recordList)):
			if recordList[listIndex][0] > i:
				for j in range (i, min(recordList[listIndex][0], endDate+1)):
					fullRecordList.append([i,mileCounter]) #add a [day,mile] pair to the output list until the current date has been reached
					i+=1
			#if the item encountered in the input list is the same date as the current date, add an updated [day, mile] pair
			elif recordList[listIndex][0] == i: 
				mileCounter += recordList[listIndex][1]
				fullRecordList.append([i, mileCounter])
				listIndex+=1
				i+=1
			#if the item encountered in the input list is less than the current date -- will only happen at the beginning of a list
			else:
                                #iterate through all the items at the beginning of the input list that correspond to a day before the current day
				while (listIndex < len(recordList) and recordList[listIndex][0] < i):
					mileCounter+=recordList[listIndex][1]
					listIndex+=1
                #handle the cases of the end date being later than the last list entry
		else: 
			fullRecordList.append([i, mileCounter])
			i+=1
	return fullRecordList

testInput1 = [[4, 5], [12, 6], [16, 3]]
testInput2 = [[1,10],[2,7],[4, 5], [12, 6], [16, 3]]
testInput3 = [[12, 6], [16, 3], [17,10], [18,2]]
testInput4 = [[14, 5], [15, 6], [16, 3], [22,9]]
testInput5 = [[14, 5], [15, 6], [26, 3],[132,5]]
testInput6 = [[24, 5], [32, 6], [36, 3]]
testInput7 = [[10, 5], [12, 6], [20, 3]]
testInput8 = [[4, 5], [6, 6], [7, 3]]
startDate = 10
endDate = 20
#print("Test Input:", testInput, "start and end:", startDate, endDate)
#print("Brute Force Solution:", fitnessRecordBruteForce(startDate, endDate, testInput))
#print("Solution:", fitnessRecord(startDate, endDate, testInput))'''

