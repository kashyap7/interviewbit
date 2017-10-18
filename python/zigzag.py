def zigzag(A, B) :
    if B == 1:
        return A
    row = B * ['']
    which_row = 0
    down_slant = -1
    for i in range(len(A)) :
        # if my_count%B == 0 :
        #     my_count +=2
        print "which_row: ", which_row, "down_slant: ", down_slant, "i: ", i
        row[which_row] += A[i]
        if which_row == B - 1 :
            down_slant *= -1
        if which_row == 0 :
            down_slant *= -1
        which_row += down_slant
    output = ""
    print row
    for i in range(B) :
        output += row[i]
    return output
print zigzag("PAYPALISHIRING", 3)
print zigzag("ABCD", 2)
A = "kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
print zigzag(A, 1)