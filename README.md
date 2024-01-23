# FRACTION BINGO GAME APP
#### Video Demo: <https://youtu.be/oa1_YA8M9VQ>

## Final project: Fraction Bingo
Fraction Bingo project is a simple web-based Bingo game application, where users can generate bingo cards and play bingo as numbers are drawn randomly, developed as part of the CS50 course offered by Harvard University. This README provides an overview of the project and an explanation of the design choices and code structure.

## About the project
Fraction Bingo aims to create bingo cards with rational or decimal numbers at random, offering an educational and playful tool that allows educators and teachers to teach rational number concepts in an engaging and fun way for students. Using the game as a base, students can learn while having fun and competing for prizes. This makes the learning process more enjoyable and interactive. The application is developed using the Flask framework in Python and incorporates web technologies such as HTML, CSS, JavaScript and Bootstrap.

## Summary of features
- Home page with an explanation of Bingo and how to use the site to play;
- Register, log in and log out;
- Button to create game (the user must choose a name);
- Once the user chooses the name of the game, they will have access to the page to choose how many cards the user wants to generate, as well as the type of cards (decimal, fractional or both);
- Once the cards are generated, they will be displayed on a page with the option of pressing a button to generate a PDF for download;
- Generate PDF for download;
- Access the Draw page and choose which game you want to draw;
- Carry out the draw.

## How to Run
This application is built with Python using the Flask framework and can be run locally or deployed to a web server.

### Prerequisites
- Python 3

Pip package manager

### Installing Dependencies
Install the required Python packages by running:

pip install -r requirements.txt

## Running the Application
To run the application locally, navigate to the project directory and run:

flask run

## Deployment
The application can be deployed on any web server that supports Python applications. An example for deployment could be using Gunicorn:

gunicorn wsgi:app

Remember to replace wsgi:app with your Flask application's respective module and app name.

## User Guide
- Upon accessing the web app, users can generate new bingo cards by clicking the "Generate Cards" button.
- The drawn numbers will be displayed at the top of the page as they are randomly selected.
- Players can mark off numbers on their cards that match the drawn numbers.
- The teacher will check for a win when a user claims a bingo.

## Technologies Used
- Frontend: HTML, CSS
- Backend: Flask (Python)
- CSS Framework: Bootstrap (for navbar and responsive design)

## Files Structure
- app.py: The main Flask application file.
- templates/: Folder containing HTML templates.
- static/: Folder containing static files like CSS, JavaScript and images.
- requirements.txt: Required Python packages for the project.

### app.py
This is the main code of the Flask application that manages bingo games for teachers. It enables users (teachers) to register, log in, and manage bingo games, including creating bingo cards and conducting draws.

Moreover, the code leverages a SQLite database to store user and game information, and it uses the reportlab library to generate PDFs of the bingo cards.

Here is an overview of some of the routes and functionalities:

- `/`: The home page that displays whether the user is logged in.
- `/register`: Allows new users (teachers) to register on the platform.
- `/login` and `/logout`: Manage the login and logout process for users.
- `/jogar`: Redirects users to the bingo card generation page or to the login page if they are not logged in.
- `/geracao`: Enables users (teachers) to generate bingo cards for a game.
- `/cartelas`: Displays the generated bingo cards.
- `/gerar_pdf`: Generates a PDF of the bingo cards for printing.
- `/sorteio`: Manages the drawing of numbers for a selected game.

The code also contains helper functions to check if a username (email) already exists in the database, generate hashed passwords, generate unique fractions, and convert decimal numbers to irreducible fractions.

The rest of the code contains the logic for the aforementioned draw, the conversion of drawn numbers into the appropriate format (fraction or decimal), the updating of the database with the drawn numbers, and also include the response to the client after a draw is performed, returning the drawn number and updating the user interface.

### helpers.py
These functions are intended to support the main functionality of generating bingo cards with either fractions or decimals that don't result in recurring decimals. Here's a brief overview of each function:

#### gerar_fracoes_unicas(qtd_numeros, max_numerador=99):
- This function generates a set of unique fractions, ensuring that they are in their simplest form and don't result in recurring decimals. It takes two arguments:
    - qtd_numeros: The quantity of unique fractions to generate.
    - max_numerador: The maximum value for the numerator, defaulting to 99.
