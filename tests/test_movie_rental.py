from movie_rental import Customer, Rental, Movie


def generate_customer() -> Customer:
    customer = Customer("Bob")
    rentals = [
        ("Jaws", Movie.REGULAR, 2),
        ("Golden Eye", Movie.REGULAR, 3),
        ("Short New", Movie.NEW_RELEASE, 1),
        ("Long New", Movie.NEW_RELEASE, 2),
        ("Bambi", Movie.CHILDRENS, 3),
        ("Toy Story", Movie.CHILDRENS, 4),
    ]
    for title, category, days_rented in rentals:
        movie = Movie(title, category)
        customer.addRental(Rental(movie, days_rented))
    return customer


def test_text_statement():
    customer = generate_customer()

    expected = "Rental Record for Bob\n"
    expected += "\tJaws\t2.0\n"
    expected += "\tGolden Eye\t3.5\n"
    expected += "\tShort New\t3.0\n"
    expected += "\tLong New\t6.0\n"
    expected += "\tBambi\t1.5\n"
    expected += "\tToy Story\t3.0\n"
    expected += "Amount owed is 19.0\n"
    expected += "You earned 7 frequent renter points"

    assert expected == customer.statement()


def test_html_statement():
    customer = generate_customer()

    expected = "<h1>Rental Record for <em>Bob</em></h1>\n"
    expected += "<table>\n"
    expected += "\t<tr><td>Jaws</td><td>2.0</td></tr>\n"
    expected += "\t<tr><td>Golden Eye</td><td>3.5</td></tr>\n"
    expected += "\t<tr><td>Short New</td><td>3.0</td></tr>\n"
    expected += "\t<tr><td>Long New</td><td>6.0</td></tr>\n"
    expected += "\t<tr><td>Bambi</td><td>1.5</td></tr>\n"
    expected += "\t<tr><td>Toy Story</td><td>3.0</td></tr>\n"
    expected += "</table>\n"
    expected += "<p>Amount owed is <em>19.0</em></p>\n"
    expected += "<p>You earned <em>7</em> frequent renter points</p>"

    assert expected == customer.statement(htmlFormat=True)
