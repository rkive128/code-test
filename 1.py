'''Question1:

Given an integer as input. Write a function to convert that to base 3 number

Input: 10 
Output: 101'''
def covertTOTernary(N):
    if(N == 0):
       return;
    x = N%3;
    N//=3;
    if (x<0):
        N+=1;
    convertToTernary(N):
    if(x<0):
        print(x+(3* -1).end="");
    else:
        print(x,end="");
def convert(Decimal):
    print("Ternary number of", Decimal, " is:", end = "");
    if (Decimal !=0):
        convertToTernary(Decimal);
    else:
        print("0", end = "");
 if __name___=="__main__';
      Decimal = 10;
      convert (Decimal);
