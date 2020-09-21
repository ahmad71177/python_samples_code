import xml.etree.ElementTree as ET
tree = ET.parse('mydata.xml')
root = tree.getroot()
i = 1
a=[]
b=[]
c=[]
print("yaw:")
for x in root.findall('result'):
        yaw = x.find('yaw').text
        a.append(float(yaw))
        print(yaw)
z1=a[80]-a[0]
print("different_yaw(n)_yaw(0)=" + str(z1))
print("pitch:")
for x in root.findall('result'):
        pitch = x.find('pitch').text
        b.append(float(pitch))
        print(pitch)
z2=b[80]-b[0]
print("different_pitch(n)_pitch(0)=" + str(z2))
print("roll:")
for x in root.findall('result'):
        roll = x.find('roll').text
        c.append(float(roll))
        print(roll)
        
print(roll)
z3=c[80]-c[0]
print("different_roll(n)_roll(0)=" + str(z3))

