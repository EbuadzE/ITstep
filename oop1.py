#Book კლასის ფუნქციაში ხდება წიგნის მახასიათებლების გაწერა, კერძოდ: სახელი, ავტორი, წელი
class Book:
    def __init__ (self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
# რეპრ მეთოდი გამოიყენება პითონის პროგრამის მიერ წიგნის მახასიატებლების თვალსაჩინოდ დასაბეჭდად.
    def __repr__(self):

        return f"წიგნი ({self.name!r}, {self.author!r}, {self.year!r})"

#იქმნება BookManager კლასი სადაც მეთოდების სახით ხდება აუცილებებლი ფუნქციონალის გაწერა, კერძოდ: წიგნის დამატება, ბიბლითეკის ჩვენება, წიგნის ძებნა.
class BookManager:
    def __init__(self):
        self.books = []
#წიგნის დამატების მეთოდი სადაც ვიძახებთ ბუქ კლასს და გადავაწოდებთ არგუმენტებს რომელიც შემდომ ემატება self.books ლისტს.
    def add_book(self, name, author, year):
        new_book = Book(name, author, year)
        self.books.append(new_book)
        print (f"{new_book} დაემატა ბიბლიოთეკას")
#აჩვენებს ლისტში არსებულ წიგნებს ცალ-ცალკე, თუ არცერთი წიგნი არაა აძლევს მომხმარებელს შესაბამის ინფორმაციას
    def show_books(self):
        if not self.books:
            print("ბიბილიოთეკაში წიგნები არ არის")
        else:
            for i in self.books:
                print (i)
#ეძებს წიგნის ლისტში სახელით. სახელის გადაწოდება ხდება სერჩ მეთოდის არგუმენტად.
    def search_book(self, name):
        found_book = [book for book in self.books if name.lower() in book.name]
        if found_book:
            for book in found_book:
                print(f"მოიძებნა {book}") #თუ დასახელების წიგნი არის ბიბლიოთეკაში ბეჭდავს მას
        else:
            print("ამ დასახელების წიგნი ვერ მოიძებნა ბიბლიოთეკაში") #თუ მითითებული წიგნი ვერ მოიძებნა მომხმარებელს აწვდის ამ შეტყობინებას


bookmanager = BookManager()

while True:
    print("მოგესალმებით თქვენ ხართ ბიბლიოთეკის აპლიკაციაში") #განსაზღვრულია მომხარებლის ფუნქციონალი
    action = input("""აირჩიეთ შემდეგი მოქმედება "
                   "1) - წიგნის დამატება,"
                    2) - ბიბლიოთეკის ჩვენება"
                    3) - წიგნის ძებნა"
                    4) - აპლიკაციიდან გასვლა    
                        """ ).strip().lower()

    if action == "1":   #წიგნის ჩაამტების შემთხვევაში მისათითებელი მონაცემები
        chamateba1 = input("შეიყვანე სახელი   ").strip().lower()
        chamateba2 = input("შეიყვანე ავტორი    ").strip().lower()
        chamateba3 = int(input("შეიყვანე წელი   ").strip().lower())
        if chamateba3 > 2025:
            print("შეიყვანეთ სწორი წელი!!!") #თუ არარეალისტური წელი შეიყვანა ანუ 2025 წელს ზემოთ
        else:
            bookmanager.add_book(chamateba1, chamateba2, chamateba3) #ამატებს წიგნს მითითებული მონაცემებით

    elif action == "2":
        bookmanager.show_books()   #ბიბლიოთეკის ჩვენება

    elif action == "3":
        search = input("შეიყვანეთ წიგნის სახელი   ").strip().lower()
        bookmanager.search_book(search)      #წიგნის მოძებნა სახელით

    elif action == "4":   #პირობითი მომხარებლის ინტერფეისიდან გამოსვლა
        print("თქვენ დატოვეთ ბიბლიოთეკის აპლიკაცია, ნახვამდის!")
        break

    else:
        print("არასწორი არჩევანია, უნდა აირჩიოთ (1-4) მოქმედება.")  #შეტყობინება არავალიდური ფუნქციონალის მითითებისას




