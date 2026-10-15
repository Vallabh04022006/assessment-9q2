import pytest

HTML_FILE = "index.html"


@pytest.fixture
def page_content():
    with open(HTML_FILE, "r", encoding="utf-8") as file:
        return file.read()


def test_title_exists(page_content):
    assert "Online Bookstore" in page_content


def test_at_least_six_books(page_content):
    assert page_content.count('class="book"') >= 6


def test_search_feature(page_content):
    assert 'id="search"' in page_content


def test_book_categories(page_content):
    categories = [
        "Programming",
        "Computer Science",
        "AI",
        "Web",
        "Database"
    ]

    found = any(category in page_content for category in categories)
    assert found


def test_prices_exist(page_content):
    assert "₹499" in page_content
    assert "₹550" in page_content


def test_availability_label(page_content):
    assert "Available" in page_content


def test_cart_button(page_content):
    assert "Add to Cart" in page_content


def test_order_tracking(page_content):
    assert "Track Order Status" in page_content


def test_thank_you_feature(page_content):
    assert "Thank You for Visiting
