# QA Test Automation Framework - Sauce Demo

A comprehensive test automation framework for the Sauce Demo e-commerce website, built using Selenium WebDriver, Python, and pytest. This project demonstrates professional QA testing practices including the Page Object Model design pattern, automated test execution, and detailed reporting.

## Project Overview

This framework automates testing for [Sauce Demo](https://www.saucedemo.com), covering:
- User authentication and login flows
- Product browsing and catalog functionality
- Shopping cart operations
- Checkout process
- UI/visual element validation
- Negative test scenarios and edge cases

## Technologies Used

- **Python 3.8+** - Programming language
- **Selenium WebDriver** - Browser automation
- **pytest** - Test framework and runner
- **webdriver-manager** - Automatic driver management
- **pytest-html** - HTML test report generation

## 📁 Project Structure

```
qa-automation-project/
├── pages/                           # Page Object Model classes
│   ├── __init__.py
│   ├── login_page.py                # Login page interactions
│   ├── products_page.py             # Products page interactions
│   ├── cart_page.py                 # Shopping cart interactions
│   └── checkout_page.py             # Checkout process interactions
├── tests/                           # Test cases
│   ├── __init__.py
│   ├── test_login.py                # Login functionality tests
│   ├── test_products.py             # Product page tests
│   ├── test_cart.py                 # Shopping cart tests
│   ├── test_checkout.py             # Checkout process tests
│   ├── test_ui_visual.py            # UI/Visual validation tests
│   └── test_negative_edge_cases.py  # Negative scenarios
├── reports/                         # Test execution reports
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher installed
- Google Chrome browser installed
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd qa-automation-project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Requirements.txt Contents

```
selenium
pytest
pytest-html
webdriver-manager
```

## Running Tests

### Run all tests:
```bash
pytest tests/ -v
```

### Run specific test file:
```bash
pytest tests/test_login.py -v
```

### Run specific test case:
```bash
pytest tests/test_login.py::TestLogin::test_error_messages_for_invalid_credentials -v
```

### Generate HTML report:
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

### Run tests in headless mode (no browser window):
```bash
pytest tests/ -v --headless
```

## 📊 Test Coverage

### Login Tests
- Valid user login
- Invalid credentials (username, password)
- Locked user scenario
- Empty field validation
- Error message verification

### Product Tests
- Product image loading validation
- Product name display verification
- Product price display
- Sorting functionality (A-Z, Z-A, price)
- Add to cart functionality

### Cart Tests
- Add single/multiple items
- Remove items from cart
- Cart badge count verification
- Cart page navigation
- Item verification in cart

### Checkout Tests
- Complete checkout flow
- Form validation (missing fields)
- Order summary verification
- Purchase completion

### UI/Visual Tests
- Footer elements presence
- Social media icons
- Page title verification
- Copyright text validation

### Negative/Edge Cases
- Unauthorized page access
- Empty cart scenarios
- Multiple rapid submissions
- All items in cart scenario

## Design Pattern

This project implements the **Page Object Model (POM)** design pattern, which provides:

- **Maintainability**: UI changes only require updates to page objects, not individual tests
- **Reusability**: Page objects can be used across multiple test cases
- **Readability**: Tests are cleaner and easier to understand
- **Scalability**: Easy to add new tests and pages

### Example Structure:
- **Page Objects** contain element locators and interaction methods
- **Test Files** contain test logic and assertions
- **Fixtures** handle setup and teardown

## 📈 Reporting

Test reports are generated in the `reports/` directory and include:
- Test execution summary (passed/failed/skipped)
- Detailed test results
- Execution time
- Failure screenshots (if configured)
- Browser and environment information

## 🎓 Skills Demonstrated

- Test automation framework development
- Page Object Model implementation
- Test case design and execution
- Cross-browser testing setup
- Continuous testing practices
- Documentation and reporting
- Version control with Git

## 🔧 Configuration

### Browser Configuration
By default, tests run on Chrome. To use different browsers, modify the driver initialization in test fixtures.

### Wait Times
Explicit waits are configured in page objects using WebDriverWait with a 10-second timeout.

## 📝 Future Enhancements

- [ ] Cross-browser testing (Firefox, Edge, Safari)
- [ ] Parallel test execution
- [ ] CI/CD integration (GitHub Actions, Jenkins)
- [ ] Screenshot capture on test failure
- [ ] Data-driven testing with CSV/JSON
- [ ] API testing integration
- [ ] Performance testing metrics
- [ ] Docker containerization

## 🤝 Contributing

This is a personal portfolio project. Feedback and suggestions are welcome!

## 👤 Author

**Efe Awo-Osagie**
- GitHub: [efe_cKia00](https://github.com/efe-cKia00/)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/efe-awo-osagie-b4b796381/)
- Email: deafveid@gmail.com

## 📄 License

This project is open source and available under the MIT License.

## Acknowledgments

- [Sauce Demo](https://www.saucedemo.com) for providing a testing playground
- Selenium WebDriver documentation
- pytest documentation and community

---

**Note**: This project is created for educational and portfolio purposes to demonstrate software quality assurance and test automation skills.
