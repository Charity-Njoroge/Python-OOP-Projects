""" A program that returns a formatted bibliography of a book """
import operator


class Book(object):
    def __init__(self, authorFirst, authorLast, title, year, publisher, place):
        self.authorFirst = authorFirst
        self.authorLast = authorLast
        self.title = title
        self.year = year
        self.publisher = publisher
        self.place = place

    def write_bib_format(self):
        return self.authorLast + ',' + self.authorFirst + ',' + '"' + \
               self.title + '"' + ',' + self.place + ':' \
               + self.publisher + ',' + self.year + '.'

    def make_author_year(self):
        author_year = self.authorLast + '(' + self.year + ')'
        return author_year


class Article(object):
    def __init__(self, authorLast, authorFirst, articleTitle, journalTitle,
                 volumeNumber, no_of_pages, year):
        self.authorLast = authorLast
        self.authorFirst = authorFirst
        self.articleTitle = articleTitle
        self.journalTitle = journalTitle
        self.volumeNumber = volumeNumber
        self.no_of_pages = no_of_pages
        self.year = year

    def write_bib_format(self):
        return self.authorLast + ',' + self.authorFirst + ',' + '"' + \
               self.articleTitle + '"' + ',' + self.journalTitle + ':' \
               + self.volumeNumber + ',' + self.no_of_pages + ',' \
               + self.year + '.'

    def make_author_year(self):
        author_year = self.authorLast + '(' + self.year + ')'
        return author_year


class Bibliography(object):
    """ a Bibliography class that will manage a bibliography,
    given instances of Book and Article objects """
    def __init__(self, entries_list):
        self.entries_list = entries_list

    def sort_entries_alpha(self):
        temp = sorted(self.entries_list,
                      key=operator.attrgetter('authorLast', 'authorFirst'))
        self.entries_list = temp
        del temp

    def write_bibliog_alpha(self):
        self.sort_entries_alpha()
        # To initialize a string, in order to grow it in concatenation steps
        #  such as in a for loop, start by setting the string variable to an
        #  empty string
        output = ''
        for ientry in self.entries_list:
            output = output + ientry.write_bib_entry() + '\n\n'
            return output[:-2]


beauty = Book("James", "Goodwill", "Beauty and the Beast", "1985", "Berlin"
                                                                   "Publishers",
              "Berlin")
health = Article("Charity", "Johnes", "My life is my masterpiece!", "Health "
                                                                    "Magazine",
                 "Volume 120", "12 pages", "2017")
print(beauty.write_bib_format())
print(beauty.make_author_year())
print(health.write_bib_format())
print(health.make_author_year())
