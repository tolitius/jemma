def clarify_user_story(role,
                       requirements,
                       user_story,
                       engineer_response):
    return f"""
# INSTRUCTIONS
As the {role}, your task is to review the engineer's feedback on the user story and provide clarifications while ensuring the user story remains concise and focused on a single unit of work.

Consider the following guidelines:
1. Address the specific questions or points raised by the engineer.
2. Provide clear and concise clarifications without adding unnecessary details.
3. Ensure that the clarified user story still aligns with the overall feature requirements.
4. Keep the user story focused on a single, well-defined unit of work.
5. Use simple language and avoid ambiguity or vague statements.
6. If the engineer has confirmed that no clarification is needed, simply return the original user story.

you task is to return the clarified acceptance criteria of the original user story. ALL in the Gherkin format (Given/When/Then). and NOTHING ELSE: no headers, no footers, no explanations, just the user story.

Return the acceptance criteria of the original user story clarified in the following JSON format:

"Given <precondition>,",
"When <action>,",
"And <additional action>,",
"Then <expected outcome>.",
"",
"Given <precondition>,",
"When <action>,",
"And <additional action>,",
"And <additional action>,",
"Then <expected outcome>.",
"",
"<additional acceptance criterias>",
...

make sure the final acceptance criteria covers ALL the points raised by the engineer
AS WELL AS the previous acceptance criteria, so no context is lost

* Use clear and concise language
return this acceptance criteria without any additional text, headings or footers: just a list of acceptance criteria in Gherkin format.

# FEATURE REQUIREMENTS
{requirements}

# ORIGINAL USER STORY
{user_story}

# ENGINEER'S RESPONSE
{engineer_response}

# CLARIFIED USER STORY
"""

def split_requirements_to_features(role,
                                   requirements,
                                   evaluation,
                                   features):
    return f"""
# INSTRUCTIONS
As a {role}, your task is to take in:

* requirements: high level requirements for the project
* evaluation: previous feedback on the current features split
* features: the current features split

and, given all three, split the requirements into feature names by looking at the current features split and the previous evaluation.

# REQUIREMENTS
{requirements}

# FEATURES
{features}

# EVALUATION
{evaluation}

# GUIDELINES
1. Review the current features split and the previous evaluation.
2. Split the requirements into features based on evaluation and these guidelines.
3. Name them by their business goal and purpose: DON'T start their name with "Implement"
4. To determine the appropriate granularity of the features make sure each feature is
   - focused on a single business aspect of the requirements
   - cohesive busineswise
   - prefer delivering incremental value to the user
     - for example if something can be delivered read only with a follow up feature to edit or change, prefer that
5. Ensure that an individual feature is NOT too small to implement.
   - example of TOO SMALL:
     - "edit one field"
     - "when naviated to a link user can see a view"
     - "display a button, component on the screen"
     - "validate email field", etc.
6. Return each feaure on a separate line. Do not add empty lines.
7. Return no other information, only a list of features.
   - NO additional text, headers, or footers

Remember feature is not a small task, it is a business functionality
Make sure that the list of feature names FULLY addresses every aspect of the requirements.
think step by step before providing a response

# RESPONSE FORMAT EXAMPLE
<feature 1>: <description of feature 1>
<feature 2>: <description of feature 2>
<feature 3>: <description of feature 3>
<feature 4>: <description of feature 3>
<feature 5>: <description of feature 3>
...

(!) return a list of features ONLY: no other headers, footers, or additional text
"""

