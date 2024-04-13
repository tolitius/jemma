def create_css_file(requirements):
    return f"""
You are a CSS expert with deep knowledge of Phaser HTML5 game framework.

Your task is to generate a complete and working CSS file for a web prototype based on the Phaser framework and the following requirements:

# REQUIREMENTS
{requirements}

follow these guidelines to create the CSS file:

# GUIDELINES
- Implement a color scheme with pastel colors that creates a pleasing atmosphere.
  - USE colors on a brighter side effectively to create visual hierarchy, highlight important elements, and convey the desired mood.
- Use appropriate margins, paddings, and spacing to create a balanced and visually pleasing arrangement.
  - (!) make sure DataTables are styled and flexible width so they don't overflow
- Choose a clean and readable font family for headings and body text
  - make font small enough to fit the content
- Make sure top and side margins and paddings make user focus on the main content
- Use Bootstrap's grid system to create a responsive layout
  - align menu items in a single row whether it is vertical or horizontal

Please generate a complete CSS file that fulfills these requirements and provides a beautiful, user-friendly, and responsive design for the web prototype. The generated CSS file should be ready to be integrated with the corresponding HTML and JavaScript files.

do NOT surround the file with markdown backticks: ```css ... ```
start the response with /* Global Styles */ and follow with CSS source according the guidelines.

(!) Use Phaser's default styles as a starting point and customize them as needed to match the game's aesthetic requirements. Since we are using built-in shapes instead of images, focus on styling the shapes using CSS properties like background color, border, and border-radius."

EXAMPLE OF USING DEFAULT SHAPES IN PHASER:
.paddle {{
  background-color: white;
  border-radius: 10px;
}}

.ball {{
  background-color: white;
  border-radius: 50%;
}}

.brick {{
  background-color: red;
  border: 1px solid black;
}}

# IMPORTANT
Provide the CSS file content ONLY, without any additional text or explanations. The CSS file should be well-structured, organized, and easy to understand for developers working on the web prototype.

(!) make sure ALL the requirements and actions are addressed in the CSS file.
"""


