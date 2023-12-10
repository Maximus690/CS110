import sys
def mult():
    args = [float(sys.argv[i]) for i in range(1,5)]
    return args[0]*args[1]*args[2]*args[3]

def main():
    print(mult())



if __name__ == '__main__':
    main()
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
