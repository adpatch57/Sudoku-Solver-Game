OOP VilniusTech Coursework Report : Sudoku Solver Game
============

Introduction
============

What is your application?
----------------
This application is a Sudoku solver game. It generate a random sudoku each time we launch the application or by pressing the button “regenerate”. The user can resolve a given sudoku by himself and reveal the solution or simply save the sudoku as a .png file.  

How to run the program?
The program needs python3 to be installed on the user’s operating system. Open a terminal and simply type:
```
$ pip install -r requirements.txt
```

To install necessary libraries.
Double click on main.py or type
```
$ python3 main.py
```

How to use the program?
----------------
On execution, the program will launch on a menu containing three buttons. The quit button is used to exit the application. The solve from image button allows you to upload a sudoku image and click on a solve button to solve the sudoku automatically. Unfortunately this is not yet implemented. Finally, the main button: solve it yourself allows users to solve a randomly generated sudoku themselves. Simply click on the white coloured buttons to change the number and solve the sudoku. The regenerate button allows you to regenerate a sudoku. The result button displays the sudoku result on the right. Finally, the 'save' button saves the sudoku as a png image. The user must choose a name and a save path for the image.

Body/Analysis
============
The program implement all 4 object-oriented programming pillars
- Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types or classes). In Python, polymorphism is achieved through method overriding and method overloading. Method overriding involves redefining a method in a subclass that is already defined in the superclass, while method overloading involves defining multiple methods with the same name but with different parameters. In the Sudoku solver, polymorphism might be demonstrated through the use of a common function for organizing different objects in the windows, the use of the function .grid.
- Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object to the outside world. Abstraction is achieved by defining classes with methods and properties that provide a high-level interface for interacting with objects, while hiding the internal implementation details. In the Sudoku solver, abstraction might be exemplified by defining classes for the puzzle, cell. These classes expose methods for interacting with the puzzle (e.g., solving, validating), hiding the intricacies of the puzzle-solving algorithms.
- Inheritance is the mechanism by which a new class inherits properties and behavior (methods) from an existing class (superclass). It promotes code reusability and establishes a hierarchy of classes. In Python, inheritance is implemented by creating a new class that derives from an existing class using the syntax class NewClass(BaseClass):. The new class inherits attributes and methods from the base class. In the Sudoku solver, inheritance might be demonstrated by creating subclasses for different frames of the UI. These subclasses inherit common solving logic from a superclass representing a generic frame from the tkinter library.
- Encapsulation is the bundling of data and methods that operate on the data into a single unit, called a class. It restricts direct access to some of the object's components, protecting the integrity of the data. Encapsulation is achieved by defining class attributes and providing public methods (getters and setters) to access or modify these attributes. In the Sudoku solver, encapsulation might be illustrated by defining attributes for the puzzle grid and providing public methods for accessing and updating the grid. This ensures that the internal state of the puzzle is controlled and manipulated only through designated interfaces.


It also use at least 2 design patterns such as singletons and decorators.
The Singleton design pattern ensures that a class has only one instance and provides a global point of access to that instance. The Singleton pattern is most suitable in scenarios where exactly one instance of a class is needed, such as managing shared resources or maintaining global state. In the Sudoku solver, ensuring a single puzzle instance simplifies coordination between different solving strategies and prevents unnecessary duplication of puzzle data. Moreover, decorators are functions that modify the behavior of other functions or methods. They allow additional functionality to be added to existing functions dynamically without modifying their code directly. This promotes code reusability and simplifies maintenance by keeping the core functionality of classes and methods focused on their primary purpose.

Compared to other design patterns or techniques, the Singleton pattern and decorators are particularly suitable for the Sudoku solver program due to their ability to enforce single instance semantics and add modular functionality seamlessly. These patterns contribute to the program's clarity, maintainability, and extensibility
 
 
The program implement functions to import and export data such as images files. 



Results and Summary
============
The application is functional. It indeed works as intended, we can resolve our own randomly generated sudoku. Moreover, all the requirements have been completed. The biggest challenge was interacting with the tkinter library. Even though I'd already worked with it, this library gave me a lot of trouble organising the ui and getting everything to work properly. However, I was able to learn some new things.


Conclusions
----------------
The coursework involved the development of a Sudoku solver game in Python. Key findings include the successful creation of a program capable of generating and solving Sudoku puzzle. The outcomes of this work include a functional Python script that can accurately generate and solve Sudoku puzzles by employing logic-based strategies and backtracking techniques.
The result of the Sudoku solver program is its ability to generate an unsolved Sudoku puzzle. This achievement demonstrates the effectiveness of the implemented algorithms in generating complex logic puzzles.
Future prospects for the program include potential enhancements such as optimizing the solving algorithms for faster performance, and incorporating additional features such as difficulty levels. Furthermore, the program could be extended to solve other types of logic-based puzzles beyond Sudoku, broadening its utility and appeal.


