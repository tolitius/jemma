def create_css_file(requirements):
    return f"""
You are a CSS expert with deep knowledge of Twitter Bootstrap CSS framework.

Your task is to generate a complete and working CSS file for a web prototype based on a twitter's "bootstrap.css" framework and the following requirements:

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

# IMPORTANT
Provide the CSS file content ONLY, without any additional text or explanations. The CSS file should be well-structured, organized, and easy to understand for developers working on the web prototype.

(!) make sure ALL the requirements and actions are addressed in the CSS file.
"""


def create_javascript_file(requirements, css):
    return f"""
You are a JavaScript expert who specializes in jQuery with a focus on Twitter Bootstrap and DataTables libraries.

Given requirements and a CSS file (based on "bootstrap.css") your task is to generate a JavaScript file that utilizes the jQuery library to create an interactive and dynamic web prototype based on these requirements that relies on that CSS file.

for tables, use a DataTables jQuery plugin to enhance the functionality and appearance of the tables.

This JavaScript file should be self-contained as this would be the only file that would be used to run the web prototype.

# REQUIREMENTS
{requirements}

# CSS FILE
{css}

follow these guidelines to create the JavaScript file:

# GUIDELINES
- Make sure layout pieces do not overlap or are not hidden by other elements.
- Make sure tables are used to store grid and tabular data
- Ensure that the generated JavaScript file seamlessly integrates with the provided CSS file.
- Instead of calling backend APIs populate test data or MINIMUM 7 entries in the JavaScript file to simulate the dynamic behavior of the web prototype.
  - doublechek that the data is visible to the user
  - doublecheck that the data is POPULATED
- Make sure edits happen in either inline within the table rows or in a modal window.
- do not forget to close all the code forms in parentheses, brackets, etc. $(function() {{ foo = [..] }});
- don't use todo action comments such as "// Add more test data here" or "// add code for to do X": instead IMPLEMENT the data / action

do NOT surround the file with markdown backticks: ```javascript ... ```
- start your response with a comment "// jQuery implementation"
- followed by the source code according to guidelines.
- ending with a comment "// prototype implementation"

IMPORTANT: Provide the JavaScript file content ONLY, without any additional text or explanations. The JavaScript file should be well-structured, organized, and easy to understand for developers working on the web prototype.

# IMPORTANT
(!) make sure ALL the requirements and actions are addressed in the JavaScript file.
"""

def create_html_file(requirements, css, js):
    return f"""
Code Generator Agent,

Given requirements, a CSS file (based on "bootstrap.css"), and a JavaScript file, your task is to generate a complete and semantic HTML file that serves as the foundation for the web prototype based on these requirements.
The HTML file should import these in the following order:

- remote "bootrap.css"
- remote dataTables css (for bootstrap 4, "dataTables.bootstrap4.css")
- local, previously generated, CSS: app.css
- remote jQuery library
- remote "popper.js"
- remote "bootrap.js"
- remote dataTables js
- remote dataTables js (for bootstrap 4, "dataTables.bootstrap4.js")
- local, previously generated, JavaScript: app.js

example:

  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css">
  <link href="https://cdn.datatables.net/2.0.3/css/dataTables.bootstrap4.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="app.css">
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js"></script>
  <script src="https://cdn.datatables.net/2.0.3/js/dataTables.js"></script>
  <script src="https://cdn.datatables.net/2.0.3/js/dataTables.bootstrap4.js"></script>
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

- rely on the BOOTSTRAP GRID SYSTEM to create a responsive layout.
  - (!) make sure the grid pieces, including offsets, in a single row do not exceed 12 columns.
  - (!) don't waste space, if an box (such as a "side menu") needs to be "col-1" or "col-2" make it so
- (!) make sure layout pieces do not overlap or are not hidden by other elements.
- make sure tables are used to store grid and tabular data

Please generate a complete and semantic HTML file that fulfills these requirements and creates the best layout and user experience possible. The generated HTML file should seamlessly integrate with the previously generated CSS and JavaScript files to form a cohesive web prototype.

do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and follow the guidelines.

IMPORTANT: Provide the HTML file content ONLY, without any additional text or explanations: no text headers, no footers. The HTML file should be well-structured, organized, and easy to understand for developers working on the web prototype.

# IMPORTANT
(!) make sure ALL the requirements and actions are addressed in the HTML file.
"""

