# ques 1

f = open("poem.txt")
done = f.read()
if "twinkle" in done:
    print("The word twinkle lies in poem.txt")

else:
    print("The word twinkle not lies in poem.txt")
# print(done)
f.close()

with open("myFile.txt") as f:
    print(f.read())

with open("poem.txt") as f:
    done = f.read()
    if "twinkle" in done:
        print("The word twinkle lies in the file poem.txt")
        
    else:    
        print("The word twinkle not lies in the file poem.txt")

# ques 2

import random

def game():
    print("We are going to generate random number")
    score = random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)

        else:
            hiscore = 0

    print(f"Your score is {score}")

    if score > hiscore:
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))

    return score 

game()

# ques 3

def generate_table(n):
    table = ""
    for i in range(1,11):
        table += (f"{n} x {i} = {n*i}\n")

    with open(f"tables/table_{n}.txt" , "w") as f:
        f.write(table)

for i in range(2,21):
    generate_table(i)

# ques 4

word = "donkey"

with open("word.txt") as f:
    done = f.read()
    if word in done:
        new = done.replace(word , "######")
    with open("word.txt" , "w") as f:
        f.write(new)

# ques 5

words = ["donkey" , "chutiya" , "madrchod" , "budhu"]

with open("word.txt") as f:
    done = f.read()
    for word in words:
        done = done.replace(word , "#"*len(word))
    with open("word.txt" , "w") as f:
         f.write(done)

# ques 6

word = "python"
with open("log.html") as f:
    done = f.read()

if word in done:
    print("The python word present in the log html file")

else:
    print("The python word is not lies in the log html file ")

# ques 7

word = "python"
with open("log.html") as f:
    lines = f.readlines()

line_num = 1
for line in lines:
    if(word in line):
        print(f"The python word is lies in: {line_num}")
        break
    line_num += 1

else:
    print("The python word is not lies in the log html file ")

# ques 8

with open("new.txt") as f:
    done = f.read()

with open("Copy_new.txt" , "w") as f:
    f.write(done)

# ques 9

with open("new.txt") as f:
    done_1 = f.read()

with open("Copy_new.txt") as f:
    done_2 = f.read()

if done_1 == done_2:
    print("Both files are matches")

else:
    print("Both files data are different")

# ques 10

with open("Copy_new.txt" , "w") as f:
    f.write("")

# ques 11

with open("new.txt") as f:
    done = f.read()

with open("renamed_by_python.txt" , "w") as f:
    f.write(done)