from base64 import encode
from encodings import utf_8

get_sentence="ഇവിടെ ഒരു"
unicode_name = get_sentence
# .encode(encoding="utf-8",errors="xmlcharrefreplace").decode(encoding="utf-8",errors="xmlcharrefreplace")
print(unicode_name)
f = open("captured_text.txt", "w",encoding="utf_8")
f.write(unicode_name)
f.close()
