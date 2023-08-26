# python-selenium-qubika

Por supuesto, aquí tienes un ejemplo de archivo `README.md` en formato Markdown que puedes utilizar para documentar tu proyecto:

---

# Python Selenium Behave Automation Framework

This repository contains an end-to-end test automation framework using Python, Selenium WebDriver, and Behave. The framework follows the Page Object Model (POM) design pattern for better maintainability and readability.
Qubika

## Table of Contents

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Page Object Model (POM)](#page-object-model-pom)

## Installation

1. **Clone the repository**

    ```
    git clone https://github.com/GastonAGenaud/python-selenium-qubika.git
    ```

2. **Navigate to the project directory**

    ```
    cd python-selenium-qubika
    ```

3. **Create a virtual environment (Optional but recommended)**

    ```
    python -m venv venv
    ```

4. **Activate the virtual environment**

    - On Windows:
        ```
        .\venv\Scripts\Activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

5. **Install the required packages**

    ```
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests and generate an HTML report, execute the following command:

```
behave -f html -o behave-report.html
```

## Project Structure

- `.idea`: IDE configuration files (not part of the framework).
- `features`: Contains the Gherkin feature files and step definitions.
    - `Search.feature`: Feature file containing scenarios for Google search.
    - `steps`: Folder containing the step definition files.
- `pages`: Contains the Page Object classes.
    - `base_page.py`: BasePage class with common methods.
    - `google_main_page.py`: Page Object for the Google main page.
    - `search_results_page.py`: Page Object for the Google search results page.
- `support`: Contains utility and setup files.
    - `driver_setup.py`: Contains the WebDriver setup logic.
- `venv`: Virtual environment folder.
- `.gitignore`: Specifies files and folders to ignore in Git.
- `behave.ini`: Behave configuration file.
- `requirements.txt`: Lists the required Python packages.
- `LICENSE`: License file.
- `README.md`: This documentation file.

## Page Object Model (POM)

The framework uses the Page Object Model design pattern to separate the test logic from the page-specific logic. This makes the tests easier to maintain and extend. Each page in the application has a corresponding Page Object class in the `pages` folder. These classes contain methods to interact with the page elements.

---

## Possible Improvements

### 1. Enhanced Logging and Reporting

- Incorporate a logging system to capture events and actions during test execution.
- Use a more advanced report generator that can include graphs, screenshots in case of failures, and other details.

### 2. Test Parallelization

- Utilize tools like Selenium Grid or cloud services to run tests in parallel and reduce the overall execution time.

### 3. Cross-Browser Testing

- Extend the framework to support testing across multiple browsers and platforms.

### 4. Continuous Integration/Continuous Deployment (CI/CD)

- Integrate the project with CI/CD tools like Jenkins, GitLab CI, or GitHub Actions to automatically run tests when code changes are made.

### 5. Code Improvements

- Refactor the code to make it more modular and easier to maintain.
- Add more comments and documentation in the code to explain the logic and design decisions.

### 6. Regression and Smoke Tests

- Add tags to the scenarios in your `.feature` files to be able to run subsets of tests, such as regression tests or smoke tests.

### 7. Test Data Management

- Use configuration files or databases to manage test data, instead of hardcoding them in the feature files or code.

### 8. More Comprehensive Validations

- Incorporate more types of assertions and validations, such as verifying the states of elements, colors, fonts, etc.

### 9. Negative Testing

- Add negative tests to ensure the application handles errors and non-ideal conditions correctly.

### 10. Documentation

- Keep the documentation up-to-date with every change in the code or the functionalities being tested.

---
