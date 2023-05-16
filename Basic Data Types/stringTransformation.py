#String is datatype that enclosed with "" or ''
#Note: Strings cannot be​ concatenated with numbers

#str.replace() is used to replace 
#str.lower() is the lower
#str.upper() is the upper
#str.strip() is used to strip all whitespace from strings
#str.split() is used to split strings
#str.join() is used to join strings
#str.find() is used to find
#str.count() is used to count
#str.startswith() is used to find strings that start with 
#str.endswith() is used to find strings that end with \
#str.format() is used to format strings 

def getStr(s):
  s=s[:1] + s[0] + s[1:]# Transform the string 
  s=s[:1] + s[0] + s[1:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]
  # Update the length of string
  strlen = len(s)
  return [s, strlen]