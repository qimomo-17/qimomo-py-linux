str_a2str={}
a2str_str={}
ap_str="ⅩzxcvbnmlkjhgfdsapoiuytrewqZXCVBNMLKJHGFDSAQWERTYUIOP$@9876543210_:~!&|\\></*-+#[]\'\"=%,;(){}.?^¥±÷≠≯≮≥≤≒≈√π‰⅓½℅％¾¼⅔∵∴∷㏒∭∬∫㏑∮∉∈∏∑⊆⊃⊂∅⊊⊅⊄⊇⊈⫋⫌∀∃∩∪∧∥⊕⊙∨⊥⌒∟∠∽∝⊿△∞≌°℉\r\t\n\b\f\v\0，。？！＃：、；＊—…＆￥·（）‘’“”⁰¹²³⁴⁵⁶⁷⁸⁹ⁱ⁺⁻₁₂₃₄₅₆₇₈₉₊₋₌₍₎①②③④⑤⑥⑦⑧⑨⑩⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑壹贰叁肆伍陆柒捌玖拾佰仟萬億⇅⇔⇕↱↰↑↓←→"
a2str_ax16={}
ax16_a2str={}
ap_str_x16="0123456789ABCDEF"
TF_B=2
TF_p=True
def init():
    ap=-1
    for i in ap_str:
        ap+=1
        ap2=format(ap,"08b")
        str_a2str[i]=ap2
        a2str_str[ap2]=i
    ap=-1
    for i in ap_str_x16:
        for j in ap_str_x16:
            ap+=1
            ap2=format(ap,"08b")
            ax16_a2str[i+j]=ap2
            a2str_ax16[ap2]=i+j



def to_2str_2(b,bt=8,):  #01转二进制
    kj2=b""
    a=0;c=len(b);TF= (c>=1024**TF_B) and TF_p
    if TF: 
        print("to_2str_2:正在处理中...")
    for i in range(0,len(b),bt):
        a+=1
        kj2+=int(b[i:i+bt],2).to_bytes(1,"big")
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_2str_2:处理完成" )
    return kj2

def to_2_2str(b,bt=8):  #二进制转01
    kj2=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_2_2str:正在处理中...")
    for i in b: #class_i:int; class_b:bytes
        a+=1
        kj2+=format(i,f"0{bt}b")
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_2_2str:处理完成")
    return kj2


def to_str_2str(text):  #字符转01
    str2=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_str_2str:正在处理中...")
    for i in text:
        a+=1
        str2+=str_a2str[i]
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_str_2str:处理完成")
    return str2
    
def to_2str_str(b,bt=8):  #01转字符
    return_str=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_2str_str:正在处理中...")
    for i in range(0,len(b),bt):
        a+=1
        return_str+=a2str_str[b[i:i+bt]]
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_2str_str:处理完成")
    return return_str
    


def to_str_2(b,bt=8):  #字符转二进
    return to_2str_2(to_str_2str(b),bt=bt)

def to_2_str(b,bt=8):  #二进制转字符
    return to_2str_str(to_2_2str(b,bt=bt))



def to_x16str_2str(b,bt=2):  #16进制转01
    kj2=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_x16str_2str:正在处理中...")
    for i in range(0,len(b),bt):
        a+=1
        kj2+=ax16_a2str[b[i:i+bt]]
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_x16str_2str:处理完成")
    return kj2

def to_2str_x16str(b,bt=8):  #01转16进制
    kj2=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_2str_x16str:正在处理中...")
    for i in range(0,len(b),bt):
        a+=1
        kj2+=a2str_ax16[b[i:i+bt]]
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_2str_x16str:处理完成")
    return kj2


def to_x16str_2(b,bt=2):  #16进制转二进制
    kj2=b""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_x16str_2:正在处理中...")
    for i in range(0,len(b),bt):
        a+=1
        kj2+=int(ax16_a2str[b[i:i+bt]],2).to_bytes(1,'big')
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}/10%",end="\r")
    if TF:
        print("to_x16str_2:处理完成")
    return kj2
    
