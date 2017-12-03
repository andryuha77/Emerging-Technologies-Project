# Emerging-Technologies-Project
My name is Andrei Petruk final year Software Development student.
This is project for the [Emerging Technologies](https://emerging-technologies.github.io/) 2017 module.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

### Project Requirements Overview
In this project you will create a web application in Python to recognise digits in images.
Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image.
You should use [tensorflow](https://www.tensorflow.org/) and [flask](http://flask.pocoo.org/) to do this.
Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

## Instructions
1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
2. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
3. Add a route to your application that accepts requests containing a user input image and responds with the digit.
4. Connect the HTML page to the route using AJAX.

## Research
### What is a [flask](http://flask.pocoo.org/)?
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed.

The latest stable version of Flask is 0.12.2 as of May 2017.

Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

### What is a [TensorFlow™](https://www.tensorflow.org/)?

[TensorFlow™](https://www.tensorflow.org/) is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

#### To accomplish this project I divided the work into some main points to research and complete:

1. Created simple page using [flask](http://flask.pocoo.org/) example
2. Upload an image to webapp
3. Send that image to server
4. Be able to process/reize etc the image
5. Create a tensorflow or keras model
6. Use mnist to train and  test it
7. Save that model
8. Use the uploaded images
9. Send prediction to webapp

## Design and Implementation
During the research and creation of a solution for the project, I went through multiple solutions available online and complete [TensorFlow™](https://www.tensorflow.org/) examples in labs.  References to used solutions available at the end of this readme file. 

### Difficulties

Environment Installation on my two machines homes PC and laptop. It takes me awhile to figure out how to install [TensorFlow™](https://www.tensorflow.org/) to be able to use it in Jupiter notebook for the course labs.

From the history of my commits on GitHub, it is possible to see that some of the flies/solutions were completely removed or rebuild as it was difficult to put some of the pieces together, for example, resize saved pictures or send values to HTML page using ajax.


### Created simple page using [flask](http://flask.pocoo.org/) example  
Create simple Web App was not difficult as we complete Data Representation course year ago, so I just refresh memory going thru my previous single page app project and [flask](http://flask.pocoo.org/) example.


to run it:
```
$ set FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```

### Digits Recognition

Tensorflow tutorials were used for digits recognition. The home HTML page displays two results: regression function that is a model for recognizing MNIST digits, based on looking at every pixel in the image and a multilayer convolutional neural network with improved results.  The final decision number based on multilayer result and displayed using AJAX.

![](https://image.ibb.co/ci7qeb/Capture.png)

## How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.
Alternatively, this can be easily achieved by installing [Anaconda](https://www.anaconda.com/download/) which includes both of them.

boto3 also need to be installed:
```
pip install boto3
```
I had an issue to install it on my laptop, so I used:
```
easy_install boto3
```
More required software names can be found in the  [requirements](https://github.com/andryuha77/Emerging-Technologies-Project/blob/master/requirements.txt) file, but most of it included in [Anaconda](https://www.anaconda.com/download/).

#### Installing TensorFlow on Windows

Installing with Anaconda

1. Follow the instructions on the [Anaconda](https://www.anaconda.com/download/) download site to download and install Anaconda.

2. Create a conda environment named tensorflow by invoking the following command:
```
C:> conda create -n tensorflow python=3.5
``` 
Activate the conda environment by issuing the following command:
```
C:> activate tensorflow

 (tensorflow)C:>  # Your prompt should change 
 ```
Issue the appropriate command to install TensorFlow inside your conda environment. To install the CPU-only version of TensorFlow, enter the following command:
```
(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow 
```
To install the GPU version of TensorFlow, enter the following command (on a single line):
```
(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow-gpu
```
keras.io was used for model generation, use:
```
easy_install keras
```
for keras instalation.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python main.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

### References:
adapted from: http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application

adapted from: https://habrahabr.ru/company/ods/blog/335998/

adapted from: https://github.com/Erlemar/digits_little

adapted from: https://github.com/visraman26/DigitRecognition/blob/master/digitRecognition.py

adapted from: https://github.com/sugyan/tensorflow-mnist/blob/master/main.py

adapted from: https://www.tensorflow.org/get_started/mnist/beginners

adapted from: https://www.tensorflow.org/get_started/mnist/pros
