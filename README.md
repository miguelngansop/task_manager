# Django Task Management with Swagger

## Description
This project is a full-stack web application designed to help users manage a personal task list efficiently. It features task creation, editing, deletion, and completion marking, all accessible through a RESTful API. Built with Django, this application leverages a robust backend with modern development practices.

## Key Technologies and Tools
- **Django Framework**: The backbone of the backend, providing ORM capabilities and RESTful API functionalities.
- **Swagger**: Used to document the API, allowing easy interaction and testing of endpoints, enhancing developer experience.
- **Docker**: The application is containerized, enabling easy deployment and scalability across environments.
- **OAuth and JWT**: Implemented for secure authentication and authorization, ensuring only authorized users can access certain features.
- **Django ORM**: Utilized for seamless database interactions and establishing model relationships.
- **CI/CD**: Implemented continuous integration and continuous deployment pipelines to automate testing and deployment, ensuring rapid development cycles.
- **Unit Tests and TDD**: The project follows Test-Driven Development, with extensive unit tests to guarantee code quality and reliability.

## Prerequisites
To run this application, you'll need:
- Python 3.x installed on your system.
- Pip installed to manage Python dependencies.
- A configured database (e.g., SQLite, PostgreSQL, or MySQL).
- Docker installed to build and deploy the application in a container.
- Django installed via pip.
- Swagger UI to visualize and test the API.


## Installation
Here are the steps to set up the environment and install the necessary dependencies:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/miguelngansop/task_manager.git
   cd your-repo
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Apply the migrations**:
    ```bash
   python manage.py migrate
5. **Create a superuser to access the Django admin interface:**
   ```bash
   python manage.py createsuperuser
## Running Unit Tests
To ensure code quality and reliability, you should run the unit tests. Here's how I do it:

1. **Run the tests**:
   ```bash
   python manage.py test
2. This command executes all the unit tests in the project. Ensure all tests pass before deploying or making significant changes.

## Usage
Here's how I use the application:
  1. **Start the Django server:**
    ```bash
    python manage.py runserver
2. **Access the Swagger interface to explore the API**:
- Open a browser and navigate to http://127.0.0.1:8000/swagger/.
- Interact with the API:
- Use the Swagger interface to create, read, update, and delete tasks.
- Mark tasks as completed.
3. **Authentication** :
- Use your credentials to access secured features.
- Test the authentication and authorization mechanisms.

## Building the Docker Image
To build a Docker image for this Django application, follow these steps:

1. **Build the Docker image**:
   ```bash
   docker build -t your-username/your-image-name .
2. **Push the image to a Docker registry (like Docker Hub):**
   ```bash
   docker push your-username/your-image-name