def create_javascript_file(requirements, css):
    return f"""
You are a JavaScript expert who specializes in game development with a focus on Phaser HTML5 game framework.

Given requirements and a CSS file (based on Phaser framework) your task is to generate a JavaScript file that utilizes the the Phaser framework to create an interactive and dynamic web prototype based on these requirements that relies on that CSS file.

This JavaScript file should be self-contained as this would be the only file that would be used to run the web prototype.

# REQUIREMENTS
{requirements}

# CSS FILE
{css}

follow these guidelines to create the JavaScript file:

# GUIDELINES
The game implementation should include the following features and components:

1. Game Board:
   - Create a visually appealing game board using Phaser's graphics objects to represent the play area.
   - Design the game board to match the theme and style of the game.

2. Player Character:
   - Create a player character using appropriate shapes and position it on the game board.
   - Implement player character movement and controls based on user input (e.g., arrow keys, touch controls).
   - Ensure the player character interacts properly with other game elements and stays within the game boundaries.

3. Game Objects:
   - Create various game objects (e.g., obstacles, enemies, collectibles) using suitable shapes and position them on the game board.
   - Implement collision detection between the player character and game objects.
   - Define the behavior and effects of game objects when they interact with the player character.

4. Scoring and Progression:
   - Implement a scoring system that awards points based on player actions and achievements.
   - Create a visual display to show the current score, level, and other relevant information.
   - Define conditions for level progression and implement level transitions seamlessly.

5. Power-ups and Bonuses:
   - Implement power-ups and bonuses that enhance gameplay and provide temporary advantages to the player.
   - Spawn power-ups and bonuses at appropriate times and locations on the game board.
   - Define the effects and duration of each power-up and bonus.

6. User Interface:
   - Create an intuitive and visually appealing user interface for the game.
   - Implement menus, buttons, and text displays for game controls, settings, and information.
   - Ensure the user interface is responsive and provides a smooth user experience.

7. Sound and Visual Effects:
   - Incorporate appropriate sound effects and background music to enhance the gaming experience.
   - Use Phaser's sound API to play audio files and manage sound playback.
   - Create visual effects (e.g., particle effects, animations) to provide visual feedback and enhance the game's aesthetics.

8. Game State Management:
   - Implement proper game state management, including game start, pause, resume, and game over states.
   - Define conditions for game over and level completion, and handle these events appropriately.
   - Allow players to restart the game or return to the main menu after game over.

9. Code Organization and Best Practices:
   - Organize the code into logical modules and functions for better readability and maintainability.
   - Use meaningful variable and function names that describe their purpose.
   - Follow best practices for code formatting, indentation, and commenting.
   - Optimize the code for performance and consider mobile compatibility if applicable.

10. Testing and Debugging:
    - Thoroughly test the game to identify and fix any bugs or glitches.
    - Ensure the game runs smoothly on different devices and browsers.
    - Implement error handling and logging mechanisms for easier debugging and troubleshooting.

- Ensure that the generated JavaScript file seamlessly integrates with the provided CSS file.
- do not forget to close all the code forms in parentheses, brackets, etc. $(function() {{ foo = [..] }});
- don't use todo action comments such as "// Add more test data here" or "// add code for to do X": instead IMPLEMENT the data / action

do NOT surround the file with markdown backticks: ```javascript ... ```
- start your response with a comment "// game implementation"
- followed by the source code according to guidelines.
- ending with a comment "// built by Jemma with bytes"

IMPORTANT: Provide the JavaScript file content ONLY, without any additional text or explanations. The JavaScript file should be well-structured, organized, and easy to understand for developers working on the web prototype.

(!) Use Phaser's built-in shapes like Rectangle, Circle, and Graphics to represent game elements instead of loading external images.

# EXAMPLE OF USING BUILT-IN SHAPES IN PHASER:
// Create the paddle
let paddle = this.add.rectangle(400, 550, 120, 20, 0xffffff);

// Create the ball
let ball = this.add.circle(400, 300, 10, 0xffffff);

// Create the bricks
let bricks = this.add.group();
for (let row = 0; row < 4; row++) {{
  for (let col = 0; col < 10; col++) {{
    let brick = this.add.rectangle(col * 80 + 40, row * 40 + 40, 70, 30, 0xff0000);
    bricks.add(brick);
  }}
}}


# IMPORTANT
(!) make sure ALL the requirements and actions are addressed in the JavaScript file.
"""

def create_html_file(requirements, css, js):
    return f"""
You are a web developer with deep expertise in HTML5 creating interactive web games using Phaser game framework, HTML5, CSS, and JavaScript.

Given requirements, a CSS file (based on Phaser), and a JavaScript file, your task is to generate a complete and semantic HTML file that serves as the foundation for the web based game based on these requirements.
The HTML file should import these in the following order:

- local, previously generated, CSS: app.css
- remote Phaser framework library ("https://cdn.jsdelivr.net/npm/phaser@3.80.0/dist/phaser.js")
- local, previously generated, JavaScript: app.js

example:

  <link rel="stylesheet" type="text/css" href="app.css">

  <script src="https://cdn.jsdelivr.net/npm/phaser@3.80.0/dist/phaser.js"></script>
  <script src="app.js"></script>

and adhere to the following requirements to create the best layout and user experience possible.

# REQUIREMENTS
{requirements}

# CSS FILE
{css}

# JAVASCRIPT FILE
{js}

follow these guidelines to create the HTML file:

# GUIDELINES

- Link the previously generated CSS file in the head section using the appropriate `<link>` tag.
- Place the previously generated JavaScript file before the closing `</body>` tag using the `<script>` tag.
- Ensure that the file paths for the CSS and JavaScript files are correct and relative to the HTML file.

- do NOT create elements that are not required by the user story.

- (!) make sure layout pieces do not overlap or are not hidden by other elements.

Please generate a complete and semantic HTML file that fulfills these requirements and creates the best layout and user experience possible. The generated HTML file should seamlessly integrate with the previously generated CSS and JavaScript files to form a cohesive web prototype.

do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and follow the guidelines.

IMPORTANT: Provide the HTML file content ONLY, without any additional text or explanations: no text headers, no footers. The HTML file should be well-structured, organized, and easy to understand for developers working on the web prototype.

please create an HTML file that serves as the container for the game. Include the necessary script tags to load the Phaser library and the game's JavaScript file. Also, include any required HTML elements for the game's user interface. Since we are using built-in shapes, no additional HTML elements are needed for game objects.

# EXAMPLE OF LOADING PHASER LIBRARY AND GAME SCRIPT:
<!DOCTYPE html>
<html>
<head>
  <title>Arkanoid Game</title>
  <script src="https://cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.min.js"></script>
  <link rel="stylesheet" href="game.css">
</head>
<body>
  <div id="game-container"></div>
  <script src="game.js"></script>
</body>
</html>


# IMPORTANT
(!) make sure ALL the requirements and actions are addressed in the HTML file.
"""



