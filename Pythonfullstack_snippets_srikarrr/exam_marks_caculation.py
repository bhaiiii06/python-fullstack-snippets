
s1=int(input("enter the s1 marks:"))
s2=int(input("enter the s2 marks:"))
s3=int(input("enter the s3 marks:"))
s4=int(input("enter the s4 marks:"))
s5=int(input("enter the s5 marks:"))
total=s1+s2+s3+s4+s5
avg=total/5
if s1>40 and s2>40 and s3>40 and s4>40 and s5>40:
    if total>490:
        print("student got A grade:")
        print("total marks:", total)
        print("average marks:", avg)
    elif total>450 and total<=490:
        print("student got B+ grade")
        print("student got B grade")
        print("total marks:", total)
        print("average marks:", avg)
    elif total>400 and total<=450:
        print("student got C grade")
        print("total marks:", total)
        print("average marks:", avg)
    else:
        print("student got D grade")
        print("total marks:", total)
        print("average marks:", avg)
else:
    print("student is fail")
    print("total marks:", total)
    print("average marks:", avg)