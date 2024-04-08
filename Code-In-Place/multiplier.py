def main():
    """
    You should write your code here. 
    """
    var = input("Enter a number: ")
    curr_value = int(var)
    while curr_value < 128:
        if curr_value % 2 == 0:
            curr_value = curr_value * 2
            print(curr_value)
    
if __name__ == '__main__':
    main()