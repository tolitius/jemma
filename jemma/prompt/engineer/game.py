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

make sure the game-container and game-canvas are styled by ids as follows:
#game-container {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}
#game-canvas {{
  border: 2px solid #00FFFF;
  box-shadow: 0 0 20px 0 #00FFFF;
}}


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
   - Make sure there is no sound in the game
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

Implement the startGame function completely, including all the necessary game logic and interactions. The startGame function should be the entry point for the game and should set up the game environment, initialize game objects, and start the game loop.

do not include a "preload" function since we are not using images, but instead built-in shapes such as "circles, squares, dots, etc.".

instead use basic shapes in "create" function to represent game elements.
### EXAMPLE OF USING BUILT-IN SHAPES IN PHASER CREATE FUNCTION:
function create() {{
  // Set up the game world
  game.physics.startSystem(Phaser.Physics.ARCADE);
  game.stage.backgroundColor = '#000000';

  // Create the player's spaceship
  player = game.add.graphics(400, 550);
  player.beginFill(0xffffff);
  player.drawRect(-20, -20, 40, 40);
  player.endFill();
  game.physics.arcade.enable(player);
  player.body.collideWorldBounds = true;
  player.body.immovable = true;

  // Create the enemy ships
  enemies = game.add.group();
  enemies.enableBody = true;
  enemies.physicsBodyType = Phaser.Physics.ARCADE;

  // Create the player's projectiles
  playerProjectiles = game.add.group();
  playerProjectiles.enableBody = true;
  playerProjectiles.physicsBodyType = Phaser.Physics.ARCADE;

  // Create the enemy projectiles
  enemyProjectiles = game.add.group();
  enemyProjectiles.enableBody = true;
  enemyProjectiles.physicsBodyType = Phaser.Physics.ARCADE;

  // Create the UI elements
  scoreText = game.add.text(16, 16, 'Score: 0', {{ fontSize: '32px', fill: '#fff' }});
  highScoreText = game.add.text(game.width - 200, 16, 'High Score: 0', {{ fontSize: '32px', fill: '#fff' }});
  startButton = game.add.text(game.width / 2, game.height / 2, 'Start Game', {{ fontSize: '24px', fill: '#fff' }});
  startButton.anchor.set(0.5);
  startButton.inputEnabled = true;
  startButton.events.onInputDown.add(startGame, this);

  // Initialize game variables
  score = 0;
  highScore = 0;
  gameStarted = false;
}}

make action functions to to create basic shapes instead of using loaded assets
### EXAMPLE OF ACTION FUNCTION TO CREATE BASIC SHAPES:
function fireBullet(x, y, xVelocity, yVelocity, group) {{
  var bullet = group.create(x, y, null);
  var graphics = game.add.graphics(0, 0);
  graphics.beginFill(0x00FF00);
  graphics.drawRect(0, 0, 10, 20);
  graphics.endFill();
  bullet.addChild(graphics);
  bullet.body.velocity.x = xVelocity;
  bullet.body.velocity.y = yVelocity;
}}

since we are using built-in shapes,
make sure to create individual Sprite objects for each object and then draw the shapes on those sprites.
### EXAMPLE OF CREATING SPRITES AND DRAWING SHAPES:
function spawnEnemies() {{
  if (enemies.countLiving() === 0) {{
    for (var y = 100; y < 400; y += 50) {{
      for (var x = 100; x < 700; x += 50) {{
        var enemy = enemies.create(x, y, null);
        var graphics = game.add.graphics(0, 0);
        graphics.beginFill(0xFF0000);
        graphics.drawCircle(0, 0, 20);
        graphics.endFill();
        enemy.addChild(graphics);
        enemy.body.velocity.y = ENEMY_SPEED;
      }}
    }}
  }}
}}

make sure to load the game in Phaser that matches CSS sizing as well as attaches to the game container:
parent: 'game-container',
canvas: document.getElementById('game-canvas'),

### EXAMPLE OF LOADING THE GAME IN PHASER:
// make sure the Phaser Game starts exactly like this:
var game = new Phaser.Game({{
  width: 800,  // Match the CSS
  height: 600, // Match the CSS
  renderer: Phaser.AUTO,
  parent: 'game-container',
  canvas: document.getElementById('game-canvas'),
  state: {{ preload: preload, create: create, update: update }}
}});

make sure not to play an animation on a sprite that doesn't have a loaded texture or spritesheet
for this add a remove effects correctly:
### EXAMPLE OF REMOVING EFFECTS:
function createExplosion(x, y) {{
  var explosion = explosions.create(x, y, null);
  var graphics = game.add.graphics(0, 0);
  graphics.beginFill(0xFF9900);
  graphics.drawCircle(0, 0, 50);
  graphics.endFill();
  explosion.addChild(graphics);
  explosion.scale.set(0.5);

  // Remove the explosion after a short delay
  game.time.events.add(200, function() {{
    explosion.kill();
  }}, this);
}}

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
- remote Phaser framework library ("https://cdnjs.cloudflare.com/ajax/libs/phaser/2.6.2/phaser.js")
- local, previously generated, JavaScript: app.js

and adhere to the following requirements to create the best layout and user experience possible.

# REQUIREMENTS
{requirements}

# CSS FILE
{css}

# JAVASCRIPT FILE
{js}

HTML body should only have the "game-container" div and NO OTHER COMPONENTS:
### EXAMPLE OF HTML BODY:
<!DOCTYPE html>
<html>
<head>
  <title>Retro Galaga Game</title>
  <link rel="stylesheet" type="text/css" href="app.css">
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
</head>
<body>
  <div id="game-container"/>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/phaser/2.6.2/phaser.js"></script>
  <script src="app.js"></script>
</body>
</html>

do not add scores, buttons, or any other elements to the HTML file. The game will be controlled by the JavaScript file and styled by the CSS file.

IMPORTANT: Provide the HTML file content ONLY, without any additional text or explanations: no text headers, no footers.
do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and end with </html>
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
4. Ensure compatibility with the refactored CSS code, especially considering the use of Twitter Bootstrap classes and conventions.
5. Integrate the refactored JavaScript code seamlessly, making sure that all necessary elements have the correct IDs, classes, and data attributes required by Phaser.
6. Improve the overall user experience and usability of the HTML page based on the user's feedback.

do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and follow the instructions.

Please provide only the refactored HTML code without any additional explanations, comments. The code will be written into a separate "index.html" file.
    """
