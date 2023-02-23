from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.payment_details_page import PaymentDetailsPage
from pages.pricing_page import PricingPage


def test_payments_failed(driver):
    LoginPage(driver).open()
    LoginPage(driver).accept_cookies()

    # Log in to the page
    LoginPage(driver).fill_input_email("vincent-sqa+rekrutacja@bold.com")
    LoginPage(driver).fill_input_password("parmezan6")
    LoginPage(driver).submit_login()

    # Check the resume file
    DashboardPage(driver).load_page()
    assert DashboardPage(driver).is_document_present("CV - TEST")
    DashboardPage(driver).download_resume()

    # Fill payment form
    PricingPage(driver).load_page()
    PricingPage(driver).proceed_pricing()
    PaymentDetailsPage(driver).load_page()
    PaymentDetailsPage(driver).fill_card_number("4000 000 000 0051")
    PaymentDetailsPage(driver).fill_card_expiration_date("10/23")
    PaymentDetailsPage(driver).fill_card_cvv("123")
    PaymentDetailsPage(driver).fill_card_holder_name("Vincent Testowy")
    PaymentDetailsPage(driver).click_payment_button()

    # Check error message
    expected_url = "https://app.interviewme.pl/cart/error"
    PaymentDetailsPage(driver).wait_for_url(expected_url)
    assert PaymentDetailsPage(driver).get_current_url() == expected_url
    assert PaymentDetailsPage(driver).is_link_displayed("/cart/payment-details")
    expected_message = "Coś poszło nie tak z Twoją płatnością"
    assert PaymentDetailsPage(driver).is_header_with_text_displayed(expected_message)
