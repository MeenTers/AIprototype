import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ##basic
    subprocess.run(["ls","-l"])
    for i in [2,5,6,8]:
        subprocess.run(["python","python101.py","9","--x",f"{i}"])
    
    ## use output of subprocess
    #pro = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pro.communicate()
    #print(out)

    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ โดยไม่ต้องแก้โปรแกรมเก่า
    for i in [2,5,6,8]:
        pro = subprocess.Popen(["python","python101.py","9","--x",f"{i}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = pro.communicate()
        text = str(out,'utf-8')
        text = text.rstrip("\n")
        print(text[23:26])
      