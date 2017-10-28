# Emerging-Technologies-Project
Project for the module for [Emerging Technologies](https://emerging-technologies.github.io/) 2017 module.
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

### What is a [flask](http://flask.pocoo.org/)?

### What is a [tensorflow](https://www.tensorflow.org/)?

## Design

## Implementation
1. Create simple page using [flask](http://flask.pocoo.org/) 

### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python run.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework.
Python 3 and Flask were requirements for the project.

### Reference
Adapted from:

Adapted from:
