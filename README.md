# Effortless Rest

EffortlessREST is a powerful tool that aims to simplify the process of transforming dataclasses into RESTful microservices. Please note that the project is currently in development, and the minimum viable product (MVP) has not been completed yet. As a result, the project is not yet usable. We appreciate your interest and encourage you to stay tuned for updates as we work diligently to deliver a robust and user-friendly solution.

# Usage

Inside of a python environment, you can import the requirements and run the following commands to start the project.

```bash
pip install -r requirements.txt
python -m project_name
```

If you prefer to use docker, you can use the docker image.
```bash
docker build -t project_name --target RUN .
docker run project_name
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