def to_2_x16str(b,bt=8):  #二进制转16进制
    kj2=""
    a=0;c=len(b);TF=(c>=1024**TF_B) and TF_p
    if TF:
        print("to_2_x16str:正在处理中...")
    for i in b: #class_i:int; class_b:bytes
        a+=1
        kj2+=a2str_ax16[format(i,f"0{bt}b")]
        if TF:
            print(f"{a}/{c}#{int(a/c*1000)/10}%",end="\r")
    if TF:
        print("to_2_x16str:处理完成")
    return kj2

class iox16(): #16进制编辑工具
    def __init__(Iox16,TF_p=TF_p,TF_print_h=True):
        Iox16.help="h:查看帮助\nls:查看所有值\nls 序号a:查看序a号的值\n序号a 值:修改序号a的值，00~FF\nexit:退出"
        if TF_print_h:
            print(Iox16.help)
        
        Iox16.命令列表=[]
        Iox16.path_print=">x16>"
        Iox16.run=Iox16.执行命令
        Iox16.TF_p=TF_p
        Iox16.file_path=""
        Iox16.file=bytearray() #创建bytearray类型
     
    def iox16_open_file(Iox16,file_path,bt=8):
        try:
            with open(file_path,"rb") as file:
                Iox16.file_path=file_path
                #class_Iox16.file :bytearray
                Iox16.file=bytearray(file.read())
        except Exception as Ex:
            print(f"iox16_open:打开文件时发生错误[{Ex}]")
    
    def iox16_return(Iox16):
        return bytes(Iox16.file)
    
    def iox16_write(Iox16):
        try:
            with open(Iox16.file_path,"wb") as file:
                file.write(bytes(Iox16.file))
        except Exception as Ex:
            print(f"iox16_write:在写入文件时发生错误[{Ex}]")
    
    def close(Iox16):
        Iox16.__init__(TF_print_h=False)
    
    def 执行命令(Iox16,命令=None):
        命令= 命令 if 命令 and 命令 !="\r" else input(Iox16.path_print)
        命令列表=命令.split(" ") 
        命令长度=len(命令列表)
        if not 命令列表[0]:
            return None
        elif 命令列表[0]=="ls":
            if 命令长度 == 1:
                print("翻页查看，exit退出，回车下一页")
                for i in range(0,len(Iox16.file)): # class_i:int
                    print(str(i)+":"+to_2str_x16str(format(Iox16.file[i],'08b')))
                    if i%20==0 and i>=20:
                        if input(">") == "exit":
                            break
            elif 命令长度==2:
                print(to_2str_x16str(format(Iox16.file[int(命令列表[1])],'08b')) if int(命令列表[1]) <= len(Iox16.file) else f"没有序号{命令列表[1]}")
            #
        elif 命令列表[0]=="exit":
            return "exit"
        elif 命令列表[0]=="h":
            print(Iox16.help)
        elif 命令列表[0].isdigit(): #判断是否为非负整数
            命令列表0=int(命令列表[0])
            file_len=len(Iox16.file)
            if (-file_len <= 命令列表0 <= file_len) or (命令列表0+1 > len(Iox16.file) and 命令列表0 <= file_len) or 命令列表[0]=="0" :
                if 命令长度==2:
                    if 命令列表[1] in ax16_a2str:
                        #bytearray[0]=int
                        if 命令列表0+1 > file_len:
                            Iox16.file.append(int(to_x16str_2str(命令列表[1]),2))
                        else:
                            Iox16.file[命令列表0]=to_x16str_2(命令列表[1])[0]
                    else:
                        print("iox16:无效值")
                else:
                    print("iox16:无效值")
            else:
                print("iox16:无效序号")
        else:
            print("iox16:无效命令")
        #


init()

"""
#字符串转单字节
s = "11001101"
b = int(s, 2).to_bytes(1, 'big')   # b'\xcd' 占 1 字节
print(b)
#单字节转字符串
s = format(b[0], '08b')     # '11001101'
"""
"""
from collections import Counter
c = Counter(ap_str)
dups = {k: v for k, v in c.items() if v > 1}
print(dups)
print("重复字符总数：", sum(v - 1 for v in c.values() if v > 1))
"""