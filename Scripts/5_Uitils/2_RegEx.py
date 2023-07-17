import re

stringa1 = "Str1nga d1provA!"
stringa2 ="SoloLettere"
email = "simone.tomboli@ni@gmail.com"
password= "Password11!"
r = re.search("", stringa1)
print (r)

#inizia con una lettera maiuscola
r= re.search("^[A-Z]", stringa1)
print (r)

#trova finche non ha trovato un carattere non alfabetico
r = re.search("[a-zA-Z]*", stringa1)
print (r)

#per controllare che sia solo caratteri dell'alfabeto
r = re.search("^[a-zA-Z]*$", stringa1)
print(r)

r = re.search("^[a-zA-Z]*$", stringa2)
print(r)

#regex per controllare il dominio di una mail
r= re.search("[@].*$", email)
print(r)
r= re.search("^[A-Za-z\d._-]*@gmail.com", email)
print(r)

#password con alemto 6 max 20 caratteri una maiuscola una minuscola e un carattere fra ! e ?
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
r = re.search(reg, stringa2)
print(r)
r = re.search(reg, password)
print(r)



