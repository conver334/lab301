import numpy as np
import pandas as pd

readfile = 'PUBLISH.csv'
lines = pd.read_csv(readfile).values

llen = len(lines) 
print(llen)
fp = open('./_data/sources_test.yaml', 'w') 
for i in range(llen):
    str1=("- id: "+lines[i][0]+"\n")
    fp.write(str1)
    str1=("  image: images/paperimage/"+lines[i][1]+"\n")
    fp.write(str1)
    str1=("  tags:\n")
    fp.write(str1)
    str1=("    - "+lines[i][2]+"\n")
    fp.write(str1)
    if str(lines[i][3])!="nan":
        str1=("  extra-links:\n")
        fp.write(str1)
        str1=("    - type: source\n")
        fp.write(str1)
        str1=("      link: "+str(lines[i][3])+"\n")
        fp.write(str1)
    str1=("\n")
    fp.write(str1)
fp.close()  # 关闭文件

   