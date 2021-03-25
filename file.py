def summ(num1,num2):
    return num1+num2

print(summ(5,6))


def palendrime(something):
    reverse = something[::-1]
    if something == reverse:
        print("Hey yoyo!")
    else:
        print("nothing")
        
palendrime("aibohphobia")


def counter():
    sentence = input("Please enter any sentence")
    counter = dict()
    for x in sentence:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] +=1

    print(counter)
counter()

def substract(num1,num2):
    return num1-num2
substract(10,6)

