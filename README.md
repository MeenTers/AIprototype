# AIprototype 2022
> นายธนพล ทาโยธี 613020241-3 สาขาสารสนเทศสถิติ ชั้นปีที่ 4 
-------------------------------
## Command line

    ls          ตรวจเช็คไฟล์ในrootต่างๆ
    ls -l       แสดงข้อมูลของไฟล์อย่างละเอียด
    clear       เคลียร์ คำสั่งต่างๆที่แสดงบน terminal
    cd          เลือก path ที่ต้องการเข้าถึง
    mkdir       สร้างโฟล์เดอร์
    rm          ลบไฟล์
    rm -R       ลบทุกไฟล์ที่อยู่ในโฟล์เดอร์นั้น
    code        คำสั่งเพื่อเปิดไฟล์ด้วย visual studio code
    screen -S   สร้างหน้าต่างเพิ่มขึ้นอีก 1 หน้า
    screen -R   ย้อนกลับไปในหน้า screen นั้น ๆ
    ctrl+A+D    ออกจากหน้า screen
    screen -R   กลับเข้าไปใน screen ที่สร้างไว้
## การติดตั้ง git เพื่อใช้งานgit
 
    conda install git
## setup git ครั้งแรก

    $ git config --global user.name "MeenTers"  ชื่อusernam git
    $ git config --global user.email meenthanapon@kkumail.com email git
## การใช้งาน package git
    
    git status    ตรวจสอบว่ามีไฟล์ใดบ้างมีการเปลี่ยนแปลง
    git clone     ดาวน์โหลดgithubลงเครื่องของuser
    git pull      ดึงไฟล์ล่าสุดบนgithub ลงสู่เครื่องuser
    git add       เพิ่มไฟล์ที่ต้องการขึ้นสู่ github
    git commit -m เพื่อคอมเมนท์ข้อความ
    git push      ส่งไฟล์จากเครื่องสู่ github
    
* ### Subprocess : [[code]](https://github.com/MeenTers/AIprototype/blob/main/testsub.py)
* ### Python Argparse : [[code]](https://github.com/MeenTers/AIprototype/blob/main/python101.py)
---------------------------------------------------------------------------------------------------------
 ## Flask เป็น Package ที่ใช้สำหรับพัฒนาเว็บแอปพลิเคชัน
  * ###  flask file : [[code]](https://github.com/MeenTers/AIprototype/blob/main/testflask.py)
  * ### Home.html file : [[code]](https://github.com/MeenTers/AIprototype/blob/main/templates/home.html)
  * ### csv file : [[code]](https://github.com/MeenTers/AIprototype/blob/main/testdb.csv)
* ### Test Requests [[code]](https://github.com/MeenTers/AIprototype/blob/main/postrequests.py)
* ### Cloud DB & Cloud AI [[code]](https://github.com/MeenTers/AIprototype/blob/main/Cloud_DB_and_AI.ipynb)
## Neural Network with Tensorflow [[code]](https://github.com/MeenTers/AIprototype/blob/main/Tensorflow(network).ipynb)
 การสร้าง Neural Network ด้วย Tensorflow Sequential API:
        
         Sequentail - สามารถสร้างได้ง่าย ไม่มีความซับซ้อน แต่ network จะวิ่งเป็นเส้นตรง
        
         Functional - สร้างได้ยากกว่า Sequentail  ได้ network ที่สามารถปรับแต่งเส้นทางให้มีความซับซ้อนได้
        
         Subclassing - สร้างได้ยาก โดยในส่วนนี้ไม่ได้เรียนในคอร์ส
  Download and prepare the CIFAR10 dataset: 
               
         https://www.kaggle.com/datasets/wordroid/cifar10-object-recognition-in-images-zip-file
