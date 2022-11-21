'''Question3:
An LCD (Liquid Crystal Display) can represent multiple digits between 0 to 9 
If you turn the LCD upside-down, some of the numbers still remain valid numbers. For example, 16 becomes 91, 10 becomes 01, which are valid numbers.
If you index all positive numbers (>0) that can produce valid numbers when you upside down the display (like 1st one is 1, 2nd one is 2, 3rd one 5... 7th one is 10), 
Write program to print the ’Nth’ number in the series

Input: 8
Output: 11'''
n=int(input())
vd=[0,1,2,5,6,8,9]
vd1=vd.copy()
c=0
i=1
while(i>0):
  d=[int(x) for x in str(i)]
  vd.extend(d)
  if(set(vd)== set(vd1)):
      c+=1
      if(c==n):
          print(int("".join(list(map(str,d)))))
          break
  i+=1
  vd=[0,1,2,5,6,8,9]
