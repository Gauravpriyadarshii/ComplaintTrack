# ComplaintEase

ComplaintEase is a web application built with Flask that allows users to register complaints and track their status. It provides a simple and efficient way for users to submit their complaints and for administrators to manage and process them.

## Features

- **User Complaint Registration**: Users can register their complaints by providing details such as the complaint text.
- **Complaint Status Tracking**: Users can check the status of their complaints by entering the token provided upon registration.
- **Administrator Panel**: Administrators can log in and view all complaints, as well as approve or reject them.
- **Superuser Creation**: An initial superuser account is created upon setup for administrative access.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Gauravpriyadarshii/ComplainTrack.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ComplaintEase
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- To register a complaint, navigate to the homepage and fill out the complaint form.
- To check the status of a complaint, click on the "Check Status" link and enter the provided token.
- Administrators can log in to the admin panel using the provided credentials to view and manage complaints.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
