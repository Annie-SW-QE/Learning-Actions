import os
phrase = "I am a barbie girl I hate this stupid wooooorrrrllld"
print(phrase)
os.makedirs("artifacts")
with open("artifacts/printed_text.txt","w") as f:
    f.write(phrase)
    f.close()
    