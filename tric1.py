# num = [1,2,3,4]
# #using for loop
# squared = []
# for n in num:
#         squared.append(n**2)
# print(squared)#output:[1, 4, 9, 16]
# ======== another method using lambda function===
# using map built-in function inside lambda function
# num = [1,2,3,4]
# squared = list(map(lambda x : x**2,num))
# print(squared)#output:[1, 4, 9, 16]
# ========= process test data using regular expressions 
#extract data from text using re:
# import re
# text = "meeting on 12/08/2023 and 15/09/2035"
# date = re.findall(r"\d{2}/\d{2}/\d{4}",text)#no spaces output:
#['12/08/2023', '15/09/2035']
# print(date)
# import re
# text = "meeting on 12/08/2023 and 15/09/2035"
# date = re.findall(r"\d{2}/\d{2}/\d{4}", text)
# print(date)#output:['12/08/2023', '15/09/2035']
"""
You said:
import re
text = "meeting on 12/08/2023 and 15/09/2035"
date = re.findall(r"\d{2}/\ d {2} /\ d{4}",text)
print(date) why output is empty []
ChatGPT said:
Your output is empty because the regular expression is written incorrectly.
What’s wrong in your regex?
You wrote:
r"\d{2}/\ d {2} /\ d{4}"
Problems:
There are spaces inside the pattern (\ d {2} and /\ d{4}).
\d must be written together (no space).
\d → means a digit
\ d → means “space + d” ❌
So your regex does not match any date, resulting in [].
Correct regex
Dates like 12/08/2023 follow this pattern:
\d{2}/\d{2}/\d{4}
Fixed code
import re
text = "meeting on 12/08/2023 and 15/09/2035"
date = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print(date)
Output
['12/08/2023', '15/09/2035']
Tip for exams / learning regex
\d → digit (0–9)
{2} → exactly 2 times
{4} → exactly 4 times
/ → literal slash
If you want, I can also show:
how to validate dates (not just match format)
how to use re.search vs re.findall
how to extract day, month, year separately
"""
# ========= replace all digits with x =====
# import re
# text ="my number is 07230306"
# new_text  = re.sub(r"\d","x",text)
# print(new_text)#output:my number is xxxxxxxx
# ==============================================
import re
phone = "9655 543 210"
print(bool(re.fullmatch(r"\d{10}", phone)))
print(phone)#output:
# False
# 9655 543 210
# ========= find all numbers in text ========
import re
text = "order 123 cost 456 dollars"
nums = re.findall(r"\d+",text)
print(nums)# output: ['123', '456']
# ====== find all emails addresses =====
import re
test = "contact us at help@gmail.com or admin@yahoo.com"
# emails = re.findall(r"\s+@\st", test)
# print(emails)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", test)
print(emails)#output:['help@gmail.com', 'admin@yahoo.com']
"""Skip to content
Chat history



You said:
import re
test = "contact us at help@gmail.com or admin@yahoo.com"
emails = re.findall(r"\s+@\st", test)
print(emails) why output []
ChatGPT said:
Your output is empty because the regex pattern is wrong. Let’s break it down clearly 👇
Your code
import re
test = "contact us at help@gmail.com or admin@yahoo.com"
emails = re.findall(r"\s+@\st", test)
print(emails)
Why it returns []
Your pattern:
\s+@\st
means:
\s+ → one or more spaces@ → literal @
\s → a space
t → the letter t
So it’s trying to match something like:
"   @ t"
That sequence does not exist in your string, so nothing is found.
✅ Correct regex to extract email addresses
Use this instead:
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", test)
print(emails)
Output
['help@gmail.com', 'admin@yahoo.com']
🔍 Explanation of the correct pattern
[a-zA-Z0-9._%+-]+ → username part
@ → at symbol
[a-zA-Z0-9.-]+ → domain name
\. → dot
[a-zA-Z]{2,} → domain extension (com, net, etc.)
If you want:
Simpler regex
Validation vs extraction
Step-by-step regex practice
just tell me 👍
Do you like this personality?

"""



