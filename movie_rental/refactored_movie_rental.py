def _wrapElement(text: str, tag: str) -> str:
    return f"<{tag}>{text}</{tag}>"


class Customer:
    def __init__(self, name):
        self._rentals = []
        self.name = name

    def getName(self):
        return self.name

    @property
    def totalAmount(self) -> float:
        return float(sum([r.amount for r in self._rentals]))

    @property
    def frequentRenterPoints(self) -> int:
        return sum([r.frequentRenterPoints for r in self._rentals])

    def addRental(self, param):
        self._rentals.append(param)

    def statement(self, htmlFormat: bool = False):
        result = self._getHeader(htmlFormat)
        result += self._getRentalListStr(htmlFormat)
        result += self._getFooter(htmlFormat)
        return result

    def _getHeader(self, htmlFormat: bool):
        name = self.getName() if not htmlFormat else _wrapElement(self.getName(), 'em')
        header = f"Rental Record for {name}"
        if htmlFormat:
            header = _wrapElement(header, 'h1')
        return header + '\n'

    def _getRentalListStr(self, htmlFormat: bool) -> str:
        strList = ['\t' + r.toStr(htmlFormat) + '\n' for r in self._rentals]
        result = ''.join(strList)
        if not htmlFormat:
            return result
        return _wrapElement('\n' + result, 'table') + '\n'

    def _getFooter(self, htmlFormat: bool) -> str:
        amt = str(self.totalAmount)
        frp = str(self.frequentRenterPoints)
        if htmlFormat:
            amt = _wrapElement(amt, 'em')
            frp = _wrapElement(frp, 'em')
        amtMsg = f"Amount owed is {amt}"
        frpMsg = f"You earned {frp} frequent renter points"
        if htmlFormat:
            amtMsg = _wrapElement(amtMsg, 'p')
            frpMsg = _wrapElement(frpMsg, 'p')
        return f"{amtMsg}\n{frpMsg}"


class Movie:
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0

    def __init__(self, title, priceCode):
        self.title = title
        self.priceCode = priceCode

    def getPriceCode(self):
        return self.priceCode

    def setPriceCode(self, arg):
        self.priceCode = arg

    def getTitle(self):
        return self.title

    def getPrice(self, daysRented: int) -> float:
        if self.priceCode == Movie.REGULAR:
            price = 2
            if daysRented > 2:
                price += (daysRented - 2) * 1.5
        elif self.priceCode == Movie.NEW_RELEASE:
            price = daysRented * 3
        elif self.priceCode == Movie.CHILDRENS:
            price = 1.5
            if daysRented > 3:
                price += (daysRented - 3) * 1.5
        else:
            raise ValueError('Invalid price code')
        return float(price)


class Rental:
    def __init__(self, movie, daysRented):
        self.daysRented = daysRented
        self.movie = movie

    def getDaysRented(self):
        return self.daysRented

    def getMovie(self):
        return self.movie

    @property
    def _getsFrequentRenterBonus(self) -> bool:
        return (self.getMovie().getPriceCode() == Movie.NEW_RELEASE) and self.getDaysRented() > 1

    @property
    def frequentRenterPoints(self) -> int:
        return 2 if self._getsFrequentRenterBonus else 1

    @property
    def amount(self) -> float:
        return self.getMovie().getPrice(self.getDaysRented())

    def toStr(self, htmlFormat: bool = False):
        if not htmlFormat:
            return self.getMovie().getTitle() + "\t" + str(self.amount)
        title = _wrapElement(self.getMovie().getTitle(), 'td')
        amount = _wrapElement(str(self.amount), 'td')
        return _wrapElement(title + amount, 'tr')
