x=int(input('what are  birth year ?:'))
y=int(input('what are birth month ? :'))
z=int(input('what are  birth day ? :'))
k=10# k is left months (12-2=2)
#today date : 11/10/2024
t=2024-x
# 10=12-2,01+1=2 for 01:birth month
# 9=12-3, 02+1=3 for 02: birth month
# 8=12-3,03+1=4 fof 03 : birth month
# in general 12 minus birth month plus one (12-birth month-1=11-birth month)
z=11-y
# 290=360-2*30-10 (ten is today day date ),01+1=2 for 01:birtday 
#in general 360 minus remaining months times 30 month minus ten 
r=k
print( 'your age information : ' , r, z,t)
