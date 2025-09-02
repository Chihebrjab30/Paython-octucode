library=[]
wish_list=[]
book=input("Enter a book you own ")
library.append(book)
book=input("Enter another writer or skip ")
if book:
    library.append(book)
print("\nYour library is in it",library)

wish=input("Enter the book you want to get ")
wish_list.append(wish)
wish=input("Add another book you want or skip ")
if wish:
    wish_list.append(wish)
print("\n The wish list is",wish_list)

get=input("Enter a book from your wish list that you have already obtained, or do not skip.")
if get in wish_list:
    library.append(get)
    wish_list.remove(get)
print("\nupdate library",library)
print("\nupdate wish_list",wish_list)
donate=input("Is there a book from your library you would like to donate? Or skip ")
if donate in library:
    library.remove(donate)
print("\nYour library",library)
print("\nYour wish list",wish_list)


