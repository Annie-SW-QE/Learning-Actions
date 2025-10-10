phrase = "I'm a barbie girl, I hate this stupid wooooorrrrllld."
print(phrase)

with open("printed_text.txt","w") as f:
    f.write(phrase)
    f.close()