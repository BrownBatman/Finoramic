from pip._internal import main as pipmain
import json
import sys
def installer(package):
    pipmain(['install',package])
    package1 = package[:package.find('=')]
    #print (package1)
    try:
        __import__(package1)
    except ImportError:
        print(package)
c = (json.loads(open('Package.json').read()))
l = c['Dependencies']
for i in l:
    installer(i)
