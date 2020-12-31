import os

image_files = []
os.chdir(os.path.join("data", "Person_90"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/Person_90/" + filename)
os.chdir("..")
with open("train_1203.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")