#2. Описать класс Книга. (год, название, автор) Описать метод __eq__  для сравнения
#>> book1 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
#>> book2 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
#>> book3 = Book(‘Над пропастью во ржи’, 1951, ‘Jerome David Salinger’)
#>book1 == book2
#True
#>>book1 == book3
#alse
#Добавить поле с отзывами и методы добавить отзыв, посмотреть все отзывы.
#>>book1.add_review(‘Cool!!’)
#>>book1.add_review(‘Not bad’)
#>>book1.show_reviews()
#.
#Cool!!
#2.
#Not bad


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self._feedb = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'name: {}\nname: {}\nyear: {}\nauthor:{}'.format(self.name, self.year, self.author)

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year and self.author == other.author:
            return print('True')
        else:
            return print('False')

    def add_review(self, feedb):
        self.feedb = feedb
        print('Adding feedback:', self.feedb, '\nDone')
        return self._feedb.append(self.feedb)

    def del_review(self, feedb):
        self.feedb = feedb
        if self._feedb.__contains__(self.feedb):
            print('Deleting Feedback: ', self.feedb, '\nDone')
            return self._feedb.remove(self.feedb)

        else:
            print('Add this feedback before deleting')

    def show_reviews(self):
        print('List of feedback of ibject:')
        for k in range(len(self._feedb)):
            print('{}.\n{}'.format(k+1, self._feedb[k]))
        return self._feedb

book1 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book3 = Book('Над пропастью во ржи', 1951, 'Jerome David Salinger')

book1 == book2
print('*'* 40 )
book1 == book3
print('*'* 40 )
book1.add_review('Cool!!')
print('*'* 40 )
book1.add_review('Not bad')
print('*'* 40 )
book1.add_review('Not so Cool!!')
print('*'* 40 )
book1.show_reviews()
print('*'* 40 )
book1.del_review('Cool!!')
print('*'* 40 )
book1.show_reviews()
print('*'* 40 )
book1.del_review('Cool!!!!!!!!!!!!!!!')

