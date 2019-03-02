# 打开文件  
file=open("/sys/class/thermal/thermal_zone0/temp")
# 将读取结果并转换为浮点数  
temp=float(file.read())/1000
# 关闭文件  
file.close()
# 打印结果  
print("temp:%.3f℃"%(temp))
