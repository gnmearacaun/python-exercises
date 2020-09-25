# python-exercises

These are exercises from the Jetbrains Academy that I have either completed or have skipped and intend to go back over. 

Here is an a transcript of the Project lessons, a website in Django, and the Python topics that are covered along the way.

    JetBrains Academy / Hyperskill 

Stage #1: Creating models
Description
The "HyperJob" recruitment agency is a very conservative one. Its history starts on January 1st, 1970 . The managers in the agency prefer communicating by phone or email and searching for employees personally. That was an efficient strategy some ten years ago, but now the candidates prefer to apply for jobs online. The problem is that "HyperJob" still doesn't have a site, so they need you to create the service as soon as possible.

We start with a simple site that will be suitable for:

Creating a new vacancy by the agency's manager
Creating a new resume by a candidate
We know that it will be a long road, so at each stage you will make only a small part of work. By the end, we'll have a working site that fulfills all the requirements.

Objectives
Your first task is to prepare the models for the data. It's important to keep all the data safe. We need to store all the vacancies and resumes persistently in the database. Create models to manage the database tables.

Use the default settings of the project with a predefined SQLite database.
Throughout the project, we will need at least two models: Vacancy and Resume. Both of them should have the description and author fields. The description is a text field with no more than 1024 symbols, and the author is a foreign key to django.contrib.auth.models.User model.

Define Vacancy and Resume in models.py module and migrate them to the database. We check your work this time, so that at the next steps you are confident enough to add new models by yourself.
object keeps current state in the fields and the behavior in the methods.
about hypernews project:
 Itertools, random module, and some other topics were required to complete all the tasks.  Reworking the JSON data for each page was particularly challenging.

It's highly recommended to read the documentation for the ORM library before using it. It helps you to get acquainted with the effects and consequences of applied operations.

To start working with an ORM library, you may consider SQLAlchemy for Python, Hibernate or JPA for Java/Kotlin, Sequalize or TypeORM for JavaScript.

The model layer represents the database layer, used for data storage. Django abstracts you from writing SQL queries. Instead of SQL, you use Python objects, and the load/save operations are handled for you.


list of priorities for all considered operations:
parentheses
power
unary minus
multiplication, division, and remainder
addition and subtraction

..........................

Theory: Introduction to OOP
Fundamentals

Object-oriented programming (OOP) is a programming paradigm based on the concept of objects that interact with each other to perform the program functions. Each object can be characterized by a state and behavior. An object keeps the current state in the fields and the behavior in the methods.
Basic principles of OOP

There are four basic principles of OOP. They are encapsulation, abstraction, inheritance, and polymorphism.

    Data encapsulation is the mechanism of hiding the internal data of objects from the world. All interaction with the object and its data are performed through its public methods. Encapsulation allows programmers to protect the object from inconsistency.
    Data abstraction means that objects should provide the simplified, abstract version of their implementations. The details of their internal work usually aren't necessary for the user, so there's no need to represent them. Abstraction also means that only the most relevant features of the object will be presented.
    Inheritance is a mechanism for defining parent-child relationships between classes. Often objects are very similar, so inheritance allows programmers to reuse common logic and at the same time introduce unique concepts into the classes.
    Polymorphism literally means one name and many forms, and it concerns the inheritance of the classes. Just as the name suggests, it allows programmers to define different logic of the same method. So, the name (or interface) stays the same, but the actions performed may be different. In practice, it is done with overloading or overriding.

These are the key concepts of OOP. Each object-oriented language implements these principles in its own way, but the essence stays the same from language to language.
Objects

The key notion of the OOP is, naturally, an object. There are a lot of real-world objects around you: pets, buildings, cars, computers, planes, you name it. Even a computer program may be considered as an object.

It's possible to identify some important characteristics for real-world objects. For instance, for a building, we can consider a number of floors, the year of construction and the total area. Another example is a plane that can accommodate a certain number of passengers and transfer you from one city to another. These characteristics constitute the object's attributes and methods. Attributes characterize objects' data or states, and methods — its behavior.

In OOP, everything can be considered an object. Programs are made from different objects interacting with each other. An object's state and behavior are usually placed together, but it's not always so. Sometimes, we will see objects without a state or methods. This, of course, depends on the purpose of the program and the nature of an object.
Classes

Often, many individual objects have similar characteristics. We can say these objects belong to the same type or class.

A class is another important notion of OOP. A class describes a common structure of similar objects: their fields and methods. It may be considered a template or a blueprint for similar objects. An object is an individual instance of a class.

Let's look at some examples below.

Example 1. The building class
An abstract building for describing buildings as a type of object (class)
Each building has the same attributes:

    the number of floors (an integer number);
    area (a floating-point number, square meters);
    year of construction (an integer number).

Each object of the building type has the same attributes but different values.

For instance:

    Building 1: the number of floors = 4, area = 2400.16, year of construction = 1966;
    Building 2: the number of floors = 6, area = 3200.54, year of construction = 2001.

It's quite difficult to determine the behavior of a building. But this example demonstrates attributes pretty well.

Example 2. The plane class
Unlike the building, it is easy to define the behavior of a plane. It can fly and transfer you between two points on the planet.
An abstract plane for describing all planes as a type of object (class)

Each plane has the following attributes:

    a name (a string, for example, "Airbus A320" or "Boeing 777");
    passengers capacity (an integer number);
    standard speed (an integer number);
    current coordinates (they are needed to navigate).

Also, it has a behavior (a method): transferring passengers from one geographical point to another. This behavior changes the state of a plane, namely, its current coordinates.
Conclusion about objects and classes

To put it concisely, you should remember the following:

    an object-oriented program consists of a set of interacting objects;
    as a rule, the internal state of an object is hidden;
    an object may have characteristics: fields and methods;
    an object is an instance of a class (type);
    a class is a more abstract concept than an individual object; it may be considered a template or blueprint that describes the common structure of a set of similar objects.

.......................................
Essentials Object-oriented programming Inheritance
Theory: Inheritance

Software development is strongly associated with real-world entities. However, we should consider not only the entities themselves but also the interactions between them. One of the ways it is presented in object-oriented programming is inheritance. This time we'll talk about this technique, and you'll get to know why it can be useful to apply it in your code.
What is inheritance?

We start making our program with basic objects and methods. Imagine a messenger application. The main objects in messengers are chats, so we start ours with the CHAT class. The time comes, and we diversify the chats to:

    direct messages to someone
    group chat
    saved messages only for yourself

If we want to make more types of chats, do we need to write the code from scratch for each one? The answer is no! With the help of inheritance, we can instead reuse the code we already have.

Inheritance is a relation between entities that we interpret as "is a" or "is a kind of" relation. In the case of programming methods and attributes, it means that a child entity has every feature of the parent entity. On the other side, we can also change inherited features or define the new ones in such relation.

Here are some examples of inheritance:

    A swan is a bird. A swan can do everything that a typical bird can do, but it has an additional feature: it can swim.

    A dentist is a doctor. He has medical education, he can cure a cold, and he knows a lot more about teeth than any other doctor.
    A laptop is a computer. It has processor units, memory, keyboard, and all other stuff computers typically have, but it is also portable.

Inheritance modeling

Let's stick to the example with a chat and see how we can model the classes of our program.

We can start by moving all the shared methods and attributes to the base CHAT class. For the sake of simplicity, we define only one attribute and only one method:

To make our base class more useful, we can add some more features like SEND_FILE, EDIT_MESSAGE, POSTPONE_MESSAGE, and others.

Next, we draw child classes and methods they need to work properly:

Let's take a closer look at the diagram and figure out what benefits the inheritance gives us. First, we don't need to implement any other methods to make a new class SAVED_MESSAGES: we add only one participant there, and it can work right out of the box! For the other two classes, we implement only some new methods like FETCH_MESSAGES to get updates from other participants and ADD_PARTICIPANT to add a new person to a group chat.

You may notice that we can even inherit the GROUP_CHAT from the DIRECT_MESSAGES to reuse its methods. It makes sense because there is not much difference between two, three, hundred persons to communicate in a chat, but the hierarchy is fine too.

Conclusion

Inheritance is a very flexible and useful mechanism in software development. It allows us to simplify and speed up the development process by reusing the code we've already written. As you have learned, it also reflects the dependency between the parent and child classes that we can express as "is a kind of" relation.
..................................

Theory: The concept of patterns
Code design

If you are reading this, you must be really interested in programming. It doesn't matter whether you are an experienced developer, just starting your career, or still working on the basics; what really matters is that you are curious, so welcome.

To begin with, let's talk about code design. In general, the design of your code is about expressing your ideas clearly to your teammates, colleagues, and clients. We can compare code to text: if you put the lines in the right order and make the structure clear, it will be much easier to explain and understand the text later. From an engineering point of view, your code is well-designed if you can agree with the following statements:

1) When you make a small change, it does not produce a ripple effect elsewhere in the code.
2) Your code is easy to reuse.
3) It is easy to maintain your code after release.
Design patterns

In application development, the design of code has to match the problem and be general enough in order to fit all the requirements that may arise in the future. Everyone tries to find more elegant, suitable and flexible solutions that can also be reused. Here is where design patterns come into play: these are repeatable solutions to common problems that developers face. Design patterns even have names! For example, if you want to confine yourself to just one instance of a class, Singleton pattern is going to be the best choice; if you see family relations between objects and you want to encapsulate creational process, you should use AbstractFactory, etc.

As a rule, examples of well-structured object-oriented architecture make use of patterns a lot. When a suitable pattern is used, it tells us that the developer has really paid attention to typical interactions between elements in the system. As a result, the architecture of an application becomes easier to understand.

Being so useful, design patterns have made it onto many programmers' bookshelves: one of the most famous examples is the book Design Patterns: Elements of Reusable Object-Oriented Software. You probably heard about its authors, "Gang of Four", which is frequently abbreviated as "GoF". Today it is considered one of the classic books on software design and programming. You may check it out to deepen your understanding or proceed directly to practical learning here.

Note that in this topic we will only consider object-oriented design patterns.

Software design patterns and related concepts

A great thing about patterns is that they help you not to waste your time reinventing the wheel so you can spend it on developing cool features instead. The structure of design patterns is strict: describe the problem, the solution, when to apply the solution, and its consequences. Theoretically, you can combine a few patterns and create your own monster pattern that contains, for example, Builder, Abstract Factory and Decorator simultaneously. However, as you will see from the following topics, it's better to avoid such monsters because patterns have already been well-grouped for you. In other words, don't get too excited, it's really better to use them one at a time.

Using patterns does not require any specific programming language skills or striking imagination. Patterns are also language-independent: even though they can be implemented differently in different languages, the general idea of each pattern is common for all of them. That means that it's possible for you to speak the language of architecture with your colleagues even if they work with different technologies.
Why should I know design patterns?

Here is a list of quite convincing reasons to get familiar with design patterns:

    Patterns provide tested and commonly used solution templates for design problems; you don't have to invent anything!
    Patterns improve flexibility and maintainability of object-oriented systems, which makes it easier to react to changing requirements.
    Patterns can speed up the development process.
    Patterns are a universal vocabulary that allows developers to describe a program design using a set of well-known identifiable concepts.
    Patterns are often used in standard libraries and frameworks.
    You can find patterns in the source codes of many applications and quickly understand how they work, instead of reading thousands of lines of code.

Caveats

In order to achieve flexibility, design patterns usually introduce additional levels of indirection, which in some cases may complicate the resulting designs and hurt application performance. In other words, even though patterns are supposed to make things easier for you, they may also become an unnecessary complication if applied unwisely. Beginner developers may try to apply patterns everywhere, even in situations where a simpler code would do just fine. Look how design patterns can complicate even the simplest "Hello, World" program.

To avoid misusing the patterns, you should apply them wisely and be able to correctly adapt them to your problem and language.
Final remarks

When you master the principles of working with patterns so that after successfully applying them you scream "Eureka!" without any doubt in your thoughts, your perception of object-oriented programming will probably change once and for all. In the following topics, you will learn about Creational, Structural and Behavioral design patterns. Be concentrated and attentive: these matters are quite advanced. Happy coding!
...........................

What are frameworks?

Every program is different just like snowflakes, yet it is the similarities that we want to direct your attention to, or rather, how these similarities can be used to the developer's advantage. In programming, it is common practice to reuse code packed into libraries in order to simplify the development and avoid making the same errors over and over. Such libraries exist for most programming languages; they provide good documentation and well-tested code used by many people.

Large applications like Internet stores, online banks or social networks often need the same typical components and functionality such as user authorization, database interaction, sending notifications and so on. To reuse them, developers created a special kind of software called frameworks for all popular programming languages.

A framework is a universal, reusable piece of software that facilitates the development of typical applications or their parts. It consists of structured code templates and provides generic functionality which can be easily extended for the needs of a specific application. To relinquish control on low-level tasks and focus on the high-level problems, you should use the API provided by the framework. It can significantly reduce total development time.

Some frameworks are so large that they are in fact a union of different frameworks under a single name.

Frameworks are extremely useful and relatively easy to grasp: for example, the very concept of frameworks has some real-life analogies that would make comprehension painless for all sorts of learners.
Frameworks vs libraries

At first glance, it might seem like frameworks and libraries are very similar, but it's not quite true.

Applications that use frameworks are built on top of them and extend their code to get specific functionality. In a sense, a framework serves as the skeleton of an application or its parts and sets "the rules of the game". A library, on the other hand, only provides some specific operations without having such a global influence. This is the key difference between frameworks and libraries. However, libraries can be provided as parts of frameworks.

Of course, there's no escape from evident similarities between frameworks and libraries. The programmer who uses a framework does not modify its source code — he/she acts only as its user.
Inversion of Control

The most common principle that comes with frameworks is Inversion of Control (IoC).

In a framework, unlike in libraries or standard user applications, the overall program's flow of control is dictated not by the caller, but by the framework. It means the framework calls your code, and not vice versa:

This happens because a framework provides templates for solving possible tasks and the interaction between the templates has been defined by developers of the framework. The user of a framework just takes the templates and extends them with application-specific code.
Advantages and disadvantages

Time to weigh everything. To start on a positive note, the use of frameworks has a number of strong advantages:

    rapid prototyping and development;
    standardization of project structures — it is easier to understand similar projects with the same structure;
    wide use in companies around the world;
    bug fixes and security updates by the authors;
    a well-designed skeleton — as a rule, frameworks use up-to-date practices and patterns to provide a firm skeleton for applications.

Despite the advantages, there is a number of common drawbacks:

    selecting an unsuitable framework can make an application harder to implement;
    application slowdown — frameworks often do a lot of heavyweight things hidden from programmers;
    it is difficult to replace the used framework with another one if yours no longer suits you (while libraries can be easily replaced);
    you may encounter a bug in the framework which may affect your work.

This might not be a complete list of advantages and disadvantages, but as you'll be getting more practice with using frameworks, you'll discover them for yourself.
How to choose frameworks

As a rule, each programming language has several frameworks to choose from. Of course, if you come to a company where some framework is already being used, there may be no choice for you. But if you do have a choice, try to take into account all possible benefits and problems when making a decision.

Here is some general advice for choosing a suitable framework:

    Pay attention to well-known frameworks with good documentation. This will greatly simplify the use and allow you to easily find developers already familiar with this framework. Some popular frameworks even become a de-facto standard for developing specific types of applications. Such frameworks should be considered first.
    If you write a small application that will most probably never change, you can develop it without frameworks. Moreover, for such an application they can introduce unnecessary additional complexity. But you may also consider the use of the so-called lightweight frameworks or choose a framework only for some part(s) of your application.

This is general information; as we said, programs are different, and so are the possible frameworks out there. The best part is getting to know specific frameworks and working with them closely.
............................

Theory: Data and object mapping

Programming languages may include primitive types, classes and data structures to store information. If you want to modify an object or interact with it somehow, you would prefer to do it in your favorite programming language, wouldn't you? As a developer, you use tools you're familiar with. In the local environment, you can complete most of your tasks this way. However, to communicate with other systems and to store data persistently, you need to convert your local types to commonly used data representation.
Data mapping

Assume that you are developing a social network service. Every moment, some users search for a friend and the service should reply with some information about other users in the network.

We represent each person as an instance of the Person class in the code. Let's stick to a simple diagram to avoid using any specific programming language:

The problem arises when you want to retrieve the information about a person from the storage you use. Relational databases often play the role of the storage but in the form of tables and relations between them. Luckily you're not the first person that faces the task to convert one common data type to another. Just find a library for data mapping and it will help you a lot.

Data mapping is matching fields of source data representation to the fields of its destination. In our case, the source is a database, and the destination is the Person class, but the operation is applicable vice versa. In other tasks, we could use other mappings for the Person class and convert it to/from JSON, XML.

We use data mapping to convert the information from one type to another, but we don't synchronize the data changes over time by default, we only want a different view at the particular moment.
Object Mapping

The structure of data in the source system may be different from the structure of data in the destination system. We could store the information about the name in one place and the information about the age in another because retrieving data to Person class is not the only purpose of the storage. This time data mapping will only match the part of the data we needed. For complex operations like this one, we need a more appropriate instrument such as object mapping.

Object mapping is matching data from a source system to a complex object in the destination system.

The most commonly used example is ORM (Object-Relational Mapping) when the data from relational databases is matched with the classes in object-oriented languages.

The main distinction between data and object mapping is that object mapping not only stores data but also emulates the behavior of an object and reflects changes in its source system. As a developer, you can call methods of the class, and data mappings will change at the same time. In short, object mapping is like data mapping, but with high-level control over changes.
The life cycle of mapping

To see what is data and object mapping in action, let's continue our work with the social network. We receive a query with some name and look for it in our data storage. As soon as we find an appropriate result, we retrieve the information about the person from the database. We fill the class instance with the result of the search.

Now our class is only a data container and nothing more, and this action is an example of data mapping. If we store the object in the database, it's a reversed example.

The age of a person is changing over time, but the storage is not aware of such changes, so we implement a method that adds a year to the age attribute:

After the age is changed in the instance of the class, the value in the storage becomes outdated. If we want to mirror it, we should put some effort into working with the storage, then we need to synchronize the information. This can take place in the same method or we can define another one for it.

This operation refers to object mapping; we are not only changing the object but also synchronizing data for it. Now our object has actual information in the storage, too. Synchronization is one of the important features of mapping; we want to have the definite representation of an object in our language and in the storage it uses. However, it's not obligatory to synchronize objects every time we change them. Sometimes it's more efficient to accumulate all the changes before the synchronization.
Conclusion

We have learned two new concepts: data mapping and object mapping. We use data mapping to match data in two different systems, and we use object mapping to represent more complex objects and to add control from one system to data in another.
............................

Theory: Introduction to databases

The world today is overloaded with information, and so are we. How do you keep important information safe and sorted? You may simply hope you neither forget nor confuse anything, but it's better to write it down or save it on your device. So you have it on your computer or phone, and the program keeps the information safe. While the program is active, it "remembers" everything. However, quitting the program may result in losing all that information. That's why it is better to keep the data using more sophisticated tools.

The challenge is to navigate a huge and complex web of information and ensure everything important is safe and organized: a task that databases handle well.
Database

A database is a collection of data that is specifically organized for rapid search and retrieval processed by a computer.

The difference between a database and a usual file is that a file may be structured or not, but a database must have a specific structure. For example, you can create a file with a to-do list:

Obviously, we'd say that this file has some kind of a structure, but from a computer's perspective, it's still a plain file, until you write a program that manages data in it. Usually, the information in databases is compressed and stored as binaries rather than plain text, so it's clear that this kind of structure is meant for computers, not humans.

Unlike us, computers can easily understand the binary format of data, but what allows them to read and write it correctly? It is a program called Database Management System that controls the data in a database.
Database Management System

Database Management System (DBMS) is a type of software that allows users to define, create, and control data in a database.

DBMS is a mediator between a user and a database, which means that users can work with databases through the interface of DBMS.

We need DBMS to make databases more efficient, because developers can optimize data structures and algorithms for databases independently of the user interface.

Another goal of this software is to help users work with different databases without exposing their actual differences.

Most database management systems have pretty good descriptions and tutorials on their sites. There are also specific languages that you need to learn to start working with a database, but if you know programming languages, you can work with a database with their tools instead.

Although it sounds like all databases have different syntax, most of them actually implement common standards. Almost all relational databases use the SQL standard, so you can apply the same commands in different DBMS's.

Access to data

At this stage, you may still have doubts as to using databases. You have to learn a new language to update and select the data, which can be time-consuming, so why not use plain files instead?

Of course, you can keep the files locally, but as they grow in number, you won't be able to find information quickly. Databases provide schemas and metadata that allow for a quick search of the needed data.

A schema describes how YOU organize the data. Metadata holds structural and statistical information.

If you want to access your data from multiple devices, most systems provide a convenient way to work with them through the web.

To open restricted access to another person, some management systems use simple login/password authentication, while some provide more powerful instruments. With their help, you can grant access to a limited portion of data for each user.

If you still are not convinced how great the DBMSs are, let's look at what else you can get from them.
Data consistency

One of the best features of databases is their ability to keep and restore the data correctly. It doesn't mean that the DBMS knows how to be correct, but once you define the correctness with the configuration or schema, you can be sure that nothing will break these rules. DBMS can provide you with formats you can use for your data. You can also set up all the tests and constraints that you want to have.

Say you have some data that multiple users with their devices have access to: this may potentially create a conflict of updates. Updates in files usually follow the "last save wins" rule. Databases, on the other hand, isolate different users and can be configured to resolve conflicts between their updates

There's another good thing about databases. When a usual file becomes corrupted and cannot be opened, you've lost your data forever. Using DBMS instead, you can make backups and then restore the data to continue your work.

Of course, you can emulate all of these operations and develop your DBMS, but first, try to work with the existing solutions.

Conclusion

There's a lot of learning you need to do before you start working with databases. No pains, no gains, and here you can actually gain a lot.

With databases you can:

    Store, retrieve and update data
    Get metadata and data dictionaries
    Access database remotely
    Restrict accesses to data
    Make concurrent updates
    Recover to some point of time
    Check the rules for data consistency automatically

In a data-driven world, this kind of functionality is golden. Welcome to the world of new opportunities and good luck with exploring the databases!
............................

Theory: What is SQL
Introduction

SQL (Structured Query Language) is a domain-specific programming language designed to handle data in tables. It was developed in the 1970s, and to this day SQL-like interfaces are widely used and supported in data management systems, even those that are not based on the concept of a table.

Because of its applicability, you'll probably find SQL quite useful. If you are a software engineer, it's a good idea to learn it because many software systems store and process business data via services that support SQL. For example, the information system backend of an insurance company may use SQL to extract and update data about the clients.

If you are interested in analytics, with the help of SQL you'll be able to easily aggregate data and calculate statistics. Suppose you need to evaluate changes in popularity of the name Jessie between 1920 and 2000 (inclusive) based on census data. In SQL, this task would take only 11 strings of code! You may not understand the code now, just try to read it as a sentence in English. It selects records about individuals named Jessie and born between 1920 and 2000; then it groups records for each pair of year and gender; counts the number of records in each group; and generates, as a result, a table with columns "year", "gender", and "cnt" sorted by year and gender.

If you work in a data-based company, know that SQL is basically a standard of data manipulation language.

There's a lot to take from SQL and there's a lot to learn. We suggest to start with the very basics: that is, what SQL stands for. Let's take apart the abbreviation to know what we're dealing with.
S is for Structured

SQL is a language used to extract and update data structured as tables. Such data appears in various application areas: for example, Excel sheets with accounting data, census statistics in Google BigQuery, or online stores that utilize a special software system for storing and using tables called Relational Database Management System (RDBMS) which helps process information about goods, orders, and customers.

SQL is designed for tables with the following structure: a table contains rows each representing an entity or an object and columns with attribute names of these entities. A table cell from row R and column C stores the value of attribute C of entity R. For instance, in table "census" from our example rows represent individuals and each of them having attributes "id", "year", "name", and "gender". For instance, the third row contains data about Willie, a man born in 1985.

Quite often, data is organized in a bunch of tables with names, what is usually called a database, and one may address these tables by their names. For example, in a database for an online store, a table "Customers" contains data about customers (their names and contacts), while "Orders" stores information about orders (customer, goods, payment details).
Q is for Query

SQL is a programming language with a large feature set for data processing. SQL is a declarative language and thus any statement written in it is a query that states to the system what should be done or evaluated, but not how.

Let's focus on the simplest and most basic functionality of data extraction from a table. For example, if we have a table named "Customers", a query that extracts all rows and columns is the following:

SELECT * FROM Customers;
L is for Language

That simple query from the example above may be read as "select everything from customers". SQL was designed to be similar to natural language. Declarative nature of SQL hides the complexities from the user and, to some extent, you just declare your will while the system analyses the query, chooses the control flow, and executes it.

Just like any natural language, SQL has a standard of the American National Standards Institute (ANSI) and many dialects implemented by vendors of software that support SQL. Usually, dialects are based on the standard, but they still show differences in some technical details, for example, in processing dates and strings. This means that SQL queries in different dialects are not compatible. However, once you know the SQL basics, you'll be able to adapt to different dialects, like with American and British English.

Here and further, in case of incompatibility between vendors and ANSI standard we provide syntax for MySQL.
Conclusion

Now you know that SQL is a domain-specific declarative language for those who work with structured data.

If you have data that can be organized in tables and you want to know how to select rows and columns according to some criteria, join facts, create groups of entities, calculate statistics and much more, let's dive deeper in SQL.
............................

Theory: Object-Relational Mapping(ORM)

A programming language is a tool to process data from one state to another. If we want to save the state of data permanently, we need some storage. Usually, for this purpose, we use a relational database, but then a problem occurs: programming languages and databases work with data differently. Moreover, relational databases have their language named SQL (Structured Query Language).

Luckily we are not the first people on Earth to suffer from this trouble. There is an approach called Object-Relational Mapping or ORM that is able to "translate" the database-way of interacting with information in an object-oriented way or to translate it backward.
ORM concept

Almost all programming languages have ORM libraries, but before you start using them, let's find out what is ORM idea about.

Object-Relational Mapping is a concept of converting data from an object-oriented programming language to relational database representation and vice versa. It solves the problem of matching two different type systems together and synchronize the data flow between them.

The main parts of ORM are:

    Virtual tables
    Relations
    Operations with objects

So what are these parts, and why do we need them?
Virtual tables

Relational databases use tuples and tables to store data. Most of the programming languages have tuples but don't have tables. How can we represent them in a programming language?

The main idea is to use classes as tables descriptions. We create a class as a virtual table for the given table in the database. We use or define methods for this class to retrieve, change and delete data

To represent one row from the table, we can define another class (for some libraries it can be the same class), and match its attributes to columns of the table. The instance of this class can manipulate not only the values of the row but also relations this row has, we will discuss it below.

Let's look at the example with the class City. We match values in tables with scalar attributes in the class. The name can be a string. Longitude and latitude can be real numbers.

As you know, a class can have attributes that represent a list of other objects. For example, a city may have a lot of streets. It contradicts attribute-to-column mapping, but the ORM provides instruments for these cases too. In terms of relational databases, the link between one object and several others is called one-to-many relation. It's quite similar to a list attribute of an object.
Relations

The relation is a link that connects a value from one table to the row in another. The database can store such links as keys. You can think about it as an object containing another object as an attribute.

Relations in databases are more than simple links. When you delete the root row from one table, it can imply cascade deletions of all related rows from other tables. It's not the same logic as for a programming language. If you have a link in an object, you expect that when you delete this link, only the link will disappear, not the connected object itself. On the other hand, if your database has a table "City" and London city in it, you can suppose when you delete London city from the table, all related rows from the table "Street" will disappear too. A street belongs to the city; without the city, there are no streets.

We can represent the example as the class City with a list of streets or as the many instances of class Street with an attribute City.

You may expect that if you delete the city, you will remove it with all the appropriate streets. However, if you delete the street and it has an attribute city, the city will stay in the database. It means that relations have directions. The cascade deletions imply the deletion of dependent objects, not dependent on ones.

Operations on objects

Four common-used operations with rows in the database are known as CRUD (Create, Read, Update, Delete) operations. It's similar to what we can do with objects in the programming language.

After you've read about tables and relations, you can try to control them via ORM library. Libraries usually provide high-level commands that look like working with any other objects in the programming language. Knowing something about relations and tables helps you not to corrupt data in the database.

It's highly recommended to read the documentation for the ORM library before using it. It helps you to get acquainted with the effects and consequences of applied operations.

Pros and Cons

If you still do not know, should you use ORM for your project or not, you can consider some pros and cons that this concept has.

Pros:

    You work with a database the same manner you write another code
    The library isolates your code from the specificity of SQL language of the database you're using
    The code using ORM is usually easier to read, write and maintain
    You don't have to know SQL to work with a database

Cons:

    Sometimes ORM libraries generate inefficient queries to a database
    It's hard to control the generation of queries
    You cannot use all the features and strengths of the specific database you have
    You should learn how to work with the library still

ORM is a good starting point for a project working with a database. Give it a chance and only then start interacting with a database directly. ORM will likely serve all your needs.

To start working with an ORM library, you may consider SQLAlchemy for Python, Hibernate or JPA for Java/Kotlin, Sequalize or TypeORM for JavaScript.

............................
Theory: Django ORM
Working With a Database From Python

Chances are, the storage you most often work with is a file system. It works well for HTML pages and templates, but how do you keep small objects like login, age or, say, favorite color for each individual person? Relational databases can help you organize and manipulate such data.

We will start from scratch and learn how to work with databases using only Python.

We define models to describe the schema of our data. To convert Python objects and primitives to database types, we will use adaptor classes, Fields. These abstractions help us pay less attention to the database specifics and focus mainly on what to store and how.

Once we declare the models and the fields in them, we create migrations and apply them to the SQLite3 database. Feel free to change it to another database backend. No matter which database you choose, our code will remain valid.
Relational Databases

If your first thought is "I need to keep the data with a common structure", then your second thought should surely be "databases".

A relational database is a collection of multiple data sets organized by tables, records, and columns. It works fine for most types of data. Each implementation provides you the universal language called structured query language (SQL). You can read about it, but as we say, we will work with the database in another way.

The most popular databases are PostgreSQL, Oracle SQL, MS SQL, and MySQL. There is also a simple database that works on your smartphone in many applications: it's called SQLite. It's perfect for one-client use and trying out Django models for the first time. Check whether you have it on your computer:

sqlite3 --version

If you don't, try to install it with your package manager or download it from the official site.
Object-Relational Mapping

With the fall approaching and clouds getting denser, the new season of Quidditch is starting. As you know, wizards really lack computer science classes in Hogwarts, even though programming is a kind of magic. They want to store the teams, their results and the rosters on the website, and they wonder if there is a way to do to it with Django. Well, there sure is! For this purpose, we will make the quidditch project with the tournament app in it. Let's meet and greet Django Models!

Django Models are classes that map the objects from the real world to the database records. We have teams, so we call our model the Team. This approach is called Object-Relational Mapping(ORM).

The ORM is a concept to map one type system to the other. We will work with databases by means of Python classes and methods. Our strong side is the programming language and we are going to make the most of it. The objects are similar to database records and their methods resemble SQL commands. There's no need to know SQL directly as we apply the instruments that imitate it.

To tell Django that it's a special class which maps its structure to the database table, we inherit the Team from django.models.Model. Also, we have players and game tables. Let's make the stubs for our classes in tournament/models.py module:

from django.db import models


class Team(models.Model):
    name = ...


class Player(models.Model):
    height= ...
    name = ...
    team = ...


class Game(models.Model):
    date = ...
    home_team = ...
    home_team_points = ...
    rival_team = ...
    rival_team_points = ...

We gave names to our classes and described their content. The restriction of all relational databases is that we should define the types for all the fields in the Model. So how can we match the types with the fields?
Fields

To get most of the database's features, we use special Fields classes. They map the attribute of the class to a particular column in the database table. Does it mean we need the instance of a class for each field? Yes, but don't worry, it's actually easier than it may seem.

To build the whole schema, we start from the core element, the Team:

class Team(models.Model):
    name = models.CharField(max_length=64)

CharField is similar to Python string but has one restriction: the length limit. "Wigtown Wanderers" is the longest team name in the league now, but the league is still open to new teams, so we ensure max_length with 64 symbols.

Each team has players. Let's define a model for a player:

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

We already know what the CharField means, so the FloatField should sound familiar to you, too. It's the same as Python's float type. What's more interesting is the ForeignKey field. It means that the player is bound to a specific Team and the restriction on_delete=models.CASCADE means that if the Team is deleted from the database, it will be erased with all the players. That sounds unfair, but you should try harder to stay in the league!

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

There are no games without teams, so again we set on_delete=models.CASCADE for each ForeignKey. Also, we add the related_name for the Game model, by which we can access it from the Team model. It's necessary to add such names because we have two foreign keys to the Team and you should differ one from another.

Points is an int type, so we make it IntegerField, and the date is clearly a DateField.

You can think of Fields as expansions of Python's primitive types for simple cases like IntegerField, CharField, and FloatField. They also have special cases like ForeignKey and other relations between objects.
Migrations

At this point, we describe the mappings between Python classes and database tables, but we don't have any tables yet. That's sad news. Should we learn some fancy SQL to create a database and tables in it? No, because we can simply describe to Django what we want and it will do the dirty work for us — again.

Add tournament to INSTALLED_APPS in the quidditch/settings.py module:

INSTALLED_APPS = [
    # other installed apps
    'tournament',
]

We have the schema of the league in our code, we are ready to migrate it to the database. It takes two steps:

python manage.py makemigrations
python manage.py migrate

The first command creates migrations. Migration is a piece of code that describes what actions should be done in the database to synchronize the models with the tables. You can find the created code in the tournament/migrations/0001_initital.py file.

In the second step, we apply the changes and run the generated commands.

Preceding manage.py <command> with python is the platform-independent way to launch any django command. It's a valid syntax for both Unix and Windows systems.

If you want to make and then apply migrations to a particular application in your project, you should add the application name after each command:

python manage.py makemigrations tournament
python manage.py migrate tournament

When you run these commands, your database will finally have the tables to work with. We are ready to fill them with real data!
............................

Theory: Intro to computational thinking

A programming language allows us to explain to a computer how to execute a solution to a particular problem in the real world. But first, a programmer has to come up with the solutions, also using a skill necessary for any type of programming no matter the language. It is called computational thinking.
What is computational thinking?

Computers can only deal with clear, concise instructions that agree with the rules of formal logic. However, real-world problems are rarely cut so clearly. Computational thinking is a set of mental skills helping to see the problems as a set of complex information processes that we can transform into a particular set of instructions for a computer.

Approach every problem you encounter while learning a programming language as not only the opportunity to remember the syntax of the language but also as an opportunity to train computational thinking.

To do that, you can follow a simple algorithm:

    Describe the problem
    What exactly needs to be done? What input data are you given and how does the desired outcome look like?
    Identify the important details needed to solve this problem
    Before thinking of a solution, make sure you took into account all the important aspects of the problem. The devil is in the details, and in case of programming, it hides in edge cases.
    Decompose
    Break the problem down into small, logical steps until you know exactly how to code each part of it.
    Use these steps to create an algorithm that solves the problem
    Connect the pieces of the problem in a way that would produce the desired outcome in all specified cases.
    Evaluate the process
    Usually, a problem has at least a few solutions, and it’s very useful to evaluate your idea to make sure you've chosen a way that is as efficient as possible.

Conclusion

Since computational thinking is a skill, it requires lots of practice before you can easily apply it. Don’t despair if your only thought when looking at a problem is that you have no idea how to achieve the desired results. Use the algorithms we described and keep on breaking the problem down until you see how to explain it to a computer with the tools of the programming language you chose.
..................

Theory: Components of computational thinking

Computational thinking is a set of skills that helps you come up with a generalizable solution to a problem and solve it using a computer.
Let’s elaborate on the main foundations of this skill, namely: abstraction, decomposition, pattern recognition, and evaluation.
Decomposition

Complex problems are easier to solve when we break them down into separate steps and subproblems. We do this all the time in our daily life as well. For example, if your goal is to make a pizza, you’d need to find a recipe, shop for all the relevant ingredients, heat the oven, make the dough, chop the toppings and finally bake the pizza for an appropriate amount of time. Breaking down a problem like that helps to focus on solving each subproblem separately (and maybe even reusing solutions other people came up with) and avoid being overwhelmed by the requirements.
Extracting and Generalizing patterns

Once the problem is decomposed our next step would be to look for patterns in the smaller subproblems. A pattern is a set of features in a task that is shared among more than one instance of the problem. For example, if you need to cook Pepperoni pizza, you’d need to make a flat pizza bottom. The bottom is a pattern shared among all the pizzas, so you can generalize this pattern and if you wish to later make Margherita you can reuse all the information and steps you took for preparing Pepperoni pizza.

Pattern recognition is based on the five key steps:

    Identify common elements in problems or systems

    Identify and Interpret common differences in problems or systems

    Identify individual elements within sub-problems

    Describe patterns that have been identified

    Make predictions based on identified patterns.

Abstraction

Abstraction helps us generalize the solution by figuring out a model of a situation. We get rid of all the unnecessary details to focus on what’s actually important. One can say that a programming language is an abstraction. You use variables to perform operations instead of listing all the data these variables stand for every time.

It’s exactly the abstraction that helps us come up with a generalizable solution without writing a separate program for each variation of the problem.

If we come back to pizza, and try to apply abstraction we would say that for pizza to be a pizza it needs flat dough, sauce, and toppings.

The shape of the pizza and the fact that it has cheese would be unnecessary details since it is possible to imagine square pizza with no cheese.

Therefore if we abstract our pizza like a flat dough open pie with toppings and sauce we would be able to write one program to perform operations on all the pizzas, no matter their taste, shape, and vegan friendliness.
Evaluation

Once you found a solution to your problem it is helpful to go through an evaluation checklist. At times your solution won’t work and this checklist can also help you to find out where you’ve gone wrong.

Make sure your solution is:

    easy to understand – usually that would be the case if the problem is well decomposed

    complete – Your solution covers all the aspects of the problem. Remember, the devil is in the corner cases.

    efficient – Make sure you are making the best of the tools you have, in case of programming it can regard using appropriate syntax constructions. Speed is one of the most important markers of the solution’s efficiency and becomes incredibly important when writing production code.

Applying the concepts we discussed is helpful to develop a more efficient and structured problem-solving process. After all, the ability to solve problems is what makes a programmer out of a person who knows a programming language.
............................

Theory: Integer arithmetic

In real life, we often perform arithmetic operations. They help us to calculate the change from a purchase, determine the area of a room, count the number of people in a line, and so on. The same operations are used in programs.
Basic operations

Python supports basic arithmetic operations:

    addition +
    subtraction -
    multiplication *
    division /
    integer division //

The examples below show how it works for numbers.

print(10 + 10)   # 20
print(100 - 10)  # 90
print(10 * 10)   # 100
print(77 / 10)   # 7.7
print(77 // 10)  # 7

There is a difference between division / and integer division //. The first produces a floating-point number (like 7.7), while the second one produces an integer value (like 7) ignoring the decimal part.

Python raises an error if you try to divide by zero.

ZeroDivisionError: division by zero

Writing complex expressions

Arithmetic operations can be combined to write more complex expressions:

print(2 + 2 * 2)  # 6

The calculation order coincides with the rules of arithmetic operations. Multiplication has a higher priority level than addition and subtraction, so the operation 2 * 2 is calculated first.

To specify an order of execution, you can use parentheses, as in the following:

print((2 + 2) * 2)  # 8

Like in arithmetic, parentheses can be nested inside each other. You can also use them for clarity.

The minus operator has a unary form that negates the value or expression. A positive number becomes negative, and a negative number becomes positive.

print(-10)  # -10
print(-(100 + 200))  # -300
print(-(-20))  # 20

Other operations

The remainder of a division. Python modulo operator % is used to get the remainder of a division. It may come in handy when you want to check if a number is even. Applied to 2, it returns 1 for odd numbers and 0 for the even ones.

print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

Here are some more examples:

# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)    # 4
print(11 % -5)    # -4

Taking the remainder of the division by 0 also leads to ZeroDivisionError.

The behavior of the mod function in Python might seem unexpected at first glance. While 11 % 5 = 1 and -11 % -5 = -1 when both numbers on the left are of the same sign, 11 % -5 = -4 and -11 % 5 = 4 if we have one negative number. The thing is, in Python, the remainder always has the same sign as the divisor.

In the first case, 11 % -5 = -4, as the remainder should be negative, we need to compare 15 and 11, not 10 and 11: 11 = (-5) * (-3) + (-4). In the second case, -11 % 5 = 4, the remainder is supposed to be positive: -11 = 5 * (-3) + 4.

Exponentiation. Here is a way to raise a number to a power:

print(10 ** 2)  # 100

This operation has a higher priority over multiplication.
Operation priority

To sum up, there is a list of priorities for all considered operations:

    parentheses
    power
    unary minus
    multiplication, division, and remainder
    addition and subtraction

As mentioned above, the unary minus changes the sign of its argument.

Sometimes operations have the same priority:

print(10 / 5 / 2)  # 1.0
print(8 / 2 * 5)   # 20.0

The expressions above may seem ambiguous to you, since they have alternative solutions depending on the operation order: either 1.0 or 4.0 in the first example, and either 20.0 or 0.8 in the second one. In such cases, Python follows a left-to-right operation convention from mathematics. It's a good thing to know, so try to keep that in mind, too!
PEP time!

There are a few things to mention about the use of binary operators, that is, operators that influence both operands. As you know, readability matters in Python. So, first, remember to surround a binary operator with a single space on both sides:

number=30+12      # No!

number = 30 + 12  # It's better this way

Also, sometimes people use the break after binary operators. But this can hurt readability in two ways:

    the operators are not in one column,
    each operator has moved away from its operand and onto the previous line:

# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

Mathematicians and their publishers follow the opposite convention in order to solve the readability problem. Donald Knuth explains this in his Computers and Typesetting series: "Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations". Following this tradition makes the code more readable:

# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

In Python code, it is permissible to break before or after a binary operator, as long as the convention is consistent locally. For new code, Knuth's style is suggested, according to PEP 8.

............................

Theory: Program with numbers

Programs in which there's nothing to calculate are quite rare. Therefore, learning to program with numbers is never a bad idea. An even more valuable skill we are about to learn is the processing of user data. With its help, you can create interactive and by far more flexible applications. So let's get started!
Reading numbers from user input

Since you have become familiar with the input() function in Python, it's hardly new to you that any data passed to this function is treated as a string. But how should we deal with numerical values? As a general rule, they are explicitly converted to corresponding numerical types:

integer = int(input())
floating_point = float(input())

Pay attention to current best practices: it's crucial not to name your variables as built-in types (say, float or int). Yet another caveat is related to user mistakes. If a user writes an inaccurate input, ValueError will occur. At the moment, we'll limit ourselves to this. But not to worry, more information about errors is available in a dedicated topic. Now, consider a more detailed and pragmatic example of handling numerical inputs.
Free air miles

Imagine you have a credit card with a free air miles bonus program (or maybe you already have one). As a user, you are expected to input the amount of money you spend on average from this card per month. Let's assume that the bonus program gives you 2 free air miles for every dollar you spend. Here's a simple program to figure out when you can travel somewhere for free:

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per piece of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)

This program will calculate how many months you need to travel the selected distance and back.

Although it is recommended to write messages for users in the input() function, avoid them in our educational programming challenges, otherwise your code may not pass our tests.

Advanced forms of assignment

Whenever you use an equal sign =, you actually assign some value to a name. For that reason, = is typically referred to as an assignment operator. Meanwhile, there are other assignment operators you can use in Python. They are also called compound assignment operators, for they carry out an arithmetic operation and assignment in one step. Have a look at the code snippet below:

# simple assignment
number = 10
number = number + 1  # 11

This code is equivalent to the following one:

# compound assignment
number = 10
number += 1  # 11

One can clearly see from the example that the second piece of code is more concise (for it doesn't repeat the variable's name).

Naturally, similar assignment forms exist for the rest of arithmetic operations: -=, *=, /=, //=, %=, **=. Given the opportunity, use them to save time and effort.

One possible application of compound assignment comes next.
Counter variable

In programming, loops are used alongside special variables called counters. A counter counts how many times a particular code is run. It also follows that counters should be integers. Now we are getting to the point: you can use the operators += and -= to increase or decrease the counter respectively.

Consider this example where a user determines the value by which the counter is increased:

counter = 1
step = int(input())  # let it be 3
counter += step
print(counter)  # it should be 4, then

In case you need only non-negative integers from the user (we are increasing the counter after all!), you can prevent incorrect inputs by using the abs() function. It is a Python built-in function that returns the absolute value of a number (that is, value regardless of its sign). Let's readjust our last program a bit:

counter = 1
step = abs(int(input()))  # user types -3
counter += step
print(counter)  # it's still 4

As you can see, thanks to the abs() function we got a positive number.

For now, it's all right that you do not know much about the mentioned details of errors, loops and built-in functions in Python. We will catch up and make sure that you know these topics comprehensively. Keep learning!

Thus, we have shed some light on new details about integer arithmetic and the processing of numerical inputs in Python. Feel free to use them in your future projects.
...............................

Theory: Boolean logic
Boolean type

The Boolean type, or simply bool, is a special data type that has only two possible values: True and False. In Python the names of boolean values start with a capital letter.

In programming languages the boolean, or logical, type is a common way to represent something that has only two opposite states like on or off, yes or no, etc.

If you are writing an application that keeps track of door openings, you'll find it natural to use bool to store the current door state.

is_open = True
is_closed = False

print(is_open)    # True
print(is_closed)  # False

Boolean operations

There are three built-in boolean operators in Python: and, or and not. The first two are binary operators which means that they expect two arguments. not is a unary operator, it is always applied to a single operand. First, let's look at these operators applied to the boolean values.

    and is a binary operator, it takes two arguments and returns True if both arguments are true, otherwise, it returns False.

    a = True and True    # True
    b = True and False   # False
    c = False and False  # False
    d = False and True   # False

    or is a binary operator, it returns True if at least one argument is true, otherwise, it returns False.

    a = True or True    # True
    b = True or False   # True
    c = False or False  # False
    d = False or True   # True

    not is a unary operator, it reverses the boolean value of its argument.

    to_be = True           # to_be is True
    not_to_be = not to_be  # not_to_be is False

The precedence of boolean operations

Logical operators have a different priority and it affects the order of evaluation. Here are the operators in order of their priorities: not, and, or. So, not is considered first, then and, finally or. Having this in mind, consider the following expression:

print(False or not False)  # True

First, the part not False gets evaluated, and after evaluation, we are left with False or True. This results in True, if you recall the previous section.

While dealing solely with the boolean values may seem obvious, the precedence of logical operations will be quite important to remember when you start working with so-called truthy and falsy values.
Truthy and falsy values

Though Python has the boolean data type, we often want to use non-boolean values in a logical context. And Python lets you test almost any object for truthfulness. When used with logical operators, values of non-boolean types, such as integers or strings, are called truthy or falsy. It depends on whether they are interpreted as True or False.

The following values are evaluated to False in Python:

    constants defined to be false: None and False,
    zero of any numeric type: 0, 0.0,
    empty sequences and containers: "", [], {}.

Anything else generally evaluates to True. Here is a couple of examples:

print(0.0 or False)  # False
print("True" and True)  # True
print("" or False)  # False

Generally speaking, and and or could take any arguments that can be tested for a boolean value.

Now we can demonstrate more clearly the difference in operator precedence:

# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100

Again, let's break the above expression into parts. Since the operator and has a higher priority than or, we should look at the 5 and 100 part. Both 100 and 5 happen to be truthy values, so this operation will return 100. You have never seen this before, so it's natural to wonder why we have a number instead of the True value here. We'll cover this surprising fact shortly. Coming back to the original expression, you can see that the last part False or 100 does exactly the same thing, returns 100 instead of True.

The operators or and and return one of their operands, not necessarily of the boolean type. Nonetheless, not always returns a boolean value.

Another tricky example is below:

tricky = not (False or '')  # True

A pair of parentheses is a way to specify the order in which the operations are performed. Thus, we evaluate this part of the expression first: False or ''. This operand '' evaluates to False and or returns this empty string. Since the result of the enclosed expression is negated, we get True in the end: not '' is the same as True. Why didn't we get, say, a non-empty string? The not operator creates a new value, which by default has the boolean type. So, as stated earlier, the unary operator always returns a logical value.
Short-circuit evaluation

The last thing to mention is that logical operators in Python are short-circuited. That's why they are also called lazy. That means that the second operand in such an expression is evaluated only if the first one is not sufficient to evaluate the whole expression.

    x and y returns x if x is falsy; otherwise, it evaluates and returns y.

    x or y returns x if x is truthy; otherwise, it evaluates and returns y.

For instance:

# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False

Those were the very basics of boolean values and logical operations in Python. It's definitely good to know them right from the beginning!
....................................

Theory: List

In your programs, you often need to group several elements in order to process them as a single object. For this, you will need to use different collections. One of the most useful collections in Python is a list. It is one of the most important things in Python.

Creating and printing lists

Look at a simple list that stores several names of dogs' breeds:

dog_breeds = ['corgi', 'labrador', 'poodle', 'jack russell']
print(dog_breeds)  # ['corgi', 'labrador', 'poodle', 'jack russell']

In the first line, we use square brackets to create a list that contains four elements and then assign it to the dog_breeds variable. In the second line, the list is printed through the variable's name. All the elements are printed in the same order as they were stored in the list because lists are ordered.

Here is another list that contains five integers:

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

Another way to create a list is to invoke the list function. It is used to create a list out of an iterable object: that is, a kind of object where you can get its elements one by one. The concept of iterability will be explained in detail further, but let's look at the examples below:

list_out_of_string = list('danger!')
print(list_out_of_string)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

list_out_of_integer = list(235)  # TypeError: 'int' object is not iterable

So, the list function creates a list containing each element from the given iterable object. For now, remember that a string is an example of an iterable object, and an integer is an example of a non-iterable object. A list itself is also an iterable object.

Let's also note the difference between the list function and creating a list using square brackets:

multi_element_list = list('danger!')
print(multi_element_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

single_element_list = ['danger!']
print(single_element_list)  # ['danger!']

The square brackets and the list function can also be used to create empty lists that do not have elements at all.

empty_list_1 = list()
empty_list_2 = []

In the following topics, we will consider how to fill empty lists.

Features of lists
Lists can store duplicate values as many times as needed.

on_off_list = ['on', 'off', 'on', 'off', 'on']
print(on_off_list)  # ['on', 'off', 'on', 'off', 'on']

Another important thing about lists is that they can contain different types of elements. So there are neither restrictions, nor fixed list types, and you can add to your list any data you want, like in the following example:

different_objects = ['a', 1, 'b', 2]

Length of a list

Sometimes you need to know how many elements are there in a list. There is a built-in function called len that can be applied to any iterable object, and it returns simply the length of that object

So, when applied to a list, it returns the number of elements in that list.

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

empty_list = list()
print(len(empty_list))  # 0

single_element_list = ['danger!']
print(len(single_element_list))  # 1

multi_elements_list = list('danger!')
print(len(multi_elements_list))  # 7

In the example above, you can see how the len() function works. Again, pay attention to the difference between list() and [] as applied to strings: it may not result in what you expected.
Recap

As a recap, we note that lists are:

    ordered, i.e. each element has a fixed position in a list;
    iterable, i.e. you can get their elements one by one;
    able to store duplicate values;
    able to store different types of elements.

............................
Theory: If statement
Simple if statement

There are situations when your program needs to execute some piece of the code only if a particular condition is true. Such a piece of the code should be placed within the body of an if statement. The pattern is the same as in the English language: first comes the keyword if , then a condition, and then a list of expressions to execute. The condition is always a Boolean expression, that is, its value equals either True or False. Here is one example of how the code with a conditional expression should look like:

biscuits = 17
if biscuits >= 5:
    print("It's time for tea!")

Note that the condition ends with a colon and a new line starts with an indentation. Usually, 4 spaces are used to designate each level of indentation. A piece of code in which all lines are on the same level of indentation is called a block of code. In Python, only indentation is used to separate different blocks of code, hence, only indentation shows which lines of code are supposed to be executed when the if statement is satisfied, and which ones should be executed independently of the if statement. Check out the following example:

if biscuits >= 5:
    print("It's time for tea!")
    print("What tea do you prefer?")
print("What about some chocolate?")

In this example, the line "It's time for tea!", as well as "What tea do you prefer?", will be printed only if there are 5 or more biscuits. The line "What about some chocolate?" will be printed regardless of the number of biscuits.

An if statement is executed only if its condition holds (the Boolean value is True), otherwise, it's skipped.

Boolean values basically make it clear whether a piece of code needs to be executed or not. Since comparisons result in bool, it's always a good idea to use them as a condition.

There is one pitfall, though. You should not confuse the comparison operator for equality == with the assignment operator =. Only the former provides for a proper condition. Try to avoid this common mistake in your code.

Nested if statement

Sometimes a condition happens to be too complicated for a simple if statement. In this case, you can use so-called nested if statements. The more if statements are nested, the more complex your code gets, which is usually not a good thing. However, this doesn't mean that you need to avoid nested if statements at whatever cost. Let's take a look at the code below:

rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colors = "red, yellow, orange"
my_color = "orange"

if my_color in rainbow:
    print("Wow, your color is in the rainbow!")
    if my_color in warm_colors:
        print("Oh, by the way, it's a warm color.")

The example above illustrates a nested if statement. If the variable my_color is a string that contains the name of a color from the rainbow, we enter the body of the first if statement. First, we print the message and then check if our color belongs to the warm colors. The membership operator in simply shows whether my_color is a substring of the respective string, rainbow or warm_colors. Just like arithmetic comparisons, it returns a boolean value.

Here is what we will see in our case:

Wow, your color is in the rainbow!
Oh, by the way, it's a warm color.

When it comes to nested if statements, proper indentation is crucial, so do not forget to indent each statement that starts with the if keyword.
Report a typo
............................
Theory: For loop
What is iteration?

Computers are known for their ability to do things which people consider to be boring and energy-consuming. For example, repeating identical tasks without any errors is one of these things. In Python, the process of repetitive execution of the same block of code is called an iteration.

There are two types of iteration:

Definite iteration, where the number of repetitions is stated in advance.

Indefinite iteration, where the code block executes as long as the condition stated in advance is true.

After the first iteration, the program comes back to the beginning of the code’s body and repeats it, making the so-called loop. The most used one is the for loop, named after the for operator that provides the code’s execution.
For loop syntax

Here is the scheme of the loop:

for variable in iterable:
    statement

where statement is a block of operations executed for each item in iterable, an object used in iteration (e.g. string or list). Variable takes the value of the next iterable after each iteration.

Now try to guess which output we'll get if we execute the following piece of code:

oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)

During each iteration the program will take the items from the list and execute the statements with them, so the output will be:

Atlantic
Pacific
Indian
Southern
Arctic

Even strings are iterable, so you can spell the word, for example:

for char in 'magic':
    print(char)

Like this:

m
a
g
i
c

Range function

The range() function is used to specify the number of iterations. It returns a sequence of numbers from 0 (by default) and ends at a specified number. Be careful: the last number won’t be in the output.

Let's look at the example below:

for i in range(5):
    print(i)

What we'll get is this:

0
1
2
3
4

You can change the starting value if you’re not satisfied with 0, moreover, you can configure the increment (step) value by adding a third parameter:

for i in range(5, 45, 10):
    print(i)

According to the parameters included, we’ve asked to print the numbers from 5 to 45 with an increment value of 10. Be careful again, the last value is not included in the output:

5
15
25
35

If you're not going to use the counter variable in your loop, you can show it by replacing its name with an underscore symbol:

for _ in range(100):
    do_smth()

In the example above, we don't need the counter variable in any way, we simply use the loop to repeat do_smth() function a given amount of times.
Input data processing

You can also use the input() function that helps a user to pass a value to some variable and work with it. Thus, you can get the same output as with the previous piece of code:

word = input()
for char in word:
    print(char)

Oh, look, you can write a piece of code with a practical purpose:

times = int(input('How many times should I say "Hello"?'))
for i in range(times):
    print('Hello!')

You can, therefore, ask a user to specify the number of iterations to be performed.
Nested loop

In Python, it is easy to put one loop inside another one – a nested loop. The type of inner and outer loops doesn't matter, the first to execute is the outer loop, then the inner one executes:

names = ['Rose', 'Daniel']
surnames = ['Miller']
for name in names:
    for surname in surnames:
         print(name, surname)

The output is shown below:

Rose Miller
Daniel Miller

In this example, we use the two for loops to create fictional people's names. Obviously, you can deal with iterable objects of different sizes without too much fuss.
To sum up

All in all, for loops are an efficient way to automatize some repetitive actions. You can add variables and operations to make a nested loop. Moreover, you can control the number of iterations with the help of the range() function. Be careful with the syntax: an extra indent or lack of colon can cause a mistake!
Report a typo
............................
Invoking a function

min() and max() revisited
Easy
2 minutes
6719 users solved this problem. Latest completion was
9 minutes ago
.

Fun fact about min() and max() is that these functions can help you to sort in alphabetical order! If a string is passed as an argument, min() will return the first letter (alphabetically) and max() the last one (somewhat zetabetically). And if you specify more than one value, min() will return the first string in alphabetical order and max(), in contrast, the last one. For example, min("alpha", "omega") gives you "alpha", while max("alpha", "omega") returns "omega".

Follow this example and select correct outputs for the function calls below.
Match the items from left and right columns
max("gloomy", "grew", "green")
min("gloomy", "grey", "green")
min("green", "grass")
max("gloomy", "grey", "green")
"grass"
"grey"
"grew"
"gloomy"
............................

Theory: Declaring a function

Often enough, built-in functions cannot suffice even beginners. In such a case, there is no choice but to create your own function using the keyword def (right, derived from define). Let's have a look at the syntax:

def function_name(parameter1, parameter2, ...):
    # function's body
    ...
    return "return value"

After def, we write the name of our function (so as to invoke it later) and the names of parameters, which our function can accept, enclosed in parentheses. Do not miss the colon at the end of the line. The names of a function and its parameters follow the same convention as variable names, that is, they should be written in lowercase with underscores between words.

An indent of 4 spaces shows the interpreter where the function's body starts and where it ends. All statements in the function's body must be indented. You can make calculations inside your function and use the return keyword to send the result back. Only when the indentation is absent, the definition of the function ends.

Later, the parameters take on values passed in a function call. Those values we pass to a function are known as arguments. The only distinction between parameters and arguments is that we introduce parameters in a function definition and give arguments (some specific values) in a function call. Here is a bit less abstract example of a function:

# Function definition
def multiply(x, y):
    return x * y


# Function calls
a = multiply(3, 5)   # 15
b = multiply(a, 10)  # 150

In case you don't want to pass any arguments, the round brackets remain empty:

def welcome():
    print("Hello, people!")

You can also declare a sort of empty function with pass statement:

# This function does nothing (yet)
def lazy_func(param):
    pass

When you choose to call lazy_func() with an arbitrary value as its argument, nothing will happen. So pass is just a placeholder, but at least your code will be valid with it.
Parameters vs arguments

It's not quite clear right now, what the parameters are, is it? In fact, parameters are just aliases for values, which can be passed to a function. Consider the following example:

def send_postcard(address, message):
    print("Sending a postcard to", address)
    print("With the message:", message)


send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

send_postcard("Piccadilly, London", "Hi, London!")
# Sending a postcard to Piccadilly, London
# With the message: Hi, London!

As you can see, this function is a reusable piece of code, that can be executed with different arguments, i.e. different values passed into this function. Here, address and message are just the aliases under which the function receives values and then processes them in the body.

This function takes exactly 2 arguments, so you will not be able to execute it with more or less than 2 arguments:

send_postcard("Big Ben, London")

TypeError: send_postcard() missing 1 required positional argument: 'message'

Execution and return

Our previous function only performed some actions, but it didn't have any return value. However, you might want to calculate something in a function and return the result at some point. Check the following example:

def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# Convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp)  # 212.0

The keyword return is used to indicate what values the function outputs. Basically, it is the result of the function call. So, in the example above, we've stored the value returned by our function in the variable water_bp. Just to be sure, we printed the result.

One more thing to say is that functions do not necessarily have return values. The well-known print() function does not, in fact, return anything. Examine the code below:

chant = print("We Will Rock You")
print(chant)

And its output:

We Will Rock You
None

We declared the variable chant and invoked print(). Obviously, the function was executed. But the variable itself turned out to be the None object, which means the called function had nothing to return. The value of chant is None.

Python interpreter stops performing the function after return. But what if the function body contains more than one return statement? Then the execution will end after the first one. Please, keep that in mind!

Conclusion

Thus, we've learned the syntax for declaring functions. Now you also know that:

    Parameters of a function are simply aliases, or placeholders, for values that you will pass to them. Parameters are re-initialized every time you call the function. Inside the function, you have access to these values, which means you can perform calculations on them.
    A function can simply perform an action without returning anything or return a specific result. If your function doesn't return anything, assigning its result to a variable or printing it will give you None.

Declaring your own functions makes your code more structured and reusable. Whenever you use the same piece of code more than once, try to create a function of it!
...........................

Theory: Scopes

A scope is a part of the program where a certain variable can be reached by its name. The scope is a very important concept in programming because it defines the visibility of a name within the code block.
Global vs. Local

When you define a variable it becomes either global or local. If a variable is defined at the top-level of the module it is considered global. That means that you can refer to this variable from every code block in your program. Global variables can be useful when you need to share state information or some configuration between different functions. For example, you can store the name of a current user in a global variable and then use it where needed. It makes your code easier to change: in order to set a new user name you will only have to change a single variable.

Local variables are created when you define them in the body of a function. So its name can only be resolved inside the current function's scope. It lets you avoid issues with side-effects that may happen when using global variables.

Consider the example to see the difference between global and local variables:

phrase = "Let it be"

def global_printer():
    print(phrase)  # we can use phrase because it's a global variable

global_printer()  # Let it be is printed
print(phrase)  # we can also print it directly

phrase = "Hey Jude"

global_printer()  # Hey Jude is now printed because we changed the value of phrase

def printer():
    local_phrase = "Yesterday"
    print(local_phrase)  # local_phrase is a local variable

printer()  # Yesterday is printed as expected

print(local_phrase)  # NameError is raised

Thus, a global variable can be accessed both from the top-level of the module and the function's body. On the other hand, a local variable is only visible inside the nearest scope and cannot be accessed from the outside.
LEGB rule

A variable resolution in Python follows the LEGB rule. That means that the interpreter looks for a name in the following order:

    Locals. Variables defined within the function body and not declared global.
    Enclosing. Names of the local scope in all enclosing functions from inner to outer.
    Globals. Names defined at the top-level of a module or declared global with a global keyword.
    Built-in. Any built-in name in Python.

Let's consider an example to illustrate the LEGB rule:

x = "global"
def outer():
    x = "outer local"
    def inner():
        x = "inner local"
        def func():
            x = "func local"
            print(x)
        func()
    inner()

outer()  # "func local"

When the print() function inside the func() is called the interpreter needs to resolve the name x. It'll first look at the innermost variables and will search for the local definition of x in func() function. In the case of the code above, the interpreter will find the local x in func() successfully and print its value, 'func local'. But what if there isn't a definition of x in func()? Then, the interpreter will move outward and turn to inner() function. Check out the following example:

x = "global"
def outer():
    x = "outer local"
    def inner():
        x = "inner local"
        def func():
            print(x)
""""""
        func()
    inner()

outer()  # "inner local"

As you see, the name x was resolved in inner() function, since the value "inner local" was printed.

If we remove the definition of x from the inner() function as well and run the code again, the interpreter will continue the search among the outer() locals in the same fashion. If we keep deleting the lines of code defining x, the interpreter will move on to outer() locals, then globals, and then built-in names. In case there is no matching built-in name, an error will be raised. Look at the example where the global definition of x is reached by the interpreter:

x = "global"
def outer():
    def inner():
        def func():
            print(x)
        func()
    inner()

outer()  # "global"

Don't forget about LEGB rule if you plan on using enclosing functions.
Keywords "nonlocal" and "global"

We already mentioned one way to assign a global variable: make a definition at the top-level of a module. But there is also a special keyword global that allows us to declare a variable global inside a function's body.

You can't change the value of a global variable inside the function without using the global keyword:

x = 1
def print_global():
    print(x)

print_global()  # 1

def modify_global():
    print(x)
    x = x + 1

modify_global()  # UnboundLocalError

An error is raised because we are trying to assign to a local variable x the expression that contains x and the interpreter can't find this variable in a local scope. To fix this error, we need to declare x global:

x = 1
def global_func():
    global x
    print(x)
    x = x + 1

global_func()  # 1
global_func()  # 2
global_func()  # 3

When x is global you can increment its value inside the function.

nonlocal keyword lets us assign to variables in the outer (but not global) scope:

def func():
    x = 1
    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

def nonlocal_func():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

func()  # inner: 2
        # outer: 1

nonlocal_func()  # inner: 2
                 # outer: 2

Though global and nonlocal are present in the language, they are not often used in practice, because these keywords make programs less predictable and harder to understand.
Why do we need scopes?

First of all, why does Python need the distinction between global and local scope? Well, from the experience of some other programming languages that do not have local scopes it became clear, that using only global scope is highly inconvenient: when every variable is accessible from every part of the code, a whole bunch of bugs is inevitable. The longer the code, the more difficult it becomes to remember all the variables' names and not accidentally change the value of the variable that you were supposed to keep untouched. Therefore, Python saves you the trouble by allowing you to "isolate" some variables from the rest of the code when you split it into functions.

On the other hand, why do we need global scope then? Well, as was already mentioned above, global scope is one of the easiest ways to retain information between function calls: while local variables disappear the moment the function returns, global variables remain and help functions to transfer the necessary data between each other. Similarly, global variables can enable the communication between more complex processes, such as threads in multithreaded applications.
............................

Theory: Else statement
Simple if-else

An if-else statement is another type of conditional expressions in Python. It differs from an if statement by the presence of the additional keyword else. The block of code that else contains executes when the condition of your if statement does not hold (the Boolean value is False). Since an else statement is an alternative for an if statement, only one block of code can be executed. Also, else doesn't require any condition:

if today == "holiday":
    print("Lucky you!")
else:
    print("Keep your chin up, then.")

Note that the 4-space indentation rule applies here too.

As you may soon find out, programmers do like all sorts of shortcuts. For conditional expressions there's a trick as well – you can write an if-else statement in one line. This is called a ternary operator and looks like this:

print("It’s a day now!" if sun else "It’s a night for sure!")

Or, more generally:

first_alternative if condition else second_alternative

It's a matter of convenience, but remember that the code you create should still be readable.
Nested if-else

It should be mentioned, that if-else statements can be nested the same way as if statements. An additional conditional expression may appear after the if section as well as after the else section. Once again, don't forget to indent properly:

if x < 100:
    print('x < 100')
else:
    if x == 100:
        print('x = 100')
    else:
        print('x > 100')
    print('This will be printed only because x >= 100')

Now you are ready not only to set conditions but also to consider different alternatives. Congratulations!
............................

Python Control flow statements Elif statement
Theory: Elif statement

Since you are familiar with basic conditional statements, such as if statement and if-else statement, it’s time for the more advanced elif statement.

Elif statement is used when we want to specify several conditions in our code. How does it differ from if-else statements? Well, it's simple. Here we add the elif keyword for our additional conditions. It is mostly used with both if and else operators and the basic syntax looks like this:

# basic elif syntax
if condition1:
    action1
elif condition2:
    action2
else:
    action3

The condition is followed by a colon, just like with the if-else statements, then desired action is placed within the elif body and don't forget about an indentation, i.e., 4 spaces at the beginning of a new line. Here we first check the condition1 in the if statement and if it holds (the value of the Boolean expression is True), action1 is performed. If it is False, we skip action1 and then check the condition2 in the elif statement. Again, if condition2 is True, action2 is performed, otherwise, we skip it and go to the else part of the code.

Let's take a look at the example below:

# elif example
price = 10000 # there should be some int value
if price > 5000:
    print("That's too expensive!")
elif price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")

To buy or not to buy? To answer the question we first check if the price is higher than 5000. If ‘price > 5000’ is True, we print that it’s too expensive and set off, looking for something cheaper. But what if the price was less than 5000? In this case, we check the next condition is ‘price > 500’, and again, if it is True, we print out that we can afford that, and if it is False, we go to the else block and print that it's too cheap. So “I can afford it!” will be printed if the price is less than 5000 but more than 500, and “That’s too cheap” if the price is lower than 500.

Elif statement differs from else in one key moment: it represents another specific option while else fits all cases that don't fall into the condition given in if statement. That's why sometimes you may encounter conditional statements without else:

pet = 'cat'  # or 'dog'?

# cats vs dogs conditional
if pet == 'cat':
    print('Oh, you are a cat person. Meow!')
elif pet == 'dog':
    print('Oh, you are a dog person. Woof!')

In this example, it's possible to add an else statement to slightly expand a perspective, but it's not necessary if we are only interested in dogs and cats.
Why elif and not if?

The last example probably made you wonder: why did we use elif statement instead of just two ifstatements? Wouldn't two if statements be easier?

if pet == 'cat':
    print('Oh, you are a cat person. Meow!')
if pet == 'dog':
    print('Oh, you are a dog person. Woof!')

In this particular case, the result would be the same as with elif. But this wouldn't work as needed for the first example of this topic:

price = 6000
if price > 5000:
    print("That's too expensive!")
if price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")
# The output is 'That's too expensive!\nI can afford that!'

See? We got two contradicting messages instead of one that we originally intended to output. The difference between the above examples is that in the example with pets, the cases described by conditional statements are mutually exclusive, that is, there's no string that would be equal both to 'dog' and 'cat' at the same. In the other example, the cases aren't mutually exclusive, and there are values for price that can satisfy both conditions.

So, elif statement is a better alternative than two if statements when you want to show that only one of the conditions is supposed to be satisfied. A chain of if statements implies that the conditions stated in them are totally unrelated and can be satisfied independently of each other, like in the following example:

animal = 'unicorn'
if animal in 'crow, dog, frog, pony':
    print('This animal exists')
if animal in 'unicorn, pegasus, pony':
    print('This animal is a horse')

With this distinction in mind, you'll be able to make your code more clear and less error-prone. Now, let's get back to studying elif functionality.
Multiple elifs and a decision tree

There can be as many elif statements as you need, so your conditions can be very detailed. No matter, how many elif statements you have, the syntax is always the same. The only difference is that we add more elifs:

# multiple elifs syntax
if condition1:
    action1
elif condition2:
    action2
# here you can add as many elifs as you need
elif conditionN:
    actionN
else:
    actionN1

The code inside the else block is executed only if all conditions before it are False. See the following example:

# multiple elifs example
light = "red"  # there can be any other color
if light == "green":
    print("You can go!")
elif light == "yellow":
    print("Get ready!")
elif light == "red":
    print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")

In this program, the message from the else block is printed for the light of any color except green, yellow and red for which we’ve written special messages.

Conditionals with multiple branches make a decision tree, in which a node is a Boolean expression and branches are marked with either True or False. The branch marked as True leads to the action that has to be executed, and the False branch leads to the next condition. The picture below shows such a decision tree of our example with traffic lights.

Nested elif statements

Elif statements can also be nested, just like if-else statements. We can rewrite our example of traffic lights with nested conditionals:

# nested elifs example
traffic_lights = "green, yellow, red"
# a string with one color
light = "purple"  # variable for color name
if light in traffic_lights:
    if light == "green":
        print("You can go!")
    elif light == "yellow":
        print("Get ready!")
    else:
        # if the lights are red
        print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")

Since you have mastered the topic of conditionals, from now on you can make your program do what you want when you want it!
............................
Theory: Functional decomposition

At this point, you already know how to declare functions in Python. This is a very useful skill, no doubt about that, but to make the most of it, we need to know when to declare them. In this topic, we'll see how to decompose the solution of a particular problem into functions.
Real-life example

Before we go to the actual decomposing, let's figure out what it is that we want to decompose.

Suppose, we are writing a program that simulates an ATM. How do real-life ATMs work? Well, usually a client inserts the card, enters the pin, and, if the pin is correct, performs some operations, for example, withdraws money or deposits money to an account. We can reimagine these actions as parts of a computer program. This is how the algorithm can be described in general:

    Parse the input data (card and entered pin);
    Check that the pin is correct;
    Ask the client what they want to do;
    If the operation is supported, perform it.

Before we program this algorithm, let's settle a few things. Obviously, a real bank has a database that stores all necessary data, like the encrypted correct pin or the current card balance. Here we are creating a very simple version of an ATM, so we're not going to include database checkups. Instead, we will define variables card_pin and card_balance. These variables will represent the correct pin and card balance that we would've gotten from a database.

We also need to determine which operations we'll allow. Let's settle on three: displaying the card balance, adding money to the account and withdrawing money from the account.

Now let's see the code:

# operations
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
DISPLAY = "DISPLAY"

# read the data
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database

# check that the pin is correct
if card_pin == input_pin:
    # ask the client what they want to do
    action = input("Enter desired action: ")
    if action == DEPOSIT:
        money = float(input("Enter the sum of money to DEPOSIT: "))
        card_balance += money
        print("Deposited: $", money)
        print("Current balance:", card_balance)
    elif action == WITHDRAW:
        money = float(input("Enter the sum of money to WITHDRAW: "))
        card_balance -= money
        print("Withdrawn: $", money)
        print("Current balance:", card_balance)
    elif action == DISPLAY:
        print("Current balance:", card_balance)
    else:
        ...
else:
    print("Incorrect pin!")

As you can see, a lot is going on and it's a bit hard to follow. The main logic is the same we've described above. This code works perfectly fine for our problem and we could leave it like that.

However, what if we want this script to work for many users and not just one? What if we want to process other cases and perform other actions, for instance, check if the card is in the database or change the pin? Some parts of this code will be useful, other parts we'll have to comment or delete. We would also need to track all places where we're introducing changes to make sure that everything runs smoothly. Now it starts to sound like we may have a problem with our code. The solution, as you may have guessed, is decomposition.
Functional decomposition

Functional decomposition is simply a process of decomposing the problem into several functions. Each function does a particular task and we can perform these functions in a row to get the results we need.

When we look at a problem, we need to think about which actions we may want to repeat multiple times or, alternatively, perform separately. This is how we can get the desired functions. Let's look at our ATM simulation again and figure out which steps can be turned into separate functions.

First, an action that we do frequently is reading the input with a particular message displayed. Second, we perform a certain sequence of actions when the pin is correct, specifically we ask what we should do next. Third, depending on the answer from the client, we either perform certain actions to deposit the sum to the account or withdraw them from the account. And lastly, whatever the action, we always print out the current balance.

Some of these actions can be converted to separate functions to make the program simpler.

Let's go over them step by step. First, let's separate our main operations into functions.

def deposit_money(amount, card_balance):
    """Deposit given amount of money to the account."""
    card_balance += amount
    # save new balance to the database
    return card_balance


def withdraw_money(amount, card_balance):
    """Withdraw given amount of money from the account."""
    card_balance -= amount
    # save new balance to the database
    return card_balance

You may have noticed that in the original program we print the current balance regardless of what we've done before. This means that we can also create a separate function that would log everything.

def log_transaction(action, money, card_balance):
    if action in (DEPOSIT, WITHDRAW):
        print(action + ": $", money)
    print("Current balance:", card_balance)

This function is going to be called after we've done something and it will display information about the current balance and the changes that have been made.

Next, it makes sense to create a function that would manage these operations:

def move_money(action, money, card_balance):
    if action == DEPOSIT:
        return deposit_money(money, card_balance)
    elif action == WITHDRAW:
        return withdraw_money(money, card_balance)
    elif action == DISPLAY:
        return card_balance

You can see that this function returns the card balance that we get after our manipulations. This is helpful because, as we've seen before, we always want to know how much money we end up with. The main purpose of this function, however, is to simplify the process of revising the functionality of our program. If we want to add some other action, we just add another option to the if - else statement and specify the function that would carry out this task. Removing is similar.

One important part that we haven't covered yet is getting the information about the money we'll be moving somewhere. We know that we don't need this information for display, but it is necessary for other operations.

def get_amount_of_money(action):
    if action == DISPLAY:
        return 0.0
    money = input("Enter the sum of money to " + action + ": ")
    return float(money)

At this moment, we only have bits and pieces of our final program. Another important step is creating a function that would put it all together.

def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transaction(action, money, card_balance)

This is when the main logic takes place. We have a single entry point that determines the order of operations and calls necessary functions.
The result

Now, let's rewrite the program above using these functions:

card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database

if card_pin == input_pin:
    action = input("Enter desired action: ")
    make_transaction(action, card_balance)
else:
    print("Incorrect pin!")

That's it! Sure, together with the functions, the code is much bigger, but this provides us with more advantages than disadvantages. We can understand the general direction of the program and can easily introduce changes if needed. Now, for example, if we want to add another action, we just need to define its function and modify the move_money function. We can also easily test separate components since they are determined in separate functions. All in all, our program now is a real functioning program that won't fall apart when we decide to change it a bit.
Summary

In this topic, we've covered the concept of functional decomposition, dividing the process into several functions.

Among other things, decomposing allows us to:

    structure code better;
    see the general logic of the program;
    introduce changes easily;
    test separate functions.

Obviously, functional decomposition is not a universal solution. However, if you can think of your problem in terms of a sequence of some functions, it can be of great help to you!
............................
Theory: Load module

Module basics
While working on simple examples you probably type your code directly into the interpreter. But every time you quit from the interpreter and start it again you lose all the definitions you made before. So as you start writing larger programs it makes sense to prepare your code in advance using a text editor and then run it with the interpreter. A file containing a list of operations that further are read and interpreted is called script.

You also may want to write some functions and then use them in other programs or even reuse code someone else wrote before. One way is just to copy the code into your program, but it soon leads to code that is bad-structured and hard to read. Luckily, there is another way in Python to organize and reuse code called modules.

The module is simply a file that contains Python statements and definitions. It usually has a .py extension. What really makes the module system powerful is the ability to load or import one module from another.
Module loading

To load a module just use an import statement. In a basic form, it has the following syntax import module.

import super_module

super_module.super_function()  # calling a function defined in super_module

print(super_module.super_variable)  # accessing a variable defined in super_module

super_module is the name of the module you want to import. For example, a file called super_module.py has a name super_module. In order to be available for import, super_module.py should be located in the same directory as the file you are trying to import it from. At first, Python importing system looks for a module in the current directory, then it checks the built-in modules, and if nothing is found an error will be raised. After importing, the module becomes available under its name and you can access functions and variables defined in it using the dot notation.

It's also common to only import required functions or variables from a module but not the module itself. You can do this by using a from form of import statement.

from super_module import super_function

super_function()  # super_function is now available directly at the current module

super_module.super_function()  # note, that in this case name super_module is not imported,
                               # so this line leads to an error

A good practice is to load a single module in a single line and put all your imports at the top of the file because it increases readability.

import module1
import module2
import module3

# the rest of module code goes here

A special form of import statement allows you to load all the names defined in a module. It is called wildcard import and has syntax from module import *. You should generally avoid this in your code. It can cause unexpected behavior because you don't know what names exactly are imported into the current namespace. Besides, these names may shadow some of the existing ones without your knowledge. It's better to make it explicit and specify what you're importing.

In case you have to use several import statements, pay attention to their order:

    standard library imports
    third party dependency imports
    local application imports

Having your imports grouped, you may put a blank line between import sections. Also, some guidelines, including ours, recommend sorting imports alphabetically.
Built-in modules

Python comes with a great standard library. It contains a lot of built-in modules that provide useful functions and data structures. Another advantage is that the standard library is available on every system that has Python installed. Here you can find an official library reference.

Python has a math module that provides access to mathematical functions.

import math

print(math.factorial(5))  # prints the value of 5!

print(math.log(10))  # prints the natural logarithm of 10

print(math.pi)  # math also contains several constants
print(math.e)

string module contains common string operations and constants.

from string import digits

print(digits)  # prints all the digit symbols

random module provides functions that let you make a random choice.

from random import choice

print(choice(['red', 'green', 'yellow']))  # print a random item from the list

....................

Theory: Create module

Module design
Basically, a module is just a file that has a .py extension and contains statements and definitions. What is the point? Well, modules help you organize and reuse code. Once you wrote a module you can load it from the interpreter or another module.

A simple module that is written for direct execution is often called a script. The difference between a module and a script in Python is only in the way they are used. Modules are loaded from other modules or scripts and scripts are executed directly.

Let's take a look at the example of a simple script below:

# hello.py script

print("Hello, World!")

You have already seen this example but now we want to turn it into a script. What you need to do is simple: you just save this code in a file named hello.py and then run it with Python. To run a script use python <script>, where <script> is the path to your Python file.

~$ python hello.py
Hello, World!

Congratulations! This is your first script in Python.
Module importing

A module can be loaded from another module. That allows you to write a piece of code once and then use it wherever you want. It is really helpful when you work on larger projects and want to separate concerns between different modules. We already saw examples of an imported module from another module in the previous topic.

When working in the interactive mode of the interpreter you can load modules as well. Pay attention, that the module should be placed in the directory from which you run Python. For example, you can load hello.py file we discussed in the previous section from the interpreter like this:

~$ python
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import hello
Hello, World!

Common mistakes

Now it is time to cover some common mistakes you can make when defining or importing modules.

If you accidentally import a module from itself, the code of the module will be executed twice and that is generally not something you want to happen.

# itself.py

import itself

print("Hello, it's me!")

The output looks like this:

Hello, it's me!
Hello, it's me!

So be careful and avoid situations when you import a module from itself.

Another common mistake is name shadowing. For example, you have created a local module that has the same name as some built-in module. In this case, you won't be able to import anything from the original module, because the import system will search names in your custom module.

Imagine, you created a module socket.py and then you try to import some function from the standard Python socket module within your module.

# socket.py

from socket import socket

print("All cool!")

You'll see an error message that says that Python cannot import socket from socket module:

...

ImportError: cannot import name 'socket'

One way to avoid this is not to name your files the same as the built-in modules you might use. Just suffix _script to the name of your scripts and modules and you will be safe from this name shadowing problem.

Whenever the module is imported it is fully executed and then added to your current namespace. Even special forms of import statement such as from module import something don't affect that fact. This may become a problem in situations when you want to be able to both import your module and execute it as a script.

Consider the example:

# unsafe_module.py

name = "George"

print("Hello,", name)

If you define another script and import name from unsafe_module you'll see Hello, George printed.

# unsafe_bye.py script

from unsafe_module import name

print("Bye,", name)

The output:

Hello, George
Bye, George

To solve this issue you can simply divide your file into two: one containing only definitions, another containing the code that imports definitions from the first file and uses them. But it's also common to use the __main__ pattern.
__main__ pattern

Let's learn another option of how to make your script safe to import. We will change the unsafe_module.py file from the previous section.

# safe_module.py

name = "George"

if __name__ == "__main__":
    print("Hello,", name)

The name of the module is always available in the built-in variable __name__. When you are executing a script __name__ has a value "__main__". So here we check the value of __name__ and print the line only if the module is executed as a script.

# safe_bye.py script

from safe_module import name

print("Bye,", name)

The output is the following:

Bye, George

In general, if you have more than just one line to execute in a script it's convenient to move all that code into a function called main and then call it like that:

# safe_main_module.py

name = "George"

def main():
    print("Hello,", name)

if __name__ == "__main__":
    main()

Note, that the naming itself doesn't affect the way a function is executed, it's just a convention to indicate that this function is run only when the file is used like a script.
.........
Theory: Packages

Package definition and structure
When our code is becoming bigger, it becomes very difficult to maintain and keep track of all the modules included. In order to make the code more organized, we can resort to packages. A package is a way of structuring modules hierarchically with the help of the so-called "dotted module names". Thus the module name sun.moon designates a submodule named "moon" in a package named "sun".

The possible structure might be the following:

package/                           # first we name the main or top-level package
            __init__.py            # this directory should be treated as a package
            subpackage/            # we can add subpackage with extra modules
                  __init__.py      # this directory should be treated as a subpackage
                   artificial.py
                   amateurs.py
                   ...
            subpackage2/
                  __init__.py
                  amazing.py
                  animate.py
                  barriers.py
                  ...

NB: it’s necessary to create __init__.py files, that will make Python treat the directory as a package/subpackage. They can be empty or execute the initialization code for the package.
Importing and referencing packages

Let us suppose we’d like to import a specific module from the package. There are two ways to import the "artificial" submodule from the subpackage:

from package.subpackage import artificial

This method allows to use the submodule content without naming the package and subpackage:

artificial.function(arg1, arg2)

The second method is more straightforward:

import package.subpackage.artificial

After we’ve loaded the submodule in such a way, its content should be referenced with its full name:

package.subpackage.artificial.function(arg1, arg2)

Besides, it’s possible to import a particular function from the submodule:

from package.subpackage.artificial import function

After that, you can address the function() directly, without specifying the full path to a module.

The method of importing modules depends on your current program and needs. The main rule is readability!
Import * from …: advantages and disadvantages

You can also use from package.subpackage import *. This code will import all the submodules that your subpackage has, although you might not really need that. Moreover, it will be really time-consuming and considered to be a bad practice. How can we manage these side-effects?

The major thing to do is to provide the package with a particular index with the help of __all__ statement that should be inserted into __init__.py file. There you want to list the submodules to be imported while from package import * operation is executed.

__all__ = ["submodule1", "submodule10"]

Intra package references

Python is even more powerful than you could imagine: if you have a need, you can refer to submodules of siblings packages. For instance, if you use the package.subpackage1.artificial and there you need something from package.subpackage2.amazing, you can import it by from package.subpackage2 import amazing in the artificial.py file.

You can also carry out the so-called "relative imports" that use leading dots to indicate the current and parent packages involved. Thereby, for "amateurs" you can use the following:

from . import artificial    # one dot means addressing to a current package/subpackage

from .. import subpackage2  # two dots mean addressing to a parent package/subpackage

from ..subpackage2 import module

PEP Time!

Using wildcard imports (from <module> import *) is considered bad practice, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools.

Absolute imports are recommended, as they are usually more readable. They also give better error messages if something goes wrong:

import package.subpackage.amateurs
from package.mypackage import amateurs

Explicit relative imports are also acceptable, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:

from . import animate           # in amazing.py, for example
from .barriers import function  # in animate.py, for example

Standard library code should avoid complex package layouts and always use absolute imports.
Conclusion

    Using packages is a very good way to structure your code.

    Packages make your project simpler to perceive. They allow reusing code more easily.
    Different ways of importing have their own advantages and disadvantages. Remember one of the main rules of Python: readability counts!

...................
Theory: Class

As you already know, object-oriented programming (OOP) is a programming paradigm that is based on the concept of objects. Objects interact with each other and that is how the program functions. Objects have states and behaviors. Many objects can have similar characteristics and if you need to work with them in your program it may be easier to create a class for similar objects. Classes represent the common structure of similar objects: their data and their behavior.
Declaring classes

Classes are declared with a keyword class and the name of the class:

# class syntax
class MyClass:
    var = ...  # some variable

    def do_smt(self):
    # some method

Generally, class name starts with a capital letter and it is usually a noun or a noun phrase. The names of the classes follow the CapWords convention: meaning that if it's a phrase, all words in the phrase are capitalized and written without underscores between them.

# good class name
class MyClass:
    ...

# not so good class name:
class My_class:
    ...

Classes allow you to define the data and the behaviors of similar objects. The behavior is described by methods. A method is similar to a function in that it is a block of code that has a name and performs a certain action. Methods, however, are not independent since they are defined within a class. Data within classes are stored in the attributes (variables) and there are two kinds of them: class attributes and instance attributes. The difference between those two will be explained below.
Class attribute

A class attribute is an attribute shared by all instances of the class. Let's consider the class Book as an example:

# Book class
class Book:
    material = "paper"
    cover = "paperback"
    all_books = []

This class has a string variable material with the value "paper", a string variable cover with the value "paperback" and an empty list as an attribute all_books. All those variables are class attributes and they can be accessed using the dot notation with the name of the class:

Book.material  # "paper"
Book.cover  # "paperback"
Book.all_books  # []

Class attributes are defined within the class but outside of any methods. Their value is the same for all instances of that class so you could consider them as the sort of "default" values for all objects.

As for the instance variables, they store the data unique to each object of the class. They are defined within the class methods, notably, within the __init__ method. In this topic, we'll deal with the class attributes, but don't worry you'll have plenty of time to learn more about instance attributes.
Class instance

Now, let's create an instance of a Book class. For that we would need to execute this code:

# Book instance
my_book = Book()

Here we not only created an instance of a Book class but also assigned it to the variable my_book. The syntax of instantiating a class object resembles the function notation: after the class name, we write parentheses.

Our my_book object has access to the contents of the class Book: its attributes and methods.

print(my_book.material)  # "paper"
print(my_book.cover)  # "paperback"
print(my_book.all_books)  # []

Summary

Well, those were the very basics of classes in Python. Classes represent the common structure of similar objects, their attributes, and methods. There are class attributes and instance attributes. Class attributes are common to all instances of the class.

All in all, classes are an extremely useful tool that can help you optimize your code and organize the program in a logical and readable way. We hope you'll make use of them!
......................
Theory: Class instances

By now, you already know what classes are and how they're created and used in Python. Now let's get into the details about class instances.

A class instance is an object of the class. If, for example, there was a class River, we could create such instances as Volga, Seine, and Nile. They would all have the same structure and share all class attributes defined within the class River.

However, initially, all instances of the class would be identical to one another. Most of the time that is not what we want. To customize the initial state of an instance, the __init__ method is used.
def __init__()

The __init__ method is a constructor. Constructors are a concept from the object-oriented programming. A class can have one and only one constructor. If __init__ is defined within a class, it is automatically invoked when we create a new class instance. Take our class River as an example:

class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)

volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.name)
# Output:
# Volga
# Seine
# Nile

We created three instances (or objects) of the class River: volga, seine, and nile. Since we defined name and length parameters for the __init__, they must be explicitly passed when creating new instances. So something like volga = River() would cause an error.

The __init__ method specifies what attributes we want the instances of our class to have from the very beginning. In our example, they are name and length.
self

You may have noticed that our __init__ method had another argument besides name and length: self. The self argument represents a particular instance of the class and allows us to access its attributes and methods. In the example with __init__, we basically create attributes for the particular instance and assign the values of method arguments to them. It is important to use the self parameter inside the method if we want to save the values of the instance for the later use.

Most of the time we also need to write the self parameter in other methods because when the method is called the first argument that is passed to the method is the object itself. Let's add a method to our River class and see how it works. The syntax of the methods is not of importance at the moment, just pay attention to the use of the self:

class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))

Now if we call this method with the objects we've created we will get this:

volga.get_info()
# The length of the Volga is 3530 km
seine.get_info()
# The length of the Seine is 776 km
nile.get_info()
# The length of the Nile is 6852 km

As you can see, for each object the get_info() method printed its particular values and that was possible because we used the self keyword in the method.

Note that when we actually call an object's method we don't write the self argument in the brackets. The self parameter (that represents a particular instance of the class) is passed to the instance method implicitly when it is called. So there are actually two ways to call an instance method: self.method() or class.method(self). In our example it would look like this:

# self.method()
volga.get_info()
# The length of the Volga is 3530 km

# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km

Instance attributes

Classes in Python have two types of attributes: class attributes and instance attributes. You should already know what class attributes are so here we'll focus on the instance attributes. Instance attributes are defined within methods and they store instance-specific information.

In the class River, the attributes name and length are instance attributes since they are defined within a method (__init__) and have self before them. Usually, instance attributes are created within the __init__ method since it's the constructor, but you can define instance attributes in other methods as well. However, it's not recommended so we advise you to stick to the __init__.

Instance attributes are available only from the scope of the object which is why this code will produce a mistake:

print(River.name)  # AttributeError

Instance attributes, naturally, are used to distinguish objects: their values are different for different instances.

volga.name  # "Volga"
seine.name  # "Seine"
nile.name   # "Nile"

So when deciding which attributes to choose in your program, you should first decide whether you want it to store values unique to each object of the class or, on the contrary, the ones shared by all instances.
Summary

In this topic, you've learned about class instances.

If classes are an abstraction, a template for similar objects, a class instance is a sort of example of that class, a particular object that follows the structure outlined in the class. In your program, you can create as many objects of your class as you need.

To create objects with different initial states, classes have a constructor __init__ that allows us to define necessary parameters. Reference to a particular instance within methods is done through the self keyword. Within the __init__ method, we define instance attributes that are different for all instances.

Most of the time in our programs we'll deal not with the classes directly, but rather with their instances, so knowing how to create them and work with them is very important!
......................
Theory: Methods and attributes

Now that you've learned how to create instance methods let's go even further and learn to use the methods for creating and modifying attributes.
Creating attributes with methods

Instance attributes are the ones defined within methods so by definition we can create new attributes inside our custom methods. Let's take the class Ship as an example.

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

Every ship needs a captain so let's define a method called name_captain for those purposes:

class Ship:
    # constructor
    # ...

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))

When called for the first time, the name_captain method creates a new attribute called captain and prints the corresponding message. When used next, it just changes the value of the self.captain attribute (and prints the message as well).

To see how it would work, let's create the ship "Black Pearl":

black_pearl = Ship("Black Pearl", 800)

If we tried to print the value of the captain attribute now, we would get an error:

print(black_pearl.captain)  # AttributeError

This is because this attribute is only created within the name_captain method. If we call it, we will be able to access the attribute captain:

black_pearl.name_captain("Jack Sparrow")
# prints "Jack Sparrow is the captain of the Black Pearl"

print(black_pearl.captain)  # "Jack Sparrow"

Note that only those instances that have called this method, will have the captain attribute. It's an important thing to remember! You may get an error if you try to use the attribute and the method hasn't been called yet.

To avoid these problems, it is recommended to define all possible attributes in the __init__. This can not only help you avoid AttributeError, but also give a good understanding of the class and its objects from the get-go. If you do want to create the value for the attribute in a special instance method, then list it in the __init__ as None:

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

Then, in the specific method, you simply modify the default value which is what we'll consider in the next section.
Modifying attributes with methods

Methods can also be used to modify the instance attributes. Take the methods load_cargo and unload_cargo for example:

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")

Both these methods are supposed to change the value of the attribute cargo if those changes are possible. The load_cargo method first checks that the loading of a particular weight will not exceed the capacity of the ship and the unload_cargo checks that the unloading will not make the weight of the cargo negative. Then they both make the changes or print a message that those changes are impossible.

# example
black_pearl.load_cargo(600)
# "Loaded 600 tons"

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"

black_pearl.load_cargo(700)
# "Cannot load that much"

black_pearl.unload_cargo(300)
# "Cannot unload that much"

If we wanted to print out the value of cargo after all these manipulations, we would see that it would equal 200 (tons). Because of the restrictions that we placed, only the first callings of load_cargo and unload_cargo made changes to the attribute cargo.

So far our methods haven't been returning any values since we only used the print() function, but we can make our methods return any type of value that we want. For example, let's create a method that calculates how much more cargo can our ship load.

class Ship:
    # all other methods

    def free_space(self):
        return self.capacity - self.cargo

If we were to call this method on our Black Pearl we wouldn't get any messages, because the method doesn't print anything. But instead, we could use the value it returns in our further calculations. We could, for instance, rewrite the load_cargo method by using thefree_space method:

class Ship:
    # updated load_cargo method
    def load_cargo(self, weight):
        if weight <= self.free_space():
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

In this example, we called a method inside another method and used the values in our calculations. Again, we used self to make sure that we only deal with the particular instance of the class Ship and that all calculations concern this instance.
Summary

In this topic, we focused on more advanced uses of instance methods in Python.

Methods can be used for creating new attributes and modifying existing ones. You can call methods inside other methods, use the results for calculations or just output messages. Knowing how methods and attributes interact can help you expand the functionality of your classes and make your programs very efficient.

We hope that you'll experiment with instance methods and use them in your projects!
.........................
Theory: Magic methods

There are different ways to enrich the functionality of your classes in Python. One of them is creating custom methods which you've already learned about. Another way, the one that we'll cover in this topic, is using "magic" methods.
What are "magic" methods?

Magic methods are special methods that make using your objects much easier. They are recognizable in the code of the class definitions because they are enclosed in double underscores: __init__ , for example, is one of those "magic" methods in Python. Since they are characterized by double underscores they are often called dunders.

Dunders are not meant to be invoked directly by you or the user of your class, it happens internally on a certain action. For example, we do not explicitly call the __init__ method when we create a new object of the class, but instead, this method is invoked internally. All we need to do is to define the method inside the class in a way that makes sense for our project.

There are many different dunders that you can use, but in this topic, we will focus on the most helpful ones.
__new__ vs __init__

So far we've been calling __init__ the constructor of the class, but in reality, it is its initializer. New objects of the class are in fact created by the __new__ method that in its turn calls the __init__ method.

The first argument of the __new__ method is cls. It represents the class itself, similar to how self represents an instance of the class. This also makes __new__ a different kind of method since it doesn't require an instance of the class. This makes sense since it is supposed to create those instances. The method returns a new instance of the class which is then passed to the __init__ method.

Usually, there is no need to define a special __new__ method, but it can be useful if we want to return instances of other classes or restrict the number of objects in our class.

Imagine, for example, that we want to create a class Sun and make sure that we create only one object of this class. We would need to define a class variable that would track the number of instances in the class and forbid the creation of new ones if the limit has been reached.

class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0:
            cls.n += 1
            return object.__new__(cls)  # create new object of the class

The code above may be a bit unexpected so let's analyze it. We first check that the class variable n has a value of zero. If it does, it means that no instances of the class have been created and we can do that. We then update the class variable and call __new__ method of object class which allows us to create a new instance.

If we now try to create 2 objects of this class we will not succeed:

sun1 = Sun()
sun2 = Sun()

print(sun1)  # <__main__.Sun object at 0x1106884a8>
print(sun2)  # None

__str__ vs __repr__

Printing out information and data is very important when programming. You can print the results of calculations for yourself or the user of your program, find the mistakes in the code or print out messages.

For example, let's consider the class Transaction:

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

If we create a transaction and try to print it out we will not get what we want:

payment = Transaction("000001", 9999.999)
print(payment)
# example of the output: <__main__.Transaction object at 0x11068f5f8>

Instead of the values that we would like to see, we get information about the object itself. This can be altered if we deal with __str__ or __repr__ methods.

As the names suggest, __str__ defines the behavior of the str() function and __repr__ defines the repr() function. A general rule with the __str__ and __repr__ methods is that the output of the __str__ should be highly readable and the output of the __repr__ should be unambiguous. In other words, __str__ creates a representation for users and __repr__ creates a representation for developers and debuggers. If possible, __repr__ should return Python code that could be used to create this object or, at least, a comprehensive description.

Both __repr__ and __str__ should return a string object!

A good rule is to always define the __repr__ method first since it is the method used by developers in debugging. It is also a fallback method for __str__which means that if the __str__ method isn't defined, in the situations where it's needed, the __repr__ will be called instead. This is, for example, the case with print().

In our example here, let's create the __repr__ method that would create an unambiguous representation of the transaction and all its attributes.

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

Now if we try to print any transaction we will get a standard readable string:

payment = Transaction("000001", 9999.999)
print(payment)
# Transaction(000001, 9999.999)

You can see that we've called print and got the representation from __repr__. Now let's add __str__ and see if things change.

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

    def __str__(self):
        return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)


payment = Transaction("000001", 9999.999)
print(payment)
# Transaction 000001 for 9999.999 (active)
print(repr(payment))
# Transaction(000001, 9999.999)

Now that we have __str__, when we call print, we get the representation defined there. To see the "official" representation we need to directly call the repr function.
Summary

Magic methods are said to add "magic" to your classes and that is somewhat true. Dunders really make working with classes much easier and far more efficient.

In this topic, we've covered only a couple of these magic methods. We highly encourage you to look them up (for example, in "A Guide to Python's Magic Methods" by Rafe Kettler) and try them out in your projects. As for the magic methods for arithmetics and comparisons, we'll look into them in another topic!
..................
Theory: Inheritance

One of the main principles of object-oriented programming is inheritance. In this topic, we'll focus on inheritance in Python: what it means and how it's done.

What is inheritance?
Inheritance is a mechanism that allows classes to inherit methods or properties from other classes. Or, in other words, inheritance is a mechanism of deriving new classes from existing ones.

The purpose of inheritance is to reuse existing code. Often, objects of one class may resemble objects of another class, so instead of rewriting the same methods and attributes, we can make it so that a class inherits those methods and attributes from another class.

When we talk about inheritance, the terminology resembles biological inheritance: we have child classes (or subclasses, derived classes) that inherit methods or variables from parent classes (or base classes, superclasses). Child classes can also redefine methods of the parent class if necessary.
Class object

Inheritance is very easy to implement in your programs. Any class can be a parent class, so all we need to do is to write in the definition of the child class the name of the parent class in parentheses after the child class:

# inheritance syntax
class ChildClass(ParentClass):
    # methods and attributes
    ...

The definition of the parent class should precede the definition of the child class, otherwise, you'll get a NameError! If a class has several subclasses, its definition should precede them all. The "sibling" classes can be defined in any order.

When we don't define a parent for our class, it doesn't mean that it doesn't have any! By default, all classes have the class object as their parent. In Python 3.x we don't need to explicitly indicate that, so the definitions below are equivalent:

# parent class is explicit
class SomeClass(object):
    # methods and attributes
    ...


# parent class is implicit
class SomeClass:
    # methods and attributes
    ...

Subclasses of object inherit its methods and attributes. So, all standard methods like __init__ or __repr__ are inherited from the class object. If we don't redefine those methods for our custom classes, we end up using their implementations defined for the object.
Single inheritance

Unlike some other programming languages, Python supports two forms of inheritance: single and multiple. Single inheritance is when a child class inherits from one parent class. Multiple inheritance is when a child class inherits from multiple parent classes. In this topic, we'll cover only single inheritance. Don't worry, though, you'll have a chance to learn about multiple inheritance in the next topics!

Let's consider an example of single inheritance.

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

# child class
class Dog(Animal):
    pass

Here we have a base class Animal with the __init__ method and a subclass Dog that inherits from the base class. The keyword pass allows us not to write anything in the definition of the child class.

Now that we've defined classes, we can create objects:

cow = Animal("Bessie")  # instance of Animal
corgi = Dog("Baxter")   # instance of Dog

We haven't defined the __init__ for the class Dog but since it's a child of Animal, it inherited its __init__. So if we tried to declare an instance of the class Dog in a different way, we would get an error:

labrador = Dog()  # TypeError

type() vs isinstance()

There are two main ways to check the type of an object: type() or isinstance() functions.

The type() function takes one argument, an object, and returns its type. The isinstance() function takes two arguments: an object and a class. It checks if the given object is an instance of the given class and returns a boolean value.

For built-in types, they work the same, but when inheritance is involved, their results are different. Let's check it out!

First, let's look at the type() function:

print(type(cow) == Animal)  # True
print(type(corgi) == Animal)  # False

print(type(cow) == Dog)     # False
print(type(corgi) == Dog)     # True

As you can see, this allows us to check for the immediate type of the object. Now, isinstance() works differently:

print(isinstance(cow, Animal))    # True
print(isinstance(corgi, Animal))  # True

print(isinstance(cow, Dog))    # False
print(isinstance(corgi, Dog))  # True

With this, we get True not only with the immediate type but also with the parent type and even with the parent of the parent type! This distinction is important to remember for future projects!
issubclass()

While isinstance() checks the type of an instance of a class, another built-in function asks whether a given class is a subclass of another class:

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False

print(issubclass(Dog, Dog))     # True
print(issubclass(corgi, Dog))   # TypeError

As shown, the issubclass() function returns True if the first class inherits from the second class, and False otherwise. Each class is considered a subclass of itself. Notice that the function can't work with instances of a class, both its arguments should be classes. However, you can use a tuple of classes to check if your class inherits from several parents.

print(issubclass(Dog, object))            # True
print(issubclass(Dog, (Animal, object)))  # True

The case with several classes might be somewhat misleading, though. The thing is that the function checks whether any element of the tuple is a parent. Say, we have defined a new class Robot:

class Robot:
    pass

Then issubclass() will return the following:

print(issubclass(Dog, Robot))            # False
print(issubclass(Dog, (Robot, Animal)))  # True

Even though Dog has nothing to do with Robot, in the last case, we got True. So keep this detail in mind when calling this function!
Summary

As one of the pillars of OOP, inheritance is very important! In Python, declaring parent classes is quite simple and straightforward. In this topic, we've covered the basics of the inheritance in Python: how it's done, what is class object, how to define a single parent for the class, and then check the type of an object or a class without any mistakes.

Inheritance is what really makes classes so powerful and useful. It also allows programmers to stick to the DRY (Don't Repeat Yourself) principle and pushes them to think about the effectiveness and clarity of their classes.
............................
Theory: Introduction to operating systems

How can it be that there are thousands of different computer models but they all can run the same programs? Have you ever thought about how the programs interact with the hardware? These and other features are made possible by the operating systems.
Operating system

An operating system (OS) is a set of software that manages communication between all other applications and hardware. It turns a computer into something more than just a bunch of metal parts, a complex system that can effectively perform different tasks.

Nowadays, there exist a lot of operating systems for you to choose from. For personal computers, the most popular ones are Microsoft Windows, macOS, and Linux distributions. The two top mobile operating systems are Android and iOS. If you've ever heard of smart kettles and smart fridges, even they have their own OS.

Of course, the operating systems for such a range of devices differ greatly from one another. What they have in common are the means they provide to the programs and those who use them.

On the one hand, it's only an illusion that your favorite browser is the same on Windows as it is on macOS. On the other hand, you can run the same application on different computers with the same OS.

Functions of the OS

An operating system controls the communication between all the computer software and hardware. An OS can give programs restricted access to processor units, memory, hard drives, network, peripherals, and other resources.

You can run a browser, a media player, and ten other applications, and your OS is the one giving them all the resources they need to run properly. At the same time, this OS acts as a fair referee prohibiting any application to take up more resources than it actually needs.

As a mediator between the applications and hardware, the operating system allows us to communicate with the device without going into details about its specificity or mechanics.

Any operating system has several essential functions. Here is a list of some of them:

    data protection and secure access;
    resource management;
    interaction between hardware and peripherals;
    file management;
    running other programs.

It is possible to distinguish more functions of modern operating systems, but those listed above are enough for starters.
Operating systems' components

A mandatory part of all operating systems, its core, is the kernel. Usually, it's one of the first programs that load when you turn on your computer. It provides all the necessary means to run the programs you want.

Typically, when you start your OS, you see the Graphical User Interface (GUI). It is the type of interface that allows users to interact with the device using graphical icons and audio indicators. Another way to interact with the OS is to use commands in a text-based terminal known as Command Line Interface (CLI).

There are two types of kernels, known as monolithic kernel and microkernel. The monolithic kernel is a large program that performs most of the OS functions. At the same time, the microkernel performs only a small subset of the operating system functions, but we can extend it with additional modules known as drivers.

There are other important parts of the operating system besides the kernel and the graphical user interface. We will review them in the next topic. For now, use the following image to brush up everything we've covered so far:

Conclusion

The operating system efficiently distributes the resources of the computer in a way we've described above. It is important to understand that without the operating system, it would not be possible to use the computer.

Now you know about the main functions of the operating systems and their essential elements. Let's test what you've learned so far!
........................................
skipped some!!
......................................

Theory: Datetime module

Often, in our projects, we need to work with dates and time. For example, we may want to track the current date and time or see how long our code runs. For these purposes, we can use the datetime module.

The datetime module has several classes that make working with time easy:

    datetime.date represents standard date;
    datetime.time represents standard time, independent from the date;
    datetime.timedelta represents the difference between two points in time;
    datetime.tzinfo represents timezones;
    datetime.datetime represents both time and date together.

In this topic, we'll focus on the datetime.datetime class.
datetime.datetime

The datetime.datetime class is a sort of combination of the date and time classes. Similarly to those two, it assumes the current Gregorian calendar and that there are exactly 86 400 seconds in each day.

The constructor of the datetime.datetime objects takes the following parameters:

import datetime

# necessary parameters
datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

The year, month and day parameters are required, others are optional. All arguments (except tzinfo) should be integers and just like in real life, their values are restricted:

    datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999);
    1 ≤ month ≤ 12;
    1 ≤ day ≤ number of days in this month and year;
    0 ≤ hour < 24;
    0 ≤ minute < 60;
    0 ≤ second < 60;
    0 ≤ microsecond < 1000000.

The tzinfo argument can be an instance of the datetime.tzinfo class, but its default value is None, so we don't need to worry about it here.

To see how this all works, let's create a datetime.datetime object. For example, the date and time of the first flight to space which took place on April 12, 1961, at 6:07 UTC:

import datetime

vostok_1 = datetime.datetime(1961, 4, 12, 6, 7)
print(vostok_1)  # 1961-04-12 06:07:00

datetime methods

The datetime.datetime class has several very handy methods.

If you need to get the current time and date, there are two methods you can use: datetime.datetime.today() and datetime.datetime.now(tz=None). They are very similar and the only difference between these two methods is that datetime.datetime.now() has a keyword argument tz. If you don't specify it, the two methods work the same. However, in some cases or on some platforms, the datetime.datetime.now() method may be more precise.

This is an example of how they perform:

print(datetime.datetime.now())  # 2019-09-12 17:18:23.620734
print(datetime.datetime.today())  # 2019-09-12 17:18:23.625716

You can also transform a datetime.datetime object to a datetime.time or datetime.date objects using datetime.datetime.time() or datetime.datetime.date() methods respectively:

print(vostok_1.time())  # 06:07:00
print(vostok_1.date())  # 1961-04-12

Those were just a couple of methods available in the datetime.datetime class. There are many more: the ones that deal with timestamps or timezones or the ones that help parse and convert datetime objects. Don't worry, you'll have a chance to work with them in the next topics!
Report a typo
..............................
Theory: Pip

One astonishing fact about Python is that it has a huge and diverse community of contributors. Essentially, that means that there are plenty of solutions to a significantly vast range of problems in open access. This fact comes in handy, especially when you are working on your own projects. It's highly likely that you'll be able to find a proper task-specific package and use it effectively to meet your needs. Now we are going to learn about standard tools for package management in Python.
What is pip

By this time you've probably familiarized yourself with the Python standard library. It contains a lot of useful built-in modules and should be preinstalled with your Python distribution. In fact, one more thing that is preinstalled (starting with Python 3.4) is the standard package manager called pip (the acronym is commonly expanded as "Pip Installs Packages").

Pip is designed both to extend the functionality of the standard library by installing the additional packages on your computer and to help you share your own projects and thereby contribute to the development of Python.

Now let's make sure that you have pip installed. All you need to do is open a command prompt/terminal and run this line:

pip --version

The output should report your current pip version. For example, the latest version is:

pip 20.0.2

In case it's not installed (or you want to upgrade it), please follow these installation instructions specifically for your operating system.

If your terminal cannot find the pip command, try to use pip3 instead.

Pip capabilities

Since pip is the recommended installer for Python, the most obvious and crucial command to begin with is install. Have a look at the following line:

pip install some_package

The installation is really that simple. However, if you are interested in a certain version of the package, you need to specify it after the package name like this:

pip install some_package==1.1.2

Or, at least, define a minimal suitable version:

pip install "some_package>=1.1.2"

Note that the last expression should be enclosed within double quotes for the comparison operator to be interpreted without any problem.

Another useful thing is the show command. It shows information about installed packages, for instance, their version, author, license, location or requirements. Here is a general example:

pip show some_package

Also, the list command might be of use. It lists all the packages you've installed on your computer in alphabetical order:

pip list

If you print the list command with the option --outdated, or just -o, you'll get the list of outdated packages coupled with both the current and latest versions available.

pip list --outdated

or with a bit shorter variant:

pip list -o

After executing one of the mentioned lines, you will see a similar output:

first_package (Current: 2.1.1 Latest: 3.0.1)
second_package (Current: 4.2.1 Latest: 4.2.2)

Having discovered outdated packages, you might want to update them to the newest available version:

pip install --upgrade some_package

To remove a package from your computer run the uninstall command:

pip uninstall some_package

When developing your project, it may be advantageous to keep a list of packages to be installed, i.e. dependencies, in a special file (see Requirements File Format). It is convenient because you can install the packages directly from it:

pip install -r requirements.txt

Of course, you are not supposed to write this file yourself listing all the necessary packages. It will be enough to run the code below in order to obtain it:

pip freeze > requirements.txt

Let's examine the line above in detail. freeze is a command used to get all installed packages in the format of requirements. So all the packages you had installed before the execution of the command and presumably had used in some projects would be listed in the file named "requirements.txt". Furthermore, their exact versions would be specified (see Requirement Specifiers).

Consider an example output of the freeze command:

beautifulsoup4==4.7.1
nltk==3.4.1
numpy==1.16.3
scikit-learn==0.21.1
scipy==1.3.0

What's important is that freeze actually lists all the installed libraries, which is rarely necessary and might be considered a bad practice. For this reason, we recommend that you take a more conscious approach and revise the obtained requirements file by yourself.
Recap

On the whole, we've learned the basics for package installation through pip:

    how to install packages (either a specific version or non-specific one),
    how to create a requirements file and use it for installation,
    how to obtain information about installed packages,
    and, finally, how to uninstall packages.

For further details, try consulting the documentation or running the command help.

Now let's get to practice so that you can use all this information in the future!
Report a typo
.................
Theory: Introduction to Django

Django is one of the most-used Python frameworks in web programming. When you are browsing through boards on Pinterest, reviewing code on Bitbucket, or making comments with the help of Disqus, you are using Django products. You can find out about more well-known services that use Django on this page.

The name of the framework is inspired by the stage name of a famous jazz guitarist Django Reinhardt, so the developers who created many handy add-ons for the framework call their group Jazzband. At first, you won’t need all of the tools, but whenever you need more, you can find them at this Github account.

Django framework provides an API for templating HTML pages, making connections to databases, and using HTTP backend services. Django has many useful web development shortcuts and utilities in one place. To start working with the framework, choose the version you'll use. For Django in its A.B.C version, A.B stands for a feature release and C for a patch release. When choosing an appropriate version, pay attention to its feature release number. When you're done choosing, download the latest patch release for this version. To get the most of Django, start with the latest version.

The first stable release of Django was issued in 2008. The first Long-Term Support (LTS) release with version 1.4 came four years later, in 2012.
LTS

LTS is a well-known standard in software development. It means that developers will support this version of the framework for an extended period of time (for Django, it's usually 3 years or more). You can safely update your version to a newer patch release without fear of breaking compatibility with the source code. For this period, all bugs and security losses will be fixed as soon as possible. Conversely, non-LTS versions are supported only until a newer feature release comes out (note that Django developers support the last two feature releases at a time).

For example, the LTS version 1.11 is supported until April 2020, but the later, non-LTS version 2.0 is already not supported by the developing team.

In this course, we will use the latest LTS release of Django as of April 2019, version 2.2.

Surely you can't wait to finally install Django and get to work. There are two ways to install the package: you can install it globally, which is simpler, or get it in a Python virtualenv.
Global Installation

To install Django, you need a Python package manager pip. Django is no different from any other Python package, so if you want to install it on your system, run:

pip install Django==2.2

To use the framework, you will probably need a database. For the sake of simplicity, you can install SQLite unless it's already present on your system.
Installation in Virtual Environment

To isolate your development environment from other Python packages on your computer, you need to create and activate Python virtualenv. Then install the framework to keep it separate:

# If you don't have virtualenv yet
pip install virtualenv

# Unix
python -m venv hyperskill-django
source hyperskill-django/bin/activate
pip install Django==2.2

# Windows
python -m venv hyperskill-django
hyperskill-django\Scripts\activate
pip install Django==2.2

# If you want to deactivate a virtual environment
deactivate

A virtual environment is also helpful if you want to keep different versions of a package on your system. You can install each one of them in separate virtualenv. Thus if you already have the older version of Django, you can try out the new one with virtualenv.
Check Installation

After you've installed Django, you'll get django-admin command in your shell (if you've installed Django in a virtual environment, do not forget to activate it). Django-admin is a helper that can create a template layout for a new project or add an application to an existing project. You can do this manually, but it's much easier to use django-admin for this purpose.

Now you only need to check the version of the installed package:

django-admin version
# 2.2

It means that your installation was successful and you can start using Django! You've got the basic essentials to create your first project, so good luck!
..............................
Theory: Django MVC
MVC Paradigm

Complex software products have their own architecture. Though each example is unique, usually they all contain common design patterns. Patterns are repeatable and rather language-independent structures, so getting familiar with just one of them means understanding a whole bunch of applications that share it. It is basically a general language to express ideas, and Model-View-Controller (MVC) is one particularly useful pattern to learn, since many popular frameworks like Django (Python), Spring (Java), and Ruby On Rails (Ruby) are using it.

The main idea of MVC is dividing responsibilities between three components. The Model part contains business objects, the View represents the application and the Controller manages data flow between two of them. The advantage of this design pattern is that we can create different views from the same models, so we write less code by reusing the existing parts. Distinguishing one component from another is the main principle to be guided by.

Each component has its associated files in the default Django layout.

Let's say that we are creating an online magazine. The folder "magazine" is the root of your site and the inner folder "blog" is one of the applications. You can link the components with those files:

magazine/
├── blog
    ├── ...
    ├── models.py    # Model
    └── views.py     # Controller
├── magazine
    ├── ...
    └── urls.py      # Controller
└── templates        # View

Let's take a closer look at the files that you will need in order to make a web service.
Starting a New Project

For this example, we will use "magazine" for a project and "blog" for an application. If you want to get creative and use other names, feel free to change the given ones in the code.

The Django project is the root of all code you are writing for the service, and it should have at least one application. To isolate units of code with different business logic, you can create more of them. For example, the magazine project can have the blog, authors, forum, and support applications.

With time the codebase becomes large, dividing it into applications helps to control the complexity.

The django-admin utility helps organize the layout of your project. You may create all these files manually, but using django-admin will be a good guide to the common structure of a project for you. Note that different versions of Django have different default layouts, and whichever version you use, try to stick to its provided structure: it will make your code easier to maintain.

To create a project and the first application, run the following in the command line:

django-admin startproject magazine
cd magazine
django-admin startapp blog

Having executed these commands, you'll get a whole file tree for the project with a piece of code. Now let's get down to using our MVC pattern.
Model

magazine/
└── blog
    └── models.py

It's nice to have the same content for all users, but if we want to customize it a bit, we need tools from Python interface.

The Model component includes all the database operations with the business objects in your project. A business object is an entity with custom attributes; it reflects a structured piece of data from your application which you want to store persistently or temporarily. For example, in a shop application, it can be a customer, a product and a purchase; in a blog, business objects can be authors, posts and comments.

To keep your code clear, you should implement all operations with the business objects in the "models.py" module. The bigger the codebase gets, the harder it is to maintain everything in one file, but it's a good starting point.

You may use User and Group models from django.contrib.auth.models: Django provides them from the box. The User is a registered person in your web service and the Group is a collection of Users. We'll create some of those when we attach a database to your project.
View

magazine/
├── blog
    └── templates
        └── blog
            └── index.html
└── templates
    └── base.html

No one will know what the service does unless it has some form of visual rendition. The View is a representation of your web service. Simply put, it is what the user sees.

The View component is stored in templates. Templates are files that support Django/Jinja2 template languages. Besides, they can include content with HTML, CSS, and JavaScript. Template language utilizes the ability to use similar constructs you use in Python. It's has a different syntax but the same function words.

To create "templates" directory for the project and for the application, run:

# Unix
mkdir templates
mkdir -p blog/templates/blog

# Windows
mkdir templates
mkdir blog\templates\blog

In the project folder you keep base files for all other templates, applications folder contains only application-specific templates.

When you create "templates" directory for your application, you should name it "<application name>/templates/<application name>". This redundancy is obligatory. If you use the same file name without the second repetition of <application name>, like "blog/templates/index.html" and "news/templates/index.html", then in both cases Django template loader will return the first file it found, which isn't always what the user actually needs.
Controller

magazine/
├── blog
     └── views.py
└── magazine
      └── urls.py

Views and models are good instruments, but something should manage how they work together, which is where we turn to the Controller part.

The Controller consists of two types of files: "views.py" and "urls.py". In "urls.py", you define the routing for your service. Routing is a process of matching request links with appropriate view handlers. You can include routes from "urls.py" files one into another, but the main will be "<project_name>/<project_name>/urls.py". If you want to create routing files for each application, do it and include them in the main one.

In "views.py" you define view handlers, which play a mediator role between the Model and the View. A view handler is a function or a class that responds to requests. Since communication between client and server is an implementation of the HTTP protocol, handler answers with a status code. If the request was successful, the server typically responds with 200 code. In case the requested page is not found, it will be 404; if the server is down, it's 500. Other examples of codes can be found at https://httpstatuses.com/.
Request to the Web Site

Now that you know how functions are divided between the components, let's see how they interact when there's a web site request.

1. A user sees a link or a button in a View, presses it and creates a request.
2. The Controller receives the request.
3. It passes the request to the appropriate handler.
4. The handler calls Model methods to retrieve objects from data storage.
5. It chooses the View template to render a response.
6. A user sees a response.

Each part has its own methods and base classes in the Django package. You should separate the work with each component as Django developers do: this way other developers will understand your code and you will understand theirs.
.......................
Theory: Django ORM
Working With a Database From Python

Chances are, the storage you most often work with is a file system. It works well for HTML pages and templates, but how do you keep small objects like login, age or, say, favorite color for each individual person? Relational databases can help you organize and manipulate such data.

We will start from scratch and learn how to work with databases using only Python.

We define models to describe the schema of our data. To convert Python objects and primitives to database types, we will use adaptor classes, Fields. These abstractions help us pay less attention to the database specifics and focus mainly on what to store and how.

Once we declare the models and the fields in them, we create migrations and apply them to the SQLite3 database. Feel free to change it to another database backend. No matter which database you choose, our code will remain valid.
Relational Databases

If your first thought is "I need to keep the data with a common structure", then your second thought should surely be "databases".

A relational database is a collection of multiple data sets organized by tables, records, and columns. It works fine for most types of data. Each implementation provides you the universal language called structured query language (SQL). You can read about it, but as we say, we will work with the database in another way.

The most popular databases are PostgreSQL, Oracle SQL, MS SQL, and MySQL. There is also a simple database that works on your smartphone in many applications: it's called SQLite. It's perfect for one-client use and trying out Django models for the first time. Check whether you have it on your computer:

sqlite3 --version

If you don't, try to install it with your package manager or download it from the official site.
Object-Relational Mapping

With the fall approaching and clouds getting denser, the new season of Quidditch is starting. As you know, wizards really lack computer science classes in Hogwarts, even though programming is a kind of magic. They want to store the teams, their results and the rosters on the website, and they wonder if there is a way to do to it with Django. Well, there sure is! For this purpose, we will make the quidditch project with the tournament app in it. Let's meet and greet Django Models!

Django Models are classes that map the objects from the real world to the database records. We have teams, so we call our model the Team. This approach is called Object-Relational Mapping(ORM).

The ORM is a concept to map one type system to the other. We will work with databases by means of Python classes and methods. Our strong side is the programming language and we are going to make the most of it. The objects are similar to database records and their methods resemble SQL commands. There's no need to know SQL directly as we apply the instruments that imitate it.

To tell Django that it's a special class which maps its structure to the database table, we inherit the Team from django.models.Model. Also, we have players and game tables. Let's make the stubs for our classes in tournament/models.py module:

from django.db import models


class Team(models.Model):
    name = ...


class Player(models.Model):
    height= ...
    name = ...
    team = ...


class Game(models.Model):
    date = ...
    home_team = ...
    home_team_points = ...
    rival_team = ...
    rival_team_points = ...

We gave names to our classes and described their content. The restriction of all relational databases is that we should define the types for all the fields in the Model. So how can we match the types with the fields?
Fields

To get most of the database's features, we use special Fields classes. They map the attribute of the class to a particular column in the database table. Does it mean we need the instance of a class for each field? Yes, but don't worry, it's actually easier than it may seem.

To build the whole schema, we start from the core element, the Team:

class Team(models.Model):
    name = models.CharField(max_length=64)

CharField is similar to Python string but has one restriction: the length limit. "Wigtown Wanderers" is the longest team name in the league now, but the league is still open to new teams, so we ensure max_length with 64 symbols.

Each team has players. Let's define a model for a player:

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

We already know what the CharField means, so the FloatField should sound familiar to you, too. It's the same as Python's float type. What's more interesting is the ForeignKey field. It means that the player is bound to a specific Team and the restriction on_delete=models.CASCADE means that if the Team is deleted from the database, it will be erased with all the players. That sounds unfair, but you should try harder to stay in the league!

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

There are no games without teams, so again we set on_delete=models.CASCADE for each ForeignKey. Also, we add the related_name for the Game model, by which we can access it from the Team model. It's necessary to add such names because we have two foreign keys to the Team and you should differ one from another.

Points is an int type, so we make it IntegerField, and the date is clearly a DateField.

You can think of Fields as expansions of Python's primitive types for simple cases like IntegerField, CharField, and FloatField. They also have special cases like ForeignKey and other relations between objects.
Migrations

At this point, we describe the mappings between Python classes and database tables, but we don't have any tables yet. That's sad news. Should we learn some fancy SQL to create a database and tables in it? No, because we can simply describe to Django what we want and it will do the dirty work for us — again.

Add tournament to INSTALLED_APPS in the quidditch/settings.py module:

INSTALLED_APPS = [
    # other installed apps
    'tournament',
]

We have the schema of the league in our code, we are ready to migrate it to the database. It takes two steps:

python manage.py makemigrations
python manage.py migrate

The first command creates migrations. Migration is a piece of code that describes what actions should be done in the database to synchronize the models with the tables. You can find the created code in the tournament/migrations/0001_initital.py file.

In the second step, we apply the changes and run the generated commands.

Preceding manage.py <command> with python is the platform-independent way to launch any django command. It's a valid syntax for both Unix and Windows systems.

If you want to make and then apply migrations to a particular application in your project, you should add the application name after each command:

python manage.py makemigrations tournament
python manage.py migrate tournament

When you run these commands, your database will finally have the tables to work with. We are ready to fill them with real data!
........................
Work on project. Stage 1/5: Creating models
Project: HyperJob Agency

The "HyperJob" recruitment agency is a very conservative one. Its history starts on January 1st, 1970 . The managers in the agency prefer communicating by phone or email and searching for employees personally. That was an efficient strategy some ten years ago, but now the candidates prefer to apply for jobs online. The problem is that "HyperJob" still doesn't have a site, so they need you to create the service as soon as possible.

We start with a simple site that will be suitable for:

    Creating a new vacancy by the agency's manager
    Creating a new resume by a candidate

We know that it will be a long road, so at each stage you will make only a small part of work. By the end, we'll have a working site that fulfills all the requirements.
Objectives

Your first task is to prepare the models for the data. It's important to keep all the data safe. We need to store all the vacancies and resumes persistently in the database. Create models to manage the database tables.

Use the default settings of the project with a predefined SQLite database.

Throughout the project, we will need at least two models: Vacancy and Resume. Both of them should have the description and author fields. The description is a text field with no more than 1024 symbols, and the author is a foreign key to django.contrib.auth.models.User model.

Define Vacancy and Resume in models.py module and migrate them to the database. We check your work this time, so that at the next steps you are confident enough to add new models by yourself.


..........................


Theory: Introduction to OOP

Fundamentals
Object-oriented programming (OOP) is a programming paradigm based on the concept of objects that interact with each other to perform the program functions. Each object can be characterized by a state and behavior. An object keeps the current state in the fields and the behavior in the methods.
Basic principles of OOP

There are four basic principles of OOP. They are encapsulation, abstraction, inheritance, and polymorphism.

    Data encapsulation is the mechanism of hiding the internal data of objects from the world. All interaction with the object and its data are performed through its public methods. Encapsulation allows programmers to protect the object from inconsistency.
    Data abstraction means that objects should provide the simplified, abstract version of their implementations. The details of their internal work usually aren't necessary for the user, so there's no need to represent them. Abstraction also means that only the most relevant features of the object will be presented.
    Inheritance is a mechanism for defining parent-child relationships between classes. Often objects are very similar, so inheritance allows programmers to reuse common logic and at the same time introduce unique concepts into the classes.
    Polymorphism literally means one name and many forms, and it concerns the inheritance of the classes. Just as the name suggests, it allows programmers to define different logic of the same method. So, the name (or interface) stays the same, but the actions performed may be different. In practice, it is done with overloading or overriding.

These are the key concepts of OOP. Each object-oriented language implements these principles in its own way, but the essence stays the same from language to language.
Objects

The key notion of the OOP is, naturally, an object. There are a lot of real-world objects around you: pets, buildings, cars, computers, planes, you name it. Even a computer program may be considered as an object.

It's possible to identify some important characteristics for real-world objects. For instance, for a building, we can consider a number of floors, the year of construction and the total area. Another example is a plane that can accommodate a certain number of passengers and transfer you from one city to another. These characteristics constitute the object's attributes and methods. Attributes characterize objects' data or states, and methods — its behavior.

In OOP, everything can be considered an object. Programs are made from different objects interacting with each other. An object's state and behavior are usually placed together, but it's not always so. Sometimes, we will see objects without a state or methods. This, of course, depends on the purpose of the program and the nature of an object.
Classes

Often, many individual objects have similar characteristics. We can say these objects belong to the same type or class.

A class is another important notion of OOP. A class describes a common structure of similar objects: their fields and methods. It may be considered a template or a blueprint for similar objects. An object is an individual instance of a class.

Let's look at some examples below.

Example 1. The building class
An abstract building for describing buildings as a type of object (class)
Each building has the same attributes:

    the number of floors (an integer number);
    area (a floating-point number, square meters);
    year of construction (an integer number).

Each object of the building type has the same attributes but different values.

For instance:

    Building 1: the number of floors = 4, area = 2400.16, year of construction = 1966;
    Building 2: the number of floors = 6, area = 3200.54, year of construction = 2001.

It's quite difficult to determine the behavior of a building. But this example demonstrates attributes pretty well.

Example 2. The plane class
Unlike the building, it is easy to define the behavior of a plane. It can fly and transfer you between two points on the planet.
An abstract plane for describing all planes as a type of object (class)

Each plane has the following attributes:

    a name (a string, for example, "Airbus A320" or "Boeing 777");
    passengers capacity (an integer number);
    standard speed (an integer number);
    current coordinates (they are needed to navigate).

Also, it has a behavior (a method): transferring passengers from one geographical point to another. This behavior changes the state of a plane, namely, its current coordinates.
Conclusion about objects and classes

To put it concisely, you should remember the following:

    an object-oriented program consists of a set of interacting objects;
    as a rule, the internal state of an object is hidden;
    an object may have characteristics: fields and methods;
    an object is an instance of a class (type);
    a class is a more abstract concept than an individual object; it may be considered a template or blueprint that describes the common structure of a set of similar objects.

............................

Theory: Inheritance

Software development is strongly associated with real-world entities. However, we should consider not only the entities themselves but also the interactions between them. One of the ways it is presented in object-oriented programming is inheritance. This time we'll talk about this technique, and you'll get to know why it can be useful to apply it in your code.
What is inheritance?

We start making our program with basic objects and methods. Imagine a messenger application. The main objects in messengers are chats, so we start ours with the CHAT class. The time comes, and we diversify the chats to:

    direct messages to someone
    group chat
    saved messages only for yourself

If we want to make more types of chats, do we need to write the code from scratch for each one? The answer is no! With the help of inheritance, we can instead reuse the code we already have.

Inheritance is a relation between entities that we interpret as "is a" or "is a kind of" relation. In the case of programming methods and attributes, it means that a child entity has every feature of the parent entity. On the other side, we can also change inherited features or define the new ones in such relation.

Here are some examples of inheritance:

    A swan is a bird. A swan can do everything that a typical bird can do, but it has an additional feature: it can swim.

    A dentist is a doctor. He has medical education, he can cure a cold, and he knows a lot more about teeth than any other doctor.
    A laptop is a computer. It has processor units, memory, keyboard, and all other stuff computers typically have, but it is also portable.

Inheritance modeling

Let's stick to the example with a chat and see how we can model the classes of our program.

We can start by moving all the shared methods and attributes to the base CHAT class. For the sake of simplicity, we define only one attribute and only one method:

To make our base class more useful, we can add some more features like SEND_FILE, EDIT_MESSAGE, POSTPONE_MESSAGE, and others.

Next, we draw child classes and methods they need to work properly:

Let's take a closer look at the diagram and figure out what benefits the inheritance gives us. First, we don't need to implement any other methods to make a new class SAVED_MESSAGES: we add only one participant there, and it can work right out of the box! For the other two classes, we implement only some new methods like FETCH_MESSAGES to get updates from other participants and ADD_PARTICIPANT to add a new person to a group chat.

You may notice that we can even inherit the GROUP_CHAT from the DIRECT_MESSAGES to reuse its methods. It makes sense because there is not much difference between two, three, hundred persons to communicate in a chat, but the hierarchy is fine too.

Conclusion

Inheritance is a very flexible and useful mechanism in software development. It allows us to simplify and speed up the development process by reusing the code we've already written. As you have learned, it also reflects the dependency between the parent and child classes that we can express as "is a kind of" relation.
............................
Theory: The concept of patterns
Code design

If you are reading this, you must be really interested in programming. It doesn't matter whether you are an experienced developer, just starting your career, or still working on the basics; what really matters is that you are curious, so welcome.

To begin with, let's talk about code design. In general, the design of your code is about expressing your ideas clearly to your teammates, colleagues, and clients. We can compare code to text: if you put the lines in the right order and make the structure clear, it will be much easier to explain and understand the text later. From an engineering point of view, your code is well-designed if you can agree with the following statements:

1) When you make a small change, it does not produce a ripple effect elsewhere in the code.
2) Your code is easy to reuse.
3) It is easy to maintain your code after release.
Design patterns

In application development, the design of code has to match the problem and be general enough in order to fit all the requirements that may arise in the future. Everyone tries to find more elegant, suitable and flexible solutions that can also be reused. Here is where design patterns come into play: these are repeatable solutions to common problems that developers face. Design patterns even have names! For example, if you want to confine yourself to just one instance of a class, Singleton pattern is going to be the best choice; if you see family relations between objects and you want to encapsulate creational process, you should use AbstractFactory, etc.

As a rule, examples of well-structured object-oriented architecture make use of patterns a lot. When a suitable pattern is used, it tells us that the developer has really paid attention to typical interactions between elements in the system. As a result, the architecture of an application becomes easier to understand.

Being so useful, design patterns have made it onto many programmers' bookshelves: one of the most famous examples is the book Design Patterns: Elements of Reusable Object-Oriented Software. You probably heard about its authors, "Gang of Four", which is frequently abbreviated as "GoF". Today it is considered one of the classic books on software design and programming. You may check it out to deepen your understanding or proceed directly to practical learning here.

Note that in this topic we will only consider object-oriented design patterns.

Software design patterns and related concepts

A great thing about patterns is that they help you not to waste your time reinventing the wheel so you can spend it on developing cool features instead. The structure of design patterns is strict: describe the problem, the solution, when to apply the solution, and its consequences. Theoretically, you can combine a few patterns and create your own monster pattern that contains, for example, Builder, Abstract Factory and Decorator simultaneously. However, as you will see from the following topics, it's better to avoid such monsters because patterns have already been well-grouped for you. In other words, don't get too excited, it's really better to use them one at a time.

Using patterns does not require any specific programming language skills or striking imagination. Patterns are also language-independent: even though they can be implemented differently in different languages, the general idea of each pattern is common for all of them. That means that it's possible for you to speak the language of architecture with your colleagues even if they work with different technologies.
Why should I know design patterns?

Here is a list of quite convincing reasons to get familiar with design patterns:

    Patterns provide tested and commonly used solution templates for design problems; you don't have to invent anything!
    Patterns improve flexibility and maintainability of object-oriented systems, which makes it easier to react to changing requirements.
    Patterns can speed up the development process.
    Patterns are a universal vocabulary that allows developers to describe a program design using a set of well-known identifiable concepts.
    Patterns are often used in standard libraries and frameworks.
    You can find patterns in the source codes of many applications and quickly understand how they work, instead of reading thousands of lines of code.

Caveats

In order to achieve flexibility, design patterns usually introduce additional levels of indirection, which in some cases may complicate the resulting designs and hurt application performance. In other words, even though patterns are supposed to make things easier for you, they may also become an unnecessary complication if applied unwisely. Beginner developers may try to apply patterns everywhere, even in situations where a simpler code would do just fine. Look how design patterns can complicate even the simplest "Hello, World" program.

To avoid misusing the patterns, you should apply them wisely and be able to correctly adapt them to your problem and language.
Final remarks

When you master the principles of working with patterns so that after successfully applying them you scream "Eureka!" without any doubt in your thoughts, your perception of object-oriented programming will probably change once and for all. In the following topics, you will learn about Creational, Structural and Behavioral design patterns. Be concentrated and attentive: these matters are quite advanced. Happy coding!
............................
Theory: Frameworks
What are frameworks?

Every program is different just like snowflakes, yet it is the similarities that we want to direct your attention to, or rather, how these similarities can be used to the developer's advantage. In programming, it is common practice to reuse code packed into libraries in order to simplify the development and avoid making the same errors over and over. Such libraries exist for most programming languages; they provide good documentation and well-tested code used by many people.

Large applications like Internet stores, online banks or social networks often need the same typical components and functionality such as user authorization, database interaction, sending notifications and so on. To reuse them, developers created a special kind of software called frameworks for all popular programming languages.

A framework is a universal, reusable piece of software that facilitates the development of typical applications or their parts. It consists of structured code templates and provides generic functionality which can be easily extended for the needs of a specific application. To relinquish control on low-level tasks and focus on the high-level problems, you should use the API provided by the framework. It can significantly reduce total development time.

Some frameworks are so large that they are in fact a union of different frameworks under a single name.

Frameworks are extremely useful and relatively easy to grasp: for example, the very concept of frameworks has some real-life analogies that would make comprehension painless for all sorts of learners.
Frameworks vs libraries

At first glance, it might seem like frameworks and libraries are very similar, but it's not quite true.

Applications that use frameworks are built on top of them and extend their code to get specific functionality. In a sense, a framework serves as the skeleton of an application or its parts and sets "the rules of the game". A library, on the other hand, only provides some specific operations without having such a global influence. This is the key difference between frameworks and libraries. However, libraries can be provided as parts of frameworks.

Of course, there's no escape from evident similarities between frameworks and libraries. The programmer who uses a framework does not modify its source code — he/she acts only as its user.
Inversion of Control

The most common principle that comes with frameworks is Inversion of Control (IoC).

In a framework, unlike in libraries or standard user applications, the overall program's flow of control is dictated not by the caller, but by the framework. It means the framework calls your code, and not vice versa:

This happens because a framework provides templates for solving possible tasks and the interaction between the templates has been defined by developers of the framework. The user of a framework just takes the templates and extends them with application-specific code.
Advantages and disadvantages

Time to weigh everything. To start on a positive note, the use of frameworks has a number of strong advantages:

    rapid prototyping and development;
    standardization of project structures — it is easier to understand similar projects with the same structure;
    wide use in companies around the world;
    bug fixes and security updates by the authors;
    a well-designed skeleton — as a rule, frameworks use up-to-date practices and patterns to provide a firm skeleton for applications.

Despite the advantages, there is a number of common drawbacks:

    selecting an unsuitable framework can make an application harder to implement;
    application slowdown — frameworks often do a lot of heavyweight things hidden from programmers;
    it is difficult to replace the used framework with another one if yours no longer suits you (while libraries can be easily replaced);
    you may encounter a bug in the framework which may affect your work.

This might not be a complete list of advantages and disadvantages, but as you'll be getting more practice with using frameworks, you'll discover them for yourself.
How to choose frameworks

As a rule, each programming language has several frameworks to choose from. Of course, if you come to a company where some framework is already being used, there may be no choice for you. But if you do have a choice, try to take into account all possible benefits and problems when making a decision.

Here is some general advice for choosing a suitable framework:

    Pay attention to well-known frameworks with good documentation. This will greatly simplify the use and allow you to easily find developers already familiar with this framework. Some popular frameworks even become a de-facto standard for developing specific types of applications. Such frameworks should be considered first.
    If you write a small application that will most probably never change, you can develop it without frameworks. Moreover, for such an application they can introduce unnecessary additional complexity. But you may also consider the use of the so-called lightweight frameworks or choose a framework only for some part(s) of your application.

This is general information; as we said, programs are different, and so are the possible frameworks out there. The best part is getting to know specific frameworks and working with them closely.
............................
Theory: Data and object mapping

Programming languages may include primitive types, classes and data structures to store information. If you want to modify an object or interact with it somehow, you would prefer to do it in your favorite programming language, wouldn't you? As a developer, you use tools you're familiar with. In the local environment, you can complete most of your tasks this way. However, to communicate with other systems and to store data persistently, you need to convert your local types to commonly used data representation.
Data mapping

Assume that you are developing a social network service. Every moment, some users search for a friend and the service should reply with some information about other users in the network.

We represent each person as an instance of the Person class in the code. Let's stick to a simple diagram to avoid using any specific programming language:

The problem arises when you want to retrieve the information about a person from the storage you use. Relational databases often play the role of the storage but in the form of tables and relations between them. Luckily you're not the first person that faces the task to convert one common data type to another. Just find a library for data mapping and it will help you a lot.

Data mapping is matching fields of source data representation to the fields of its destination. In our case, the source is a database, and the destination is the Person class, but the operation is applicable vice versa. In other tasks, we could use other mappings for the Person class and convert it to/from JSON, XML.

We use data mapping to convert the information from one type to another, but we don't synchronize the data changes over time by default, we only want a different view at the particular moment.
Object Mapping

The structure of data in the source system may be different from the structure of data in the destination system. We could store the information about the name in one place and the information about the age in another because retrieving data to Person class is not the only purpose of the storage. This time data mapping will only match the part of the data we needed. For complex operations like this one, we need a more appropriate instrument such as object mapping.

Object mapping is matching data from a source system to a complex object in the destination system.

The most commonly used example is ORM (Object-Relational Mapping) when the data from relational databases is matched with the classes in object-oriented languages.

The main distinction between data and object mapping is that object mapping not only stores data but also emulates the behavior of an object and reflects changes in its source system. As a developer, you can call methods of the class, and data mappings will change at the same time. In short, object mapping is like data mapping, but with high-level control over changes.
The life cycle of mapping

To see what is data and object mapping in action, let's continue our work with the social network. We receive a query with some name and look for it in our data storage. As soon as we find an appropriate result, we retrieve the information about the person from the database. We fill the class instance with the result of the search.

Now our class is only a data container and nothing more, and this action is an example of data mapping. If we store the object in the database, it's a reversed example.

The age of a person is changing over time, but the storage is not aware of such changes, so we implement a method that adds a year to the age attribute:

After the age is changed in the instance of the class, the value in the storage becomes outdated. If we want to mirror it, we should put some effort into working with the storage, then we need to synchronize the information. This can take place in the same method or we can define another one for it.

This operation refers to object mapping; we are not only changing the object but also synchronizing data for it. Now our object has actual information in the storage, too. Synchronization is one of the important features of mapping; we want to have the definite representation of an object in our language and in the storage it uses. However, it's not obligatory to synchronize objects every time we change them. Sometimes it's more efficient to accumulate all the changes before the synchronization.
Conclusion

We have learned two new concepts: data mapping and object mapping. We use data mapping to match data in two different systems, and we use object mapping to represent more complex objects and to add control from one system to data in another.
............................
Theory: Introduction to databases

The world today is overloaded with information, and so are we. How do you keep important information safe and sorted? You may simply hope you neither forget nor confuse anything, but it's better to write it down or save it on your device. So you have it on your computer or phone, and the program keeps the information safe. While the program is active, it "remembers" everything. However, quitting the program may result in losing all that information. That's why it is better to keep the data using more sophisticated tools.

The challenge is to navigate a huge and complex web of information and ensure everything important is safe and organized: a task that databases handle well.
Database

A database is a collection of data that is specifically organized for rapid search and retrieval processed by a computer.

The difference between a database and a usual file is that a file may be structured or not, but a database must have a specific structure. For example, you can create a file with a to-do list:

Obviously, we'd say that this file has some kind of a structure, but from a computer's perspective, it's still a plain file, until you write a program that manages data in it. Usually, the information in databases is compressed and stored as binaries rather than plain text, so it's clear that this kind of structure is meant for computers, not humans.

Unlike us, computers can easily understand the binary format of data, but what allows them to read and write it correctly? It is a program called Database Management System that controls the data in a database.
Database Management System

Database Management System (DBMS) is a type of software that allows users to define, create, and control data in a database.

DBMS is a mediator between a user and a database, which means that users can work with databases through the interface of DBMS.

We need DBMS to make databases more efficient, because developers can optimize data structures and algorithms for databases independently of the user interface.

Another goal of this software is to help users work with different databases without exposing their actual differences.

Most database management systems have pretty good descriptions and tutorials on their sites. There are also specific languages that you need to learn to start working with a database, but if you know programming languages, you can work with a database with their tools instead.

Although it sounds like all databases have different syntax, most of them actually implement common standards. Almost all relational databases use the SQL standard, so you can apply the same commands in different DBMS's.

Access to data

At this stage, you may still have doubts as to using databases. You have to learn a new language to update and select the data, which can be time-consuming, so why not use plain files instead?

Of course, you can keep the files locally, but as they grow in number, you won't be able to find information quickly. Databases provide schemas and metadata that allow for a quick search of the needed data.

A schema describes how YOU organize the data. Metadata holds structural and statistical information.

If you want to access your data from multiple devices, most systems provide a convenient way to work with them through the web.

To open restricted access to another person, some management systems use simple login/password authentication, while some provide more powerful instruments. With their help, you can grant access to a limited portion of data for each user.

If you still are not convinced how great the DBMSs are, let's look at what else you can get from them.
Data consistency

One of the best features of databases is their ability to keep and restore the data correctly. It doesn't mean that the DBMS knows how to be correct, but once you define the correctness with the configuration or schema, you can be sure that nothing will break these rules. DBMS can provide you with formats you can use for your data. You can also set up all the tests and constraints that you want to have.

Say you have some data that multiple users with their devices have access to: this may potentially create a conflict of updates. Updates in files usually follow the "last save wins" rule. Databases, on the other hand, isolate different users and can be configured to resolve conflicts between their updates

There's another good thing about databases. When a usual file becomes corrupted and cannot be opened, you've lost your data forever. Using DBMS instead, you can make backups and then restore the data to continue your work.

Of course, you can emulate all of these operations and develop your DBMS, but first, try to work with the existing solutions.

Conclusion

There's a lot of learning you need to do before you start working with databases. No pains, no gains, and here you can actually gain a lot.

With databases you can:

    Store, retrieve and update data
    Get metadata and data dictionaries
    Access database remotely
    Restrict accesses to data
    Make concurrent updates
    Recover to some point of time
    Check the rules for data consistency automatically

In a data-driven world, this kind of functionality is golden. Welcome to the world of new opportunities and good luck with exploring the databases!
.........................
Theory: What is SQL
Introduction

SQL (Structured Query Language) is a domain-specific programming language designed to handle data in tables. It was developed in the 1970s, and to this day SQL-like interfaces are widely used and supported in data management systems, even those that are not based on the concept of a table.

Because of its applicability, you'll probably find SQL quite useful. If you are a software engineer, it's a good idea to learn it because many software systems store and process business data via services that support SQL. For example, the information system backend of an insurance company may use SQL to extract and update data about the clients.

If you are interested in analytics, with the help of SQL you'll be able to easily aggregate data and calculate statistics. Suppose you need to evaluate changes in popularity of the name Jessie between 1920 and 2000 (inclusive) based on census data. In SQL, this task would take only 11 strings of code! You may not understand the code now, just try to read it as a sentence in English. It selects records about individuals named Jessie and born between 1920 and 2000; then it groups records for each pair of year and gender; counts the number of records in each group; and generates, as a result, a table with columns "year", "gender", and "cnt" sorted by year and gender.

If you work in a data-based company, know that SQL is basically a standard of data manipulation language.

There's a lot to take from SQL and there's a lot to learn. We suggest to start with the very basics: that is, what SQL stands for. Let's take apart the abbreviation to know what we're dealing with.
S is for Structured

SQL is a language used to extract and update data structured as tables. Such data appears in various application areas: for example, Excel sheets with accounting data, census statistics in Google BigQuery, or online stores that utilize a special software system for storing and using tables called Relational Database Management System (RDBMS) which helps process information about goods, orders, and customers.

SQL is designed for tables with the following structure: a table contains rows each representing an entity or an object and columns with attribute names of these entities. A table cell from row R and column C stores the value of attribute C of entity R. For instance, in table "census" from our example rows represent individuals and each of them having attributes "id", "year", "name", and "gender". For instance, the third row contains data about Willie, a man born in 1985.

Quite often, data is organized in a bunch of tables with names, what is usually called a database, and one may address these tables by their names. For example, in a database for an online store, a table "Customers" contains data about customers (their names and contacts), while "Orders" stores information about orders (customer, goods, payment details).
Q is for Query

SQL is a programming language with a large feature set for data processing. SQL is a declarative language and thus any statement written in it is a query that states to the system what should be done or evaluated, but not how.

Let's focus on the simplest and most basic functionality of data extraction from a table. For example, if we have a table named "Customers", a query that extracts all rows and columns is the following:

SELECT * FROM Customers;
L is for Language

That simple query from the example above may be read as "select everything from customers". SQL was designed to be similar to natural language. Declarative nature of SQL hides the complexities from the user and, to some extent, you just declare your will while the system analyses the query, chooses the control flow, and executes it.

Just like any natural language, SQL has a standard of the American National Standards Institute (ANSI) and many dialects implemented by vendors of software that support SQL. Usually, dialects are based on the standard, but they still show differences in some technical details, for example, in processing dates and strings. This means that SQL queries in different dialects are not compatible. However, once you know the SQL basics, you'll be able to adapt to different dialects, like with American and British English.

Here and further, in case of incompatibility between vendors and ANSI standard we provide syntax for MySQL.
Conclusion

Now you know that SQL is a domain-specific declarative language for those who work with structured data.

If you have data that can be organized in tables and you want to know how to select rows and columns according to some criteria, join facts, create groups of entities, calculate statistics and much more, let's dive deeper in SQL.
.....................
Theory: Object-Relational Mapping(ORM)

A programming language is a tool to process data from one state to another. If we want to save the state of data permanently, we need some storage. Usually, for this purpose, we use a relational database, but then a problem occurs: programming languages and databases work with data differently. Moreover, relational databases have their language named SQL (Structured Query Language).

Luckily we are not the first people on Earth to suffer from this trouble. There is an approach called Object-Relational Mapping or ORM that is able to "translate" the database-way of interacting with information in an object-oriented way or to translate it backward.
ORM concept

Almost all programming languages have ORM libraries, but before you start using them, let's find out what is ORM idea about.

Object-Relational Mapping is a concept of converting data from an object-oriented programming language to relational database representation and vice versa. It solves the problem of matching two different type systems together and synchronize the data flow between them.

The main parts of ORM are:

    Virtual tables
    Relations
    Operations with objects

So what are these parts, and why do we need them?
Virtual tables

Relational databases use tuples and tables to store data. Most of the programming languages have tuples but don't have tables. How can we represent them in a programming language?

The main idea is to use classes as tables descriptions. We create a class as a virtual table for the given table in the database. We use or define methods for this class to retrieve, change and delete data

To represent one row from the table, we can define another class (for some libraries it can be the same class), and match its attributes to columns of the table. The instance of this class can manipulate not only the values of the row but also relations this row has, we will discuss it below.

Let's look at the example with the class City. We match values in tables with scalar attributes in the class. The name can be a string. Longitude and latitude can be real numbers.

As you know, a class can have attributes that represent a list of other objects. For example, a city may have a lot of streets. It contradicts attribute-to-column mapping, but the ORM provides instruments for these cases too. In terms of relational databases, the link between one object and several others is called one-to-many relation. It's quite similar to a list attribute of an object.
Relations

The relation is a link that connects a value from one table to the row in another. The database can store such links as keys. You can think about it as an object containing another object as an attribute.

Relations in databases are more than simple links. When you delete the root row from one table, it can imply cascade deletions of all related rows from other tables. It's not the same logic as for a programming language. If you have a link in an object, you expect that when you delete this link, only the link will disappear, not the connected object itself. On the other hand, if your database has a table "City" and London city in it, you can suppose when you delete London city from the table, all related rows from the table "Street" will disappear too. A street belongs to the city; without the city, there are no streets.

We can represent the example as the class City with a list of streets or as the many instances of class Street with an attribute City.

You may expect that if you delete the city, you will remove it with all the appropriate streets. However, if you delete the street and it has an attribute city, the city will stay in the database. It means that relations have directions. The cascade deletions imply the deletion of dependent objects, not dependent on ones.

Operations on objects

Four common-used operations with rows in the database are known as CRUD (Create, Read, Update, Delete) operations. It's similar to what we can do with objects in the programming language.

After you've read about tables and relations, you can try to control them via ORM library. Libraries usually provide high-level commands that look like working with any other objects in the programming language. Knowing something about relations and tables helps you not to corrupt data in the database.

It's highly recommended to read the documentation for the ORM library before using it. It helps you to get acquainted with the effects and consequences of applied operations.

Pros and Cons

If you still do not know, should you use ORM for your project or not, you can consider some pros and cons that this concept has.

Pros:

    You work with a database the same manner you write another code
    The library isolates your code from the specificity of SQL language of the database you're using
    The code using ORM is usually easier to read, write and maintain
    You don't have to know SQL to work with a database

Cons:

    Sometimes ORM libraries generate inefficient queries to a database
    It's hard to control the generation of queries
    You cannot use all the features and strengths of the specific database you have
    You should learn how to work with the library still

ORM is a good starting point for a project working with a database. Give it a chance and only then start interacting with a database directly. ORM will likely serve all your needs.

To start working with an ORM library, you may consider SQLAlchemy for Python, Hibernate or JPA for Java/Kotlin, Sequalize or TypeORM for JavaScript.

............................
Theory: Django ORM
Working With a Database From Python

Chances are, the storage you most often work with is a file system. It works well for HTML pages and templates, but how do you keep small objects like login, age or, say, favorite color for each individual person? Relational databases can help you organize and manipulate such data.

We will start from scratch and learn how to work with databases using only Python.

We define models to describe the schema of our data. To convert Python objects and primitives to database types, we will use adaptor classes, Fields. These abstractions help us pay less attention to the database specifics and focus mainly on what to store and how.

Once we declare the models and the fields in them, we create migrations and apply them to the SQLite3 database. Feel free to change it to another database backend. No matter which database you choose, our code will remain valid.
Relational Databases

If your first thought is "I need to keep the data with a common structure", then your second thought should surely be "databases".

A relational database is a collection of multiple data sets organized by tables, records, and columns. It works fine for most types of data. Each implementation provides you the universal language called structured query language (SQL). You can read about it, but as we say, we will work with the database in another way.

The most popular databases are PostgreSQL, Oracle SQL, MS SQL, and MySQL. There is also a simple database that works on your smartphone in many applications: it's called SQLite. It's perfect for one-client use and trying out Django models for the first time. Check whether you have it on your computer:

sqlite3 --version

If you don't, try to install it with your package manager or download it from the official site.
Object-Relational Mapping

With the fall approaching and clouds getting denser, the new season of Quidditch is starting. As you know, wizards really lack computer science classes in Hogwarts, even though programming is a kind of magic. They want to store the teams, their results and the rosters on the website, and they wonder if there is a way to do to it with Django. Well, there sure is! For this purpose, we will make the quidditch project with the tournament app in it. Let's meet and greet Django Models!

Django Models are classes that map the objects from the real world to the database records. We have teams, so we call our model the Team. This approach is called Object-Relational Mapping(ORM).

The ORM is a concept to map one type system to the other. We will work with databases by means of Python classes and methods. Our strong side is the programming language and we are going to make the most of it. The objects are similar to database records and their methods resemble SQL commands. There's no need to know SQL directly as we apply the instruments that imitate it.

To tell Django that it's a special class which maps its structure to the database table, we inherit the Team from django.models.Model. Also, we have players and game tables. Let's make the stubs for our classes in tournament/models.py module:

from django.db import models


class Team(models.Model):
    name = ...


class Player(models.Model):
    height= ...
    name = ...
    team = ...


class Game(models.Model):
    date = ...
    home_team = ...
    home_team_points = ...
    rival_team = ...
    rival_team_points = ...

We gave names to our classes and described their content. The restriction of all relational databases is that we should define the types for all the fields in the Model. So how can we match the types with the fields?
Fields

To get most of the database's features, we use special Fields classes. They map the attribute of the class to a particular column in the database table. Does it mean we need the instance of a class for each field? Yes, but don't worry, it's actually easier than it may seem.

To build the whole schema, we start from the core element, the Team:

class Team(models.Model):
    name = models.CharField(max_length=64)

CharField is similar to Python string but has one restriction: the length limit. "Wigtown Wanderers" is the longest team name in the league now, but the league is still open to new teams, so we ensure max_length with 64 symbols.

Each team has players. Let's define a model for a player:

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

We already know what the CharField means, so the FloatField should sound familiar to you, too. It's the same as Python's float type. What's more interesting is the ForeignKey field. It means that the player is bound to a specific Team and the restriction on_delete=models.CASCADE means that if the Team is deleted from the database, it will be erased with all the players. That sounds unfair, but you should try harder to stay in the league!

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

There are no games without teams, so again we set on_delete=models.CASCADE for each ForeignKey. Also, we add the related_name for the Game model, by which we can access it from the Team model. It's necessary to add such names because we have two foreign keys to the Team and you should differ one from another.

Points is an int type, so we make it IntegerField, and the date is clearly a DateField.

You can think of Fields as expansions of Python's primitive types for simple cases like IntegerField, CharField, and FloatField. They also have special cases like ForeignKey and other relations between objects.
Migrations

At this point, we describe the mappings between Python classes and database tables, but we don't have any tables yet. That's sad news. Should we learn some fancy SQL to create a database and tables in it? No, because we can simply describe to Django what we want and it will do the dirty work for us — again.

Add tournament to INSTALLED_APPS in the quidditch/settings.py module:

INSTALLED_APPS = [
    # other installed apps
    'tournament',
]

We have the schema of the league in our code, we are ready to migrate it to the database. It takes two steps:

python manage.py makemigrations
python manage.py migrate

The first command creates migrations. Migration is a piece of code that describes what actions should be done in the database to synchronize the models with the tables. You can find the created code in the tournament/migrations/0001_initital.py file.

In the second step, we apply the changes and run the generated commands.

Preceding manage.py <command> with python is the platform-independent way to launch any django command. It's a valid syntax for both Unix and Windows systems.

If you want to make and then apply migrations to a particular application in your project, you should add the application name after each command:

python manage.py makemigrations tournament
python manage.py migrate tournament

When you run these commands, your database will finally have the tables to work with. We are ready to fill them with real data!
............................
Theory: Intro to computational thinking

A programming language allows us to explain to a computer how to execute a solution to a particular problem in the real world. But first, a programmer has to come up with the solutions, also using a skill necessary for any type of programming no matter the language. It is called computational thinking.
What is computational thinking?

Computers can only deal with clear, concise instructions that agree with the rules of formal logic. However, real-world problems are rarely cut so clearly. Computational thinking is a set of mental skills helping to see the problems as a set of complex information processes that we can transform into a particular set of instructions for a computer.

Approach every problem you encounter while learning a programming language as not only the opportunity to remember the syntax of the language but also as an opportunity to train computational thinking.

To do that, you can follow a simple algorithm:

    Describe the problem
    What exactly needs to be done? What input data are you given and how does the desired outcome look like?
    Identify the important details needed to solve this problem
    Before thinking of a solution, make sure you took into account all the important aspects of the problem. The devil is in the details, and in case of programming, it hides in edge cases.
    Decompose
    Break the problem down into small, logical steps until you know exactly how to code each part of it.
    Use these steps to create an algorithm that solves the problem
    Connect the pieces of the problem in a way that would produce the desired outcome in all specified cases.
    Evaluate the process
    Usually, a problem has at least a few solutions, and it’s very useful to evaluate your idea to make sure you've chosen a way that is as efficient as possible.

Conclusion

Since computational thinking is a skill, it requires lots of practice before you can easily apply it. Don’t despair if your only thought when looking at a problem is that you have no idea how to achieve the desired results. Use the algorithms we described and keep on breaking the problem down until you see how to explain it to a computer with the tools of the programming language you chose.
.......................
Theory: Components of computational thinking

Computational thinking is a set of skills that helps you come up with a generalizable solution to a problem and solve it using a computer.
Let’s elaborate on the main foundations of this skill, namely: abstraction, decomposition, pattern recognition, and evaluation.
Decomposition

Complex problems are easier to solve when we break them down into separate steps and subproblems. We do this all the time in our daily life as well. For example, if your goal is to make a pizza, you’d need to find a recipe, shop for all the relevant ingredients, heat the oven, make the dough, chop the toppings and finally bake the pizza for an appropriate amount of time. Breaking down a problem like that helps to focus on solving each subproblem separately (and maybe even reusing solutions other people came up with) and avoid being overwhelmed by the requirements.
Extracting and Generalizing patterns

Once the problem is decomposed our next step would be to look for patterns in the smaller subproblems. A pattern is a set of features in a task that is shared among more than one instance of the problem. For example, if you need to cook Pepperoni pizza, you’d need to make a flat pizza bottom. The bottom is a pattern shared among all the pizzas, so you can generalize this pattern and if you wish to later make Margherita you can reuse all the information and steps you took for preparing Pepperoni pizza.

Pattern recognition is based on the five key steps:

    Identify common elements in problems or systems

    Identify and Interpret common differences in problems or systems

    Identify individual elements within sub-problems

    Describe patterns that have been identified

    Make predictions based on identified patterns.

Abstraction

Abstraction helps us generalize the solution by figuring out a model of a situation. We get rid of all the unnecessary details to focus on what’s actually important. One can say that a programming language is an abstraction. You use variables to perform operations instead of listing all the data these variables stand for every time.

It’s exactly the abstraction that helps us come up with a generalizable solution without writing a separate program for each variation of the problem.

If we come back to pizza, and try to apply abstraction we would say that for pizza to be a pizza it needs flat dough, sauce, and toppings.

The shape of the pizza and the fact that it has cheese would be unnecessary details since it is possible to imagine square pizza with no cheese.

Therefore if we abstract our pizza like a flat dough open pie with toppings and sauce we would be able to write one program to perform operations on all the pizzas, no matter their taste, shape, and vegan friendliness.
Evaluation

Once you found a solution to your problem it is helpful to go through an evaluation checklist. At times your solution won’t work and this checklist can also help you to find out where you’ve gone wrong.

Make sure your solution is:

    easy to understand – usually that would be the case if the problem is well decomposed

    complete – Your solution covers all the aspects of the problem. Remember, the devil is in the corner cases.

    efficient – Make sure you are making the best of the tools you have, in case of programming it can regard using appropriate syntax constructions. Speed is one of the most important markers of the solution’s efficiency and becomes incredibly important when writing production code.

Applying the concepts we discussed is helpful to develop a more efficient and structured problem-solving process. After all, the ability to solve problems is what makes a programmer out of a person who knows a programming language.
............................
Theory: Integer arithmetic

In real life, we often perform arithmetic operations. They help us to calculate the change from a purchase, determine the area of a room, count the number of people in a line, and so on. The same operations are used in programs.
Basic operations

Python supports basic arithmetic operations:

    addition +
    subtraction -
    multiplication *
    division /
    integer division //

The examples below show how it works for numbers.

print(10 + 10)   # 20
print(100 - 10)  # 90
print(10 * 10)   # 100
print(77 / 10)   # 7.7
print(77 // 10)  # 7

There is a difference between division / and integer division //. The first produces a floating-point number (like 7.7), while the second one produces an integer value (like 7) ignoring the decimal part.

Python raises an error if you try to divide by zero.

ZeroDivisionError: division by zero

Writing complex expressions

Arithmetic operations can be combined to write more complex expressions:

print(2 + 2 * 2)  # 6

The calculation order coincides with the rules of arithmetic operations. Multiplication has a higher priority level than addition and subtraction, so the operation 2 * 2 is calculated first.

To specify an order of execution, you can use parentheses, as in the following:

print((2 + 2) * 2)  # 8

Like in arithmetic, parentheses can be nested inside each other. You can also use them for clarity.

The minus operator has a unary form that negates the value or expression. A positive number becomes negative, and a negative number becomes positive.

print(-10)  # -10
print(-(100 + 200))  # -300
print(-(-20))  # 20

Other operations

The remainder of a division. Python modulo operator % is used to get the remainder of a division. It may come in handy when you want to check if a number is even. Applied to 2, it returns 1 for odd numbers and 0 for the even ones.

print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

Here are some more examples:

# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)    # 4
print(11 % -5)    # -4

Taking the remainder of the division by 0 also leads to ZeroDivisionError.

The behavior of the mod function in Python might seem unexpected at first glance. While 11 % 5 = 1 and -11 % -5 = -1 when both numbers on the left are of the same sign, 11 % -5 = -4 and -11 % 5 = 4 if we have one negative number. The thing is, in Python, the remainder always has the same sign as the divisor.

In the first case, 11 % -5 = -4, as the remainder should be negative, we need to compare 15 and 11, not 10 and 11: 11 = (-5) * (-3) + (-4). In the second case, -11 % 5 = 4, the remainder is supposed to be positive: -11 = 5 * (-3) + 4.

Exponentiation. Here is a way to raise a number to a power:

print(10 ** 2)  # 100

This operation has a higher priority over multiplication.
Operation priority

To sum up, there is a list of priorities for all considered operations:

    parentheses
    power
    unary minus
    multiplication, division, and remainder
    addition and subtraction

As mentioned above, the unary minus changes the sign of its argument.

Sometimes operations have the same priority:

print(10 / 5 / 2)  # 1.0
print(8 / 2 * 5)   # 20.0

The expressions above may seem ambiguous to you, since they have alternative solutions depending on the operation order: either 1.0 or 4.0 in the first example, and either 20.0 or 0.8 in the second one. In such cases, Python follows a left-to-right operation convention from mathematics. It's a good thing to know, so try to keep that in mind, too!
PEP time!

There are a few things to mention about the use of binary operators, that is, operators that influence both operands. As you know, readability matters in Python. So, first, remember to surround a binary operator with a single space on both sides:

number=30+12      # No!

number = 30 + 12  # It's better this way

Also, sometimes people use the break after binary operators. But this can hurt readability in two ways:

    the operators are not in one column,
    each operator has moved away from its operand and onto the previous line:

# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

Mathematicians and their publishers follow the opposite convention in order to solve the readability problem. Donald Knuth explains this in his Computers and Typesetting series: "Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations". Following this tradition makes the code more readable:

# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

In Python code, it is permissible to break before or after a binary operator, as long as the convention is consistent locally. For new code, Knuth's style is suggested, according to PEP 8.
............................
Theory: Program with numbers

Programs in which there's nothing to calculate are quite rare. Therefore, learning to program with numbers is never a bad idea. An even more valuable skill we are about to learn is the processing of user data. With its help, you can create interactive and by far more flexible applications. So let's get started!
Reading numbers from user input

Since you have become familiar with the input() function in Python, it's hardly new to you that any data passed to this function is treated as a string. But how should we deal with numerical values? As a general rule, they are explicitly converted to corresponding numerical types:

integer = int(input())
floating_point = float(input())

Pay attention to current best practices: it's crucial not to name your variables as built-in types (say, float or int). Yet another caveat is related to user mistakes. If a user writes an inaccurate input, ValueError will occur. At the moment, we'll limit ourselves to this. But not to worry, more information about errors is available in a dedicated topic. Now, consider a more detailed and pragmatic example of handling numerical inputs.
Free air miles

Imagine you have a credit card with a free air miles bonus program (or maybe you already have one). As a user, you are expected to input the amount of money you spend on average from this card per month. Let's assume that the bonus program gives you 2 free air miles for every dollar you spend. Here's a simple program to figure out when you can travel somewhere for free:

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per piece of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)

This program will calculate how many months you need to travel the selected distance and back.

Although it is recommended to write messages for users in the input() function, avoid them in our educational programming challenges, otherwise your code may not pass our tests.

Advanced forms of assignment

Whenever you use an equal sign =, you actually assign some value to a name. For that reason, = is typically referred to as an assignment operator. Meanwhile, there are other assignment operators you can use in Python. They are also called compound assignment operators, for they carry out an arithmetic operation and assignment in one step. Have a look at the code snippet below:

# simple assignment
number = 10
number = number + 1  # 11

This code is equivalent to the following one:

# compound assignment
number = 10
number += 1  # 11

One can clearly see from the example that the second piece of code is more concise (for it doesn't repeat the variable's name).

Naturally, similar assignment forms exist for the rest of arithmetic operations: -=, *=, /=, //=, %=, **=. Given the opportunity, use them to save time and effort.

One possible application of compound assignment comes next.
Counter variable

In programming, loops are used alongside special variables called counters. A counter counts how many times a particular code is run. It also follows that counters should be integers. Now we are getting to the point: you can use the operators += and -= to increase or decrease the counter respectively.

Consider this example where a user determines the value by which the counter is increased:

counter = 1
step = int(input())  # let it be 3
counter += step
print(counter)  # it should be 4, then

In case you need only non-negative integers from the user (we are increasing the counter after all!), you can prevent incorrect inputs by using the abs() function. It is a Python built-in function that returns the absolute value of a number (that is, value regardless of its sign). Let's readjust our last program a bit:

counter = 1
step = abs(int(input()))  # user types -3
counter += step
print(counter)  # it's still 4

As you can see, thanks to the abs() function we got a positive number.

For now, it's all right that you do not know much about the mentioned details of errors, loops and built-in functions in Python. We will catch up and make sure that you know these topics comprehensively. Keep learning!

Thus, we have shed some light on new details about integer arithmetic and the processing of numerical inputs in Python. Feel free to use them in your future projects.
................................
Theory: Boolean logic

Boolean type
The Boolean type, or simply bool, is a special data type that has only two possible values: True and False. In Python the names of boolean values start with a capital letter.

In programming languages the boolean, or logical, type is a common way to represent something that has only two opposite states like on or off, yes or no, etc.

If you are writing an application that keeps track of door openings, you'll find it natural to use bool to store the current door state.

is_open = True
is_closed = False

print(is_open)    # True
print(is_closed)  # False

Boolean operations

There are three built-in boolean operators in Python: and, or and not. The first two are binary operators which means that they expect two arguments. not is a unary operator, it is always applied to a single operand. First, let's look at these operators applied to the boolean values.

    and is a binary operator, it takes two arguments and returns True if both arguments are true, otherwise, it returns False.

    a = True and True    # True
    b = True and False   # False
    c = False and False  # False
    d = False and True   # False

    or is a binary operator, it returns True if at least one argument is true, otherwise, it returns False.

    a = True or True    # True
    b = True or False   # True
    c = False or False  # False
    d = False or True   # True

    not is a unary operator, it reverses the boolean value of its argument.

    to_be = True           # to_be is True
    not_to_be = not to_be  # not_to_be is False

The precedence of boolean operations

Logical operators have a different priority and it affects the order of evaluation. Here are the operators in order of their priorities: not, and, or. So, not is considered first, then and, finally or. Having this in mind, consider the following expression:

print(False or not False)  # True

First, the part not False gets evaluated, and after evaluation, we are left with False or True. This results in True, if you recall the previous section.

While dealing solely with the boolean values may seem obvious, the precedence of logical operations will be quite important to remember when you start working with so-called truthy and falsy values.
Truthy and falsy values

Though Python has the boolean data type, we often want to use non-boolean values in a logical context. And Python lets you test almost any object for truthfulness. When used with logical operators, values of non-boolean types, such as integers or strings, are called truthy or falsy. It depends on whether they are interpreted as True or False.

The following values are evaluated to False in Python:

    constants defined to be false: None and False,
    zero of any numeric type: 0, 0.0,
    empty sequences and containers: "", [], {}.

Anything else generally evaluates to True. Here is a couple of examples:

print(0.0 or False)  # False
print("True" and True)  # True
print("" or False)  # False

Generally speaking, and and or could take any arguments that can be tested for a boolean value.

Now we can demonstrate more clearly the difference in operator precedence:

# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100

Again, let's break the above expression into parts. Since the operator and has a higher priority than or, we should look at the 5 and 100 part. Both 100 and 5 happen to be truthy values, so this operation will return 100. You have never seen this before, so it's natural to wonder why we have a number instead of the True value here. We'll cover this surprising fact shortly. Coming back to the original expression, you can see that the last part False or 100 does exactly the same thing, returns 100 instead of True.

The operators or and and return one of their operands, not necessarily of the boolean type. Nonetheless, not always returns a boolean value.

Another tricky example is below:

tricky = not (False or '')  # True

A pair of parentheses is a way to specify the order in which the operations are performed. Thus, we evaluate this part of the expression first: False or ''. This operand '' evaluates to False and or returns this empty string. Since the result of the enclosed expression is negated, we get True in the end: not '' is the same as True. Why didn't we get, say, a non-empty string? The not operator creates a new value, which by default has the boolean type. So, as stated earlier, the unary operator always returns a logical value.
Short-circuit evaluation

The last thing to mention is that logical operators in Python are short-circuited. That's why they are also called lazy. That means that the second operand in such an expression is evaluated only if the first one is not sufficient to evaluate the whole expression.

    x and y returns x if x is falsy; otherwise, it evaluates and returns y.

    x or y returns x if x is truthy; otherwise, it evaluates and returns y.

For instance:

# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False

Those were the very basics of boolean values and logical operations in Python. It's definitely good to know them right from the beginning!
............................
Theory: List

In your programs, you often need to group several elements in order to process them as a single object. For this, you will need to use different collections. One of the most useful collections in Python is a list. It is one of the most important things in Python.

Creating and printing lists

Look at a simple list that stores several names of dogs' breeds:

dog_breeds = ['corgi', 'labrador', 'poodle', 'jack russell']
print(dog_breeds)  # ['corgi', 'labrador', 'poodle', 'jack russell']

In the first line, we use square brackets to create a list that contains four elements and then assign it to the dog_breeds variable. In the second line, the list is printed through the variable's name. All the elements are printed in the same order as they were stored in the list because lists are ordered.

Here is another list that contains five integers:

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

Another way to create a list is to invoke the list function. It is used to create a list out of an iterable object: that is, a kind of object where you can get its elements one by one. The concept of iterability will be explained in detail further, but let's look at the examples below:

list_out_of_string = list('danger!')
print(list_out_of_string)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

list_out_of_integer = list(235)  # TypeError: 'int' object is not iterable

So, the list function creates a list containing each element from the given iterable object. For now, remember that a string is an example of an iterable object, and an integer is an example of a non-iterable object. A list itself is also an iterable object.

Let's also note the difference between the list function and creating a list using square brackets:

multi_element_list = list('danger!')
print(multi_element_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

single_element_list = ['danger!']
print(single_element_list)  # ['danger!']

The square brackets and the list function can also be used to create empty lists that do not have elements at all.

empty_list_1 = list()
empty_list_2 = []

In the following topics, we will consider how to fill empty lists.

Features of lists
Lists can store duplicate values as many times as needed.

on_off_list = ['on', 'off', 'on', 'off', 'on']
print(on_off_list)  # ['on', 'off', 'on', 'off', 'on']

Another important thing about lists is that they can contain different types of elements. So there are neither restrictions, nor fixed list types, and you can add to your list any data you want, like in the following example:

different_objects = ['a', 1, 'b', 2]

Length of a list

Sometimes you need to know how many elements are there in a list. There is a built-in function called len that can be applied to any iterable object, and it returns simply the length of that object

So, when applied to a list, it returns the number of elements in that list.

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

empty_list = list()
print(len(empty_list))  # 0

single_element_list = ['danger!']
print(len(single_element_list))  # 1

multi_elements_list = list('danger!')
print(len(multi_elements_list))  # 7

In the example above, you can see how the len() function works. Again, pay attention to the difference between list() and [] as applied to strings: it may not result in what you expected.
Recap

As a recap, we note that lists are:

    ordered, i.e. each element has a fixed position in a list;
    iterable, i.e. you can get their elements one by one;
    able to store duplicate values;
    able to store different types of elements.

............................
Theory: If statement
Simple if statement

There are situations when your program needs to execute some piece of the code only if a particular condition is true. Such a piece of the code should be placed within the body of an if statement. The pattern is the same as in the English language: first comes the keyword if , then a condition, and then a list of expressions to execute. The condition is always a Boolean expression, that is, its value equals either True or False. Here is one example of how the code with a conditional expression should look like:

biscuits = 17
if biscuits >= 5:
    print("It's time for tea!")

Note that the condition ends with a colon and a new line starts with an indentation. Usually, 4 spaces are used to designate each level of indentation. A piece of code in which all lines are on the same level of indentation is called a block of code. In Python, only indentation is used to separate different blocks of code, hence, only indentation shows which lines of code are supposed to be executed when the if statement is satisfied, and which ones should be executed independently of the if statement. Check out the following example:

if biscuits >= 5:
    print("It's time for tea!")
    print("What tea do you prefer?")
print("What about some chocolate?")

In this example, the line "It's time for tea!", as well as "What tea do you prefer?", will be printed only if there are 5 or more biscuits. The line "What about some chocolate?" will be printed regardless of the number of biscuits.

An if statement is executed only if its condition holds (the Boolean value is True), otherwise, it's skipped.

Boolean values basically make it clear whether a piece of code needs to be executed or not. Since comparisons result in bool, it's always a good idea to use them as a condition.

There is one pitfall, though. You should not confuse the comparison operator for equality == with the assignment operator =. Only the former provides for a proper condition. Try to avoid this common mistake in your code.

Nested if statement

Sometimes a condition happens to be too complicated for a simple if statement. In this case, you can use so-called nested if statements. The more if statements are nested, the more complex your code gets, which is usually not a good thing. However, this doesn't mean that you need to avoid nested if statements at whatever cost. Let's take a look at the code below:

rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colors = "red, yellow, orange"
my_color = "orange"

if my_color in rainbow:
    print("Wow, your color is in the rainbow!")
    if my_color in warm_colors:
        print("Oh, by the way, it's a warm color.")

The example above illustrates a nested if statement. If the variable my_color is a string that contains the name of a color from the rainbow, we enter the body of the first if statement. First, we print the message and then check if our color belongs to the warm colors. The membership operator in simply shows whether my_color is a substring of the respective string, rainbow or warm_colors. Just like arithmetic comparisons, it returns a boolean value.

Here is what we will see in our case:

Wow, your color is in the rainbow!
Oh, by the way, it's a warm color.

When it comes to nested if statements, proper indentation is crucial, so do not forget to indent each statement that starts with the if keyword.
Report a typo
............................
Theory: For loop
What is iteration?

Computers are known for their ability to do things which people consider to be boring and energy-consuming. For example, repeating identical tasks without any errors is one of these things. In Python, the process of repetitive execution of the same block of code is called an iteration.

There are two types of iteration:

Definite iteration, where the number of repetitions is stated in advance.

Indefinite iteration, where the code block executes as long as the condition stated in advance is true.

After the first iteration, the program comes back to the beginning of the code’s body and repeats it, making the so-called loop. The most used one is the for loop, named after the for operator that provides the code’s execution.
For loop syntax

Here is the scheme of the loop:

for variable in iterable:
    statement

where statement is a block of operations executed for each item in iterable, an object used in iteration (e.g. string or list). Variable takes the value of the next iterable after each iteration.

Now try to guess which output we'll get if we execute the following piece of code:

oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)

During each iteration the program will take the items from the list and execute the statements with them, so the output will be:

Atlantic
Pacific
Indian
Southern
Arctic

Even strings are iterable, so you can spell the word, for example:

for char in 'magic':
    print(char)

Like this:

m
a
g
i
c

Range function

The range() function is used to specify the number of iterations. It returns a sequence of numbers from 0 (by default) and ends at a specified number. Be careful: the last number won’t be in the output.

Let's look at the example below:

for i in range(5):
    print(i)

What we'll get is this:

0
1
2
3
4

You can change the starting value if you’re not satisfied with 0, moreover, you can configure the increment (step) value by adding a third parameter:

for i in range(5, 45, 10):
    print(i)

According to the parameters included, we’ve asked to print the numbers from 5 to 45 with an increment value of 10. Be careful again, the last value is not included in the output:

5
15
25
35

If you're not going to use the counter variable in your loop, you can show it by replacing its name with an underscore symbol:

for _ in range(100):
    do_smth()

In the example above, we don't need the counter variable in any way, we simply use the loop to repeat do_smth() function a given amount of times.
Input data processing

You can also use the input() function that helps a user to pass a value to some variable and work with it. Thus, you can get the same output as with the previous piece of code:

word = input()
for char in word:
    print(char)

Oh, look, you can write a piece of code with a practical purpose:

times = int(input('How many times should I say "Hello"?'))
for i in range(times):
    print('Hello!')

You can, therefore, ask a user to specify the number of iterations to be performed.
Nested loop

In Python, it is easy to put one loop inside another one – a nested loop. The type of inner and outer loops doesn't matter, the first to execute is the outer loop, then the inner one executes:

names = ['Rose', 'Daniel']
surnames = ['Miller']
for name in names:
    for surname in surnames:
         print(name, surname)

The output is shown below:

Rose Miller
Daniel Miller

In this example, we use the two for loops to create fictional people's names. Obviously, you can deal with iterable objects of different sizes without too much fuss.
To sum up

All in all, for loops are an efficient way to automatize some repetitive actions. You can add variables and operations to make a nested loop. Moreover, you can control the number of iterations with the help of the range() function. Be careful with the syntax: an extra indent or lack of colon can cause a mistake!
Report a typo
............................
Theory: Declaring a function

Often enough, built-in functions cannot suffice even beginners. In such a case, there is no choice but to create your own function using the keyword def (right, derived from define). Let's have a look at the syntax:

def function_name(parameter1, parameter2, ...):
    # function's body
    ...
    return "return value"

After def, we write the name of our function (so as to invoke it later) and the names of parameters, which our function can accept, enclosed in parentheses. Do not miss the colon at the end of the line. The names of a function and its parameters follow the same convention as variable names, that is, they should be written in lowercase with underscores between words.

An indent of 4 spaces shows the interpreter where the function's body starts and where it ends. All statements in the function's body must be indented. You can make calculations inside your function and use the return keyword to send the result back. Only when the indentation is absent, the definition of the function ends.

Later, the parameters take on values passed in a function call. Those values we pass to a function are known as arguments. The only distinction between parameters and arguments is that we introduce parameters in a function definition and give arguments (some specific values) in a function call. Here is a bit less abstract example of a function:

# Function definition
def multiply(x, y):
    return x * y


# Function calls
a = multiply(3, 5)   # 15
b = multiply(a, 10)  # 150

In case you don't want to pass any arguments, the round brackets remain empty:

def welcome():
    print("Hello, people!")

You can also declare a sort of empty function with pass statement:

# This function does nothing (yet)
def lazy_func(param):
    pass

When you choose to call lazy_func() with an arbitrary value as its argument, nothing will happen. So pass is just a placeholder, but at least your code will be valid with it.
Parameters vs arguments

It's not quite clear right now, what the parameters are, is it? In fact, parameters are just aliases for values, which can be passed to a function. Consider the following example:

def send_postcard(address, message):
    print("Sending a postcard to", address)
    print("With the message:", message)


send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

send_postcard("Piccadilly, London", "Hi, London!")
# Sending a postcard to Piccadilly, London
# With the message: Hi, London!

As you can see, this function is a reusable piece of code, that can be executed with different arguments, i.e. different values passed into this function. Here, address and message are just the aliases under which the function receives values and then processes them in the body.

This function takes exactly 2 arguments, so you will not be able to execute it with more or less than 2 arguments:

send_postcard("Big Ben, London")

TypeError: send_postcard() missing 1 required positional argument: 'message'

Execution and return

Our previous function only performed some actions, but it didn't have any return value. However, you might want to calculate something in a function and return the result at some point. Check the following example:

def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# Convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp)  # 212.0

The keyword return is used to indicate what values the function outputs. Basically, it is the result of the function call. So, in the example above, we've stored the value returned by our function in the variable water_bp. Just to be sure, we printed the result.

One more thing to say is that functions do not necessarily have return values. The well-known print() function does not, in fact, return anything. Examine the code below:

chant = print("We Will Rock You")
print(chant)

And its output:

We Will Rock You
None

We declared the variable chant and invoked print(). Obviously, the function was executed. But the variable itself turned out to be the None object, which means the called function had nothing to return. The value of chant is None.

Python interpreter stops performing the function after return. But what if the function body contains more than one return statement? Then the execution will end after the first one. Please, keep that in mind!

Conclusion

Thus, we've learned the syntax for declaring functions. Now you also know that:

    Parameters of a function are simply aliases, or placeholders, for values that you will pass to them. Parameters are re-initialized every time you call the function. Inside the function, you have access to these values, which means you can perform calculations on them.
    A function can simply perform an action without returning anything or return a specific result. If your function doesn't return anything, assigning its result to a variable or printing it will give you None.

Declaring your own functions makes your code more structured and reusable. Whenever you use the same piece of code more than once, try to create a function of it!
...........................
Theory: Scopes

A scope is a part of the program where a certain variable can be reached by its name. The scope is a very important concept in programming because it defines the visibility of a name within the code block.
Global vs. Local

When you define a variable it becomes either global or local. If a variable is defined at the top-level of the module it is considered global. That means that you can refer to this variable from every code block in your program. Global variables can be useful when you need to share state information or some configuration between different functions. For example, you can store the name of a current user in a global variable and then use it where needed. It makes your code easier to change: in order to set a new user name you will only have to change a single variable.

Local variables are created when you define them in the body of a function. So its name can only be resolved inside the current function's scope. It lets you avoid issues with side-effects that may happen when using global variables.

Consider the example to see the difference between global and local variables:

phrase = "Let it be"

def global_printer():
    print(phrase)  # we can use phrase because it's a global variable

global_printer()  # Let it be is printed
print(phrase)  # we can also print it directly

phrase = "Hey Jude"

global_printer()  # Hey Jude is now printed because we changed the value of phrase

def printer():
    local_phrase = "Yesterday"
    print(local_phrase)  # local_phrase is a local variable

printer()  # Yesterday is printed as expected

print(local_phrase)  # NameError is raised

Thus, a global variable can be accessed both from the top-level of the module and the function's body. On the other hand, a local variable is only visible inside the nearest scope and cannot be accessed from the outside.
LEGB rule

A variable resolution in Python follows the LEGB rule. That means that the interpreter looks for a name in the following order:

    Locals. Variables defined within the function body and not declared global.
    Enclosing. Names of the local scope in all enclosing functions from inner to outer.
    Globals. Names defined at the top-level of a module or declared global with a global keyword.
    Built-in. Any built-in name in Python.

Let's consider an example to illustrate the LEGB rule:

x = "global"
def outer():
    x = "outer local"
    def inner():
        x = "inner local"
        def func():
            x = "func local"
            print(x)
        func()
    inner()

outer()  # "func local"

When the print() function inside the func() is called the interpreter needs to resolve the name x. It'll first look at the innermost variables and will search for the local definition of x in func() function. In the case of the code above, the interpreter will find the local x in func() successfully and print its value, 'func local'. But what if there isn't a definition of x in func()? Then, the interpreter will move outward and turn to inner() function. Check out the following example:

x = "global"
def outer():
    x = "outer local"
    def inner():
        x = "inner local"
        def func():
            print(x)
            ............................
        func()
    inner()

outer()  # "inner local"

As you see, the name x was resolved in inner() function, since the value "inner local" was printed.

If we remove the definition of x from the inner() function as well and run the code again, the interpreter will continue the search among the outer() locals in the same fashion. If we keep deleting the lines of code defining x, the interpreter will move on to outer() locals, then globals, and then built-in names. In case there is no matching built-in name, an error will be raised. Look at the example where the global definition of x is reached by the interpreter:

x = "global"
def outer():
    def inner():
        def func():
            print(x)
        func()
    inner()

outer()  # "global"

Don't forget about LEGB rule if you plan on using enclosing functions.
Keywords "nonlocal" and "global"

We already mentioned one way to assign a global variable: make a definition at the top-level of a module. But there is also a special keyword global that allows us to declare a variable global inside a function's body.

You can't change the value of a global variable inside the function without using the global keyword:

x = 1
def print_global():
    print(x)

print_global()  # 1

def modify_global():
    print(x)
    x = x + 1

modify_global()  # UnboundLocalError

An error is raised because we are trying to assign to a local variable x the expression that contains x and the interpreter can't find this variable in a local scope. To fix this error, we need to declare x global:

x = 1
def global_func():
    global x
    print(x)
    x = x + 1

global_func()  # 1
global_func()  # 2
global_func()  # 3

When x is global you can increment its value inside the function.

nonlocal keyword lets us assign to variables in the outer (but not global) scope:

def func():
    x = 1
    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

def nonlocal_func():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

func()  # inner: 2
        # outer: 1

nonlocal_func()  # inner: 2
                 # outer: 2

Though global and nonlocal are present in the language, they are not often used in practice, because these keywords make programs less predictable and harder to understand.
Why do we need scopes?

First of all, why does Python need the distinction between global and local scope? Well, from the experience of some other programming languages that do not have local scopes it became clear, that using only global scope is highly inconvenient: when every variable is accessible from every part of the code, a whole bunch of bugs is inevitable. The longer the code, the more difficult it becomes to remember all the variables' names and not accidentally change the value of the variable that you were supposed to keep untouched. Therefore, Python saves you the trouble by allowing you to "isolate" some variables from the rest of the code when you split it into functions.

On the other hand, why do we need global scope then? Well, as was already mentioned above, global scope is one of the easiest ways to retain information between function calls: while local variables disappear the moment the function returns, global variables remain and help functions to transfer the necessary data between each other. Similarly, global variables can enable the communication between more complex processes, such as threads in multithreaded applications.
............................
Theory: Else statement
Simple if-else

An if-else statement is another type of conditional expressions in Python. It differs from an if statement by the presence of the additional keyword else. The block of code that else contains executes when the condition of your if statement does not hold (the Boolean value is False). Since an else statement is an alternative for an if statement, only one block of code can be executed. Also, else doesn't require any condition:

if today == "holiday":
    print("Lucky you!")
else:
    print("Keep your chin up, then.")

Note that the 4-space indentation rule applies here too.

As you may soon find out, programmers do like all sorts of shortcuts. For conditional expressions there's a trick as well – you can write an if-else statement in one line. This is called a ternary operator and looks like this:

print("It’s a day now!" if sun else "It’s a night for sure!")

Or, more generally:

first_alternative if condition else second_alternative

It's a matter of convenience, but remember that the code you create should still be readable.
Nested if-else

It should be mentioned, that if-else statements can be nested the same way as if statements. An additional conditional expression may appear after the if section as well as after the else section. Once again, don't forget to indent properly:

if x < 100:
    print('x < 100')
else:
    if x == 100:
        print('x = 100')
    else:
        print('x > 100')
    print('This will be printed only because x >= 100')

Now you are ready not only to set conditions but also to consider different alternatives. Congratulations!
............................
Theory: Elif statement

Since you are familiar with basic conditional statements, such as if statement and if-else statement, it’s time for the more advanced elif statement.

Elif statement is used when we want to specify several conditions in our code. How does it differ from if-else statements? Well, it's simple. Here we add the elif keyword for our additional conditions. It is mostly used with both if and else operators and the basic syntax looks like this:

# basic elif syntax
if condition1:
    action1
elif condition2:
    action2
else:
    action3

The condition is followed by a colon, just like with the if-else statements, then desired action is placed within the elif body and don't forget about an indentation, i.e., 4 spaces at the beginning of a new line. Here we first check the condition1 in the if statement and if it holds (the value of the Boolean expression is True), action1 is performed. If it is False, we skip action1 and then check the condition2 in the elif statement. Again, if condition2 is True, action2 is performed, otherwise, we skip it and go to the else part of the code.

Let's take a look at the example below:

# elif example
price = 10000 # there should be some int value
if price > 5000:
    print("That's too expensive!")
elif price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")

To buy or not to buy? To answer the question we first check if the price is higher than 5000. If ‘price > 5000’ is True, we print that it’s too expensive and set off, looking for something cheaper. But what if the price was less than 5000? In this case, we check the next condition is ‘price > 500’, and again, if it is True, we print out that we can afford that, and if it is False, we go to the else block and print that it's too cheap. So “I can afford it!” will be printed if the price is less than 5000 but more than 500, and “That’s too cheap” if the price is lower than 500.

Elif statement differs from else in one key moment: it represents another specific option while else fits all cases that don't fall into the condition given in if statement. That's why sometimes you may encounter conditional statements without else:

pet = 'cat'  # or 'dog'?

# cats vs dogs conditional
if pet == 'cat':
    print('Oh, you are a cat person. Meow!')
elif pet == 'dog':
    print('Oh, you are a dog person. Woof!')

In this example, it's possible to add an else statement to slightly expand a perspective, but it's not necessary if we are only interested in dogs and cats.
Why elif and not if?

The last example probably made you wonder: why did we use elif statement instead of just two ifstatements? Wouldn't two if statements be easier?

if pet == 'cat':
    print('Oh, you are a cat person. Meow!')
if pet == 'dog':
    print('Oh, you are a dog person. Woof!')

In this particular case, the result would be the same as with elif. But this wouldn't work as needed for the first example of this topic:

price = 6000
if price > 5000:
    print("That's too expensive!")
if price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")
# The output is 'That's too expensive!\nI can afford that!'

See? We got two contradicting messages instead of one that we originally intended to output. The difference between the above examples is that in the example with pets, the cases described by conditional statements are mutually exclusive, that is, there's no string that would be equal both to 'dog' and 'cat' at the same. In the other example, the cases aren't mutually exclusive, and there are values for price that can satisfy both conditions.

So, elif statement is a better alternative than two if statements when you want to show that only one of the conditions is supposed to be satisfied. A chain of if statements implies that the conditions stated in them are totally unrelated and can be satisfied independently of each other, like in the following example:

animal = 'unicorn'
if animal in 'crow, dog, frog, pony':
    print('This animal exists')
if animal in 'unicorn, pegasus, pony':
    print('This animal is a horse')

With this distinction in mind, you'll be able to make your code more clear and less error-prone. Now, let's get back to studying elif functionality.
Multiple elifs and a decision tree

There can be as many elif statements as you need, so your conditions can be very detailed. No matter, how many elif statements you have, the syntax is always the same. The only difference is that we add more elifs:

# multiple elifs syntax
if condition1:
    action1
elif condition2:
    action2
# here you can add as many elifs as you need
elif conditionN:
    actionN
else:
    actionN1

The code inside the else block is executed only if all conditions before it are False. See the following example:

# multiple elifs example
light = "red"  # there can be any other color
if light == "green":
    print("You can go!")
elif light == "yellow":
    print("Get ready!")
elif light == "red":
    print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")

In this program, the message from the else block is printed for the light of any color except green, yellow and red for which we’ve written special messages.

Conditionals with multiple branches make a decision tree, in which a node is a Boolean expression and branches are marked with either True or False. The branch marked as True leads to the action that has to be executed, and the False branch leads to the next condition. The picture below shows such a decision tree of our example with traffic lights.

Nested elif statements

Elif statements can also be nested, just like if-else statements. We can rewrite our example of traffic lights with nested conditionals:

# nested elifs example
traffic_lights = "green, yellow, red"
# a string with one color
light = "purple"  # variable for color name
if light in traffic_lights:
    if light == "green":
        print("You can go!")
    elif light == "yellow":
        print("Get ready!")
    else:
        # if the lights are red
        print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")

Since you have mastered the topic of conditionals, from now on you can make your program do what you want when you want it!
............................
Theory: Functional decomposition

At this point, you already know how to declare functions in Python. This is a very useful skill, no doubt about that, but to make the most of it, we need to know when to declare them. In this topic, we'll see how to decompose the solution of a particular problem into functions.
Real-life example

Before we go to the actual decomposing, let's figure out what it is that we want to decompose.

Suppose, we are writing a program that simulates an ATM. How do real-life ATMs work? Well, usually a client inserts the card, enters the pin, and, if the pin is correct, performs some operations, for example, withdraws money or deposits money to an account. We can reimagine these actions as parts of a computer program. This is how the algorithm can be described in general:

    Parse the input data (card and entered pin);
    Check that the pin is correct;
    Ask the client what they want to do;
    If the operation is supported, perform it.

Before we program this algorithm, let's settle a few things. Obviously, a real bank has a database that stores all necessary data, like the encrypted correct pin or the current card balance. Here we are creating a very simple version of an ATM, so we're not going to include database checkups. Instead, we will define variables card_pin and card_balance. These variables will represent the correct pin and card balance that we would've gotten from a database.

We also need to determine which operations we'll allow. Let's settle on three: displaying the card balance, adding money to the account and withdrawing money from the account.

Now let's see the code:

# operations
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
DISPLAY = "DISPLAY"

# read the data
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database

# check that the pin is correct
if card_pin == input_pin:
    # ask the client what they want to do
    action = input("Enter desired action: ")
    if action == DEPOSIT:
        money = float(input("Enter the sum of money to DEPOSIT: "))
        card_balance += money
        print("Deposited: $", money)
        print("Current balance:", card_balance)
    elif action == WITHDRAW:
        money = float(input("Enter the sum of money to WITHDRAW: "))
        card_balance -= money
        print("Withdrawn: $", money)
        print("Current balance:", card_balance)
    elif action == DISPLAY:
        print("Current balance:", card_balance)
    else:
        ...
else:
    print("Incorrect pin!")

As you can see, a lot is going on and it's a bit hard to follow. The main logic is the same we've described above. This code works perfectly fine for our problem and we could leave it like that.

However, what if we want this script to work for many users and not just one? What if we want to process other cases and perform other actions, for instance, check if the card is in the database or change the pin? Some parts of this code will be useful, other parts we'll have to comment or delete. We would also need to track all places where we're introducing changes to make sure that everything runs smoothly. Now it starts to sound like we may have a problem with our code. The solution, as you may have guessed, is decomposition.
Functional decomposition

Functional decomposition is simply a process of decomposing the problem into several functions. Each function does a particular task and we can perform these functions in a row to get the results we need.

When we look at a problem, we need to think about which actions we may want to repeat multiple times or, alternatively, perform separately. This is how we can get the desired functions. Let's look at our ATM simulation again and figure out which steps can be turned into separate functions.

First, an action that we do frequently is reading the input with a particular message displayed. Second, we perform a certain sequence of actions when the pin is correct, specifically we ask what we should do next. Third, depending on the answer from the client, we either perform certain actions to deposit the sum to the account or withdraw them from the account. And lastly, whatever the action, we always print out the current balance.

Some of these actions can be converted to separate functions to make the program simpler.

Let's go over them step by step. First, let's separate our main operations into functions.

def deposit_money(amount, card_balance):
    """Deposit given amount of money to the account."""
    card_balance += amount
    # save new balance to the database
    return card_balance


def withdraw_money(amount, card_balance):
    """Withdraw given amount of money from the account."""
    card_balance -= amount
    # save new balance to the database
    return card_balance

You may have noticed that in the original program we print the current balance regardless of what we've done before. This means that we can also create a separate function that would log everything.

def log_transaction(action, money, card_balance):
    if action in (DEPOSIT, WITHDRAW):
        print(action + ": $", money)
    print("Current balance:", card_balance)

This function is going to be called after we've done something and it will display information about the current balance and the changes that have been made.

Next, it makes sense to create a function that would manage these operations:

def move_money(action, money, card_balance):
    if action == DEPOSIT:
        return deposit_money(money, card_balance)
    elif action == WITHDRAW:
        return withdraw_money(money, card_balance)
    elif action == DISPLAY:
        return card_balance

You can see that this function returns the card balance that we get after our manipulations. This is helpful because, as we've seen before, we always want to know how much money we end up with. The main purpose of this function, however, is to simplify the process of revising the functionality of our program. If we want to add some other action, we just add another option to the if - else statement and specify the function that would carry out this task. Removing is similar.

One important part that we haven't covered yet is getting the information about the money we'll be moving somewhere. We know that we don't need this information for display, but it is necessary for other operations.

def get_amount_of_money(action):
    if action == DISPLAY:
        return 0.0
    money = input("Enter the sum of money to " + action + ": ")
    return float(money)

At this moment, we only have bits and pieces of our final program. Another important step is creating a function that would put it all together.

def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transaction(action, money, card_balance)

This is when the main logic takes place. We have a single entry point that determines the order of operations and calls necessary functions.
The result

Now, let's rewrite the program above using these functions:

card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database

if card_pin == input_pin:
    action = input("Enter desired action: ")
    make_transaction(action, card_balance)
else:
    print("Incorrect pin!")

That's it! Sure, together with the functions, the code is much bigger, but this provides us with more advantages than disadvantages. We can understand the general direction of the program and can easily introduce changes if needed. Now, for example, if we want to add another action, we just need to define its function and modify the move_money function. We can also easily test separate components since they are determined in separate functions. All in all, our program now is a real functioning program that won't fall apart when we decide to change it a bit.
Summary

In this topic, we've covered the concept of functional decomposition, dividing the process into several functions.

Among other things, decomposing allows us to:

    structure code better;
    see the general logic of the program;
    introduce changes easily;
    test separate functions.

Obviously, functional decomposition is not a universal solution. However, if you can think of your problem in terms of a sequence of some functions, it can be of great help to you!
............................
Theory: Load module
Module basics

While working on simple examples you probably type your code directly into the interpreter. But every time you quit from the interpreter and start it again you lose all the definitions you made before. So as you start writing larger programs it makes sense to prepare your code in advance using a text editor and then run it with the interpreter. A file containing a list of operations that further are read and interpreted is called script.

You also may want to write some functions and then use them in other programs or even reuse code someone else wrote before. One way is just to copy the code into your program, but it soon leads to code that is bad-structured and hard to read. Luckily, there is another way in Python to organize and reuse code called modules.

The module is simply a file that contains Python statements and definitions. It usually has a .py extension. What really makes the module system powerful is the ability to load or import one module from another.
Module loading

To load a module just use an import statement. In a basic form, it has the following syntax import module.

import super_module

super_module.super_function()  # calling a function defined in super_module

print(super_module.super_variable)  # accessing a variable defined in super_module

super_module is the name of the module you want to import. For example, a file called super_module.py has a name super_module. In order to be available for import, super_module.py should be located in the same directory as the file you are trying to import it from. At first, Python importing system looks for a module in the current directory, then it checks the built-in modules, and if nothing is found an error will be raised. After importing, the module becomes available under its name and you can access functions and variables defined in it using the dot notation.

It's also common to only import required functions or variables from a module but not the module itself. You can do this by using a from form of import statement.

from super_module import super_function

super_function()  # super_function is now available directly at the current module

super_module.super_function()  # note, that in this case name super_module is not imported,
                               # so this line leads to an error

A good practice is to load a single module in a single line and put all your imports at the top of the file because it increases readability.

import module1
import module2
import module3

# the rest of module code goes here

A special form of import statement allows you to load all the names defined in a module. It is called wildcard import and has syntax from module import *. You should generally avoid this in your code. It can cause unexpected behavior because you don't know what names exactly are imported into the current namespace. Besides, these names may shadow some of the existing ones without your knowledge. It's better to make it explicit and specify what you're importing.

In case you have to use several import statements, pay attention to their order:

    standard library imports
    third party dependency imports
    local application imports

Having your imports grouped, you may put a blank line between import sections. Also, some guidelines, including ours, recommend sorting imports alphabetically.
Built-in modules

Python comes with a great standard library. It contains a lot of built-in modules that provide useful functions and data structures. Another advantage is that the standard library is available on every system that has Python installed. Here you can find an official library reference.

Python has a math module that provides access to mathematical functions.

import math

print(math.factorial(5))  # prints the value of 5!

print(math.log(10))  # prints the natural logarithm of 10

print(math.pi)  # math also contains several constants
print(math.e)

string module contains common string operations and constants.

from string import digits

print(digits)  # prints all the digit symbols

random module provides functions that let you make a random choice.

from random import choice

print(choice(['red', 'green', 'yellow']))  # print a random item from the list

....................
Theory: Create module
Module design

Basically, a module is just a file that has a .py extension and contains statements and definitions. What is the point? Well, modules help you organize and reuse code. Once you wrote a module you can load it from the interpreter or another module.

A simple module that is written for direct execution is often called a script. The difference between a module and a script in Python is only in the way they are used. Modules are loaded from other modules or scripts and scripts are executed directly.

Let's take a look at the example of a simple script below:

# hello.py script

print("Hello, World!")

You have already seen this example but now we want to turn it into a script. What you need to do is simple: you just save this code in a file named hello.py and then run it with Python. To run a script use python <script>, where <script> is the path to your Python file.

~$ python hello.py
Hello, World!

Congratulations! This is your first script in Python.
Module importing

A module can be loaded from another module. That allows you to write a piece of code once and then use it wherever you want. It is really helpful when you work on larger projects and want to separate concerns between different modules. We already saw examples of an imported module from another module in the previous topic.

When working in the interactive mode of the interpreter you can load modules as well. Pay attention, that the module should be placed in the directory from which you run Python. For example, you can load hello.py file we discussed in the previous section from the interpreter like this:

~$ python
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import hello
Hello, World!

Common mistakes

Now it is time to cover some common mistakes you can make when defining or importing modules.

If you accidentally import a module from itself, the code of the module will be executed twice and that is generally not something you want to happen.

# itself.py

import itself

print("Hello, it's me!")

The output looks like this:

Hello, it's me!
Hello, it's me!

So be careful and avoid situations when you import a module from itself.

Another common mistake is name shadowing. For example, you have created a local module that has the same name as some built-in module. In this case, you won't be able to import anything from the original module, because the import system will search names in your custom module.

Imagine, you created a module socket.py and then you try to import some function from the standard Python socket module within your module.

# socket.py

from socket import socket

print("All cool!")

You'll see an error message that says that Python cannot import socket from socket module:

...

ImportError: cannot import name 'socket'

One way to avoid this is not to name your files the same as the built-in modules you might use. Just suffix _script to the name of your scripts and modules and you will be safe from this name shadowing problem.

Whenever the module is imported it is fully executed and then added to your current namespace. Even special forms of import statement such as from module import something don't affect that fact. This may become a problem in situations when you want to be able to both import your module and execute it as a script.

Consider the example:

# unsafe_module.py

name = "George"

print("Hello,", name)

If you define another script and import name from unsafe_module you'll see Hello, George printed.

# unsafe_bye.py script

from unsafe_module import name

print("Bye,", name)

The output:

Hello, George
Bye, George

To solve this issue you can simply divide your file into two: one containing only definitions, another containing the code that imports definitions from the first file and uses them. But it's also common to use the __main__ pattern.
__main__ pattern

Let's learn another option of how to make your script safe to import. We will change the unsafe_module.py file from the previous section.

# safe_module.py

name = "George"

if __name__ == "__main__":
    print("Hello,", name)

The name of the module is always available in the built-in variable __name__. When you are executing a script __name__ has a value "__main__". So here we check the value of __name__ and print the line only if the module is executed as a script.

# safe_bye.py script

from safe_module import name

print("Bye,", name)

The output is the following:

Bye, George

In general, if you have more than just one line to execute in a script it's convenient to move all that code into a function called main and then call it like that:

# safe_main_module.py

name = "George"

def main():
    print("Hello,", name)

if __name__ == "__main__":
    main()

Note, that the naming itself doesn't affect the way a function is executed, it's just a convention to indicate that this function is run only when the file is used like a script.
............
Theory: Packages
Package definition and structure

When our code is becoming bigger, it becomes very difficult to maintain and keep track of all the modules included. In order to make the code more organized, we can resort to packages. A package is a way of structuring modules hierarchically with the help of the so-called "dotted module names". Thus the module name sun.moon designates a submodule named "moon" in a package named "sun".

The possible structure might be the following:

package/                           # first we name the main or top-level package
            __init__.py            # this directory should be treated as a package
            subpackage/            # we can add subpackage with extra modules
                  __init__.py      # this directory should be treated as a subpackage
                   artificial.py
                   amateurs.py
                   ...
            subpackage2/
                  __init__.py
                  amazing.py
                  animate.py
                  barriers.py
                  ...

NB: it’s necessary to create __init__.py files, that will make Python treat the directory as a package/subpackage. They can be empty or execute the initialization code for the package.
Importing and referencing packages

Let us suppose we’d like to import a specific module from the package. There are two ways to import the "artificial" submodule from the subpackage:

from package.subpackage import artificial

This method allows to use the submodule content without naming the package and subpackage:

artificial.function(arg1, arg2)

The second method is more straightforward:

import package.subpackage.artificial

After we’ve loaded the submodule in such a way, its content should be referenced with its full name:

package.subpackage.artificial.function(arg1, arg2)

Besides, it’s possible to import a particular function from the submodule:

from package.subpackage.artificial import function

After that, you can address the function() directly, without specifying the full path to a module.

The method of importing modules depends on your current program and needs. The main rule is readability!
Import * from …: advantages and disadvantages

You can also use from package.subpackage import *. This code will import all the submodules that your subpackage has, although you might not really need that. Moreover, it will be really time-consuming and considered to be a bad practice. How can we manage these side-effects?

The major thing to do is to provide the package with a particular index with the help of __all__ statement that should be inserted into __init__.py file. There you want to list the submodules to be imported while from package import * operation is executed.

__all__ = ["submodule1", "submodule10"]

Intra package references

Python is even more powerful than you could imagine: if you have a need, you can refer to submodules of siblings packages. For instance, if you use the package.subpackage1.artificial and there you need something from package.subpackage2.amazing, you can import it by from package.subpackage2 import amazing in the artificial.py file.

You can also carry out the so-called "relative imports" that use leading dots to indicate the current and parent packages involved. Thereby, for "amateurs" you can use the following:

from . import artificial    # one dot means addressing to a current package/subpackage

from .. import subpackage2  # two dots mean addressing to a parent package/subpackage

from ..subpackage2 import module

PEP Time!

Using wildcard imports (from <module> import *) is considered bad practice, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools.

Absolute imports are recommended, as they are usually more readable. They also give better error messages if something goes wrong:

import package.subpackage.amateurs
from package.mypackage import amateurs

Explicit relative imports are also acceptable, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:

from . import animate           # in amazing.py, for example
from .barriers import function  # in animate.py, for example

Standard library code should avoid complex package layouts and always use absolute imports.
Conclusion

    Using packages is a very good way to structure your code.

    Packages make your project simpler to perceive. They allow reusing code more easily.
    Different ways of importing have their own advantages and disadvantages. Remember one of the main rules of Python: readability counts!

............................
Theory: Class

As you already know, object-oriented programming (OOP) is a programming paradigm that is based on the concept of objects. Objects interact with each other and that is how the program functions. Objects have states and behaviors. Many objects can have similar characteristics and if you need to work with them in your program it may be easier to create a class for similar objects. Classes represent the common structure of similar objects: their data and their behavior.
Declaring classes

Classes are declared with a keyword class and the name of the class:

# class syntax
class MyClass:
    var = ...  # some variable

    def do_smt(self):
    # some method

Generally, class name starts with a capital letter and it is usually a noun or a noun phrase. The names of the classes follow the CapWords convention: meaning that if it's a phrase, all words in the phrase are capitalized and written without underscores between them.

# good class name
class MyClass:
    ...

# not so good class name:
class My_class:
    ...

Classes allow you to define the data and the behaviors of similar objects. The behavior is described by methods. A method is similar to a function in that it is a block of code that has a name and performs a certain action. Methods, however, are not independent since they are defined within a class. Data within classes are stored in the attributes (variables) and there are two kinds of them: class attributes and instance attributes. The difference between those two will be explained below.
Class attribute

A class attribute is an attribute shared by all instances of the class. Let's consider the class Book as an example:

# Book class
class Book:
    material = "paper"
    cover = "paperback"
    all_books = []

This class has a string variable material with the value "paper", a string variable cover with the value "paperback" and an empty list as an attribute all_books. All those variables are class attributes and they can be accessed using the dot notation with the name of the class:

Book.material  # "paper"
Book.cover  # "paperback"
Book.all_books  # []

Class attributes are defined within the class but outside of any methods. Their value is the same for all instances of that class so you could consider them as the sort of "default" values for all objects.

As for the instance variables, they store the data unique to each object of the class. They are defined within the class methods, notably, within the __init__ method. In this topic, we'll deal with the class attributes, but don't worry you'll have plenty of time to learn more about instance attributes.
Class instance

Now, let's create an instance of a Book class. For that we would need to execute this code:

# Book instance
my_book = Book()

Here we not only created an instance of a Book class but also assigned it to the variable my_book. The syntax of instantiating a class object resembles the function notation: after the class name, we write parentheses.

Our my_book object has access to the contents of the class Book: its attributes and methods.

print(my_book.material)  # "paper"
print(my_book.cover)  # "paperback"
print(my_book.all_books)  # []

Summary

Well, those were the very basics of classes in Python. Classes represent the common structure of similar objects, their attributes, and methods. There are class attributes and instance attributes. Class attributes are common to all instances of the class.

All in all, classes are an extremely useful tool that can help you optimize your code and organize the program in a logical and readable way. We hope you'll make use of them!
............................
Theory: Class instances

By now, you already know what classes are and how they're created and used in Python. Now let's get into the details about class instances.

A class instance is an object of the class. If, for example, there was a class River, we could create such instances as Volga, Seine, and Nile. They would all have the same structure and share all class attributes defined within the class River.

However, initially, all instances of the class would be identical to one another. Most of the time that is not what we want. To customize the initial state of an instance, the __init__ method is used.
def __init__()

The __init__ method is a constructor. Constructors are a concept from the object-oriented programming. A class can have one and only one constructor. If __init__ is defined within a class, it is automatically invoked when we create a new class instance. Take our class River as an example:

class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)

volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.name)
# Output:
# Volga
# Seine
# Nile

We created three instances (or objects) of the class River: volga, seine, and nile. Since we defined name and length parameters for the __init__, they must be explicitly passed when creating new instances. So something like volga = River() would cause an error.

The __init__ method specifies what attributes we want the instances of our class to have from the very beginning. In our example, they are name and length.
self

You may have noticed that our __init__ method had another argument besides name and length: self. The self argument represents a particular instance of the class and allows us to access its attributes and methods. In the example with __init__, we basically create attributes for the particular instance and assign the values of method arguments to them. It is important to use the self parameter inside the method if we want to save the values of the instance for the later use.

Most of the time we also need to write the self parameter in other methods because when the method is called the first argument that is passed to the method is the object itself. Let's add a method to our River class and see how it works. The syntax of the methods is not of importance at the moment, just pay attention to the use of the self:

class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))

Now if we call this method with the objects we've created we will get this:

volga.get_info()
# The length of the Volga is 3530 km
seine.get_info()
# The length of the Seine is 776 km
nile.get_info()
# The length of the Nile is 6852 km

As you can see, for each object the get_info() method printed its particular values and that was possible because we used the self keyword in the method.

Note that when we actually call an object's method we don't write the self argument in the brackets. The self parameter (that represents a particular instance of the class) is passed to the instance method implicitly when it is called. So there are actually two ways to call an instance method: self.method() or class.method(self). In our example it would look like this:

# self.method()
volga.get_info()
# The length of the Volga is 3530 km

# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km

Instance attributes

Classes in Python have two types of attributes: class attributes and instance attributes. You should already know what class attributes are so here we'll focus on the instance attributes. Instance attributes are defined within methods and they store instance-specific information.

In the class River, the attributes name and length are instance attributes since they are defined within a method (__init__) and have self before them. Usually, instance attributes are created within the __init__ method since it's the constructor, but you can define instance attributes in other methods as well. However, it's not recommended so we advise you to stick to the __init__.

Instance attributes are available only from the scope of the object which is why this code will produce a mistake:

print(River.name)  # AttributeError

Instance attributes, naturally, are used to distinguish objects: their values are different for different instances.

volga.name  # "Volga"
seine.name  # "Seine"
nile.name   # "Nile"

So when deciding which attributes to choose in your program, you should first decide whether you want it to store values unique to each object of the class or, on the contrary, the ones shared by all instances.
Summary

In this topic, you've learned about class instances.

If classes are an abstraction, a template for similar objects, a class instance is a sort of example of that class, a particular object that follows the structure outlined in the class. In your program, you can create as many objects of your class as you need.

To create objects with different initial states, classes have a constructor __init__ that allows us to define necessary parameters. Reference to a particular instance within methods is done through the self keyword. Within the __init__ method, we define instance attributes that are different for all instances.

Most of the time in our programs we'll deal not with the classes directly, but rather with their instances, so knowing how to create them and work with them is very important!
......................
Theory: Methods and attributes

Now that you've learned how to create instance methods let's go even further and learn to use the methods for creating and modifying attributes.
Creating attributes with methods

Instance attributes are the ones defined within methods so by definition we can create new attributes inside our custom methods. Let's take the class Ship as an example.

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

Every ship needs a captain so let's define a method called name_captain for those purposes:

class Ship:
    # constructor
    # ...

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))

When called for the first time, the name_captain method creates a new attribute called captain and prints the corresponding message. When used next, it just changes the value of the self.captain attribute (and prints the message as well).

To see how it would work, let's create the ship "Black Pearl":

black_pearl = Ship("Black Pearl", 800)

If we tried to print the value of the captain attribute now, we would get an error:

print(black_pearl.captain)  # AttributeError

This is because this attribute is only created within the name_captain method. If we call it, we will be able to access the attribute captain:

black_pearl.name_captain("Jack Sparrow")
# prints "Jack Sparrow is the captain of the Black Pearl"

print(black_pearl.captain)  # "Jack Sparrow"

Note that only those instances that have called this method, will have the captain attribute. It's an important thing to remember! You may get an error if you try to use the attribute and the method hasn't been called yet.

To avoid these problems, it is recommended to define all possible attributes in the __init__. This can not only help you avoid AttributeError, but also give a good understanding of the class and its objects from the get-go. If you do want to create the value for the attribute in a special instance method, then list it in the __init__ as None:

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

Then, in the specific method, you simply modify the default value which is what we'll consider in the next section.
Modifying attributes with methods

Methods can also be used to modify the instance attributes. Take the methods load_cargo and unload_cargo for example:

class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")

Both these methods are supposed to change the value of the attribute cargo if those changes are possible. The load_cargo method first checks that the loading of a particular weight will not exceed the capacity of the ship and the unload_cargo checks that the unloading will not make the weight of the cargo negative. Then they both make the changes or print a message that those changes are impossible.

# example
black_pearl.load_cargo(600)
# "Loaded 600 tons"

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"

black_pearl.load_cargo(700)
# "Cannot load that much"

black_pearl.unload_cargo(300)
# "Cannot unload that much"

If we wanted to print out the value of cargo after all these manipulations, we would see that it would equal 200 (tons). Because of the restrictions that we placed, only the first callings of load_cargo and unload_cargo made changes to the attribute cargo.

So far our methods haven't been returning any values since we only used the print() function, but we can make our methods return any type of value that we want. For example, let's create a method that calculates how much more cargo can our ship load.

class Ship:
    # all other methods

    def free_space(self):
        return self.capacity - self.cargo

If we were to call this method on our Black Pearl we wouldn't get any messages, because the method doesn't print anything. But instead, we could use the value it returns in our further calculations. We could, for instance, rewrite the load_cargo method by using thefree_space method:

class Ship:
    # updated load_cargo method
    def load_cargo(self, weight):
        if weight <= self.free_space():
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

In this example, we called a method inside another method and used the values in our calculations. Again, we used self to make sure that we only deal with the particular instance of the class Ship and that all calculations concern this instance.
Summary

In this topic, we focused on more advanced uses of instance methods in Python.

Methods can be used for creating new attributes and modifying existing ones. You can call methods inside other methods, use the results for calculations or just output messages. Knowing how methods and attributes interact can help you expand the functionality of your classes and make your programs very efficient.

We hope that you'll experiment with instance methods and use them in your projects!
.........................
Theory: Magic methods

There are different ways to enrich the functionality of your classes in Python. One of them is creating custom methods which you've already learned about. Another way, the one that we'll cover in this topic, is using "magic" methods.
What are "magic" methods?

Magic methods are special methods that make using your objects much easier. They are recognizable in the code of the class definitions because they are enclosed in double underscores: __init__ , for example, is one of those "magic" methods in Python. Since they are characterized by double underscores they are often called dunders.

Dunders are not meant to be invoked directly by you or the user of your class, it happens internally on a certain action. For example, we do not explicitly call the __init__ method when we create a new object of the class, but instead, this method is invoked internally. All we need to do is to define the method inside the class in a way that makes sense for our project.

There are many different dunders that you can use, but in this topic, we will focus on the most helpful ones.
__new__ vs __init__

So far we've been calling __init__ the constructor of the class, but in reality, it is its initializer. New objects of the class are in fact created by the __new__ method that in its turn calls the __init__ method.

The first argument of the __new__ method is cls. It represents the class itself, similar to how self represents an instance of the class. This also makes __new__ a different kind of method since it doesn't require an instance of the class. This makes sense since it is supposed to create those instances. The method returns a new instance of the class which is then passed to the __init__ method.

Usually, there is no need to define a special __new__ method, but it can be useful if we want to return instances of other classes or restrict the number of objects in our class.

Imagine, for example, that we want to create a class Sun and make sure that we create only one object of this class. We would need to define a class variable that would track the number of instances in the class and forbid the creation of new ones if the limit has been reached.

class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0:
            cls.n += 1
            return object.__new__(cls)  # create new object of the class

The code above may be a bit unexpected so let's analyze it. We first check that the class variable n has a value of zero. If it does, it means that no instances of the class have been created and we can do that. We then update the class variable and call __new__ method of object class which allows us to create a new instance.

If we now try to create 2 objects of this class we will not succeed:

sun1 = Sun()
sun2 = Sun()

print(sun1)  # <__main__.Sun object at 0x1106884a8>
print(sun2)  # None

__str__ vs __repr__

Printing out information and data is very important when programming. You can print the results of calculations for yourself or the user of your program, find the mistakes in the code or print out messages.

For example, let's consider the class Transaction:

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

If we create a transaction and try to print it out we will not get what we want:

payment = Transaction("000001", 9999.999)
print(payment)
# example of the output: <__main__.Transaction object at 0x11068f5f8>

Instead of the values that we would like to see, we get information about the object itself. This can be altered if we deal with __str__ or __repr__ methods.

As the names suggest, __str__ defines the behavior of the str() function and __repr__ defines the repr() function. A general rule with the __str__ and __repr__ methods is that the output of the __str__ should be highly readable and the output of the __repr__ should be unambiguous. In other words, __str__ creates a representation for users and __repr__ creates a representation for developers and debuggers. If possible, __repr__ should return Python code that could be used to create this object or, at least, a comprehensive description.

Both __repr__ and __str__ should return a string object!

A good rule is to always define the __repr__ method first since it is the method used by developers in debugging. It is also a fallback method for __str__which means that if the __str__ method isn't defined, in the situations where it's needed, the __repr__ will be called instead. This is, for example, the case with print().

In our example here, let's create the __repr__ method that would create an unambiguous representation of the transaction and all its attributes.

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

Now if we try to print any transaction we will get a standard readable string:

payment = Transaction("000001", 9999.999)
print(payment)
# Transaction(000001, 9999.999)

You can see that we've called print and got the representation from __repr__. Now let's add __str__ and see if things change.

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

    def __str__(self):
        return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)


payment = Transaction("000001", 9999.999)
print(payment)
# Transaction 000001 for 9999.999 (active)
print(repr(payment))
# Transaction(000001, 9999.999)

Now that we have __str__, when we call print, we get the representation defined there. To see the "official" representation we need to directly call the repr function.
Summary

Magic methods are said to add "magic" to your classes and that is somewhat true. Dunders really make working with classes much easier and far more efficient.

In this topic, we've covered only a couple of these magic methods. We highly encourage you to look them up (for example, in "A Guide to Python's Magic Methods" by Rafe Kettler) and try them out in your projects. As for the magic methods for arithmetics and comparisons, we'll look into them in another topic!
.....................................
Theory: Inheritance

One of the main principles of object-oriented programming is inheritance. In this topic, we'll focus on inheritance in Python: what it means and how it's done.

What is inheritance?
Inheritance is a mechanism that allows classes to inherit methods or properties from other classes. Or, in other words, inheritance is a mechanism of deriving new classes from existing ones.

The purpose of inheritance is to reuse existing code. Often, objects of one class may resemble objects of another class, so instead of rewriting the same methods and attributes, we can make it so that a class inherits those methods and attributes from another class.

When we talk about inheritance, the terminology resembles biological inheritance: we have child classes (or subclasses, derived classes) that inherit methods or variables from parent classes (or base classes, superclasses). Child classes can also redefine methods of the parent class if necessary.
Class object

Inheritance is very easy to implement in your programs. Any class can be a parent class, so all we need to do is to write in the definition of the child class the name of the parent class in parentheses after the child class:

# inheritance syntax
class ChildClass(ParentClass):
    # methods and attributes
    ...

The definition of the parent class should precede the definition of the child class, otherwise, you'll get a NameError! If a class has several subclasses, its definition should precede them all. The "sibling" classes can be defined in any order.

When we don't define a parent for our class, it doesn't mean that it doesn't have any! By default, all classes have the class object as their parent. In Python 3.x we don't need to explicitly indicate that, so the definitions below are equivalent:

# parent class is explicit
class SomeClass(object):
    # methods and attributes
    ...


# parent class is implicit
class SomeClass:
    # methods and attributes
    ...

Subclasses of object inherit its methods and attributes. So, all standard methods like __init__ or __repr__ are inherited from the class object. If we don't redefine those methods for our custom classes, we end up using their implementations defined for the object.
Single inheritance

Unlike some other programming languages, Python supports two forms of inheritance: single and multiple. Single inheritance is when a child class inherits from one parent class. Multiple inheritance is when a child class inherits from multiple parent classes. In this topic, we'll cover only single inheritance. Don't worry, though, you'll have a chance to learn about multiple inheritance in the next topics!

Let's consider an example of single inheritance.

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

# child class
class Dog(Animal):
    pass

Here we have a base class Animal with the __init__ method and a subclass Dog that inherits from the base class. The keyword pass allows us not to write anything in the definition of the child class.

Now that we've defined classes, we can create objects:

cow = Animal("Bessie")  # instance of Animal
corgi = Dog("Baxter")   # instance of Dog

We haven't defined the __init__ for the class Dog but since it's a child of Animal, it inherited its __init__. So if we tried to declare an instance of the class Dog in a different way, we would get an error:

labrador = Dog()  # TypeError

type() vs isinstance()

There are two main ways to check the type of an object: type() or isinstance() functions.

The type() function takes one argument, an object, and returns its type. The isinstance() function takes two arguments: an object and a class. It checks if the given object is an instance of the given class and returns a boolean value.

For built-in types, they work the same, but when inheritance is involved, their results are different. Let's check it out!

First, let's look at the type() function:

print(type(cow) == Animal)  # True
print(type(corgi) == Animal)  # False

print(type(cow) == Dog)     # False
print(type(corgi) == Dog)     # True

As you can see, this allows us to check for the immediate type of the object. Now, isinstance() works differently:

print(isinstance(cow, Animal))    # True
print(isinstance(corgi, Animal))  # True

print(isinstance(cow, Dog))    # False
print(isinstance(corgi, Dog))  # True

With this, we get True not only with the immediate type but also with the parent type and even with the parent of the parent type! This distinction is important to remember for future projects!
issubclass()

While isinstance() checks the type of an instance of a class, another built-in function asks whether a given class is a subclass of another class:

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False

print(issubclass(Dog, Dog))     # True
print(issubclass(corgi, Dog))   # TypeError

As shown, the issubclass() function returns True if the first class inherits from the second class, and False otherwise. Each class is considered a subclass of itself. Notice that the function can't work with instances of a class, both its arguments should be classes. However, you can use a tuple of classes to check if your class inherits from several parents.

print(issubclass(Dog, object))            # True
print(issubclass(Dog, (Animal, object)))  # True

The case with several classes might be somewhat misleading, though. The thing is that the function checks whether any element of the tuple is a parent. Say, we have defined a new class Robot:

class Robot:
    pass

Then issubclass() will return the following:

print(issubclass(Dog, Robot))            # False
print(issubclass(Dog, (Robot, Animal)))  # True

Even though Dog has nothing to do with Robot, in the last case, we got True. So keep this detail in mind when calling this function!
Summary

As one of the pillars of OOP, inheritance is very important! In Python, declaring parent classes is quite simple and straightforward. In this topic, we've covered the basics of the inheritance in Python: how it's done, what is class object, how to define a single parent for the class, and then check the type of an object or a class without any mistakes.

Inheritance is what really makes classes so powerful and useful. It also allows programmers to stick to the DRY (Don't Repeat Yourself) principle and pushes them to think about the effectiveness and clarity of their classes.
............................
Theory: Introduction to operating systems

How can it be that there are thousands of different computer models but they all can run the same programs? Have you ever thought about how the programs interact with the hardware? These and other features are made possible by the operating systems.
Operating system

An operating system (OS) is a set of software that manages communication between all other applications and hardware. It turns a computer into something more than just a bunch of metal parts, a complex system that can effectively perform different tasks.

Nowadays, there exist a lot of operating systems for you to choose from. For personal computers, the most popular ones are Microsoft Windows, macOS, and Linux distributions. The two top mobile operating systems are Android and iOS. If you've ever heard of smart kettles and smart fridges, even they have their own OS.

Of course, the operating systems for such a range of devices differ greatly from one another. What they have in common are the means they provide to the programs and those who use them.

On the one hand, it's only an illusion that your favorite browser is the same on Windows as it is on macOS. On the other hand, you can run the same application on different computers with the same OS.

Functions of the OS

An operating system controls the communication between all the computer software and hardware. An OS can give programs restricted access to processor units, memory, hard drives, network, peripherals, and other resources.

You can run a browser, a media player, and ten other applications, and your OS is the one giving them all the resources they need to run properly. At the same time, this OS acts as a fair referee prohibiting any application to take up more resources than it actually needs.

As a mediator between the applications and hardware, the operating system allows us to communicate with the device without going into details about its specificity or mechanics.

Any operating system has several essential functions. Here is a list of some of them:

    data protection and secure access;
    resource management;
    interaction between hardware and peripherals;
    file management;
    running other programs.

It is possible to distinguish more functions of modern operating systems, but those listed above are enough for starters.
Operating systems' components

A mandatory part of all operating systems, its core, is the kernel. Usually, it's one of the first programs that load when you turn on your computer. It provides all the necessary means to run the programs you want.

Typically, when you start your OS, you see the Graphical User Interface (GUI). It is the type of interface that allows users to interact with the device using graphical icons and audio indicators. Another way to interact with the OS is to use commands in a text-based terminal known as Command Line Interface (CLI).

There are two types of kernels, known as monolithic kernel and microkernel. The monolithic kernel is a large program that performs most of the OS functions. At the same time, the microkernel performs only a small subset of the operating system functions, but we can extend it with additional modules known as drivers.

There are other important parts of the operating system besides the kernel and the graphical user interface. We will review them in the next topic. For now, use the following image to brush up everything we've covered so far:

Conclusion

The operating system efficiently distributes the resources of the computer in a way we've described above. It is important to understand that without the operating system, it would not be possible to use the computer.

Now you know about the main functions of the operating systems and their essential elements. Let's test what you've learned so far!
........................................
Theory: Datetime module
datetime module

Often, in our projects, we need to work with dates and time. For example, we may want to track the current date and time or see how long our code runs. For these purposes, we can use the datetime module.

The datetime module has several classes that make working with time easy:

    datetime.date represents standard date;
    datetime.time represents standard time, independent from the date;
    datetime.timedelta represents the difference between two points in time;
    datetime.tzinfo represents timezones;
    datetime.datetime represents both time and date together.

In this topic, we'll focus on the datetime.datetime class.
datetime.datetime

The datetime.datetime class is a sort of combination of the date and time classes. Similarly to those two, it assumes the current Gregorian calendar and that there are exactly 86 400 seconds in each day.

The constructor of the datetime.datetime objects takes the following parameters:

import datetime

# necessary parameters
datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

The year, month and day parameters are required, others are optional. All arguments (except tzinfo) should be integers and just like in real life, their values are restricted:

    datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999);
    1 ≤ month ≤ 12;
    1 ≤ day ≤ number of days in this month and year;
    0 ≤ hour < 24;
    0 ≤ minute < 60;
    0 ≤ second < 60;
    0 ≤ microsecond < 1000000.

The tzinfo argument can be an instance of the datetime.tzinfo class, but its default value is None, so we don't need to worry about it here.

To see how this all works, let's create a datetime.datetime object. For example, the date and time of the first flight to space which took place on April 12, 1961, at 6:07 UTC:

import datetime

vostok_1 = datetime.datetime(1961, 4, 12, 6, 7)
print(vostok_1)  # 1961-04-12 06:07:00

datetime methods

The datetime.datetime class has several very handy methods.

If you need to get the current time and date, there are two methods you can use: datetime.datetime.today() and datetime.datetime.now(tz=None). They are very similar and the only difference between these two methods is that datetime.datetime.now() has a keyword argument tz. If you don't specify it, the two methods work the same. However, in some cases or on some platforms, the datetime.datetime.now() method may be more precise.

This is an example of how they perform:

print(datetime.datetime.now())  # 2019-09-12 17:18:23.620734
print(datetime.datetime.today())  # 2019-09-12 17:18:23.625716

You can also transform a datetime.datetime object to a datetime.time or datetime.date objects using datetime.datetime.time() or datetime.datetime.date() methods respectively:

print(vostok_1.time())  # 06:07:00
print(vostok_1.date())  # 1961-04-12

Those were just a couple of methods available in the datetime.datetime class. There are many more: the ones that deal with timestamps or timezones or the ones that help parse and convert datetime objects. Don't worry, you'll have a chance to work with them in the next topics!
Report a typo
..............................
Theory: Pip

One astonishing fact about Python is that it has a huge and diverse community of contributors. Essentially, that means that there are plenty of solutions to a significantly vast range of problems in open access. This fact comes in handy, especially when you are working on your own projects. It's highly likely that you'll be able to find a proper task-specific package and use it effectively to meet your needs. Now we are going to learn about standard tools for package management in Python.
What is pip

By this time you've probably familiarized yourself with the Python standard library. It contains a lot of useful built-in modules and should be preinstalled with your Python distribution. In fact, one more thing that is preinstalled (starting with Python 3.4) is the standard package manager called pip (the acronym is commonly expanded as "Pip Installs Packages").

Pip is designed both to extend the functionality of the standard library by installing the additional packages on your computer and to help you share your own projects and thereby contribute to the development of Python.

Now let's make sure that you have pip installed. All you need to do is open a command prompt/terminal and run this line:

pip --version

The output should report your current pip version. For example, the latest version is:

pip 20.0.2

In case it's not installed (or you want to upgrade it), please follow these installation instructions specifically for your operating system.

If your terminal cannot find the pip command, try to use pip3 instead.

Pip capabilities

Since pip is the recommended installer for Python, the most obvious and crucial command to begin with is install. Have a look at the following line:

pip install some_package

The installation is really that simple. However, if you are interested in a certain version of the package, you need to specify it after the package name like this:

pip install some_package==1.1.2

Or, at least, define a minimal suitable version:

pip install "some_package>=1.1.2"

Note that the last expression should be enclosed within double quotes for the comparison operator to be interpreted without any problem.

Another useful thing is the show command. It shows information about installed packages, for instance, their version, author, license, location or requirements. Here is a general example:

pip show some_package

Also, the list command might be of use. It lists all the packages you've installed on your computer in alphabetical order:

pip list

If you print the list command with the option --outdated, or just -o, you'll get the list of outdated packages coupled with both the current and latest versions available.

pip list --outdated

or with a bit shorter variant:

pip list -o

After executing one of the mentioned lines, you will see a similar output:

first_package (Current: 2.1.1 Latest: 3.0.1)
second_package (Current: 4.2.1 Latest: 4.2.2)

Having discovered outdated packages, you might want to update them to the newest available version:

pip install --upgrade some_package

To remove a package from your computer run the uninstall command:

pip uninstall some_package

When developing your project, it may be advantageous to keep a list of packages to be installed, i.e. dependencies, in a special file (see Requirements File Format). It is convenient because you can install the packages directly from it:

pip install -r requirements.txt

Of course, you are not supposed to write this file yourself listing all the necessary packages. It will be enough to run the code below in order to obtain it:

pip freeze > requirements.txt

Let's examine the line above in detail. freeze is a command used to get all installed packages in the format of requirements. So all the packages you had installed before the execution of the command and presumably had used in some projects would be listed in the file named "requirements.txt". Furthermore, their exact versions would be specified (see Requirement Specifiers).

Consider an example output of the freeze command:

beautifulsoup4==4.7.1
nltk==3.4.1
numpy==1.16.3
scikit-learn==0.21.1
scipy==1.3.0

What's important is that freeze actually lists all the installed libraries, which is rarely necessary and might be considered a bad practice. For this reason, we recommend that you take a more conscious approach and revise the obtained requirements file by yourself.
Recap

On the whole, we've learned the basics for package installation through pip:

    how to install packages (either a specific version or non-specific one),
    how to create a requirements file and use it for installation,
    how to obtain information about installed packages,
    and, finally, how to uninstall packages.

For further details, try consulting the documentation or running the command help.

Now let's get to practice so that you can use all this information in the future!
Report a typo
...................................................
Theory: Introduction to Django

Django is one of the most-used Python frameworks in web programming. When you are browsing through boards on Pinterest, reviewing code on Bitbucket, or making comments with the help of Disqus, you are using Django products. You can find out about more well-known services that use Django on this page.

The name of the framework is inspired by the stage name of a famous jazz guitarist Django Reinhardt, so the developers who created many handy add-ons for the framework call their group Jazzband. At first, you won’t need all of the tools, but whenever you need more, you can find them at this Github account.

Django framework provides an API for templating HTML pages, making connections to databases, and using HTTP backend services. Django has many useful web development shortcuts and utilities in one place. To start working with the framework, choose the version you'll use. For Django in its A.B.C version, A.B stands for a feature release and C for a patch release. When choosing an appropriate version, pay attention to its feature release number. When you're done choosing, download the latest patch release for this version. To get the most of Django, start with the latest version.

The first stable release of Django was issued in 2008. The first Long-Term Support (LTS) release with version 1.4 came four years later, in 2012.
LTS

LTS is a well-known standard in software development. It means that developers will support this version of the framework for an extended period of time (for Django, it's usually 3 years or more). You can safely update your version to a newer patch release without fear of breaking compatibility with the source code. For this period, all bugs and security losses will be fixed as soon as possible. Conversely, non-LTS versions are supported only until a newer feature release comes out (note that Django developers support the last two feature releases at a time).

For example, the LTS version 1.11 is supported until April 2020, but the later, non-LTS version 2.0 is already not supported by the developing team.

In this course, we will use the latest LTS release of Django as of April 2019, version 2.2.

Surely you can't wait to finally install Django and get to work. There are two ways to install the package: you can install it globally, which is simpler, or get it in a Python virtualenv.
Global Installation

To install Django, you need a Python package manager pip. Django is no different from any other Python package, so if you want to install it on your system, run:

pip install Django==2.2

To use the framework, you will probably need a database. For the sake of simplicity, you can install SQLite unless it's already present on your system.
Installation in Virtual Environment

To isolate your development environment from other Python packages on your computer, you need to create and activate Python virtualenv. Then install the framework to keep it separate:

# If you don't have virtualenv yet
pip install virtualenv

# Unix
python -m venv hyperskill-django
source hyperskill-django/bin/activate
pip install Django==2.2

# Windows
python -m venv hyperskill-django
hyperskill-django\Scripts\activate
pip install Django==2.2

# If you want to deactivate a virtual environment
deactivate

A virtual environment is also helpful if you want to keep different versions of a package on your system. You can install each one of them in separate virtualenv. Thus if you already have the older version of Django, you can try out the new one with virtualenv.
Check Installation

After you've installed Django, you'll get django-admin command in your shell (if you've installed Django in a virtual environment, do not forget to activate it). Django-admin is a helper that can create a template layout for a new project or add an application to an existing project. You can do this manually, but it's much easier to use django-admin for this purpose.

Now you only need to check the version of the installed package:

django-admin version
# 2.2

It means that your installation was successful and you can start using Django! You've got the basic essentials to create your first project, so good luck!
..............................
Theory: Django MVC
MVC Paradigm

Complex software products have their own architecture. Though each example is unique, usually they all contain common design patterns. Patterns are repeatable and rather language-independent structures, so getting familiar with just one of them means understanding a whole bunch of applications that share it. It is basically a general language to express ideas, and Model-View-Controller (MVC) is one particularly useful pattern to learn, since many popular frameworks like Django (Python), Spring (Java), and Ruby On Rails (Ruby) are using it.

The main idea of MVC is dividing responsibilities between three components. The Model part contains business objects, the View represents the application and the Controller manages data flow between two of them. The advantage of this design pattern is that we can create different views from the same models, so we write less code by reusing the existing parts. Distinguishing one component from another is the main principle to be guided by.

Each component has its associated files in the default Django layout.

Let's say that we are creating an online magazine. The folder "magazine" is the root of your site and the inner folder "blog" is one of the applications. You can link the components with those files:

magazine/
├── blog
    ├── ...
    ├── models.py    # Model
    └── views.py     # Controller
├── magazine
    ├── ...
    └── urls.py      # Controller
└── templates        # View

Let's take a closer look at the files that you will need in order to make a web service.
Starting a New Project

For this example, we will use "magazine" for a project and "blog" for an application. If you want to get creative and use other names, feel free to change the given ones in the code.

The Django project is the root of all code you are writing for the service, and it should have at least one application. To isolate units of code with different business logic, you can create more of them. For example, the magazine project can have the blog, authors, forum, and support applications.

With time the codebase becomes large, dividing it into applications helps to control the complexity.

The django-admin utility helps organize the layout of your project. You may create all these files manually, but using django-admin will be a good guide to the common structure of a project for you. Note that different versions of Django have different default layouts, and whichever version you use, try to stick to its provided structure: it will make your code easier to maintain.

To create a project and the first application, run the following in the command line:

django-admin startproject magazine
cd magazine
django-admin startapp blog

Having executed these commands, you'll get a whole file tree for the project with a piece of code. Now let's get down to using our MVC pattern.
Model

magazine/
└── blog
    └── models.py

It's nice to have the same content for all users, but if we want to customize it a bit, we need tools from Python interface.

The Model component includes all the database operations with the business objects in your project. A business object is an entity with custom attributes; it reflects a structured piece of data from your application which you want to store persistently or temporarily. For example, in a shop application, it can be a customer, a product and a purchase; in a blog, business objects can be authors, posts and comments.

To keep your code clear, you should implement all operations with the business objects in the "models.py" module. The bigger the codebase gets, the harder it is to maintain everything in one file, but it's a good starting point.

You may use User and Group models from django.contrib.auth.models: Django provides them from the box. The User is a registered person in your web service and the Group is a collection of Users. We'll create some of those when we attach a database to your project.
View

magazine/
├── blog
    └── templates
        └── blog
            └── index.html
└── templates
    └── base.html

No one will know what the service does unless it has some form of visual rendition. The View is a representation of your web service. Simply put, it is what the user sees.

The View component is stored in templates. Templates are files that support Django/Jinja2 template languages. Besides, they can include content with HTML, CSS, and JavaScript. Template language utilizes the ability to use similar constructs you use in Python. It's has a different syntax but the same function words.

To create "templates" directory for the project and for the application, run:

# Unix
mkdir templates
mkdir -p blog/templates/blog

# Windows
mkdir templates
mkdir blog\templates\blog

In the project folder you keep base files for all other templates, applications folder contains only application-specific templates.

When you create "templates" directory for your application, you should name it "<application name>/templates/<application name>". This redundancy is obligatory. If you use the same file name without the second repetition of <application name>, like "blog/templates/index.html" and "news/templates/index.html", then in both cases Django template loader will return the first file it found, which isn't always what the user actually needs.
Controller

magazine/
├── blog
     └── views.py
└── magazine
      └── urls.py

Views and models are good instruments, but something should manage how they work together, which is where we turn to the Controller part.

The Controller consists of two types of files: "views.py" and "urls.py". In "urls.py", you define the routing for your service. Routing is a process of matching request links with appropriate view handlers. You can include routes from "urls.py" files one into another, but the main will be "<project_name>/<project_name>/urls.py". If you want to create routing files for each application, do it and include them in the main one.

In "views.py" you define view handlers, which play a mediator role between the Model and the View. A view handler is a function or a class that responds to requests. Since communication between client and server is an implementation of the HTTP protocol, handler answers with a status code. If the request was successful, the server typically responds with 200 code. In case the requested page is not found, it will be 404; if the server is down, it's 500. Other examples of codes can be found at https://httpstatuses.com/.
Request to the Web Site

Now that you know how functions are divided between the components, let's see how they interact when there's a web site request.

1. A user sees a link or a button in a View, presses it and creates a request.
2. The Controller receives the request.
3. It passes the request to the appropriate handler.
4. The handler calls Model methods to retrieve objects from data storage.
5. It chooses the View template to render a response.
6. A user sees a response.

Each part has its own methods and base classes in the Django package. You should separate the work with each component as Django developers do: this way other developers will understand your code and you will understand theirs.
.......................
Theory: Django ORM

Working With a Database From Python
Chances are, the storage you most often work with is a file system. It works well for HTML pages and templates, but how do you keep small objects like login, age or, say, favorite color for each individual person? Relational databases can help you organize and manipulate such data.

We will start from scratch and learn how to work with databases using only Python.

We define models to describe the schema of our data. To convert Python objects and primitives to database types, we will use adaptor classes, Fields. These abstractions help us pay less attention to the database specifics and focus mainly on what to store and how.

Once we declare the models and the fields in them, we create migrations and apply them to the SQLite3 database. Feel free to change it to another database backend. No matter which database you choose, our code will remain valid.
Relational Databases

If your first thought is "I need to keep the data with a common structure", then your second thought should surely be "databases".

A relational database is a collection of multiple data sets organized by tables, records, and columns. It works fine for most types of data. Each implementation provides you the universal language called structured query language (SQL). You can read about it, but as we say, we will work with the database in another way.

The most popular databases are PostgreSQL, Oracle SQL, MS SQL, and MySQL. There is also a simple database that works on your smartphone in many applications: it's called SQLite. It's perfect for one-client use and trying out Django models for the first time. Check whether you have it on your computer:

sqlite3 --version

If you don't, try to install it with your package manager or download it from the official site.
Object-Relational Mapping

With the fall approaching and clouds getting denser, the new season of Quidditch is starting. As you know, wizards really lack computer science classes in Hogwarts, even though programming is a kind of magic. They want to store the teams, their results and the rosters on the website, and they wonder if there is a way to do to it with Django. Well, there sure is! For this purpose, we will make the quidditch project with the tournament app in it. Let's meet and greet Django Models!

Django Models are classes that map the objects from the real world to the database records. We have teams, so we call our model the Team. This approach is called Object-Relational Mapping(ORM).

The ORM is a concept to map one type system to the other. We will work with databases by means of Python classes and methods. Our strong side is the programming language and we are going to make the most of it. The objects are similar to database records and their methods resemble SQL commands. There's no need to know SQL directly as we apply the instruments that imitate it.

To tell Django that it's a special class which maps its structure to the database table, we inherit the Team from django.models.Model. Also, we have players and game tables. Let's make the stubs for our classes in tournament/models.py module:

from django.db import models


class Team(models.Model):
    name = ...


class Player(models.Model):
    height= ...
    name = ...
    team = ...


class Game(models.Model):
    date = ...
    home_team = ...
    home_team_points = ...
    rival_team = ...
    rival_team_points = ...

We gave names to our classes and described their content. The restriction of all relational databases is that we should define the types for all the fields in the Model. So how can we match the types with the fields?
Fields

To get most of the database's features, we use special Fields classes. They map the attribute of the class to a particular column in the database table. Does it mean we need the instance of a class for each field? Yes, but don't worry, it's actually easier than it may seem.

To build the whole schema, we start from the core element, the Team:

class Team(models.Model):
    name = models.CharField(max_length=64)

CharField is similar to Python string but has one restriction: the length limit. "Wigtown Wanderers" is the longest team name in the league now, but the league is still open to new teams, so we ensure max_length with 64 symbols.

Each team has players. Let's define a model for a player:

class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

We already know what the CharField means, so the FloatField should sound familiar to you, too. It's the same as Python's float type. What's more interesting is the ForeignKey field. It means that the player is bound to a specific Team and the restriction on_delete=models.CASCADE means that if the Team is deleted from the database, it will be erased with all the players. That sounds unfair, but you should try harder to stay in the league!

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

There are no games without teams, so again we set on_delete=models.CASCADE for each ForeignKey. Also, we add the related_name for the Game model, by which we can access it from the Team model. It's necessary to add such names because we have two foreign keys to the Team and you should differ one from another.

Points is an int type, so we make it IntegerField, and the date is clearly a DateField.

You can think of Fields as expansions of Python's primitive types for simple cases like IntegerField, CharField, and FloatField. They also have special cases like ForeignKey and other relations between objects.
Migrations

At this point, we describe the mappings between Python classes and database tables, but we don't have any tables yet. That's sad news. Should we learn some fancy SQL to create a database and tables in it? No, because we can simply describe to Django what we want and it will do the dirty work for us — again.

Add tournament to INSTALLED_APPS in the quidditch/settings.py module:

INSTALLED_APPS = [
    # other installed apps
    'tournament',
]

We have the schema of the league in our code, we are ready to migrate it to the database. It takes two steps:

python manage.py makemigrations
python manage.py migrate

The first command creates migrations. Migration is a piece of code that describes what actions should be done in the database to synchronize the models with the tables. You can find the created code in the tournament/migrations/0001_initital.py file.

In the second step, we apply the changes and run the generated commands.

Preceding manage.py <command> with python is the platform-independent way to launch any django command. It's a valid syntax for both Unix and Windows systems.

If you want to make and then apply migrations to a particular application in your project, you should add the application name after each command:

python manage.py makemigrations tournament
python manage.py migrate tournament

When you run these commands, your database will finally have the tables to work with. We are ready to fill them with real data!
........................

Project: HyperJob Agency
54 / 54 Prerequisites
Stage 1
Description

The "HyperJob" recruitment agency is a very conservative one. Its history starts on January 1st, 1970 . The managers in the agency prefer communicating by phone or email and searching for employees personally. That was an efficient strategy some ten years ago, but now the candidates prefer to apply for jobs online. The problem is that "HyperJob" still doesn't have a site, so they need you to create the service as soon as possible.

We start with a simple site that will be suitable for:

    Creating a new vacancy by the agency's manager
    Creating a new resume by a candidate

We know that it will be a long road, so at each stage you will make only a small part of work. By the end, we'll have a working site that fulfills all the requirements.
Objectives

Your first task is to prepare the models for the data. It's important to keep all the data safe. We need to store all the vacancies and resumes persistently in the database. Create models to manage the database tables.

Use the default settings of the project with a predefined SQLite database.

Throughout the project, we will need at least two models: Vacancy and Resume. Both of them should have the description and author fields. The description is a text field with no more than 1024 symbols, and the author is a foreign key to django.contrib.auth.models.User model.

Define Vacancy and Resume in models.py module and migrate them to the database. We check your work this time, so that at the next steps you are confident enough to add new models by yourself.
Report a typo
Write a program

    Code Editor
    IDE

IDE is responding PyCharm 2020.2.1
EduTools plugin is responding 4.0-2020.2-799
Wrong, but keep on trying and never give up!
FEEDBACK

Wrong answer in test #2

no such table: vacancy_vacancy

..............................
Theory: Polymorphism

With the object-oriented paradigm, it's as if we are working with real-life objects in our code. We choose simple names for classes and methods, so anyone who speaks English can catch up with what's actually happening in the code. Sometimes methods just slightly differ from one another but do we have to create myriads of specializations for our objects with methods DO_SMTH_WITH_OBJECT_A, DO_SMTH_WITH_OBJECT_B, etc...? Of course, we should distinguish them, but with the help of polymorphism, we can do it rather smoothly.
4 sections left Expand all
bod some missing here***
............................
Theory: Immutability

In philosophy, there is a thought experiment called "Ship of Theseus". It is one of the oldest concepts in Western philosophy and it goes like this.

The famous ship of the hero Theseus has been kept as a museum piece in a harbor. Over the years, the wooden parts have rotted and been replaced. A hundred years later, all of the wooden parts of the ship have been replaced. The question is: is it still the same ship?

There are many ways to answer this question and you can check them out on Wikipedia. What is of interest to us is that this question of identity can be applied to programming as well. One of the most important concepts in programming, the one directly connected to change and identity, is the concept of (im)mutability.
Mutability and immutability

Mutability literally means "the quality of being changeable" and, in programming, it refers to the idea of changing the state of the object after it has been created.

Along this line, we can distinguish between mutable and immutable objects. To put it simply, mutable objects can be altered once they've been created and immutable cannot. This is the key difference between mutable and immutable objects.

What does this mean in practice? Immutable objects always represent the same value: if you want to have a different value, you need to create a completely new object or reassign the value of the existing one. With mutable objects, things are much easier and we can change the values they contain without reassigning the variable or creating a new object.

Returning to the ship of Theseus, if we were to consider it an immutable object, then the answer to the question of identity would be no. Once you change something, you have a different object. In other words, the ship of Theseus is no longer the ship of Theseus even though it has the same name!

Alternatively, if we regard the ship as a mutable object, then, yes, it is still the same ship. The changes that we made did not affect its identity.

Depending on the programming language you're using, different types of objects may be immutable. For instance, strings are immutable in Python and Java, but Java also has another type for strings which is mutable. In Ruby and PHP strings are mutable. When writing a program in your favorite language, you need to take into account which objects are mutable and which are immutable in that particular language.
Custom objects and immutability

In general, objects of custom classes are mutable. However, there are cases when we would want to make them immutable: immutable objects are thread-safe, easier to test and they may be more secure.

Immutable objects can be shared between different threads without additional protection. The state of mutable objects is hard to follow as long as they can be changed by any of the working threads.

In the context of custom objects, we can also talk about weak immutability and strong immutability. Weak immutability is when some fields of an object are immutable and others are mutable. Strong immutability is when all fields of an object are immutable.

Specific instructions on how to make a custom class immutable depend on the language, but we can give general guidelines. Basically, you need to forbid changing the value of the field once it has been created or forbid reassigning the value. This can be done, for example, by making the variable read-only or a constant. Another option is to modify the methods that set attribute values so that they throw exceptions. You can also work with access modifiers: make the fields unattainable from the outside of the class.
Summary

To sum up, the difference between mutable and immutable objects lies in the fact that mutable objects can change their states after creation and immutable objects cannot. Languages have their own division into mutable and immutable objects. Custom classes are usually mutable but can be made immutable using language-specific tools and techniques if necessary.
Report a typo
...................................
Theory: Bugs and debugging
What is a bug?

A software bug is a problem that causes a program to crash or produce invalid output. There are many reasons for software bugs; most common of them are human mistakes in software design, coding or understanding of the requirements.

A program is usually called stable if it doesn't have a lot of obvious bugs. If the program has a large number of bugs that affect the functionality and cause incorrect results, it is considered buggy or unstable. A user cannot successfully interact with such software. It is important to find bugs before users start interacting with your program.
Bug etymology

You've probably already heard the term "bug" and can imagine what it means. Here is a little story about this.

The first computer bug was discovered by Grace Murray at Harvard University in 1947, while she was working on Mark II computer. During the investigation of an issue, an actual moth was found between the contact of the relays. The moth was removed and added to the logbook, which now is located at the Smithsonian Institution's National Museum of American History in Washington, D.C.

So, computer errors are often called bugs. This term is used to describe any incorrect program behavior until the specific nature of the error is determined.

Some Internet sources give a different story of this term. You can google it if you are interested. Let us know if you find a story most reliable to you.

Why do programs have bugs?

Developers often say that a program without bugs doesn't exist. There are some common reasons for bugs in software:

    communication issues in the team;
    misunderstanding of the requirements;
    software complexity;
    programming errors (programmers, like anyone else, can make mistakes);
    time pressure;
    use of unfamiliar technologies;
    an error in a third-party library (yes, that happens too).

During this course, you will mainly encounter bugs caused by misunderstanding of the given requirements or programming errors.
Avoiding bugs

It is almost impossible to avoid all bugs in a large program, but it is possible to reduce their number. Here we give you five steps that can help to do that in both educational courses and industrial programming.

    Make sure you know what to do. As a programmer, you need to understand the requirements of a program that you are going to work on. If you have doubts, you can always find some help on the Internet or among fellow developers.
    Decompose a program into small units that are easy to look through and understand. A good architecture reduces software complexity, and, as a consequence, the number of errors.
    Write easy-to-read-code and follow all the standards of the language. It will also allow you to make fewer errors.
    Run the program with boundary input values. Do not forget to consider different cases: 0 or a huge number as an input value, 0 or 1 element as an input sequence. Such cases often reveal bugs.
    Write automated tests that will check the program at the build time.

We will not discuss automated tests in this topic, but we will return to that later. At this moment, you can simply create a set of input values and run the program manually (as it was described in step 4).
Debugging

Suppose you know that your program does not work correctly for some input values. To fix this bug, you need to find it in the code and then make some changes.

To locate a buggy place, you can:

    read the code and try to understand what it does for the input values;
    start the debugger and see the current values of variables and the control flow of the program;
    print the current state of the program in critical parts of the code (logging) and then analyze it.

The combination of the approaches above will allow you to find most of the bugs in your program.
Report a typo
....................
Theory: HTTP messages

The HTTP protocol relies on the "client-server" architecture that is built on the basis of messaging. HTTP messages are a way to exchange data between clients and servers in the Web. There are two types of messages: requests and responses.

A request is an operation that a client wants to perform on the server, and a response is an answer from the server to an incoming request. Usually, programmers do not need to worry about creating HTTP messages since they are produced by browsers, applications, and web servers.
The format of messages

In the HTTP protocol, all messages consist of text strings. Both requests and responses have roughly the same standardized format:

    Start line which may vary:
        for requests, it indicates the type of request (method) and the URL where to send it (target);
        for responses, it contains a status code to determine the success of the operation.
    Headers which describe the message and convey various parameters.
    Body in which the message data is located.

The start line and the header are required attributes, so the other parts may be empty.

The full format can be quite complicated for beginners, so we have considered only its part which is the most important for understanding the general principles.
The simplified HTTP interaction

Here is a simplified HTTP interaction between a browser client and a server. The client and the server interact through requests and responses which follow the studied format:

Note that there are other possible types of client programs, not just a browser. You can even write your own HTTP client and interact with servers. The only requirement is that such a program should always follow the message format.

Methods

HTTP defines a set of request methods that specify what the desired action will be for a given resource. Despite the fact that their names can be nouns, these query methods are sometimes referred to as HTTP verbs.

Let's look at the most commonly used query methods:

    GET method is only used to retrieve data from the server;
    POST method is used to send data to the server;
    HEAD requests data from the server in the same way as the GET method, but without a response body.

Every time you click on a link, you basically communicate to your browser that you want to GET this page. When you want to log in to your favorite site, you POST your login and password to receive access to it.

There are more available verbs to learn. You don't need to memorize them all right now.
Status codes

For normal operation of computer programs and web pages that work via HTTP, except for the content of the page, the server returns a three-digit code, which specifies the response request. With the help of this code, it is possible to redirect the client to another site or to indicate the change of the page, as well as to detect an error in data processing.

Currently, the standards define five classes of status codes:
1xx: Informational 	Codes beginning with "1" are called information codes. They report on how client requests are processed.
2xx: Success 	Messages of this class inform that the action requested by the client has been successfully accepted for processing.
3xx: Redirection 	It means further action must be taken in order to complete the request.
4xx: Client Error 	It reports errors on the client's side.
5xx: Server Error 	The code indicates that the operation was unsuccessful due to the fault of the server.

As an example, if you have successfully loaded a website, the response you received has code 200.

You have also probably been in a situation where your browser displays the "404 Not Found" message when you input the address of a page that does not exist. This is how these failure messages usually look:

Browsers display error messages so that users can understand that something has gone wrong, rather than continuing to look at the blank page while waiting for the content to be downloaded.

Now, when you've finished reading the topic, you can visit various sites in a browser and understand how your actions look like from the technical point of view.
Report a typo
....................
Theory: HTML page structure

Programming is not as mechanical and alien as it may seem: in many respects, it is similar to the human world. This is very easy to notice if you look at the structure of HTML pages, which contains elements like <head> and <body>. Making a site is thus a process of creation, and as a creator, you need to be familiar with all the necessary building blocks. There is a lot to learn, but any lot starts with the essential basics: please welcome on stage, HTML tags.
Basic tags in HTML

Among numerous HTML tags that form the logical structure of a page, some are considered the base. The structure can be divided into three main sections: <html>, <head>, and <body> .

Take a look at the code of a simple HTML page:

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Page title</title>
  </head>
  <body>
    <h1>This is a heading</h1>
    <p>This is a paragraph</p>
  </body>
</html>

If you save this code in the HTML format (.html) and open it in your browser, the page will look like this:

This looks quite basic, but with HTML you can do much more: customize the structure of the text, manage its visual presentation, and display paragraphs, forms, pictures, titles, and tables. Hypertext markup language allows you to format texts, which makes them friendlier to Internet users. It is much more convenient to read the text that has clear and logical markup rather than plow through unstructured text.

Let's get back to the code from the previous example and consider the listed tags in more detail.

    element <!DOCTYPE> specifies the type of the current document: DTD (Document Type Definition). It is necessary that the browser understands according to which HTML standard to display the web page. As you see, this is one of the tags that aren't paired;
    the <meta> tag with attribute charset specifies document coding. If it is not specified, some browsers may display obscure characters instead of the text;
    the <html> tag indicates that it is an HTML document;
    the <head> tag is designed to store elements that help the browser and search engines to work with data;
    the <title> contains the HTML document header. Even though this tag is not mandatory, it is still present on almost all web pages on the Internet;
    the <body> tag defines the page content area. It wraps the content displayed in the main browser window;
    the <h1> tag holds the page title within the body, and the <p> tag is responsible for the paragraphs. These tags are not the main sections and provided here as an example, but you're likely to find them useful in the future as you move from basic to artsy.

Basic HTML Page Structure

Here is a visualization of the basic HTML page structure:

As you can see, this structure bears a resemblance to our anatomy. Hopefully, this analogy will help you understand HTML better.
Conclusion

Surely, both humans and web pages are much more intricate and show a lot of variation. Modern pages can be very large and may contain a lot of different tags inside <body>, but their basic structure always remains the same. Come to think of it, this is also so very human.
Report a typo
.......................
Theory: Inline Elements

For many beginners, dealing with the structure of HTML documents may prove to be a challenge. Namely, it is sometimes hard to understand how the elements of the web page combine and what properties they have.

Trust us though: it's much easier than it may seem. To get through these issues, it is enough to simply know the exact type of a particular element of a web page.

In HTML up to version 4.01, it's common to distinguish two main types of page elements: block-level and inline. Each of them has its own properties. In HTML5, however, the elements are not just divided into block-level and inline, but also grouped by meaning and purpose, representing categories of content. This concept will be considered at length in the following topics; for now, try to understand the ins and outs of working specifically with inline elements.

Inline elements are those elements of a document that are a direct part of a line. They are intended to emphasize some part of the text and give it a certain function/meaning; they usually contain one or more words.

Let's now take a look at four examples of inline elements.
<a> tag

<a> tag is probably one of the most important elements of HTML; it's designed to create links. This tag is often used with the href attribute, which indicates the path to the file/webpage referenced. Consider a code sample that takes us to the JetBrains website:

<a href="https://jetbrains.com">Click here to access the JetBrains website!</a>

This is what we get in the browser:

The text wrapped in the <a> tag is underlined and highlighted in color. When you click on it, you're taken to the address specified in the href attribute.
<span> tag

In the paired tag <span> you can wrap the text or part of it.

<p>For the first time <span>on our site</span>?</p>
<span>Sign up now!</span>

This tag does not affect the display of text in any way:

You probably have a logical question: why and in what situations use this tag? The <span> tag is often used when you need to change the appearance of a part of text using CSS. CSS is the language used to describe the appearance of web pages. We will still learn this technology in the track "Web Developer", and in the meantime continue to get acquainted with the inline elements.

<b> tag
This paired tag sets a bold font for any text enclosed in it. This is rather straightforward, so let's proceed to the example. The limits of the text are indicated by the <p> tag; the outline of a name and surname of a person is changed:

<p>I'm <b>John Doe</b>, and what's your name?</p>

Now look at the result in the browser:

As you can see, this tag is very convenient and easy to use when you want to highlight an important part of the text.

<sub> tag
This tag is used to create subscript text: that is, the text inside this paired tag will be shifted down and reduced in size. Let's see how it works:
<p>The formula of water is H<sub>2</sub>O.</p>
This tag comes in handy when you need to write a chemical formula.

<sup> tag
This tag defines superscript text. It is similar to the previous one, except that the text enclosed in this tag will be shifted upwards:
<p>x<sup>2</sup> = 4</p>
With <sup> you can get display interesting mathematical equations on your web page.

This is by far not a complete list of inline elements – there are definitely many more to know.

Features of inline elements
The following features are characteristic of all these different inline elements:
    They can contain only data and other inline items. The exception to this rule is the <a> tag which can also contain block-level elements.
    Before and after, the browser doesn't make a line break. Take a look at the behavior of inline elements and compare it with that of block-level elements:

    Inline elements are strictly enclosed in tags.

Now that you have learned the features of inline elements, it will be easier for you to understand the structure of web pages and how it is created.
Report a typo
........................................
Theory: Regexps basics

Manipulating text data is quite a popular task in programming as well as in real life. For example, we often may need to analyze a text, find all specific strings in a file and so on. Processing text data can be quite a challenging problem. That's why there is a special tool called regular expressions that makes it easier and faster.
Why regular expressions?

A regular expression (regex or regexp for short) is a sequence of characters that describes a common pattern for a set of strings. Such patterns can be used to search, edit, and manipulate texts. They can either check if a whole string or its substring matches the given pattern or replace the substring with another one.

When do we need such patterns? Say we want to obtain all the files with the same extension (like *.pdf), or extract all the entries of a particular name in different forms (either Edgar Poe, Edgar Allan Poe, E. A. Poe or else), all email addresses, or even find all numeric structures denoting dates (02/03/2020). With regexps, such tasks can be done with one line.

How do such patterns look? Well, at first, they may seem confusing, look, for example at \d+(\.\d)? or [a-zA-Z]. And they're often substantially longer. We'll start with the basics, though.

Regexps may be regarded as a kind of sublanguage that most programming languages support, but there are some differences in a syntax called "flavors". In this topic, we will consider regexps in isolation from programming languages to understand the general idea.

While learning this topic, you can visit the regexp site to play around with regular expressions from our examples. Choose PCRE as the flavor. It means Perl Compatible Regular Expressions which are the most common standard in practice.
Matching on examples: more PARKs

Let's start by exploring how matching works formally. Although a regex pattern can be quite a complicated expression containing characters with special meaning, the simplest regex is just a string of simple characters. Suppose, there is a set of words: PARK, SPARK, PARKING, MARK, QUARKS. You need to check which of them contains the word PARK. This is what happens, for example, when you perform a Ctrl+F search on a web page.

We can easily solve this problem using the PARK pattern. The pattern means that symbols P, A, R, K in a word must follow each other from the left to the right. We suppose that the whole word matches the pattern if any part (substring) of the word matches it.

Here are some explanations:

    the word PARK exactly matches our pattern;
    the word SPARK matches our pattern because it has a suitable substring;
    the word PARKING matches our pattern due to the same reason;
    the word MARK doesn't match our pattern because of the M letter;
    the word QUARKS doesn't match our pattern since it does not have a suitable part.

To sum up, only three words match the PARK pattern.

In regular expressions, the case of characters make sense: park is not the same as PARK, i.e. they do not match.

In addition, let's consider another sequence of characters PAKR. It does not match our pattern since two characters have a wrong (reverse) order.
The power of regular expressions

Finding substrings is not very impressive, though. The real power of regular expressions comes when you start using special metacharacters called wildcards. They allow you to define a pattern, so you can match strings that do not necessarily contain the identical sequence of characters. You can skip some characters in a string or match different characters in the same positions, or even repeat a character several times.

Let's introduce two simplest wildcards: dot and question mark.
The dot character

The dot character . matches any single character including letters, digits, and so on, except for the newline character, unless it is specified.

Let's look at our previous example again with several additional words.

As you remember, in the previous example, two words did not match the pattern because of one unsuitable character. Let's consider them and also add two additional words. Here is our new pattern .ARK with the dot character. It says: "there is any character followed by ARK".

Hooray, both words MARK and QUARKS match the new pattern! But the WARM word does not match it. Think for a minute, how can this be fixed?

The word ARK also does not match our pattern since it does not have a character on the . position in the pattern, while this is required.
The question mark

The question mark ? is a special character that has “the preceding character or nothing" meaning. The question mark ? signals that the character before it can occur once or zero times in a string to match the pattern. When can we use it?

Maybe with this example, you will finally begin to feel the magic of regexps. Consider the difference between English and American spelling. Imagine, we are trying to find all the studies mentioning color blindness in some publications archive. However, it contains different sources and the spelling may vary. What word should we look for? The answer is both!

The pattern colou?r will match the strings colour and color, but not the string coloor. It is also possible to include the possibility of different letter cases to match the uppercase "Color" as well. We will learn how it is done in later topics.

Let's return to our previous example. The word ARK does not match the .ARK pattern. But if we add ? right after the dot character .?ARK, the word ARK will match the new pattern since the first character is optional now.

Note, how we combine the powers of the different wildcards in the combination .?. It is the underlying idea of regexps as well.
Conclusion

Regexps allow you to find matching strings by a certain pattern. They use special characters with special meanings along with simple characters in their literal interpretation:

    the dot . character matches any single character except for \n;
    the question mark ? character means "the previous character can be absent from the string";
    regular expressions are case-sensitive.

We hope, that you start to see that regexps provide a powerful tool for processing strings and texts. By this, we conclude our introductory topic about them. Remember, that there are many more applications of regular expressions that we have not yet discussed.
Report a typo
This content was created 11 months ago and updated 9 days ago . Share your feedback below in comments to help us improve it!
............................
Theory: Program execution

Have you ever thought about what it means to write a program in Python? From the programmer's point of view, it simply means to write a set of familiar to Python statements in a text file and later make Python execute the file. Thus, one can create a .txt file with this statement:

print("Hello, World!")

and run it via Python or OS console. Of course, by convention, all the Python files are supposed to be called with .py extension and typically people don't use text editors to write Python code — they use IDEs, but the idea is clear: from the programmer's point of view source code is just a set of statements. But that's not exactly it.

If you've been programming for at least some time, you probably have heard such terms as interpreted or compiled languages. And most likely you've heard, that Python is an interpreted one, without any details. So, let's figure this all out!
Right now, the process of program execution must look for you something like this:

In fact, taking into account the part with "interpretation" process, you can turn on your logical thinking and change the middle part:

...and that'll do. Actually, the majority of Python programmers stop going deeper at this step. It's usually enough to know that "Python is an interpreted language" and to explain anything using this mantra. Here we are going to be better — we'll go deeper!
The interpreter

Generally, what is the interpretation process? One may say that it resembles the reading of a program. Some software just "reads" your program and executes what is written in it line by line. This software is unexpectedly called Interpreter and is a part of the standard Python installation package. Another inherent part of it is the standard library with all built-in modules, functions, data, etc. An interesting fact: an interpreter can be written in basically any programming language. The default interpreter for Python is written in C and is called CPython. Some other Python interpreters are:

    PyPy is written in a restricted subset of Python called RPython (Restricted Python), which provides some restrictions to the usual Python code.
    Jython translates Python code into Java-compatible byte code, which is later executed by JVM — Java Virtual Machine.
    IronPython is an implementation of Python for the .NET framework.

Now let's try to understand, what is really happening during interpretation. In fact, this step consists of 3 smaller ones:

The compiler turns your set of statements (your source code) into so-called byte code. Byte code itself is lower level (thus more detailed), platform-independent, and more efficient version of source code, but it's not binary machine code like instructions for an Intel or AMD chip. Byte code is a Python-specific representation of source code. That's why some Python programs are executed not as fast as the analogs in C++ or C — traditional compiled languages.
Python Virtual Machine

After compilation, the byte code is given into the PVM (Python Virtual Machine). Although it sounds quite impressive, in fact, it is nothing more than a big piece of code, that iterates through byte code instructions received from a compiler and executes them one by one, thus performing the desirable operations specified by the programmer. It is an internal part of Python system and you don't need to install it as it's not a separate program. In fact, the thing which really executes your code is PVM, so we can say it is the last step of executing any Python program. All this complexity is deliberately hidden from a programmer. The "interpretation part" is fully automated, so usually you won't need to think about it. Remember: Python programmers simply write the code and run the files, everything else is done by Python itself.
Conclusion

Now you should understand that yes, Python is an interpreted language indeed, but before the interpretation stage, there is an internal process of compiling the source code into the byte code. Thus, executing a Python program implies both steps: compilation and interpretation.

When your program is turned into byte-code, it's executed line by line from top to bottom, so generally you can expect your program to work exactly the way you have written it.
..........................

Theory: Indexes

There are several types of collections to store data in Python. Positionally ordered collections of elements are usually called sequences, and both lists and strings belong to them. Each element in a list, as well as each character in a string, has an index that corresponds to its position. Indexes are used to access elements within a sequence. Indexing is zero-based, so if you see a person who counts from zero, you must have met a programmer.
Indexes of elements

To access an element of a list by its index, you need to use square brackets. You add the brackets after the list and, between them, you write the index of an element you want to get.

Don't forget, the indexes start at 0, so the index of the first element is 0. The index of the last element is equal to len(list) - 1.

Let's take a look at the example below:

colors = ['red', 'green', 'blue']

first_elem = colors[0]   # 'red'
second_elem = colors[1]  # 'green'
third_elem = colors[2]   # 'blue'

Strings work in the same way:

pet = "cat"

first_char = pet[0]   # 'c'
second_char = pet[1]  # 'a'
third_char = pet[2]   # 't'

Potential pitfalls

When using indexes, it's important to stay within the range of your sequence: you'll get an error (called IndexError) if you try to access an element with a non-existing index!

colors = ['red', 'green', 'blue']
pet = "cat"

print(colors[3])  # IndexError: list index out of range
print(pet[3])     # IndexError: string index out of range

There is one more obstacle in your way. Imagine that you want to change one of the elements in a list. It can be easily done:

colors = ['red', 'green', 'blue']

colors[1] = 'white'
print(colors)  # ['red', 'white', 'blue']

However, when it comes to strings, such reassignment is impossible. Strings, unlike lists, are immutable, so you can't modify their contents with indexes:

pet = "cat"

pet[0] = "b"
# TypeError: 'str' object does not support item assignment

Don't worry, after some practice, you will not encounter these errors.
Negative indexes

The easier way to access the elements at the end of a list or a string is to use negative indexes: the minus before the number changes your perspective in a way and you look at the sequence from the end. So, the last element of a list, in this case, has the index equal to -1, and the first element of the list has the index -len(list) (the length of the list).

For example:

colors = ['red', 'green', 'blue']

last_elem = colors[-1]    # 'blue'
second_elem = colors[-2]  # 'green'
first_elem = colors[-3]   # 'red'

pet = "cat"

last_char = pet[-1]    # 't'
second_char = pet[-2]  # 'a'
first_char = pet[-3]   # 'c'

As you can see, it works the same for lists and strings.

If you write a non-existing negative index, you'll also get IndexError. Be careful with indexes to avoid off-by-one errors in your code.

The following picture shows the general concept of indexes in a list:

Since you have learned the concept of indexes, we hope that from now on you will not encounter any difficulties when using them!
Report a typo
...........................
Theory: Dictionary

Imagine that you're a birdwatcher sitting in the park and counting birds that you see. You've observed a dozen pigeons, 5 sparrows, and even one red crossbill! Now, suppose that you want to store these observations for later use. You need to remember exactly how many birds of each kind you've seen. So, a simple list with numbers won't do because you won't be able to tell which number refers to which bird. You need a data type that can associate one thing with another: in our case, the name of the bird with the number of observations.

Luckily, Python has such a type — dictionary (dict). You can picture a real dictionary — a large book with definitions for a lot of words. The definition contains two parts: the word itself (let's call it a key) and the definition for it (a value). In our birdwatcher example, the keys are names of the birds ("pigeon", "sparrow", and "red crossbill") and the values are how many birds of that kind we've seen (12, 5 and 1, respectively).

In programming, dictionaries work in a similar way: if we want to store an object, we need to select some key for it and put our object as a value for that key into our dictionary.
Dictionary creation

A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value. If you already know the values needed, then the easiest way to create a dictionary is to use the curly braces with a comma-separated list of key: value pairs. If you want to create an empty dictionary, you can do so with the help of curly braces as well. Note that values in a dictionary can be of different types.

birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

print(type(birds))  # <class 'dict'>
print(type(prices))  # <class 'dict'>
print(type(empty_dict))  # <class 'dict'>

Another way to create a dictionary is to use the dict constructor.

another_empty_dict = dict()  # using the dict constructor

print(type(another_empty_dict))  # <class 'dict'>

When creating a non-empty dictionary, a dict constructor can take a dictionary as an argument, and / or future dictionary keys as arguments with assigned values, as in the example:

# note that the future dictionary keys are listed without quotes
prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')

print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}

When we give the dict constructor dictionary keys with assigned values, as dict(americano=8.0), the left part of the expression is treated like a variable, so it can't be an integer, a string in quotes, a list, a multiword expression, etc. That is, the following lines will give you an error:

d1 = dict(888=8.0)
d2 = dict("americano"=8.0)
d3 = dict(["americano", "filter"]=8.0)
d4 = dict(the best americano=8.0)

Finally, you can create a nested dictionary. It's a collection of dictionaries inside one single dictionary.

# a nested dictionary example
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

# another nested dictionary example
# note that keys of the outer dictionary are numbers
digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

Accessing the items

The syntax for accessing an item is quite simple — square brackets [] with a key between them. This approach works both for adding objects to a dictionary and for reading them from there:

my_pet = {}

# add 3 keys and their values into the dictionary
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'

print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}

# get information from the dictionary about an added item
print(my_pet['name'])  # Dolly

When working with a nested dictionary, getting the right value may be a little harder. As in our example, there are different levels and you need to stop at the right depth.

# our nested dictionary once again:
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}

print(my_pets['cat']['breed'])  # maine coon

Choosing the keys

You can save object of any type in a dictionary, but not all of them qualify as a key. You need a good, unique key for each object in your collection. Still, this is not the only restriction on dictionary keys and we will cover them later. For now, safely use numbers and strings.

When a key has already been added to your dictionary, its old value will be overridden:

trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
print(trilogy['IV'])  # Star Wars

trilogy['IV'] = 'A New Hope'
print(trilogy['IV'])  # A New Hope

In Python 3.7 and up, dictionaries do maintain the insertion order for values they store, but in previous versions it is not neccessarily so:

alphabet = {}
alphabet['alpha'] = 1
alphabet['beta'] = 2

print(alphabet)
# Python 3.8 output: {'alpha': 1, 'beta': 2}

Recap

In this topic we've covered some basics for the dictionary data type in Python:

    how to create a dictionary,
    what is a nested dictionary,
    how to manage dictionary items: keys and values.

In the following lesson you'll get acquainted with basic operations on dictionaries, but first, let's practice some tasks, so you would feel confident using this data type!
Report a typo
........................
Theory: Tuple

By now, you definitely know how to handle a list, the most popular collection in Python. Now let's discover an equally useful data type — tuples. You should remember that they are almost identical to lists. What sets them apart is their immutability.
Define a tuple

Since tuples cannot be changed, tuple creation is similar to opening a box of a fixed size, then putting several values into this box and sealing it. Once the box has been sealed, you cannot modify its size or content.

Use a pair of parentheses to define a tuple:

empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

Empty tuples are easy to create. Then what went wrong in the following example?

not_a_tuple = ('cat')
print(not_a_tuple)        # 'cat'
print(type(not_a_tuple))  # <class 'str'>

As you can see, the variable we created stores a string. It's actually a comma that makes a tuple, not parentheses. Let's fix this piece of code:

now_a_tuple = ('cat',)
print(now_a_tuple)        # ('cat',)
print(type(now_a_tuple))  # <class 'tuple'>

So, always use a comma when defining a singleton tuple. In fact, even if your tuple contains more than one element, separating items with commas will be enough:

weekend = 'Saturday', 'Sunday'
print(weekend)        # ('Saturday', 'Sunday')
print(type(weekend))  # <class 'tuple'>

The built-in function tuple() turns strings, lists and other iterables into a tuple. With this function, you can create an empty tuple as well.

# another empty tuple
empty_tuple = tuple()
print(empty_tuple)        # ()
print(type(empty_tuple))  # <class 'tuple'>

# a list turned into a tuple
bakers_dozen = tuple([12, 1])
print(bakers_dozen == (12, 1))  # True

# a tuple from a string
sound = tuple('meow')
print(sound)  # ('m', 'e', 'o', 'w')

What can we do with tuples?

First, let's examine what characteristics lists and tuples have in common.

Both lists and tuples are ordered, that is, when passing elements to these containers, you can expect that their order will remain the same. Tuples are also indifferent to the nature of data stored in them, so you can duplicate values or mix different data types:

tiny_tuple = (0, 1, 0, 'panda', 'sloth')

print(len(tiny_tuple))  # 5
print(tiny_tuple)       # (0, 1, 0, 'panda', 'sloth')

Just like lists, tuples support indexing. Be careful with indexes though, if you want to get along without IndexErrors.

empty_tuple = ()
print(empty_tuple[0])  # IndexError

numbers = (0, 1, 2)
print(numbers[0])   # 0
print(numbers[1])   # 1
print(numbers[2])   # 2
print(numbers[3])   # IndexError

And here the first distinctive feature of tuples comes into play. What they don't support is item assignment. While you can change an element in a list referring to this element by its index, it's not the case for tuples:

# ex-capitals
capitals = ['Philadelphia', 'Rio de Janeiro', 'Saint Petersburg']

capitals[0] = 'Washington, D.C.'
capitals[1] = 'Brasília'
capitals[2] = 'Moscow'
print(capitals)  # ['Washington, D.C.', 'Brasília', 'Moscow']

former_capitals = tuple(capitals)
former_capitals[0] = 'Washington, D.C.'  # TypeError

In the example above, we tried to update the tuple and it didn't end well. You can't add an item to a tuple or remove it from there (unless you delete the entire tuple). However, immutability has a positive side. We'll discuss it in the next section.

Immutability and its advantages
By this time, one question might have come to your mind: why use tuples when we have lists? Predictably, all answers conduce to immutability. Let's dwell on its upsides:

    Tuples are faster and more memory-efficient than lists. Whenever you need to work with large amounts of data, you should give it a thought. If you are not going to modify your data, perhaps you should decide on tuples.
    A tuple can be used as a dictionary key, whereas lists as keys will result in TypeError.
    Last but not least, it's impossible to change by accident the data stored in a tuple. It may prove a safe and robust solution to some tasks.

Summary

Those were the very basics of tuples in Python. Just like lists, tuples are ordered and iterable. Unlike lists, they are immutable. You'll learn more of tuple features in the next topics, now it's time to write your first programs with them!
Report a typo
...........................
Theory: Arguments

By now, you are on good terms with functions, since you know how to invoke and declare them. Let's deepen your knowledge a bit and discover some new features of functions.

First, a line should be drawn between the terms "argument" and "parameter". Parameters represent what a function accepts, it's those names that appear in the function definition. Meanwhile, arguments are the values we pass to a function when calling it. We'll cover both arguments and parameters further.
Positional arguments

There are different ways to assign arguments to a function. First of all, you can do it simply by position. In this case, values will associate with parameters in the order in which you passed them into your function from left to right. Such arguments are called positional, or non-keyword.

def subtract(x, y):
    return x - y


subtract(11, 4)  # 7
subtract(4, 11)  # -7

When we swapped the numbers in the second function call, we got a different result. Thus, you can see that the order determines how arguments are assigned.
Named arguments

Another way to assign arguments is by name. Sometimes you might want to control the order of passed values. That's where named, or keyword, arguments come into play.

def greet(name, surname):
    print("Hello,", name, surname)


# Non-keyword arguments
greet("Willy", "Wonka")               # Hello, Willy Wonka

# Keyword arguments
greet(surname="Wonka", name="Willy")  # Hello, Willy Wonka

The order doesn't matter here since parameters are matched by name. However, keyword arguments are always written after non-keyword arguments when you call a function:

greet("Frodo", surname="Baggins")  # Hello, Frodo Baggins
greet(name="Frodo", "Baggins")     # SyntaxError: positional argument follows keyword argument

Make sure to mention each parameter once. To understand why this is important, let's think about what happens every time we call a function. In fact, arguments are initialized so that all operations with the values in this function start from scratch. You cannot initialize an argument twice, so if a value has already been passed and associated with some parameter, attempts to assign another value to this name will fail.

def greet(name, surname):
    print("Hello,", name, surname)


greet("Clementine", name="Rose")
# TypeError: greet() got multiple values for argument 'name'

As shown in the example, multiple values for the same name cause an error.
Names are important

We have covered the main errors that you can face. Of course, there can be more parameters in a function:

def responsibility(developer, tester, project_manager, designer):
    print(developer, "writes code")
    print(tester, "tests the system")
    print(project_manager, "manages the product")
    print(designer, "develops design")

Note that when we use keyword arguments, names are important, not positions. Thus, the following example will work correctly:

responsibility(project_manager="Sara", developer="Abdul", tester="Yana", designer="Mark")
# Abdul writes code
# Yana tests the system
# Sara manages the product
# Mark develops design

However, if we call the function with the same order of names, but without named arguments, then the output will be wrong, with mixed responsibilities:

responsibility("Sara", "Abdul", "Yana", "Mark")
# Sara writes code
# Abdul tests the system
# Yana manages the product
# Mark develops design

This way, Python knows the names of the arguments that our function takes. We can ask to remind us of them using the built-in help() function.

help(responsibility)
# Help on function responsibility in module __main__:
# responsibility(developer, tester, project_manager, designer)

PEP time

Look at the declared function and function calls shown in this topic one more time: greet(name="Willy", surname="Wonka"). Have you noticed missing spaces around the equality sign? Their absence is not accidental. By PEP 8 convention, you should not put spaces around = when indicating a keyword argument.
Conclusions

Now, when we've discussed some advanced features of functions, let's sum it up:

    There's a distinction between parameters and arguments.
    You can pass arguments to a function by position and by name.
    The order of declared parameters is important, as well as the order of arguments passed into a function.
    The help() function can tell you the function arguments by name.

Report a typo
....................
Theory: Operations with list

You already know how to create lists (even empty ones), so, no wonder, that you may want to change your lists somehow. There are lots of things to do with a list, you can read about them in the Python Data Structures documentation. In this topic, we will discuss only the basic functions.
Adding one element

A list is a dynamic collection, it means you can add and remove elements. To take a closer look, let's create an empty list of dragons.

dragons = []  # we do not have dragons yet

What is next? The first thing that comes to mind is, of course, to add new elements to the list.

To add a new element to the end of an existing list, you need to invoke the list.append(element) function. It takes only a single argument, so this way you can add only one element to the list at a time.

dragons.append('Rudror')
dragons.append('Targiss')
dragons.append('Coporth')

Now you have three dragons, and they are ordered the way you added them:

print(dragons)  # ['Rudror', 'Targiss', 'Coporth']

Adding several elements

There is the list.extend(another_list) operation that adds all the elements from another iterable to the end of a list.

numbers = [1, 2, 3, 4, 5]
numbers.extend([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, 10, 20, 30]

Be careful — if you use list.append(another_list) instead of list.extend(another_list), it adds the entire list as an element:

numbers = [1, 2, 3, 4, 5]
numbers.append([10, 20, 30])
print(numbers)  # [1, 2, 3, 4, 5, [10, 20, 30]]

Alternatively, to merge two lists, you can just add one to another:

numbers_to_four = [0, 1, 2, 3, 4]
numbers_from_five = [5, 6, 7, 8, 9]
numbers = numbers_to_four + numbers_from_five
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

If you need a list with repeating elements, you can create a list with the repeating pattern, and then just multiply it by any number. This is particularly useful when you want to create a list of a specific length with the same value:

pattern = ['a', 'b', 'c']
patterns = pattern * 3
print(patterns)  # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

one = [1]
ones = one * 7
print(ones)  # [1, 1, 1, 1, 1, 1, 1]

Removing elements

The opposite of adding elements — deleting them — can be done in three ways. Let's have a look at them.

First, we can use the list.remove(element) operation.

dragons.remove('Targiss')
print(dragons)  # ['Rudror', 'Coporth']

If the element we want to delete occurs several times in the list, only the first instance of that element is removed.

dragons = ['Rudror', 'Targiss', 'Coporth', 'Targiss']
dragons.remove('Targiss')
print(dragons)  # ['Rudror', 'Coporth', 'Targiss']

The other two ways remove elements by their indexes rather than the values themselves. The del keyword deletes any kind of objects in Python, so it can be used to remove specific elements in a list:

dragons = ['Rudror', 'Targiss', 'Coporth']
del dragons[1]
print(dragons)  # ['Rudror', 'Coporth']

Finally, there is the list.pop() function. If used without arguments, it removes and returns the last element in the list.

dragons = ['Rudror', 'Targiss', 'Coporth']
last_dragon = dragons.pop()
print(last_dragon)  # 'Coporth'
print(dragons)      # ['Rudror', 'Targiss']

Alternatively, we can specify the index of the element we want to remove and return:

dragons = ['Rudror', 'Targiss', 'Coporth']
first_dragon = dragons.pop(0)
print(first_dragon)  # 'Rudror'
print(dragons)       # ['Targiss', 'Coporth']

Inserting elements at a specified position

At the beginning of this topic, we have learned how to add new elements to the end of a list. If we want to add a new element in the middle, we use the list.insert(position, element) operation. The first argument is the index of the element before which the new element is going to be inserted; so list.insert(0, element) inserts an element to the beginning of the list, and list.insert(len(list), element) is completely similar to list.append(element).

Here is an example:

years = [2016, 2018, 2019]
years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019, 2020]

Now, you can fill any empty list with something useful!
Membership testing in a list

Another thing that can be quite useful is checking if an item is present in the list. It can be done simply by using in and not in operators:

catalog = ['yogurt', 'apples', 'oranges', 'bananas', 'milk', 'cheese']

print('bananas' in catalog)      # True

product = 'lemon'
print(product in catalog)        # False
print(product not in catalog)    # True

Searching specific elements

Sometimes, knowing that the specified element is in the list is not enough; we may want to get more information about it — how many times the element occurs in the list and at which position.

The method count() can help with the quantity:

grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.count(5))  # 2

We can use the method index() to get the position of the element. It finds the index of the first occurrence of the element in the list:

print(grades.index(7))   # 2
print(grades.index(10))  # 0

We can also specify the interval for searching: list.index(element, start, end).

print(grades.index(9, 2, 5))  # 3

# if we don't specify the end of the interval, it automatically equals the end of the list
print(grades.index(10, 1))    # 5

Be careful — the end index is not included in the interval.

It is also good to know that if the element we are looking for is not in the list, the method will cause an error:

print(grades.index(8))  # ValueError: 8 is not in list

Our discussion of the basic operations with lists has come to its end. If you need more information, check out the Python Data Structures documentation.
Report a typo
............................
Theory: Identity testing
Many copies of equal values

By now, you know how to work with values in Python. For example, you know how to perform arithmetic operations with numbers. But what is a value in Python? It can't be an abstract thing, like in math, because a computer should be able to work with it. In this topic, you will get some understanding of values in Python.

Equal values in Python can exist in many copies. Consider the following code:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(c)  # [1, 2, 3]

It looks like all these variables are the same. But they aren't in some sense. To see it let's modify the list a.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

a[0] = 5

print(a)  # [5, 2, 3] - changed
print(b)  # [1, 2, 3] - didn't change
print(c)  # [5, 2, 3] - also changed

The reason is that we created two copies of [1, 2, 3]. Variables a and c refer to the first copy, and b refers to the second copy. Changing one of them doesn't affect the other one.

We call these copies as objects. An object is stored in memory and contains information about an abstract value it represents. So there can be several objects that represent the same value. You can treat such objects as twins. At first glance, they look identical, but actually, they are different people.

Let's see how to distinguish twins in Python.
Id function

Each object in Python has an associated integer called identity. You can get this integer by passing the object to the function id. Numbers, strings and other primitive types are also objects and they have an identity too. Identity never changes during the life of the object. Different objects in memory have different identities.

Using it we can distinguish two objects in Python that contain the same value. It is similar to distinguishing twins by looking at their identity documents.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, they contain the same value

# But they have different identities
print(id(a))  # 4558721352
print(id(b))  # 4560238984

Python generates id on the fly, running the pieces of code above will give you other integer values. Moreover, new objects can have smaller ids than the objects created earlier.

But if two variables refer to the same object, then the id function will return the same value.

a = [1, 2, 3]
c = a

print(a == c)  # True, they contain the same value

# And they also have the same identity
print(id(a))  # 4558721352
print(id(c))  # 4558721352

As you can see, the variables a and c share the identity, which means they refer to the same object.
Identity testing

You can check if two variables refer to the same object by comparing the results of the id function. But there is a better way to do it. Python has an identity operator is that checks if two objects have the same identity. The result is a boolean value: True or False. You should not confuse it with the equality operator == which tests whether two objects contain the same value.

a = [1, 2, 3]
b = [1, 2, 3]

identity_test = a is b  # False, because a and b refer to different objects in memory
equality_test = a == b  # True, because a and b contain the same value

b = a

identity_test = a is b  # True, because now both variables refer to the same object

The is not operator is the negation of the is operator. It returns True if its operands refer to different objects.

a = [1, 2, 3]
b = [4, 5]

print(a is not b)  # True, as expected

Use the identity operator carefully

Using the identity operator instead of the equality operator might lead to lots of mistakes. The example below shows the danger of the is operator.

a = int(input())  # 10
b = int(input())  # 10
print(a is b)     # True
print(id(a))      # 4462719392
print(id(b))      # 4462719392

a = int(input())  # 10000
b = int(input())  # 10000
print(a is b)     # False
print(id(a))      # 4466218032
print(id(b))      # 4466218160

The reason for such weird behavior is that Python optimizes the use of small integers. They are commonly used, so Python doesn't create a new object every time, but gives a reference to an existing number. The same thing happens to short strings.

However, the case of large numbers depends on the implementation. You may get True for the following expression:

a = 10000
b = 10000
print(a is b)  # True or False depending on your system

When to use the identity operator

The proper case to use the is operator is to test if something is None. None is a special keyword in Python that is used to define no value.

It is safe to use is in this case, because None is a singleton. This means that None object is created only once and then used whenever you refer to None in your code.

It is common to use None as a default value for optional arguments in functions.

def say_hello(name=None):
    if name is None:
        print('Hello!')
    else:
        print(f'Hello, {name}!')


say_hello()        # 'Hello!'
say_hello('Nick')  # 'Hello, Nick!'

True and False are also singletons, so you can use is with them too.
Conclusion

In this topic, we've learned a little about objects in Python and how to test objects for identity. In order not to make mistakes in your code pay attention to the following points:

    There can be many objects containing the same value. They are equal but not identical.
    The identity operator does not compare values, but it checks if its operands refer to the same object.
    Don't use the identity operator with primitive types.
    Use the identity operator to test if something is None.

Report a typo
.................
Theory: Basic string methods

As you already know, the string is one of the most important data types in Python. To make working with strings easier, Python has many special built-in string methods. We are about to learn some of them.

An important thing to remember, however, is that the string is an immutable data type! It means that you cannot just change the string in-place, so most string methods return a copy of the string (with several exceptions). To save the changes made to the string for later use you need to create a new variable for the copy that you made or assign the same name to the copy. So, what to do with the output of the methods depends on whether you are going to use the original string or its copy later.

"Changing" a string

The first group of string methods consists of the ones that "change" the string in a specific way, that is they return the copy with some changes made.

The syntax for calling a method is as follows: a string is given first (or the name of a variable that holds a string), then comes a period followed by the method name and parentheses in which arguments are listed.

Here’s a list of common string methods of that kind:

    str.replace(old, new[, count]) replaces all occurrences of the old string with the new one. The count parameter is optional, and if specified, only the first count occurrences are replaced in the given string.

    str.upper() converts all characters of the string to the upper case.

    str.lower() converts all characters of the string to the lower case.

    str.title() converts the first character of each word to upper case.

    str.swapcase() converts upper case to lower case and vice versa.

    str.capitalize() changes the first character of the string to the title case and the rest to the lower case.

And here's an example of how these methods are used (note that we don't save the result of every method):

message = "bonjour and welcome to Paris!"

print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
# `message` is not changed
print(message)  # bonjour and welcome to Paris!

title_message = message.title()
# `title_message` contains a new string with all words capitalized
print(title_message)  # Bonjour And Welcome To Paris!

print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)
print(replaced_message)  # b!nj!ur and welcome to Paris!

# again, the source string is unchanged, only its copy is modified
print(message)  # bonjour and welcome to Paris!

"Editing" a string

Often, when you read a string from somewhere (a file or the input) you need to edit it so that it contains only the information you need. For instance, the input string can have a lot of unnecessary whitespaces or some trailing combinations of characters. The "editing" methods that can help with that are strip(), rstrip() and lstrip().

    str.lstrip([chars]) removes the leading characters (i.e. characters from the left side). If the argument chars isn’t specified, leading whitespaces are removed.

    str.rstrip([chars]) removes the trailing characters (i.e. characters from the right side). The default for the argument chars is also whitespace.

    str.strip([chars]) removes both the leading and the trailing characters. The default is whitespace.

The chars argument, when specified, is a string of characters that are meant to be removed from the very end or beginning of the word (depending on the method you're using). See how it works:

whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

# delete spaces from the left side
whitespace_string.lstrip()  # "hey      "

# delete all "i" and "s" from the left side
normal_string.lstrip("is")  # "ncomprehensibilities"

# delete spaces from the right side
whitespace_string.rstrip()  # "     hey"

# delete all "i" and "s" from the right side
normal_string.rstrip("is")  # "incomprehensibilitie"

# no spaces from both sides
whitespace_string.strip()  # "hey"

# delete all trailing "i" and "s" from both sides
normal_string.strip("is")  # "ncomprehensibilitie"

Keep in mind that the methods strip(), lstrip() and rstrip() get rid of all possible combinations of specified characters:

word = "Mississippi"

# starting from the right side, all "i", "p", and "s" are removed:
print(word.rstrip("ips"))  # "M"

# the word starts with "M" rather than "i", "p", or "s", so no chars are removed from the left side:
print(word.lstrip("ips"))  # "Mississippi"

# "M", "i", "p", and "s" are removed from both sides, so nothing is left:
print(word.strip("Mips"))  # ""

Use them carefully, or you may end up with an empty string.
Conclusions

Thus, we have considered the main methods for strings. Here is a brief recap:

    While working with string, you have to remember that strings are immutable, thus all the methods that "change" them only return the copy of a string with necessary changes.
    If you want to save the result of the method call for later use, you need to assign this result to a variable (either the same or the one with a different name).
    If you want to use this result only once, for example, in comparisons or just to print the formatted string, you are free to use the result on spot, as we did within print().

Report a typo
..........................
Theory: Operations with dictionary

You already know how to create a dictionary and access its items. In this topic, you are going to learn what else you can do with dictionaries.
Basic operations with dictionaries

Nearly all the operations with a dictionary require a key, but not all of them need a value.

1. Get a value from the dictionary by a key. As you remember, we can access the value in a dictionary by a key:

testable = {}
testable['key'] = 'value'

print(testable['key'])  # value

However, if you try to access a non-existent key, you will get a KeyError:

print(testable['not_a_key'])  # throws a KeyError

To avoid the KeyError, we can use the get method that returns None if the specified key is not in the dictionary:

# get method does not throw an error
print(testable.get('key'))  # value
print(testable.get('not_a_key'))  # None

With the get method we can also define the default value to be returned instead of None:

print(testable.get('not_a_key', 'default'))  # default

2. Delete (remove from a dictionary) a value by its key with the del keyword:

testable = {'key1': 'value1', 'key2': 'value2'}

del testable['key1']  # this will remove both the key and the value from dictionary object
print(testable)  # {'key2': 'value2'}

del testable['not_a_key']  # throws a KeyError

del testable['key1']  # throws a KeyError as we've already deleted the object by the key

del testable  # deletes the whole dictionary

Membership testing in a dictionary

Sometimes you need to check if a specific item is present in your dictionary or not. For example, you have a furniture catalog where products (keys) are listed along with prices (values), and you want to quickly find out if there is a blue sofa in it or not. In such a case, you can use operators in and not in for this purpose. The syntax is quite simple: key in dictionary returns True if key exists in dictionary and False otherwise. The not in operator does the opposite thing, it returns True if key does not exist in dictionary.

catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}

print('blue sofa' in catalog)    # True

print('yellow chair' in catalog)    # False

# Note that the membership operator looks for keys, not values
print(1500 in catalog)    # False

Iterating over dictionary

Other important methods of the dictionary are those which return dictionary view object (it is a set-like object which can be enumerated, and has some other useful properties): keys, items and values. As you might expect, the first one provides the keys collection of a dictionary, the second one gives you the collection of (key, value) pairs (tuples), and the third one provides the collection (not a set, as values might not be unique in a dictionary) of values, without any information about keys that are used to get these values from the dictionary.

    keys method is very helpful when you want to do something with each key in a dictionary.

    tiny_dict = {'a': 1, 'b': 2, 'c': 3}

    # Get a list-like object comprising all the keys
    print(tiny_dict.keys())  # dict_keys(['a', 'b', 'c'])

    Iterating over keys is default behavior in Python, and sometimes you can omit the method's call:

    tiny_dict = {'a': 1, 'b': 2, 'c': 3}

    # Iterate over the dictionary through the sequence of its keys
    for key in tiny_dict:
        print(key)

    Here is the output:

    a
    b
    c

    values method is quite similar to the previous one, with the only difference that you get the values, not the keys. Also, it's necessary to call the method explicitly:

    tiny_dict = {'a': 1, 'b': 2, 'c': 3}

    for value in tiny_dict.values():
        # print the first value
        print(value)  # 1
        # exit the loop so that other values are not printed
        break

    items method should be used in case you need both keys and values in your code:

    tiny_dict = {'a': 1, 'b': 2, 'c': 3}

    for key, value in tiny_dict.items():
        print(value == tiny_dict[key])  # prints True three times

Recap

In this topic you've learned what you can do with dictionaries in Python:

    which basic operations can be done on dictionaries,
    how to test for membership in a dictionary,
    which methods are used to iterate over a dictionary.

If you want to see more information on dictionaries, don't forget to check out the Python documentation.
.................

Python Data types and operations Objects in Python Objects in Python
Theory: Objects in Python
14 minutes 0 / 5 problems solved

Knowing how different types of objects work in Python will help you understand some of the following topics more deeply, as well as the structure of the language in general.
Reference to an object

In Python, all values are stored in objects. You can think that an object is like a box that contains information about some value and also stores some additional data such as its identity. When you assign a value to a variable, e.g. string = "hello", Python creates a new object, places this value (the string "hello" in our case) inside the new object and then creates a reference from the variable name string to the object.

Then, if we assign one variable to another, e.g. new_string = string, Python will create a reference from the new variable new_string to the same object.

You can use the id function to see that both variables refer to the same object:

print(id(string))        # 4336233024
print(id(new_string))    # 4336233024

As a result, you can access the object using any of the two variable names. You can also assign a new value to one of these variables and this will not affect the other one.

string = "hello"
new_string = string
string = "world"

print(string, id(string))            # world 4336233136
print(new_string, id(new_string))    # hello 4336233024

Note that the identity has changed along with the value.

However, the situation is a bit more complex when we deal with mutable objects, e.g. some of the containers.
Mutable objects & references

Let's take a list as an example. The thing is, a list doesn't store its values inside itself. Instead, it stores references to objects that store values. For example, when you write lst = [2, 3, 9], Python creates the following structure:

Now, if we assign our list to a new variable and then try to alter the first object, this will also affect the new list:

lst = [2, 3, 9]
new_lst = lst

print(lst, id(lst))            # [2, 3, 9] 4334518600
print(new_lst, id(new_lst))    # [2, 3, 9] 4334518600

# we change an element of the first list
lst[2] = 0
print(lst, id(lst))            # [2, 3, 0] 4334518600

# but the new list is also modified
print(new_lst, id(new_lst))    # [2, 3, 0] 4334518600

This is so because both lists refer to the same object: when it is modified, all variables continue to refer to this very object. In the next topic, you will learn how to alter a list without changing its copies.
Conclusions

    Variables in Python do not store values themselves, they store references to objects that store values.
    When we assign one variable to another, they refer to the same object.
    After modifying mutable objects, other variables referring to it will also change.

.......................................
Theory: Default arguments

In addition to several ways that you can use to pass arguments into functions, Python also has special syntax for accepting these values from a function call. So, while in earlier topics we have learned how to work with arguments, now we will focus on parameters, the ones with default values in particular, and look into them in more detail.
Defaults

In Python, functions can have parameters with default values. Default parameters are specified in the function definition and contain default values for arguments in case they are not provided with a function call. Have a look at this code:

def locate(place, planet="Earth"):
    print(place, "on", planet)


locate("Berlin")                     # Berlin on Earth
locate("Breakfast", planet="Pluto")  # Breakfast on Pluto
locate("Craters", "Mercury")         # Craters on Mercury

Here we have two parameters, place and planet. The first one has no default value, so we should always specify it when calling the function. The second one, in contrast, can be omitted, in which case the function will simply take the default value.

Parameters with default values, such as planet, are optional in some way. You can easily call a function without them and rely on preset values. As in the example above, most of the places we might want to find are most likely on Earth. However, new values can be assigned to them either by name or by position.

When you declare this function, place non-default parameters first and then those with default values. If you try doing the opposite, SyntaxError will crop up:

def greet(greeting="Hello,", name):
    print(greeting, name)

# SyntaxError: non-default argument follows default argument

In this case, you will not be able to use the default value at all. As the second parameter still requires a value, we would always have to write both values in a call, which makes not much sense. So, when you declare a function, pay attention to the order of the parameters.
Mutable objects as defaults

When it comes to mutable objects, things are getting trickier. Let's set a list as a default value and see how this function:

def add_player(player, team=[]):
    ...
    team.append(player)
    return team

As you can see, the function simply adds a new player to a team. First, we will give both arguments to it:

ice_hockey_team = add_player("Chris", ["Robert", "Alice"])
print(ice_hockey_team)    # ['Robert', 'Alice', 'Chris']

Everything looks fine. However, when we call it relying on the default value, the function's behavior would differ from what you might have expected:

rugby_team = add_player("Robin")
print(rugby_team)     # ['Robin']

football_team = add_player("Andrew")
print(football_team)  # ['Robin', 'Andrew']
print(rugby_team)     # ['Robin', 'Andrew']

Instead of two separate lists for teams, surprisingly, you got just one. With every subsequent call, the function will append a new item to this list. Why so? It turns out that default parameter values are evaluated once.

After you have declared a function, a new object for a default value is created. It will be used from this point on. This means that if the function modifies this object in some way, the default value in the mutable will change too. For this reason, you should use mutable default values carefully.

Here is a common workaround to fix the function from our earlier example:

def add_player(player, team=None):
    if team is None:
        team = []
    team.append(player)
    return team

Setting the default value to None and explicitly reassigning the value of the team parameter allows you to create a new list each time this function is called.
PEP time

Look at the declared functions shown in this topic one more time, for example, def locate(place, planet="Earth"): .... Have you noticed missing spaces around the equals sign? Their absence is not accidental. By PEP 8 convention, you should not put spaces around = when indicating a keyword argument. This holds true for parameters with default values.
Recap

Let's go over the main points we have discussed:

    Python Functions can be quite flexible, you can use them passing fewer arguments in a call (thanks to default values).
    You should pay close attention to the order of parameters when you declare functions. Place non-default parameters first and those with default values afterward.
    Mutable defaults may work contrary to your intentions, as their values are created once at the runtime. If so, a common way to avoid trouble is by using None by default and changing the parameter's value in the function's body.

Report a typo
.....................
Theory: Args

Functions have a flexible syntax in Python. We will find out what allows functions to accept a varying number of arguments and how to unpack iterable objects when calling a function.
Multiple positional arguments

You might be surprised by the fact that everything we've done before with functions limited us in some way. For example, if we don't specify the defaults for arguments, we will always have to pass the exact number of values into such function. However, sometimes it's more convenient when the number of arguments varies. For example, if you are declaring a function that should find the sum of all values passed into it, you never know how many arguments a user might want to use. Let's start with a simple case and define a function with two parameters. It can be done as follows:

def add(a, b):
    return a + b

This function makes us pass only two values, we can't just do add(1, 2, 3). Well, what we can do is to set a default value for the third parameter and then call this function with either two or three values. But this hardly solves the problem for more complex cases.

If you are not sure about the number of arguments that your function might take, or if you don't want to limit them, use the following syntax to define a function with *args:

def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total

This allows you to work with the variable args, which is a tuple of remaining positional arguments. Its length may vary:

# The length of `args` is 3
print(add(1, 2, 3, 4, 5))

# The length of `args` is 0
print(add(1, 2))

The function add() now requires two arguments, but if you pass additional values they will be collected in a tuple and get added to the total.

As you might have guessed, args is short for "arguments". You don't have to use this conventional name all the time, though:

def will_survive(*names):
    for name in names:
        print("Will", name, "survive?")


will_survive("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth")

The output for this function call will be as follows:

Will Daenerys Targaryen survive?
Will Arya Stark survive?
Will Brienne of Tarth survive?

This works for any variable name as long as there is a single asterisk * right before it.

Normally, *args comes after specific parameters:

def func(positional_args, defaults, *args):
    pass

Once all required arguments have been passed, the remaining values are packed into the tuple.

The parameters that come after *args are keyword-only. It means that they can only be used as keywords rather than positional arguments.

def recipe(*args, sep=" or "):
    return sep.join(args)


print(recipe("meat", "fish"))               # meat or fish
print(recipe("meat", "fish", sep=" and "))  # meat and fish

Unpacking in function calls

The Python syntax enables us to pass all items from a sequence as individual positional arguments using *. A single asterisk operator unpacks an iterable. Let's invoke the print() function and see how it works:

print(*"fun")        # f u n
print(*[5, 10, 15])  # 5 10 15

This code will be equivalent to a call where elements are listed one by one: print("f", "u", "n") and print(5, 10, 15) respectively. Unpacking just takes less of your time.

Combined with *args in our slightly modified function add(), unpacking takes away the concern for the number of values both in the function's body and upcoming calls.

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


small_numbers = [1, 2, 3]
large_numbers = [9999999, 1111111]

print(add(*small_numbers))  # 6
print(add(*large_numbers))  # 11111110

This is really powerful as it allows you to conveniently handle an arbitrary number of values in your function.
Recap

Let's sum up what we discussed in the topic:

    A function with *args can accept a changing number of positional arguments.
    The variable name args is arbitrary, you can always choose another one.
    *args provides access to a tuple of remaining values.
    The order of parameters in the function definition is important, as well as the order of passed arguments.
    In function calls, you can use the unpacking operator * for iterable objects.

Report a typo
..........................
Theory: Kwargs

With *args you can create more flexible functions that accept a varying number of positional arguments. You may now wonder how to do the same with named arguments. Fortunately, in Python, you can work with keyword arguments in a similar way.
Multiple keyword arguments

Let's get acquainted with the ** operator used to pass a varying number of keyword arguments into a function. **kwargs collects all possible extra values in a dictionary with keywords as keys.

By convention, people use special names for this kind of arguments: *args for positional arguments and **kwargs for keyword arguments, but you can call them whatever you want. The main thing is that a single asterisk * matches a value by position and a double asterisk ** associates a value with a name, or keyword. So, **kwargs differs from *args in that you will need to assign keywords.

Here is an example:

def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")

Once the function has been invoked, these 4 lines will be printed:

Ottawa is the capital city of Canada
Tallinn is the capital city of Estonia
Caracas is the capital city of Venezuela
Helsinki is the capital city of Finland

So, everything works just fine! And again, the number of arguments we pass may differ in the next call.

Note that the names in a call are without quotes. That is not a mistake. Moreover, the names should be valid, for example, you cannot start a keyword with a number. Follow the same naming rules as for variables.

It is also possible to combine *args and **kwargs in one function definition:

def func(positional_args, defaults, *args, **kwargs):
    pass

The order is crucial here. Just as non-keyword arguments precede keyword arguments, *args must come before **kwargs in this case. Otherwise, both when creating and calling a function with *args and *kwargs in the wrong order, a SyntaxError will appear:

def func(positional_args, defaults, **kwargs, *args):
# SyntaxError: invalid syntax

func(positional_args, defaults, **kwargs, *args)
# SyntaxError: iterable argument unpacking follows keyword argument unpacking

Unpacking in function calls

There are two unpacking operators in Python: a single asterisk * unpacks elements of an iterable object and a double asterisk ** works with dictionaries. Let's try to get key-value pairs from a dictionary and pass them as keyword arguments using a double asterisk **:

def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

say_bye(**humans)

# Au revoir, Laura
# See you on Tuesday
#
# Au revoir, Robin
# See you on Friday

By default, you iterate over keys in a dictionary, so be careful with this. You might need this type of unpacking when setting specific parameters of a function. Saving values in a dictionary and then unpacking them in this way might be much easier than listing them in each call manually. Also, it will save time when you choose to fine-tune these parameters.
Recap

Let's go over the main points discussed in the topic:

    If you want to work with a varying number of keyword arguments, make use of **kwargs.
    The variable name kwargs is conventional, you can always choose another one.
    Notice the difference: *args provides access to a tuple of remaining values, while **kwargs collects remaining key-value pairs in a dictionary.
    The order of parameters in the function definition is important, as well as the order of passed arguments.
    In function calls, now you can use both unpacking operators: a single asterisk * for iterable objects and a double asterisk ** for dictionaries.

............................
Theory: Split and join

In Python, strings and lists are quite similar. Firstly, they both pertain to sequences, although strings are limited to characters while lists can store data of different types. In addition, you can iterate both over strings and lists. However, sometimes you need to turn a string into a list or vice versa. Python has this kind of tools. The methods that will help you to accomplish this task are split(), join() and splitlines().

Split a string
The split() method divides a string into substrings by a separator. If the separator isn't given, whitespace is used as a default. The method returns a list of all the substrings and, notably, the separator itself is not included in any of the substrings.

# split example
definition = input()  # 'Coin of the realm is the legal money of the country' 

definition.split()
# ['Coin', 'of', 'the', 'realm', 'is', 'the', 'legal', 'money', 'of', 'the', 'country']

definition.split("legal")
# ['Coin of the realm is the ', ' money of the country']

You can also specify how many times the split is going to be done with the maxsplit argument that comes after the separator. The number of elements in the resulting list will be equal to maxsplit + 1.

If the argument isn't specified, all possible splits are made.

# maxsplit example
definition = input()  # 'Coin of the realm is the legal money of the country'

definition.split("of", 1)
# ['Coin ', ' the realm is the legal money of the country']

definition.split("of")
# ['Coin ', ' the realm is the legal money ', ' the country']

If the separator doesn't occur in the string, then the result of the method is a list with the original string as its only element:

definition = input()  # 'Coin of the realm is the legal money of the country'

definition.split("hi!")  # wrong separator
# ['Coin of the realm is the legal money of the country']

Thus, in all cases split() allows us to convert a string into a list.

It may also be useful to read input directly into several variables with split():

name, surname = input().split()  # Forrest Gump

print(name)     # Forrest
print(surname)  # Gump

It's pretty efficient when you know the exact number of input values. In case you don't, it's likely to result in ValueError with a message telling you either that there are too many values to unpack or not enough of them. So keep that in mind!

Join a list
The join() method is used to create a string out of a collection of strings. However, its use has a number of limitations. First, the argument of the method must be an iterable object with strings as its elements. And second, the method must be applied to a separator: a string that will separate the elements in a resulting string object. See below the examples of that:

word_list  = ["dog", "cat", "rabbit", "parrot"]

" ".join(word_list)  # "dog cat rabbit parrot"
"".join(word_list)  # "dogcatrabbitparrot"
"_".join(word_list)  # "dog_cat_rabbit_parrot"
" and ".join(word_list)  # "dog and cat and rabbit and parrot"

Note that this method only works if the elements in the iterable object are strings. If, for example, you want to create a string of integers, it will not work. In this case, you need to convert the integers into strings explicitly or just work with strings right from the outset.

int_list = [1, 2, 3]
" ".join(int_list)  # TypeError!

str_list = ["1", "2", "3"]
" ".join(str_list)  # "1 2 3"

Split multiple lines

The splitlines() method is similar to split(), but it is used specifically to split the string by the line boundaries. There are many escape sequences that signify the end of the line, but the split() method can only take one separator. So this is where the splitlines() method comes in handy:

# splitlines example
long_text = 'first line\nsecond line\rthird line\r\nfourth line'

long_text.splitlines()
# ['first line', 'second line', 'third line', 'fourth line']

The method has an optional argument keepends that has a True or False value. If keepends = True linebreaks are included in the resulting list:

# keepends
long_text = 'first line\nsecond line\rthird line\r\nfourth line'

long_text.splitlines(keepends=True)
# ['first line\n', 'second line\r', 'third line\r\n', 'fourth line']

You can also use several string methods at once. It is called chaining, and it works because most of the string methods return a copy of the original string:

# chaining example
sent = input()  # "Mary had a little lamb"
new_sent = sent.lower().split()
# ["mary", "had", "a", "little", "lamb"]

But do not get carried away, because the length of a line should be no more than 79 characters, and we definitely do not want to break PEP 8!
Conclusion

We have learned how to convert strings to lists via the split() and splitlines() methods, and how to get strings back from lists via the join() method. As a recap, consider the following:

    Splitting and joining methods do not change the original string.
    If you need to use the "changed" string several times, you need to assign the result of the respective method to a variable.
    If you need to use this result only once, you can work with it on spot, for example, print() it.
    There are a lot of parameters in string methods. You can check the documentation if you need to fine-tune your program.

................
Theory: Experiments with Python shell

You already know how to start the Python shell and run some simple code there. Let's see how to use it for experiments. We will illustrate all of them with IDLE samples.

For instance, if you want to study a new module or library, you can conduct some code experiments in the Python shell to understand how to work with it. You can also implement your functions and classes in the shell and test them before including in the final script.
Methods, modules, and functions

Imagine you've just heard about the method type() and want to learn more about it. You can simply start the shell and, using your own examples, see how it works:

(images of operations in the shell)

The same can be done with modules:

The math module contains tools for mathematic calculations. In this example, we have imported it and tested its function that returns the square root of the given value.

This function works so that if we pass a non-numerical value as an argument, e.g. a string, it will return a TypeError.

If we don't want the program to stop executing in such cases, we can alter the method ourselves. That's how we can implement and use our own functions in the shell:

This is a simple modification of the math.sqrt() function that returns None if the passed value was neither an integer nor a float. So, in this experiment, you've found out how to implement your own function in the shell, learned how to use the type() method and got to know the sqrt() function of the math module.

Remember: everything you do in IDLE or command line shell disappears once you close it; you won't be able to use this code afterward. On the other hand, it's good because you definitely won't break anything in the program that you have copied in the shell and work with it there.
Magic? Autocomplete!

The Python shell also has an autocomplete function which is very useful when you're studying new things. In case that you don't remember the exact name of the method you'd like to use or even have no idea how it is called or you want to look up which methods are in the module, type a module name and a dot, then wait for a couple of seconds — the shell will help you with the list of available methods.

The next beautiful thing there is autocomplete for names of functions and variables. Use the TAB key for the shell to offer the function or variable name for you. You just need to type first letters and press TAB. In case of several names, you'll see a list of them:

This won't work if you launch the shell from the command line interpreter.

Recap

The Python shell provides a perfect opportunity both to play around with new modules and to refresh your memory about familiar ones. You can quickly test how methods and functions work, look up which methods an object has or which functions there are in any module. And such a useful option as autocomplete can help you with that!
Report a typo
71 users liked this theory. 1 didn't like it. What about you?
1068 users completed this topic. Latest completion was
about 3 hours ago
.
Current topic:
Experiments with Python shell
Stage 2
Topic depends on
Introduction to Python shell
Stage 2
Declaring a function
Stage 1
Load module
Stage 1
Topic is required for
Debugging in shell
Stage 2
Table of contents:
↑ Theory: Experiments with Python shell
Feedback & Comments
.................