def evaluate_features(role, features, requirements):
    return f"""
# INSTRUCTIONS
As a {role}, your task is to evaluate the following feature names against the original requirements and decide whether the feedback is needed.

Your goal is to make sure requirements are split into features that are:
 - focused on a single business aspect of the requirements
 - cohesive busineswise
 - clear, concise
 - simple to implemented by the engineering team

Remember feature is not a small task but a business functionality

# FEATURES
{features}

# REQUIREMENTS
{requirements}

# RESPONSE FORMAT

**chain of thought**
<before providing a response think step by step>

**feedback about each features**
<feedback for individual features>
<DON'T include features that are satisfactory>

# GUIDELINES
1. Review features and assess whether it aligns with the original requirements
   - ask to remove any features that are not aligned with the requirements
2. Determine whether this split needs to change, provide feedback accordingly
3. (!) Prefer delivering incremental value to the user
       - for example if something can be delivered read only with a follow up feature to edit or change, prefer that
4. Ensure that an individual feature is NOT too small to implement.
   - example of TOO SMALL:
     - "edit one field"
     - "when naviated to a link user can see a view"
     - "display a button, component on the screen"
     - "validate email field", etc.
5. Don't include features that are satisfactory in the reponse
6. Stricly follow the "RESPONSE FORMAT" provided above
7. Only in case there no suggestions or improvements to the split, reply with "APPROVED AND READY FOR REFINEMENT" in uppercase
8. If the features are not split well and require to be split differently, provide feedback indicating so.

Make sure that the list of feature names FULLY addresses every aspect of the requirements.
Remember, these are not full descriptions of the features, but a high-level feature names.
"""

def refine_feature(role, project_requiements, feature):
    return f"""
# INSTRUCTIONS
As a {role}, your task is to given the project requirements refine the business feature
This feature was carefully carfted to be a single, isolated, cohesive piece of business functionality
Please keep it that way while refining

<PROJECT REQUIREMENTS>
{project_requiements}

<BUSINESS FEATURE>
{feature}

# GUIDELINES
1. Analyze the feature and identify any areas that need improvement in terms of:
   - Cohesiveness: Ensure that the feature focuses on a single, specific functionality or business goal.
   - Size: Ensure that the feature is small enough to be easily understood and implemented.
   - Clarity: Ensure that the feature is clear, concise, and free of ambiguity.
   - Simplicity: Ensure that the feature is simple enough for an engineer to implement without requiring further clarification.
2. If any improvements are needed, refine the feature by making the necessary changes.
3. Return the refined feature.
   - don't share any additional information
   - only the refined feature name, description and the final list of detailed requirements

Remember, the goal is to create a feature that is cohesive, small, clear, concise, and simple for the engineer to implement.

# EXAMPLE RESPONSE

## "Edit Account Details Inside the Table Row"

### Description
<A brief description of the this feature>

### Requirements
<a detailed list of requirements for this feature>
"""

def combine_user_stories(role,
                         requirements,
                         user_stories):
    return f"""
# INSTRUCTIONS
As the {role}, your task is to combine the provided user stories, and the original requirements, combine these user stories into a single, cohesive set of requirements that has all the necessary details and instructions for implementation.

# REQUIREMENTS
{requirements}

# USER STORIES
{user_stories}

# GUIDELINES
1. Review the original requirements and the provided user stories.
2. Combine the user stories into a single, cohesive set of requirements that cover all the necessary details.
3. Ensure that the combined requirements are clear, concise, and free of ambiguity.
4. Make sure the combined requirements are detailed enough for an engineer to implement without requiring further clarification.
5. Return the combined requirements.
   - don't share any additional information
"""

