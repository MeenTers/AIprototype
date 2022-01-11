import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ##basic
    subprocess.run(["ls","-l"])
    for i in [2,5,6,8]:
        subprocess.run(["python","python101.py","9","--x",f"{i}"])
    
    ## use output of subprocess
    pro = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = pro.communicate()
    print(out)

    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูร โดยไม่ต้องแก้โปรแกรมเก่า