import random

def read():
    list=[]
    with open("../DataBase/data.txt","r",encoding="utf-8") as f:
        for line in f:
            list.append(line)
    return list[random.randint(1,170)]





def run():
    pass

if __name__ == "__main__":
    run()
