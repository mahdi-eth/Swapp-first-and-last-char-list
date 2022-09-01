def swaper(list):
    print("This is your list : ",list)
    first = list[0]
    last = list[-1]
    list[0] = last
    list[-1] = first
    print("This is your swapped list(first item with the last item) : ",list)

list_string = input("make a list and seprate the items with space : ")
swaper(list_string.split(" "))