def prova():
    print(__name__)
    if __name__=='__main__':
        print("sto eseguendo direttamente questo script")
    else:
        print("questo script è eseguito da un import")  

if __name__=='__main__':
    print("Run")