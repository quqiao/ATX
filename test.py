#coding=utf-8

'''
a = [1,2,3,4,5,6,7,8,9,10]

print a[:5]
print a[5:]
print a[1:5]
print a[5:9]
print a[-5:-1]
'''
# import threading
# import time
#
# def long1():
#
#     print "a"
#     print time.time()
#
# def long2():
#     print "b"
#     print time.time()
#
# threads1 = []
# t1 = threading.Thread(target=long2)
# threads1.append(t1)
# t2 = threading.Thread(target=long1)
# threads1.append(t2)
# for t in threads1:
#     t.start()

import os
import sys
type = sys.getfilesystemencoding()

package_path = raw_input("package_path:")
cmd = 'python -m atx apkparse ' + package_path
decode = cmd.decode('utf-8').encode(type)
print decode
resultGet = os.popen(decode).read()
print resultGet
dictoration = eval(resultGet)
print dictoration
activity_name = dictoration.get('main_activity')
package_name = dictoration.get('package_name')
print activity_name
print package_name


# cmd="adb devices"
# resultGet=os.popen(cmd).read()
# print resultGet
# listStr=resultGet.split("\n")
# subList=listStr[1].split("\t")
