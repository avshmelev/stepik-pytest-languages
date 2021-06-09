link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_208/'


def test_add_to_basket_button(browser):
    browser.get(link)
    buttons_add_to_basket = browser.find_elements_by_css_selector('button[type="submit"].btn-primary.btn-lg')
    assert len(buttons_add_to_basket) != 0, 'There is no button on page to add product in basket'
