#icvs.txtを取得して速報と確定のみ取り込む
import datetime

path = 'icvs.txt'
f = open(path,  "r")

line = f.readline()

sokuho = []
kakutei = []
while line:
    if line[:4] == "2012":
        sokuho.append(line)
    elif line[:4] == "2022":
        kakutei.append(line)
    line = f.readline()
f.close()


dt_now = datetime.datetime.now()
today = str(dt_now.year) + str(dt_now.month) + str(dt_now.day)
sokuhoname = "sokuho" + today + ".txt"
kakuteiname = "kakutei" + today + ".txt"

with open(sokuhoname,mode="a") as f:
    print("速報データ\n",file=f)
    for i in sokuho:
        day = i[5:11]
        num = i[42:48]
        money = i[56:62]
        come = i[80:88]
        print("入金日：" + day,file=f)
        print("顧客番号：" + num,file=f)
        print("金額：" + money + "円\n\n",file=f)
    
    

with open(kakuteiname,mode="a") as f:
    print("確定データ\n",file=f)
    for i in kakutei:
        day = i[5:11]
        num = i[42:48]
        money = i[56:62]
        come = i[80:88]
    
    
        print("入金日：" + day,file=f)
        print("顧客番号：" + num,file=f)
        print("金額：" + money + "円",file=f)
        print("振込日：" + come + "\n\n",file=f)
        
        
        