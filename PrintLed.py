def print_led(nums):
    """
    Takes numerical inputs and prints them as a 15-led screen
    """
    nums = str(nums)

    zero = " #### ## ## ####"
    one = "   #  #  #  #  #"
    two = " ###  #####  ###"
    three = " ###  ####  ####"
    four = " # ## ####  #  #"
    five = " ####  ###  ####"
    six = " ####  #### ####"
    seven = " ###  #  #  #  #"
    eight = " #### ##### ####"
    nine = " #### ####  ####"
    
    allnum = [zero, one, two, three, four, five, six, seven, eight, nine]
    for num in nums:
        print(allnum[int(num)][1],end=" ")
        print(allnum[int(num)][2],end=" ")
        print(allnum[int(num)][3],end=" ")
        print("  ",end="")
    print("")
    for num in nums:
        print(allnum[int(num)][4],end=" ")
        print(allnum[int(num)][5],end=" ")
        print(allnum[int(num)][6],end=" ")
        print("  ",end="")
    print("")
    for num in nums:
        print(allnum[int(num)][7],end=" ")
        print(allnum[int(num)][8],end=" ")
        print(allnum[int(num)][9],end=" ")
        print("  ",end="")
    print("")
    for num in nums:
        print(allnum[int(num)][10],end=" ")
        print(allnum[int(num)][11],end=" ")
        print(allnum[int(num)][12],end=" ")
        print("  ",end="")
    print("")
    for num in nums:
        print(allnum[int(num)][13],end=" ")
        print(allnum[int(num)][14],end=" ")
        print(allnum[int(num)][15],end=" ")
        print("  ",end="")
    print("")

# TEST:
print_led(502934029387849)