- It uses denominators that are powers of 2 and/or 5 up to 10 to ensure that the fractions are non-recurring when expressed in decimal form.
- The generated fractions are randomized and returned as strings in the format "numerator/denominator".

#### gerar_numero_decimal(qtd_numeros):
- This function generates a list of decimal numbers, taking one argument:
    - qtd_numeros: The quantity of decimal numbers to generate.
- It picks random divisors from a predefined list of numbers that are powers of 2 and/or 5 to ensure the decimals can be expressed as fractions without resulting in recurring decimals.

#### decimal_para_fracao_irredutivel(decimal):
- This function converts a decimal number to its irreducible fractional form.
- It uses the `Fraction` class from Python's `fractions` module to create a fraction and then limits the denominator to obtain the simplest form.

### templates/
The `layout.html` file establishes a basic structure that is utilized across all other pages. Jinja2 is employed for content blocks that can be overridden by child pages, such as `title`, `extra_classes`, `heading`, `content`, and `scripts`. Integration of Bootstrap for styling and jQuery for scripting functionalities enhances the user interface and interaction.

The `index.html` page is configured with the title "Fraction Bingo - Home Page" and provides instructions on how to play the game, ensuring clear and visual guidelines are in place for new users. It also features an image located at "/static/como_jogar1.png" to assist in this instructional process.

In `register.html`, a registration form is presented, allowing new users to create an account. The form is designed to give immediate feedback to the users after their registration attempts, highlighting either the success of account creation or errors that need to be addressed.

`login.html` mirrors the `register.html` in its structure but is purposed for user login. Feedback messages are strategically placed to notify users of the login process outcomes.

`geracao.html` contains a form dedicated to the creation of bingo cards. It provides options for users to name their game, select the type of card, and define the number of cards they wish to generate.

Displayed within `cartelas.html` are the bingo cards that have been generated, including a button to export the cards to a PDF. The appended JavaScript logic at the end of the file processes the cards in JSON format, setting them up for PDF creation.

Lastly, `sorteio.html` is the crafted page designated for the bingo number draw.

### static/

#### styles.css
The `styles.css` file contains the styling definitions for the application. Below is an overview of the key styling elements:

- `#cartelasContainer` is styled to display bingo cards in a flex container, aligning items in the center and justifying the content space-between.

- `.right` class is used to align elements to the right side of the container by adding automatic left margin.

- `.cartela` class defines the appearance of each bingo card with a solid border, margin, and padding.

- The `.cartela table` ensures that the table within a bingo card stretches to full width.

- Table cells (`td`) within `.cartela` are centrally aligned and bordered, ensuring the content is well-defined and readable.

- `#numeros-sorteio` handles the alignment and margin for the number draw section.

- `.numero-sorteado` styles the individual drawn numbers, with adjustable padding for spacing.

- `.titulo-centralizado` is used for centralized titles with non-wrapping text and adjustable right margin.

- `.background-inicial` and its pseudo-element `::before` create a background for the application with a specified image, positioning, and transparency settings.

- `.text-highlight` applies a semi-transparent white background with bold font to important text elements.

- `.underline` simply underlines the text.

- The navbar links `.navbar-dark .navbar-nav .nav-link` and their active or hover states are styled for better visual hierarchy and user navigation cues.

This styling ensures a consistent and user-friendly interface throughout the application.

## Future Improvements
- Prevent the saving of games with duplicate names to ensure each game is unique and easily identifiable.
- Develop a password reset routine for enhanced security and ease of access.
- Implement a mechanism to delete saved games for better control and organization of game activities.


## Conclusion
The "Fraction Bingo" project is an innovative and educational web application, designed to enrich social gatherings and learning environments with a classic game of bingo, reinvented with a mathematical twist. This application uses rational and decimal numbers to generate bingo cards, offering a unique way to blend fun with education. This README provides a detailed overview of the project's core functionalities, as well as the design and technological choices — such as Flask and Bootstrap — that contribute to an interactive and enjoyable user experience. Whether to liven up a classroom or add a playful element to social events, "Rational Bingo" is a cutting-edge tool that promises both entertainment and learning. Get ready for some fun!

## License
This project is open-sourced under the MIT license.

## Author
Higor Rabelo da Silva

For any inquiries or contributions to the project, please contact me at rabelohigor18@gmail.com.