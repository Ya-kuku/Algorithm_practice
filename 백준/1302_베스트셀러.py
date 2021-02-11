N = int(input())
books = dict()
for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    elif books[book]:
        books[book] += 1
Max = max(books.values())

find = []
for book, cnt in books.items():
    if cnt == Max:
        find.append(book)
print(sorted(find)[0])

# bookitem = list(books.items())
# bookitem.sort(key=lambda x:(-x[1],x[0]))