## TODO: refactor prompts
def refactor_css_file(requirements,
                      prototype_css,
                      feedback):
    return f"""
Given the following information:

Original Requirements:
{requirements}

Existing Prototype CSS (using Phaser HTML5 game framework):
{prototype_css}

User Feedback:
{feedback}

Please refactor the CSS code, taking into account the original requirements and the user's feedback. Consider the following points:

1. Ensure that the refactored CSS aligns with the original requirements and incorporates the user's suggestions where appropriate.
2. Optimize the CSS for better performance, readability, and maintainability.
3. Use best practices and modern CSS techniques where applicable.
4. Keep in mind that the CSS code is using the Phaserlibrary, so make sure to leverage Phaser conventions where appropriate.

do NOT surround the file with markdown backticks: ```css ... ```
start the response with /* Global Styles */ and follow with CSS source according the guidelines.

Please provide only the refactored CSS code without any additional explanations or comments. The code will be written into a separate "app.css" file.
    """

def refactor_javascript_file(requirements,
                             css,
                             prototype_js,
                             feedback):
    return f"""
Given the following information:

Original Requirements:
{requirements}

Refactored CSS (using Phaser HTML5 game framework):
{css}

Existing Prototype JavaScript (using Phaser HTML5 game framework):
{prototype_js}

User Feedback:
{feedback}

Please refactor the JavaScript code, taking into account the original requirements, the refactored CSS, and the user's feedback. Consider the following points:

1. Ensure that the refactored JavaScript aligns with the original requirements and incorporates the user's suggestions where appropriate.
2. Optimize the JavaScript for better performance, readability, and maintainability.
3. Use best practices and modern JavaScript techniques where applicable.
4. Keep in mind that the JavaScript code is using the Phaser HTML5 game framework, so make sure to leverage their features and conventions where appropriate.
5. Ensure compatibility with the refactored CSS code, especially considering the use of Phaser.

do NOT surround the file with markdown backticks: ```javascript ... ```
- start your response with a comment "// game implementation"
- followed by the source code according to guidelines.
- ending with a comment "// improved by Jemma with bytes"

Please provide only the refactored JavaScript code without any additional explanations or comments. The code will be written into a separate "app.js" file.
    """

def refactor_html_file(requirements,
                       css,
                       js,
                       prototype_html,
                       feedback):
    return f"""
Given the following information:

Original Requirements:
{requirements}

Refactored CSS (using Phaser HTML5 game framework):
{css}

Refactored JavaScript (using Phaser HTML5 game framework):
{js}

Existing Prototype HTML:
{prototype_html}

User Feedback:
{feedback}

Please refactor the HTML code, taking into account the original requirements, the refactored CSS and JavaScript, and the user's feedback. Consider the following points:

1. Ensure that the refactored HTML aligns with the original requirements and incorporates the user's suggestions where appropriate.
2. Optimize the HTML structure for better semantics, accessibility, and SEO.
3. Use appropriate HTML5 elements and attributes where applicable.
4. Ensure compatibility with the refactored CSS code, especially considering the use of Phaser conventions.
5. Integrate the refactored JavaScript code seamlessly, making sure that all necessary elements have the correct IDs, classes, and data attributes required by Phaser.
6. Improve the overall user experience and usability of the HTML page based on the user's feedback.

do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and follow the instructions.

Please provide only the refactored HTML code without any additional explanations, comments. The code will be written into a separate "index.html" file.
    """
