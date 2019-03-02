# 打开文件  
file = open("/sys/class/thermal/thermal_zone0/temp")
# 读取结果，并转换为浮点数  
temp = float(file.read()) / 1000
# 关闭文件  
file.close()
# 向终端控制台打印  
print("temp : %.3f" %(temp))
