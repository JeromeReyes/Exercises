def remove_dup(inputList):
    list(set(inputList))
    s = set()
    remove_dup = list(set(inputList) - set(s))

    print(remove_dup)
    return remove_dup

def main():
    while True:
        try:
            l1 = input("enter list:")
            if (len(l1) < 1):
                print ("Please Enter a List")
            else:
                remove_dup(l1)

        except KeyboardInterrupt:
            return False

if __name__=='__main__':
    main()