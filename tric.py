# for j in range (3, 0, -1):
#         print(j)
#         print(2*j +1)
# import cv2
# img = cv2.imread("htmlback.jpeg",0)
# mean = img.mean()
# gain = 150/mean
# fixed = cv2.convertScaleAbs(img, alpha=gain)
# print ("old mean: ", int(mean))
# print("new mean: ", int(fixed.mean()))
# cv2.imwrite("brightened.jpeg", fixed)
#output:
# old mean:  160
# new mean:  150
# =========== remove extra spaces ======
# import re

# from bleach import clean
# text = 'this  has extra  spaces'
# text = re.sub(r"\s+"," ",text).strip()
# print(text)
# import re

# text = 'this     has    extra     spaces'
# text = re.sub(r"\s+", " ", text).strip()
# print(text)#output:this has extra spaces
"""
You said:
import re
from bleach import clean
text = 'this  has extra  spaces'
text = clean.sub(r"\s + "," ",text)
print(text)     /usr/local/bin/python3 "/Users/michelkadi/python Tim/tric.py"
Traceback (most recent call last):
  File "/Users/michelkadi/python Tim/tric.py", line 20, in <module>
    text = clean.sub(r"\s + "," ",text)
           ^^^^^^^^^
AttributeError: 'function' object has no attribute 'sub' remove extra spaces
ChatGPT said:
You’re getting that error because clean is a function from the bleach library, not the re module.
Only the re module has .sub().
So this line is wrong:
text = clean.sub(r"\s + "," ",text)
✅ Correct way (using re)
To remove extra spaces, use re.sub():
import re
text = 'this  has extra  spaces'
text = re.sub(r"\s+", " ", text)
print(text)
Output:
this has extra spaces
❌ Why your code failed
from bleach import clean
clean → a function
Functions do not have .sub()
Hence:
AttributeError: 'function' object has no attribute 'sub'
🧠 Regex explanation
\s+ → matches one or more whitespace characters
Replaces multiple spaces with one single space✅ Optional: remove leading/trailing spaces too
text = re.sub(r"\s+", " ", text).strip()
If you want, I can also show:
how to do this without regex
or when bleach.clean() is actually useful 👍
Is this conversation helpful so far?
"""

