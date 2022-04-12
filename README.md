# Dockerized Factorial Digits Adder

## About the Project:
The project explores the containerization of a factorial algorithm. The algorithm determines the factorial of an inputted integer number and then sums the digits of the parsed factorial. 

 > **For example**  given an input of 4:
The Factorial of 4 is:

```math
4! =  4 x 3 x 2 x 1 = 24
```
>**Then,** parse the factorial and sum the digits as follows:

```math
Output = 24 =  2 + 4 = 6
```

The containerized application has been built to be executeable and requires input upon activating the container.

### Built With 
The project involved the usage of several development languages/tools and libraries including:
- [Python 3](https://docs.python.org/3/) - High level programming language used to implement the factorial digits summation algorithm.
- [Numpy](https://numpy.org/) - Python library used to implement all math operations.
- [Argparse](https://docs.python.org/3/howto/argparse.html) -  Python library that allows for input to be exchanged from a command line shell to Python script upon the Python script execution.
- [Fraction](https://www.geeksforgeeks.org/fraction-module-python/) - Python library used to ensure that rounding errors and rounding losses do not occur.  
- [Docker](https://www.docker.com/) - Used to define and build the image that containerizes the project.

### Repository Contents
The project consists of a .tar.gz compressed folder that includes a directory called Technical_Assignment. The directory has the Docker build file and the Python script that implements the algorithm.

## Project Implementation:

Several conditions need to be met in order for a successful implementation.

### Prerequisites
**Before the project can be built, certain components are needed:**

1. Firstly, since the files are compressed as a .tar.gz file, a decompression program, such as 7-Zip, would be needed to extract the contents of the compressed file.
2. Secondly, Docker should be installed on the host machine in order to build and run the containerized application.
3. Thirdly, a stable internet connection is required to download the required libraries.

### Build Instructions

Once the repository contents are cloned to a host machine, the application can then be built.
This can be done from the Technical_Assignment Directory in a terminal window by running the following command:

```bash
docker image build -t factorial-digits .
```
Note: Docker commands may need administrative priviliages in order to execute the command.

### Container Execution

Once the image being, factorial-digits, has been built, the container can be executed using the following command where INPUT_NUMBER is replaced with the input integer number:

```bash
docker run --rm factorial-digits INPUT_NUMBER
```
Note: Docker commands may need administrative priviliages in order to execute the command.
If no input or input that is not an integer value is provided with the docker command, an error saying 'requires input' or 'invalid input' will be thrown respectively. Once the program has been executed, the container and Docker command has been built to shutdown upon completion.
