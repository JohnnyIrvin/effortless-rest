# Effortless Rest Project (Under Development)

**Note: This project is currently under development and is not fully implemented yet.**

The Effortless Rest Project is an ambitious initiative aimed at simplifying the creation of full-fledged microservices. The project offers a streamlined approach to developing microservices by leveraging the power of Python dataclasses and providing seamless integration with an Object-Relational Mapping (ORM) system and a target framework.

## Project Overview
The primary goal of the Effortless Rest Project is to enable developers to define microservices using Python dataclasses as the foundation. By utilizing dataclasses, developers can focus on modeling their data structures and business logic in a concise and intuitive manner.

## Features
- **Automatic RESTful Microservice Generation**: Effortless Rest empowers developers to automatically generate RESTful microservices based on their Python dataclasses. This automated process eliminates the need for manual implementation of repetitive boilerplate code, enabling rapid development.

- **Integration with ORM**: The project seamlessly integrates with an ORM system, such as SQLAlchemy. This integration ensures effortless handling of database operations and simplifies the mapping between data models and database tables.

- **Target Framework Integration**: Effortless Rest integrates with a target framework, such as Flask or FastAPI, to provide a robust foundation for handling HTTP requests, routing, and other web-related functionalities. This integration allows developers to focus on building business logic and leaves the underlying framework intricacies to Effortless Rest.

## Roadmap
The Effortless Rest Project is actively being developed, and the roadmap includes the following key milestones:

- **Dataclass Validation**: Enhance the project to provide robust dataclass validation mechanisms, ensuring data integrity and consistency.
- **Advanced Querying and Filtering**: Implement advanced querying and filtering capabilities to enable more flexible and efficient data retrieval.
- **Expanded Framework Support**: Extend support for additional target frameworks to accommodate a wider range of developer preferences.

# Usage

Inside of a python environment, you can import the requirements and run the following commands to start the project.

```bash
pip install -r requirements.txt
python -m effortless
```

If you prefer to use docker, you can use the docker image.
```bash
docker build -t effortless --target RUN .
docker run effortless
```

# Testing
To test the library, you can use the `run_tests.py` script. It is highly recommended to use the docker image to keep your system isolated from integration tests.

Using docker, you can run the following commands to run the tests.
```bash
docker build -t tests --target TEST .
docker run tests
```

You may still run the tests on your system, but it is recommended to use the docker image.
```bash
pip install pytest
python -m pytest
```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contribution

This project is open source. Feel free to contribute to the project by making a pull request, creating an issue ticket, or sending an email to [Johnny Irvin](mailto:irvinjohnathan@gmail.com).
