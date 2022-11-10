GCS-3 Problems
Instructions:
Github repository: negpod-no-gcs3
Report name: negpod-no-gcs3_problems


Schell scripting
Create a shell script that checks if a file exists or not:
If the file doesn’t exist it should print 2
If the file exists:
I. The file can be empty, in this case print 1
II. The file is not empty, in this case print 0

Example of the file GCS_3_problems_20221105 (You are allowed to create this file manually)

If statements
Given an integer, m, perform the following conditional actions:
If m  is even, print Weird
If m is odd and in the inclusive range of 2 to 5, print Not Weird
If m is odd and in the inclusive range of 6 to 20, print Weird
If m is odd and greater than  20, print Not Weird
Days in a month range from 28 to 31 days. Write a python program that reads the name of a month from the user as a string and displays the number of days in that month. For February display  “28 or 29 days”  to account for the leap years.
Example 
Input: March
output: The month of March has 31 days.












Loops ( For and While loops)
Write a python program that takes an integer and prints all odd numbers up to the integer.
Example
Input: 5
Output: 1, 3, 5

Write a python program that given a string, it uses a while loop to print all consonant letters except vowels. The letter “y” should be considered a vowel. In this particular problem, we are working with lowercase letters only, therefore convert all words from the user to lowercase.
Example
Input: hello
Output: h, l, l





Lists

Write a python function that takes a list of integer nums and an integer target, and returns indices of the two numbers such that they add up to the target. Return the indices in a tuple. You may assume that each input would have exactly one solution, and you may not use the same element twice.
The table below shows a list of inputs you should pass to your function and the expected results. If you get anything other than the expected result, then your function is not correct and you should correct it

Input
Expected result
nums =[2,7,11,15], target = 9


(0,1)


nums = [3,2,4], target = 6


(1,2)
nums = [3,3], target = 6
(0,1)




Write a python function that takes as parameters a list of integers and a target value, it sorts the list in ascending order and returns the index if the target is found. If not, return the index where it would be if it were inserted in order.
The table below shows a list of inputs you should pass to your function and the expected results. If you get anything other than the expected result, then your function is not correct and you should correct it
Input
Expected Output
nums = [1,3,5,6], target = 5


2
nums = [1,3,5,6], target = 2


1
nums = [1,3,5,6], target = 7


4





Dictionary
The table below shows the representation of the different Roman numerals.
Symbol       
Value
I             
1
V             
5
X             
10
L            
50
C            
100
D           
500
M            
1000


The number 2 is written as II in Roman numeral, just two ones added together. 
The number 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II
Roman numerals are usually written from largest to smallest from left to right. However, the Roman numeral for 4 is not IIII. Instead, the number 4 is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number 9, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
A constraint to take note of is 1 <= len(s) <= 15 where s is the Roman numeral.
Your task is to write a python function that takes a roman numeral and converts it to an integer. After you are done with your function give each of the Roman numerals in the table below and if your function is correct you shout get the expected result as shown in the table. If you get anything other than the expected result, then your function is not correct and you should correct it.
Input
Expected Result
III
3
LVIII
58
MCMXCIV
1994
XCIX
99
MMDCCCL
2850