def idea_to_prompt(idea):
    return f"""
Title: Web App Prototype Prompt Generator

Description:
Create a prompt generator that takes a short-form web app idea and generates a detailed prompt for building a self-sufficient prototype using only HTML, CSS, and JavaScript. The generated prompt should guide an AI model to create a functional web app prototype based on the provided idea.

Web App Idea:
{idea}

Prompt:
[Web App Idea]
Description: [A brief description of the web app idea]

Desired Prompt Output:

Title: [Web App Name]

Description:
[A detailed description of the web app, including its purpose, main features, and target audience]

Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]
...

User Interface:
[A description of the desired user interface, including layout, design elements, and user interactions]

Functionality:
[Detailed explanations of the app's functionality, including any necessary algorithms, data processing, or dynamic behavior]

HTML Structure:
[Guidelines for structuring the HTML code, including specific elements, classes, and IDs to be used]

CSS Styling:
[Instructions for styling the app using CSS, including color scheme, typography, layout, and responsive design considerations]

JavaScript Interactivity:
[Directions for implementing interactivity and dynamic functionality using JavaScript, including event handling, data manipulation, and API integration if applicable]

Additional Considerations:
[Any additional features, optimizations, or best practices to keep in mind while building the prototype]

Note: The generated prompt should be clear, concise, and provide sufficient detail for an AI model to generate a functional web app prototype using only HTML, CSS, and JavaScript. The prompt should focus on guiding the model to create a self-sufficient prototype without relying on external libraries or frameworks.

Example Usage:
Input:
[Web App Idea]: Color Palette Generator
Description: A web app that generates color palettes based on user input, allowing users to discover and save color combinations for their projects.

Output:
Title: Color Palette Generator

Description:
The Color Palette Generator is a web app that helps users create, discover, and save beautiful color palettes for their design projects. Users can input a base color or select a random color, and the app will generate a visually appealing color palette based on color theory principles. The app will display the color palette along with the hex codes and RGB values for each color. Users can adjust the brightness and saturation of the colors, save their favorite palettes, and export them for use in their projects.

Requirements:
1. Color input: Allow users to input a base color using a color picker or by entering a hex code.
2. Random color generation: Provide an option to generate a random base color for the palette.
3. Color palette generation: Generate a visually appealing color palette based on the base color using color theory principles (e.g., complementary, analogous, triadic).
4. Color palette display: Show the generated color palette with the hex codes and RGB values for each color.
5. Color adjustment: Allow users to adjust the brightness and saturation of the colors in the palette.
6. Palette saving: Enable users to save their favorite color palettes for future reference.
7. Palette export: Provide options to export the color palette as an image or CSS code snippet.

User Interface:
The Color Palette Generator should have a clean, intuitive, and visually appealing user interface. The main section of the app should display the generated color palette, with each color shown as a large swatch along with its hex code and RGB values. The color input and random color generation options should be prominently placed above the palette. The color adjustment controls should be located below the palette, allowing users to easily tweak the brightness and saturation. The save and export options should be easily accessible, with clear labels and icons.

Functionality:
The app should use JavaScript to handle color input, generation, and manipulation. When a user inputs a base color or selects the random color option, the app should generate a color palette using predefined color theory algorithms. The generated colors should be displayed dynamically on the page, with their hex codes and RGB values updated in real-time. The color adjustment controls should use range sliders to allow users to modify the brightness and saturation of the colors. The adjusted colors should be updated instantly in the palette display. The save functionality should store the user's favorite palettes in the browser's local storage, while the export options should generate downloadable files or copy CSS code snippets to the clipboard.

HTML Structure:
The HTML structure should be semantically marked up and include the following main elements:
- Header with the app title and navigation menu
- Main section with the color input, random color button, and color palette display
- Color adjustment controls below the palette
- Save and export buttons
- Footer with any necessary information or links

Use appropriate classes and IDs for styling and JavaScript manipulation.

CSS Styling:
The CSS should provide an attractive and responsive design for the Color Palette Generator. Use a clean, modern color scheme that complements the generated color palettes. Ensure proper spacing, alignment, and sizing of elements. Use CSS Grid or Flexbox for the layout, and apply hover and focus states for interactive elements. Make the app responsive and mobile-friendly using media queries and relative units.

JavaScript Interactivity:
Use JavaScript to add interactivity and functionality to the app. Implement the following features:
- Color input and validation
- Random color generation
- Color palette generation based on color theory algorithms
- Real-time updates of color swatches, hex codes, and RGB values
- Color adjustment using range sliders
- Saving and loading of favorite palettes using local storage
- Exporting palettes as images or CSS code snippets

Organize the JavaScript code into modular functions and use descriptive variable and function names for clarity.

Additional Considerations:
- Implement accessibility best practices, such as proper color contrast and keyboard navigation support.
- Optimize the app's performance by minimizing DOM manipulation and using efficient algorithms for color generation and manipulation.
- Add error handling and validation for user inputs to ensure a smooth user experience.
- Consider adding a feature to share color palettes on social media or via unique URLs.
- Provide a help section or tutorial to guide users on how to use the app effectively.

By following this prompt, an AI model should be able to generate a self-sufficient and functional prototype of the Color Palette Generator web app using HTML, CSS, and JavaScript. The prototype should fulfill the specified requirements, provide an engaging user interface, and demonstrate the core functionality of the app idea.
"""

