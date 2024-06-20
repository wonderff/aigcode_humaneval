s = input("请输入字符串s：")
t = input("请输入字符串t：")
i = 0

if len(s) > len(t):
    print("s 不是")

else:
    yes = True
    for each in s:
        a = t.find(each,i)
        if a != -1:
            i = a+1
        else:
            yes = False
            break
    if yes:
        print("s 是")
    else:
        print("s 不是")