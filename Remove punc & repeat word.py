#REMOVE PUNCTUATIONS AND REPEATED WORDS

punctuations='''!()-[]{};'"\,<>/?@#$%^&*_~.,'''

my_str= " 'python' is a programming language ,& python is the wide language,@! it is a easy to learn* #&python is the use to enalyse the data"

no_punct=""
for char in my_str:
   if char not in punctuations:
      no_punct=no_punct+char
print(' '.join(dict.fromkeys(no_punct.split())))






























