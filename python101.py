import argparse #สำหรับ รับ input จากภายนอก
import subprocess #สำหรับรัน terminal command 

#import flask # สำหรับทำ web app และ web service api


def print_other():
    print('something else')

if __name__=="__main__":
    x = 2
    y = 3
    print(f'calculate {x} x {y} = {x*y}')