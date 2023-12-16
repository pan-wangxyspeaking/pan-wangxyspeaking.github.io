sex=int(input("请输入性别（女：0，男：1）："))
bmi=round(float(input("请输入体重（kg）："))/float(input("请输入身高（m）："))**2,1)

if sex==1:
    if bmi<=16.4:
        print("低体重")
    elif bmi<=23.2:
        print("正常")
    elif bmi<=26.3:
        print("超重")
    else:
        print("肥胖")

elif sex==0:
    if bmi<=16.4:
        print("低体重")
    elif bmi<=22.7:
        print("正常")
    elif bmi<=25.2:
        print("超重")
    else:
        print("肥胖")


else:
    print("人妖？")
