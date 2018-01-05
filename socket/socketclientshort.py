
import socket
import time
from collections import Counter


def add_two_dicts(x, y):
    return Counter(x) + Counter(y)

def list_to_dict(list_str):
    list_items = list_str.split(" ")
    result_dict = {}
    for item in list_items:
        # apple,4
        items = item.split(",")
        result_dict[items[0]] = int(items[1])

    return result_dict

# create a socket object
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hostname on the port.
s1.connect(('210.100.235.128', 3456))
s2.connect(('210.100.235.128', 3457))
s3.connect(('210.100.235.128', 3458))
#s1.connect(('192.168.0.3', 9999))
#s2.connect(('192.168.0.4', 9999))
#s3.connect(('192.168.0.5', 9999))


f = open("output_htmlrfc_noun.txt", 'r')
data_str = f.readline()
strarr = data_str.split(" ");
strlen = len(strarr)
data_per_machine = (int)(strlen/4)

i = 0
A = [] # 1번 라즈베리
B = [] # 2번 라즈베리
C = [] # 3번 라즈베리
D = [] # 클라이언트 노트북

while strlen>i:
    if i < data_per_machine: # 0 1 2
        A.append(strarr[i])
    elif i >= data_per_machine*3: # 9 10 11 12
        D.append(strarr[i])
    elif i >= data_per_machine*2: # 6 7 8
        C.append(strarr[i])
    elif i >= data_per_machine: # 3 4 5
        B.append(strarr[i])

    i += 1

begin = time.time()

print("시작시간")
print(time.clock())
s1.send(" ".join(A).encode())
print("A에 송신한 이후 시각")
print(time.clock())
s2.send(" ".join(B).encode())
print("B에 송신한 이후 시각")
print(time.clock())
s3.send(" ".join(C).encode())
print("C에 송신한 이후 시각")
print(time.clock())

dict4 = dict()
for i in D:
    dict4[i] = dict4.get(i, 0) + 1

#msg1 = recv_timeout(s1)

print("A에게 받기 전 시각")
print(time.clock())
list_str1 = s1.recv(102400)
print("A에게 받은 이후 시각")
print(time.clock())
list_str2 = s2.recv(102400)
print("B에게 받은 이후 시각")
print(time.clock())
list_str3 = s3.recv(102400)
print("C에게 받은 이후 시각")
print(time.clock())

dict1 = list_to_dict(list_str1.decode())
dict2 = list_to_dict(list_str2.decode())
dict3 = list_to_dict(list_str3.decode())

#print(list_str1.decode())

#print(dict1)
#print(dict2)
#print(dict3)
#print(dict4)

dict4 = add_two_dicts(dict4, dict1)
dict4 = add_two_dicts(dict4, dict2)
dict4 = add_two_dicts(dict4, dict3)

s1.close()
s2.close()
s3.close()
#print(msg1)
#print(msg1.decode('ascii'))
#print(msg2.decode('ascii'))
#print(msg3.decode('ascii'))
print(dict4)
end = time.time()
print(end - begin)
