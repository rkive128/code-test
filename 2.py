'''Question2:
Given two strings as input, find number of occurrences of last character in second string, in the first string. Don't use string library functions for this program

Input: “going to go to goa”, “go”
Output: 5 (last char of str2 is o and it appeared 5 times in str1)
'''
str1=input()
str2=input()
lc=str2[-1]
c=0
for i in str1:
    if(i==lc):
        c+=1
print(c)
