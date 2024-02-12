# RequestManagerAPI App

"RequestManagerAPI" is a delightful and interactive RESTful API service designed to manage client requests with ease and efficiency. Whether you're handling client inquiries, processing requests, or updating statuses, RequestManagerAPI provides a seamless experience. With its intuitive interface and robust features, RequestManagerAPI empowers developers to streamline request management workflows and delight users with efficient service delivery. Experience the joy of simplified request management with RequestManagerAPI today!

## Prerequisites

Before running the RequestManagerAPI app, ensure you have the following dependencies installed:

- flask==3.0.2
- flask_restful==0.3.10
- flask_sqlalchemy==3.1.1
- flask_swagger_ui==4.11.1
- pytest==8.0.0

## Installation

### Virtual Environment

To manage Python dependencies and isolate them from your system-wide Python installation, it's recommended to use a virtual environment. Here's how you can create a virtual environment for this project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/roman-dmytriv/requestmanagerapi.git

2. **Navigate to the project directory:**

    ```bash
    cd requestmanagerapi

3. **Create the Virtual Environment:**

   ```bash
   python3 -m venv venv

4. **Istall dependencies using pip:**

    ```bash
    pip install -r requirements.txt

## Configuration

1. Rename the `config.example.py` file to `config.py`.

## Running the App

To run the RequestManagerAPI app, execute the following command: `python run.py`

The app will start running on `http://localhost:5000` by default.

## Running Tests

1. To run the tests, execute the following command from the project root directory:

    ```bash
    pytest
    ```

This command will discover and run all the test cases in the project. You should see the test results displayed in the terminal.

## Additional Options

You can specify additional options to pytest, such as filtering tests by keywords or running tests in parallel. Refer to the pytest documentation for more information on available options.

## Testing Strategy

### Integration Testing

We rely on integration tests to verify the interactions between different parts of our application, ensuring they work together seamlessly.

#### Approach
  
- **API Testing:** Validates API endpoints to ensure they return the expected responses for various inputs and scenarios.

- **Mocking Dependencies:** Simulates the behavior of external dependencies using mocks to make our tests more predictable and reliable.

### Tools Used

- **Pytest:** Our preferred testing framework for writing and running integration tests in Python.

- **Mocking Libraries:** Leveraged to mock external dependencies and control their behavior during testing.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.