def idea_with_sketch_to_intel(idea, sketch):
    return f"""
Analyze the UI sketch in the image and extract the following structured information to be used to recreate this interface with HTML, CSS and JavaScript:

1. Identify all distinct UI components (text fields, labels, buttons, containers, etc.) and list them along with their:
   - Component type (input, button, div, etc.)
   - Text content
   - Placeholder text (if applicable)
   - Unique identifier (if applicable, e.g. "name", "toolbar", "upcoming-lesson", etc.)

2. Describe the overall layout and visual structure of the interface, including:
   - Relative positioning of components (e.g. "toolbar at top", "3 buttons below header", "2 column layout", etc.)
   - Any visual grouping or separation of components
   - Estimated dimensions and spacing (widths, heights, padding, margins)

3. Identify any interactive elements and describe their apparent functionality, for example:
   - "Courses dropdown opens menu on click"
   - "New buttons add new slot on click"
   - "'Concept' button likely opens a modal dialog", etc.

4. Call out any key visual styling details, such as:
   - Background colors
   - Font sizes, weights, and styles
   - Border styles
   - Button styles

Provide the extracted information in a structured JSON format like this:

{{
  "components": [
    {{
      "type": "input",
      "id": "name",
      "placeholder": "Name"
    }},
    ...
  ],
  "layout": {{
    "positioning": [...],
    "grouping": [...],
    "spacing": [...]
  }},
  "interactivity": [...],
  "styling": {{
    "colors": [...],
    "fonts": [...],
    ...
  }}
}}
    """

def sketch_intel_to_requirements(idea, sketch_intel):
    return f"""
Title: Web App Prototype Prompt Generator

Description:
Create a prompt generator that takes a short-form web app idea and a description of a mockup and generates a detailed prompt for building a self-sufficient prototype using only HTML, CSS, and JavaScript. The generated prompt should guide an AI model to create a functional web app prototype based on the provided idea and the mockup description. The generated prompt should make sure that the prototype 100% aligns with the visual structure and interactivity described in the mockup.

Web App Idea:
{idea}

Mockup Description:
{sketch_intel}

Prompt:
[Web App Idea]
Description: [A brief description of the web app idea]

Desired Prompt Output:

Title: [Web App Name]

Description:
[A detailed description of the web app, including its purpose, main features, and target audience]

Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]
...

User Interface:
[A description of the desired user interface, including layout, design elements, and user interactions based on the idea and mockup description]

Functionality:
[Detailed explanations of the app's functionality, including any necessary algorithms, data processing, or dynamic behavior based on the idea and mockup description]

HTML Structure:
[Guidelines for structuring the HTML code, including specific elements, classes, and IDs to be used based on the idea and mockup description]

CSS Styling:
[Instructions for styling the app using CSS, including color scheme, typography, layout, and responsive design considerations based on the idea and mockup description]

JavaScript Interactivity:
[Directions for implementing interactivity and dynamic functionality using JavaScript, including event handling, data manipulation, and API integration if applicable based on the idea and mockup description]

Additional Considerations:
[Any additional features, optimizations, or best practices to keep in mind while building the prototype based on the idea and mockup description]

Note: The generated prompt should be clear, concise, and provide sufficient detail for an AI model to generate a functional web app prototype using only HTML, CSS, and JavaScript. The prompt should focus on guiding the model to create a self-sufficient prototype relying on jQuery, Twitter Bootstrap and DataTable libraries.
"""
