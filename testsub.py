import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    subprocess.run(["ls","-l"])
    subprocess.run(["python101.py","9","--x","11"])