# Effective Serialization with Python
This is the repository for the LinkedIn Learning course Effective Serialization with Python. The full course is available from [LinkedIn Learning][lil-course-url].

![Effective Serialization with Python][lil-thumbnail-url] 
When you're making calls between different services, you can use serialization to move data around in a predictable manner for easy encoding and decoding. In this course, instructor Miki Tebeka takes a deep dive into the subject of serialization with Python, exploring key serialization formats, how to work with each format, and how to pick the right one for your Python project. He covers Python-specific serialization formats such as marshal and pickle; how to serialize and deserialize using JSON; how to encode and decode messages and serialize using protocol buffers; how to use msgpack; and more. Along the way, he shares challenges that allow you to put your new knowledge to the test.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `master` branch holds the final state of the code when in the course.

## Installing
1. To use these exercise files, you must have the following installed:
    - Python 3.6+
    - Requirements from `requirements.txt`, see install instructions in the file
	- [list of requirements for course]
    - `protoc` compiler from [here](https://developers.google.com/protocol-buffers/docs/downloads)
    - Optional: [IPython](https://ipython.org/) (`python -m pip install ipython`)
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.

### Instructor

**Miki Tebeka**

_CEO at 353Solutions_

Check out some of my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/miki-tebeka?u=104).

[lil-course-url]: https://www.linkedin.com/learning/effective-serialization-with-python
[lil-thumbnail-url]: https://cdn.lynda.com/course/2822693/2822693-1598022021220-16x9.jpg
