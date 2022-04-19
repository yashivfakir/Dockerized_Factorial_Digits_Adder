# Dockerized Factorial Digits Adder

## About the Project:
The project explores the Docker containerization of a factorial algorithm. The algorithm determines the factorial of an inputted integer number and then sums the digits of the parsed factorial. 

 > **For example**  given an input of 4:
 
>The Factorial of 4 is:

>          4! =  4 x 3 x 2 x 1 = 24

>**Then,** parse the factorial and sum the digits as follows:

>          Output = 24 =  2 + 4 = 6

The containerized application has been built to be executeable and requires input upon activating the container.

### Built With 
The project involved the usage of several development languages/tools and libraries including:
- [Python 3](https://docs.python.org/3/) - High level programming language used to implement the factorial digits summation algorithm.
- [Numpy](https://numpy.org/) - Python library used to implement all math operations.
- [Argparse](https://docs.python.org/3/howto/argparse.html) -  Python library that allows for input to be exchanged from a command line shell to Python script upon the Python script execution.
- [Time](https://www.programiz.com/python-programming/time) - Python library used to measure the execution time. 
- [Concurrent Futures](https://docs.python.org/3/library/concurrent.futures.html) - Python library used to implement parallel executions of python script.  
- [Docker](https://www.docker.com/) - Used to define and build the image that containerizes the project.

### Repository Contents
The project consists of a yashivfakir.tar.gz compressed folder that includes a directory called Docker_Build_Directory. The directory has the Docker build file and the Python scripts that implements the algorithm. Also included in the repsitory is a a directory named Other_Implementations, which contains a benchmark implementation that was used to benchmark the project execution in terms of time with the existing Numpy factorial library and a non-threaded implementation of the project. The implemenations are named:
- Factorial_Digits_Adder_BENCHMARK.py
- Factorial_Digits_Adder_UN_THREADED.py


## Project Implementation:

### Prerequisites
**Before the project can be built, certain components are needed:**

1. Firstly, since the project files are compressed as a .tar.gz file, a decompression program, such as 7-Zip, would be needed to extract the contents of the compressed yashivfakir.tar.gz file.
2. Secondly, Docker should be installed on the host machine in order to build and run the containerized application.
3. Thirdly, a stable internet connection is required to download the required libraries.

### Build Instructions

Once the repository contents are cloned to a host machine, the application can then be built.
This can be done by executing the following command in a terminal window from the Docker_Build_Directory file location:

```bash
sudo docker image build -t factorial-digits .
```
Note: Docker commands may need administrative priviliages in order to execute the command. The 'sudo' part of the command provides admin privileges for Linux Ubuntu and may differ for other OS's and can thus be dropped from the command.

### Container Execution

Once the image being, factorial-digits, has been built, the container can be executed using the following command where INPUT_NUMBER is replaced with the input integer number:

```bash
sudo docker run --rm factorial-digits INPUT_NUMBER
```
Note: Docker commands may need administrative priviliages in order to execute the command. The 'sudo' part of the command provides admin privileges for Linux Ubuntu and may differ for other OS's and can thus be dropped from the command.
If no input or input that is not an integer value is provided with the docker command, an error saying 'requires input' or 'invalid input' will be thrown respectively. Once the program has been executed, the Docker command implements the shutdown of the container the program execution.
