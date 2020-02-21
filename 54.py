import re

email="anukul@gmail.com hi@anukul.com"
pattern="\w+@(\w+).com"
ans=re.findall(pattern,email)
print(ans)

