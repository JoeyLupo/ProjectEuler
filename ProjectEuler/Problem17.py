import sys
sys.stdout = open('written.txt', 'w')

ONE = 3
TWO = 3
THREE = 5
FOUR = 4
FIVE = 4
SIX = 3
SEVEN = 5
EIGHT = 5
NINE = 4
TEN = 3
ELEVEN = 6
TWELVE = 6
THIRTEEN = 8
FOURTEEN = 8
FIFTEEN = 7
SIXTEEN = 7
SEVENTEEN = 9
EIGHTEEN = 8
NINETEEN = 8
TWENTY = 6
THIRTY = 6
FORTY = 5
FIFTY = 5
SIXTY = 5
SEVENTY = 7
EIGHTY = 6
NINETY = 6
HUNDRED = 7
THOUSAND = 8
AND = 3

    
def written_out(num):
    words =[]
    zero = False
    if int(num[-2:]) <= 10 or int(num[-2:])>=20:
        if num[-1] == '1':words.append(ONE); print("ONE", end =' ')
        elif num[-1]== '2':words.append(TWO); print("TWO", end =' ')
        elif num[-1]== '3':words.append(THREE); print("THREE", end =' ')
        elif num[-1]== '4':words.append(FOUR); print("FOUR", end =' ')
        elif num[-1]== '5':words.append(FIVE); print("FIVE", end =' ')
        elif num[-1]== '6':words.append(SIX); print("SIX", end =' ')
        elif num[-1]== '7':words.append(SEVEN); print("SEVEN", end =' ')
        elif num[-1]== '8':words.append(EIGHT); print("EIGHT", end =' ')
        elif num[-1]== '9':words.append(NINE); print("NINE", end =' ')
        elif num[-1]== '0':zero = True    
    
    if len(num)== 1:
        return words
    elif len(num)==2:
        if num[0] == '1': 
            if zero: words.append(TEN); print("TEN", end =' ')
            elif num[-1] == '1': words.append(ELEVEN); print("ELEVEN", end =' ')
            elif num[-1] == '2': words.append(TWELVE); print("TWELVE", end =' ')
            elif num[-1] == '3': words.append(THIRTEEN); print("THIRTEEN", end =' ')
            elif num[-1] == '4': words.append(FOURTEEN); print("FOURTEEN", end =' ')
            elif num[-1] == '5': words.append(FIFTEEN); print("FIFTEEN", end =' ')
            elif num[-1] == '6': words.append(SIXTEEN); print("SIXTEEN", end =' ')
            elif num[-1] == '7': words.append(SEVENTEEN); print("SEVENTEEN", end =' ')
            elif num[-1] == '8': words.append(EIGHTEEN); print("EIGHTEEN", end =' ')
            elif num[-1] == '9': words.append(NINETEEN); print("NINETEEN", end =' ')
            return words
        
        elif num[0] == '2': words.append(TWENTY); print("TWENTY", end =' ')
        elif num[0] == '3': words.append(THIRTY); print("THIRTY", end =' ')
        elif num[0] == '4': words.append(FORTY); print("FORTY", end =' ')
        elif num[0] == '5': words.append(FIFTY); print("FIFTY", end =' ')
        elif num[0] == '6': words.append(SIXTY); print("SIXTY", end =' ')
        elif num[0] == '7': words.append(SEVENTY); print("FORTY", end =' ')
        elif num[0] == '8': words.append(EIGHTY); print("EIGHTY", end =' ')
        elif num[0] == '9': words.append(NINETY); print("NINETY", end =' ')
        return words
    elif len(num)==3:
        words.append(HUNDRED); print('HUNDRED',end =' ')
        
        if num[-2:]!= '00': words.append(AND); print("AND", end =' ')
        if num[0] == '1': words.append(ONE); print("ONE", end =' ')
        elif num[0] == '2': words.append(TWO); print("TWO", end =' ')
        elif num[0] == '3': words.append(THREE); print("THREE", end =' ')
        elif num[0] == '4': words.append(FOUR); print("FOUR", end =' ')
        elif num[0] == '5': words.append(FIVE); print("FIVE", end =' ')
        elif num[0] == '6': words.append(SIX); print("SIX", end =' ')
        elif num[0] == '7': words.append(SEVEN); print("SEVEN", end =' ')
        elif num[0] == '8': words.append(EIGHT); print("EIGHT", end =' ')
        elif num[0] == '9': words.append(NINE); print("NINE", end =' ')
        
        if num[1] == '0':
            return words
        else:
            if int(num[1:])<= 10 or int(num[1:])>=20:
                num = num[1]+'0'
            else: 
                num = num[1:]    
            words.append(sum(written_out(num)))
            return words
    
    elif len(num) == 4:
        words = [ONE,THOUSAND]; print("ONE THOUSAND")
        return words
    
    return words


total = []
for n in range(1,1001):
    print('n =', n, end = '     ')
    total.append(sum(written_out(str(n))))
    print()
    
print(sum(total))  
