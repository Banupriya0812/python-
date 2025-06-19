def is_first_last_same(s):
    s=s.strip().lower()
    if len(s)>1:
       return False
    return s[0]==s[-1]
word="maadhhdaam"
if is_first_last_same(word):
    print("first and last words are same ")
else:
    print("first and last words are different ")
