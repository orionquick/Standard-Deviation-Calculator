
import time
from msvcrt import getch

inputNum = 0

data = []

data2 = []

print("")

print("Input data below. Press ENTER to add inputs. Press SPACE to compile. ")

while True:
	
	key = ord(getch())

	if key == 32:
		
		break
	
	print("")
	
	inputData = int(input("Input " + str(inputNum + 1) + ": "))
	
	data.extend([inputData])
	
	inputNum += 1
	
dataAvg = sum(data) / inputNum

for number in data:

	data2.extend([(number-dataAvg) ** 2])
	
data2Avg = sum(data2) / inputNum

sDev = data2Avg ** 0.5

print("")

print("Average: " + str(dataAvg))

print("")

print("Standard Deviation: " + str(sDev))

print("")

input("")
	
