# f = open("/home/guerzhoy/Desktop/ESC180/lec/w07/versedog.txt") # accessing local files on linux
# "/Users/username/...whatever the folder and files are
# for Mac
# also only works locally, not gonna work if Gradescope is reading the file

# in general
f = open("hello.txt")
text = f.read()

L = "A!!B!!C".split("!!")
"!!".join(L)

text.split("\n")[0].split()

for line in text.split("\n"):
    print(line)

def get_sentence(text):
    text = text.replace("!", ".").replace("?", ".")
    return text.split(".")

def words_per_sentence(text):
    sentences = get_sentences(text)
    words = text.split()
    return len(words)/len(sentences)

english_txt = open("losttime_en.txt", encoding = "latin1")
# read text file with each 8bit as a different character
# doesn't work well for french text (accented characters are not 8bit)

french_txt = open("losttime.txt_fr", encoding = "latin1"),read()

print(words_per_sentence)