slang = {'gr8':'great','btw':'by the way','imho':'in my huble opinion','jk':'just kidding','l8r':'later','np':'no problem','r':'are','u':'you','y':'why','ttyl':'talk to you later','l8':'late','atm':'at the moment','lmk':'let me know','np':'no problem','tia':'thanks in advance','brb':'be right back'}

usrInput = raw_input('SMS: ')

punct = ""

if usrInput[-1] in ".?!,;:":
    punct = usrInput[-1]
    usrInput = usrInput.rstrip()
    

for slang, word in slang.items():
    usrInput = usrInput.replace(slang, word)

print usrInput