def implement_user_story(approach,
                         requirements,
                         user_story,
                         existing_code = ""):
    return f"""You are an AI agent acting as an experienced software engineer. Your task is to implement a user story based on the provided approach, project requirements and existing code.

(!) provide NO EXPLAINATION, only the source code.

Follow these steps:
1. Review the project requirements for context and constraints.
2. Analyze the user story in Gherkin format and its acceptance criteria.
3. Implement the user story using the specified approach, ensuring it meets the acceptance criteria and project requirements.
4. Provide a complete, working implementation of the user story, including any necessary code, database schemas, API endpoints, or UI components.
5. Include comments in your code to explain key decisions, assumptions, or complex logic.
6. If any part of the implementation is unclear or requires further discussion, highlight it with a comment.
7. If existing code is provided, integrate your implementation with it, ensuring compatibility and consistency.

Approach:
{approach}

Project Requirements:
{requirements}

User Story:
{user_story}

Existing Code:
{existing_code}

extract ONLY source code from the existing code to reference it in your implementation.
"""

def default_implementation_approach():
    return """create a simple, but WORKING prototype.
use no libraries, dependencies or frameworks.
for UI use HTML, CSS and JavaScript.
for backend use Python
"""

def ui_prototype_implementation_approach():
    return """
Create a functional UI prototype that demonstrates the core functionality of the user story.

Guidelines:
- Use only HTML, CSS, and JavaScript in a single file to make it immediately runnable from the browser.
- Structure the HTML semantically, using appropriate tags for headings, sections, navigation, etc.
- Use inline CSS styles within the <style> tag in the <head> section of the HTML file.
- Implement the necessary interactivity using JavaScript within the <script> tag at the end of the <body> section.
- Use meaningful and diverse stub data that closely resembles real-life scenarios.
- If the user story requires data persistence, use the browser's local storage to store and retrieve data.
- Organize the code into separate sections for HTML, CSS, and JavaScript using comments for clarity.
- Keep the code clean, readable, and properly indented.
- Center the main content on the page, while positioning specific components (e.g., side menu) as required.
- Choose a simple color palette with 2-3 primary colors and appropriate contrast.
- Use a smooth, readable font for body text and a complementary font for headings.
- Ensure adequate whitespace and padding around elements to improve readability.
- Handle user input and events (e.g., clicks, form submissions) appropriately.
- Update the UI dynamically based on user actions and data changes.
- Validate user input and provide clear feedback and error messages.
- Test the prototype thoroughly across different screen sizes and devices to ensure responsiveness.

Example of the file structure:

<!DOCTYPE html>
<html>
<head>
  <title>UI Prototype</title>
  <style>
    /* CSS styles go here */
  </style>
</head>
<body>
  <!-- HTML content goes here -->

  <script>
    // JavaScript code goes here
  </script>
</body>
</html>

Remember, the goal is to create a self-contained, functional, and visually appealing prototype that showcases the core aspects of the user story. The prototype should be easily understandable by stakeholders and developers alike.

"""

def refactor_css_file(requirements,
                      prototype_css,
                      feedback):
    return f"""
Given the following information:

Original Requirements:
{requirements}

Existing Prototype CSS (using Twitter Bootstrap):
{prototype_css}

User Feedback:
{feedback}

Please refactor the CSS code, taking into account the original requirements and the user's feedback. Consider the following points:

1. Ensure that the refactored CSS aligns with the original requirements and incorporates the user's suggestions where appropriate.
2. Optimize the CSS for better performance, readability, and maintainability.
3. Use best practices and modern CSS techniques where applicable.
4. Keep in mind that the CSS code is using the Twitter Bootstrap library, so make sure to leverage Bootstrap classes and conventions where appropriate.

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

Refactored CSS (using Twitter Bootstrap):
{css}

Existing Prototype JavaScript (using jQuery and DataTables):
{prototype_js}

User Feedback:
{feedback}

Please refactor the JavaScript code, taking into account the original requirements, the refactored CSS, and the user's feedback. Consider the following points:

1. Ensure that the refactored JavaScript aligns with the original requirements and incorporates the user's suggestions where appropriate.
2. Optimize the JavaScript for better performance, readability, and maintainability.
3. Use best practices and modern JavaScript techniques where applicable.
4. Keep in mind that the JavaScript code is using the jQuery library and the DataTables plugin, so make sure to leverage their features and conventions where appropriate.
5. Ensure compatibility with the refactored CSS code, especially considering the use of Twitter Bootstrap classes and conventions.

do NOT surround the file with markdown backticks: ```javascript ... ```
- start your response with a comment "// jQuery implementation"
- followed by the source code according to guidelines.
- ending with a comment "// prototype implementation"

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

Refactored CSS (using Twitter Bootstrap):
{css}

Refactored JavaScript (using jQuery and DataTables):
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
5. Integrate the refactored JavaScript code seamlessly, making sure that all necessary elements have the correct IDs, classes, and data attributes required by jQuery and DataTables.
6. Improve the overall user experience and usability of the HTML page based on the user's feedback.

do NOT surround the file with markdown backticks: ```html ... ```
start the response with <!DOCTYPE html> and follow the instructions.

Please provide only the refactored HTML code without any additional explanations, comments. The code will be written into a separate "index.html" file.
    """
