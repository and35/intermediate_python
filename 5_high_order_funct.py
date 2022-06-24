def run ():

    #filter
    my_list = [1,2,6,6,9,13,19,21]
    odd = filter(lambda x: x%2 != 0, my_list)
    print(odd)
    odd= list(odd)
    print(odd)

    # map
    my_list = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list))
    print(squares)

    # reduce
    from functools import reduce
    my_list = [2,2,2,2,2]
    mult = reduce(lambda a,b: a*b, my_list )
    print(mult)



if __name__ == "__main__": 
    run()

