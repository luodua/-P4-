
#!/usr/bin/env python
from flask import *

import random
import os
import sys


# import send_link.py
# import send_ecn.py
# import receive_link.py
# import receive_ecn.py

app = Flask(__name__)


xxx="aa"

# 对应ajax中url路径
@app.route('/', methods=['GET', 'POST'])
def totalNumber():
    #return xxx
    return render_template('index.html')

@app.route('/2.html', methods=['GET', 'POST'])
def tow():
    # if request.method == 'GET':
    #     # args = request.args
    #     print("aaa")
    #     return render_template('index.html')
    # temp = random.randint(10,50)
    
    return render_template('2.html')

@app.route('/send_bage', methods=['GET', 'POST'])
def _3():
    if request.method == 'GET':
        print(request.args)
        f = open('h1.txt', 'r')
        
        #content = f.readline() # 表示读取一行，每次读取后指针移动一行
        lines = f.readlines() # 把文件按照换行符进行读取，返回一个列表print(content)
       
# 定义一个空列表来存储不空的四行
        non_empty_lines = []

# 遍历每一行
        for line in reversed (lines):
            # 去掉行尾的换行符
            line = line.strip()
            # 如果行不为空，就添加到列表中
            if line:
                non_empty_lines.insert(0,line)
            # 如果列表中已经有四个元素，就停止循环
            if len(non_empty_lines) == 7:
                break

        print(non_empty_lines)
        aa=(float(non_empty_lines[1])+float(non_empty_lines[6]))/2
        bb=(float(non_empty_lines[3])+float(non_empty_lines[4]))/2
        cc=(float(non_empty_lines[2])+float(non_empty_lines[5]))/2
        
        f.close()
        return [aa,bb,cc]
    #     # args = request.args
    #     print("aaa")
    #     return render_template('index.html')
    # temp = random.randint(10,50)
    #print(request.method)
@app.route('/send_test', methods=['GET', 'POST'])
def _4():
    
    print("bbb")
    mm=request.args.to_dict()
    f=open("myfile", "w")
    print(mm)
    #print("iperf "+request.args[0][1]+request.args[1][1])
    f.write("iperf "+mm['1']+' '+mm['2']+' '+mm['3'])
    f.flush()
    f.close()

@app.route('/send_ecn', methods=['GET', 'POST'])
def _5():
    
    print("ecn")
    if request.method == 'GET':
        print(request.args)
        f = open('h2_ecn.txt', 'r')
        
        #content = f.readline() # 表示读取一行，每次读取后指针移动一行
        lines = f.readlines() # 把文件按照换行符进行读取，返回一个列表print(content)
       
# 定义一个空列表来存储不空的四行
        non_empty_lines = []

# 遍历每一行
        for line in reversed (lines):
            # 去掉行尾的换行符
            line = line.strip()
            # 如果行不为空，就添加到列表中
            if line:
                non_empty_lines.insert(0,line)
            # 如果列表中已经有四个元素，就停止循环
            if len(non_empty_lines) == 7:
                break

        print(non_empty_lines)
        aa=(float(non_empty_lines[1])+float(non_empty_lines[6]))/2
        bb=(float(non_empty_lines[3])+float(non_empty_lines[4]))/2
        cc=(float(non_empty_lines[2])+float(non_empty_lines[5]))/2
        
        f.close()
        return [aa,bb,cc]
    return "false"
        
# 主函数
if __name__ == '__main__':
   
    # 设置host与端口
    #/os.system("python3 send_link.py")
    app.run(host = "127.0.0.1", port = 5000)
    
    


