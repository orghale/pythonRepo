print("This will always be run")


def main():
   # pass
    print("First module's Main Method: {}".format(__name__))

if __name__=='__main__':
    main()
    #print("Run Directly")
#else:
    #print("Second module's name: {}".format(__name__))
