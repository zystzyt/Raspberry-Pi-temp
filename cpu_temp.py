#打开核心温度文件
file=open("/sys/devices/virtual/thermal/thermal_zone0/temp")
#读取文件内数值并转换
temp=float(file.read())/1000
#关闭文件
file.close()
#打印输出
print("temp:%.3f'C"%(temp))
