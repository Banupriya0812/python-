def longest_unique_substring(s):
    start=0
    max_length=0
    used_chars={}
    longest_substr=""

    for i, char in enumerate(s):
        if char in used_chars and used_chars[char]>=start:
            start=used_chars[char]+1
        used_chars[char]=i
        if i-start+1>max_length:
            max_length=i-start+1
            longest_substr=s[start:i+1]
    return longest_substr,max_length

input_str="maadhava"
result,length=longest_unique_substring(input_str)
print("longest substring without repeating characters:",result)
print("length:",length)