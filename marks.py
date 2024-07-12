c=int(input("c marks"))
j=int(input("j marks"))
r=int(input("r marks"))
total=c+j+r
avr=total/3
per=(total/180)*100
grade=""
if per>90:
    grade="A"
elif per>85 and per<90:
    grade="A+"
elif per>80 and per<85:
    grade="B"
elif per>70 and per<80:
    grade="C"
else :
    grade="pass"
print(f"total marks :{total} \navrage :{avr}\ngrade {grade}")

#code for palidrome
'''s=input("give a string:")
revese=s[::-1]
if revese ==s:
    print("its is palidrome")
else:
    print("its is not paalidrome")
    '''