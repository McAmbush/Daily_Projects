while True:
    
    print("\t\t\tFACTORIAL CALCULATOR\n")
    num=int(input("Enter the number\n"))
    fact=1
    for i in range(num):
        fact*=num
        num-=1
    print("The factorial of entered number is ")
    print(fact)
    op=input("\nEnter y to continue")
    if op not in 'y':
        break
