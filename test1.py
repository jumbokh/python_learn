age=int(input("你的年紀是?"))
if age >=20:
    print("今年請記得去投票")
else:
    diff = 20-age
    print("還差 "+str(diff)+"歲才有投票權")