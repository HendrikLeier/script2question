import textract
import os


raw = []
source_directory = "/script_data"
for filename in os.listdir(source_directory):
    if filename.endswith(".pdf"):
        print("Processing " + filename)
        raw.append(textract.process(source_directory + "/" + filename))

print(raw)

file = open("/script_data/extracted.txt", "wb")
for text in raw:
    file.write(text)
file.close()
