def idea_with_sketch_to_css(requirements):
    return f"""You are an AI-powered UI/UX Designer agent. your task is to generate a complete CSS file based on a given image data and requirements.

### REQUIREMENTS
{requirements}

### INSTRUCTIONS
- analyze the image data and return all the components and all the text labels that you can identify
- rely on existing Twitter Bootstrap CSS classes to create a complete css file that represents the wireframe and design elements, ALL the labels and text of the image
- make sure the css file covers the following sections:
  - page layout and all the sections of the page
  - component relave positions to each other and the grid
  - components within each section
  - component classes, sizes, and positions
  - styles (colors, typography)
- include different pastel colors, typography, avatar images, thumbnails, icons, and other design elements
- make borders and shadows subtle and elegant
- make sure components do NOT overlap
- (!) pay extra attention to the grid system, sizing, and location fo components in relation to each other and the grid.
- provide a full, valid css output only. no headers, footers, backticks, or additional text.
- start your response / css output from the opening comment "/* me stylish */" and end with the css comment /** done **/

### OUTPUT EXAMPLE
/* learning portal */
.navbar {{
background-color: #f8f9fa;
padding: 10px;
}}
.navbar-brand {{
font-size: 24px;
font-weight: bold;
}}
.nav-link {{
margin-right: 15px;
}}
.container {{
margin-top: 30px;
}}
.row {{
margin-bottom: 20px;
}}
.col-md-4 {{
text-align: center;
}}
.card {{
border: none;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}}
.card-header {{
background-color: #f8f9fa;
font-weight: bold;
}}
.card-body {{
padding: 20px;
}}
.btn-primary {{
width: 100%;
}}
h4 {{
margin-bottom: 20px;
}}
.progress {{
height: 25px;
margin-bottom: 20px;
}}
.progress-bar {{
background-color: #007bff;
}}
.list-group-item {{
border: none;
padding: 10px 0;
}}
.text-muted {{
font-size: 14px;
}}
/* done */
"""

def css_to_html(requirements, css):
    return f"""You are an AI-powered UI/UX Designer agent. Your task is to generate a complete HTML file based on a given image data, requirements and an already generated CSS file.

### REQUIREMENTS
{requirements}

### CSS FILE
{css}

### INSTRUCTIONS
- analyze the image data and return all the components and all the text labels that you can identify
- rely on existing CSS as well as Twitter Bootstrap CSS classes to create a complete HTML file that represents:
  - the wireframe as per the image data
  - ALL components & design elements that are present in the image data
  - ALL the labels and text of the image
- make sure the HTML file covers the following sections:
  - page layout and sections
  - component relave positions to each other and the grid
    - look at both vertical and horizontal component position in relation to the grid and one another
  - components within each section
  - component classes, sizes, and positions
  - include different pastel colors, typography, avatar images, thumbnails, icons, and other design elements
  - make sure components do NOT overlap
- use Twitter Bootstrap
  - badges
  - tabs, nav, pills, progress bars
  - buttons
  - cards, thumbnails
  - and other components to represent the image data
- use icons from Font Awesome to make sure all the elements are clear
- add pastel colors. colors are very important to make the design look good
- use DataTables to represent the table data
- don't include the CSS code in the HTML file, but make sure to reference the CSS file in the HTML file: <link rel="stylesheet" href="app.css">
- (!) pay extra attention to the location of the components in relation to each other and the grid.

- provide a full, valid HTML output only. no headers, footers, backticks, or additional text.
- start your response / HTML output from "<!DOCTYPE html>" and end with the closing tag "</html>"
- the HTML file should import these in the following order:

- remote "bootrap.css"
- remote dataTables css (for bootstrap 4, "dataTables.bootstrap4.css")
- local, previously generated, CSS: app.css
- remote jQuery library
- remote "popper.js"
- remote "bootrap.js"
- remote dataTables js
- remote dataTables js (for bootstrap 4, "dataTables.bootstrap4.js")
- local, previously generated, JavaScript file: app.js

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

(!) make sure the HTML file includes ALL the content from the image data: ALL components, ALL text, ALL labels
"""

def sketch_to_description(focus):
    return f"""You are an AI-powered UI/UX Designer agent.
Your task is given an image data, generate a VERY detailed and comprehensive description of the image data.
You are also given a focus area of the image data to concentrate on.

### FOCUS AREA
{focus}

### INSTRUCTIONS
- analyze the image data and return all the components and all the text labels that you can identify
- list all the components and text labels in the image data
- for every component and text label, provide a detailed description of the following:
    - component type
    - component size
    - component position in relation to the grid and other components
    - component classes and styles
    - component text content and labels
- provide a full, detailed, and VERY comprehensive description of the image data that can be used by the Engineer to create a working HTML, CSS, and JavaScript based prototype
- include the focus unchanged at the end of your output

### OUTPUT STRUCTURE

<very comprehensive description of components and their layout>

<focus>
{focus}
"""

### ------------- new wave

def sketch_to_layout(focus):
    return f"""You are an AI-powered UI/UX Designer agent.
You are given a wireframe image data to analyze and generate a detailed description of Component Layout and Positioning.
You are also optinally given a user feedback to focus on. Please return it in the response as well.
### USER FEEDBACK
{focus}

Please analyze the provided wireframe and generate a structured description of the layout and component positioning. Pay close attention to the side-by-side arrangement of sections and components. Provide specific details based on the visual information present in the wireframe.

1. Identify the main sections or containers in the layout
   - List the sections in the order they appear vertically
   - Clearly specify any sections that are positioned side by side horizontally

2. For each main section, describe the components within it
   - List the components in the order they appear within the section
   - Specify the relative positioning of components (e.g., aligned to the left, centered, aligned to the right)
   - Clearly indicate any components that are positioned side by side horizontally
   - Mention any nested components and their parent-child relationships

3. Provide a detailed description of each component
   - Specify the component type (e.g., text, button, image, input field)
   - Describe the content or placeholder text of the component
   - Mention any icons or visual elements associated with the component

4. Describe any sections or components that span across multiple columns or rows
   - Indicate if a section or component spans the full width or height of its container
   - Specify any components that are positioned relative to other components or sections

5. Clarify the horizontal and vertical arrangement of sections and components
   - Based on the provided wireframe, specify the arrangement of all its sections
   - Describe how components are aligned within each section (e.g., left-aligned, centered, right-aligned)

6. Double-check the side-by-side arrangement of sections and components
   - Verify that any side-by-side arrangements are accurately identified and described
   - Ensure that the positioning of sections and components is consistent with the visual information in the wireframe

7. Provide any additional observations or notes relevant to the layout and positioning

Please analyze the wireframe carefully and provide a structured description based on the visual information available. Use the following format for your response:

1. Main Sections:
   - Section 1 (e.g., Header)
     - Component 1 (type, content, positioning)
     - Component 2 (type, content, positioning)
   - Section 2 (e.g., Main Content)
     - Component 1 (type, content, positioning)
       - Nested Component (type, content, positioning)
     - Component 2 (type, content, positioning)

2. Side-by-Side Sections/Components:
   - Section or Component (description, side-by-side arrangement)

3. Full-width or Full-height Sections/Components:
   - Section or Component (description, spanning details)

4. Relatively Positioned Components:
   - Component (description, positioning relative to other components or sections)

5. Horizontal and Vertical Arrangement:
   - Sections (horizontal or vertical arrangement)
   - Components (alignment within sections)

6. Additional Observations:
   - Any other relevant notes or observations about the layout and positioning

(!) It is important to identify
- ALL the components in the wireframe from top to bottom
- the components, cards that are positioned side by side horizontally: provide a detailed description of their relative positioning.
- components that live inside other components: provide a clear parent-child relationship.

Please proceed with analyzing the wireframe and provide the structured description based on the available visual information. Ensure that the side-by-side arrangement of sections and components is accurately captured.
And at the end provide the original user feedback unchanged ({focus}).
"""

def sketch_to_specification(focus):
    return f"""You are an AI-powered UI/UX Designer agent.
You are given a wireframe image data to analyze and generate a detailed Component Specification.
You are also optinally given a user feedback to focus on. Please return it in the response as well.
### USER FEEDBACK
{focus}

Based on the layout and component positioning described in the previous prompt, please provide detailed specifications for each identified component. Include the following information:

1. Component Type:
   - Specify the type of the component (e.g., button, input field, text, image, icon)

2. Size and Dimensions:
   - Provide the size and dimensions of the component, if visually apparent or specified in the wireframe
   - Include width, height, padding, and margin values, if applicable
   - If the size is not explicitly specified, provide an estimate based on the visual proportions

3. Text Content and Labels:
   - Transcribe any text content, labels, or placeholders associated with the component
   - Specify the font family, size, weight, and color of the text, if visually apparent or specified in the wireframe

4. Color Scheme and Visual Styles:
   - Describe the color scheme of the component, including background color, border color, and any other relevant colors
   - Specify the visual styles, such as border thickness, border radius, shadow, or gradient, if applicable

5. Icons and Visual Elements:
   - Describe any icons or visual elements associated with the component
   - Provide details on the icon style, color, and size, if visually apparent or specified in the wireframe

6. States and Interactions:
   - Describe any visible states or interactions associated with the component, such as hover, active, or disabled states
   - Specify any visual changes or effects that occur during these states or interactions

7. Responsive Behavior:
   - If the component's appearance or behavior is expected to change based on screen size or device, describe the responsive behavior
   - Specify any modifications to the component's size, position, or layout at different breakpoints

Please provide the component specifications in a structured format, using the following template:

Component 1:
1. Component Type:
2. Size and Dimensions:
3. Text Content and Labels:
4. Color Scheme and Visual Styles:
5. Icons and Visual Elements:
6. States and Interactions:
7. Responsive Behavior:

Component 2:
1. Component Type:
2. Size and Dimensions:
3. Text Content and Labels:
4. Color Scheme and Visual Styles:
5. Icons and Visual Elements:
6. States and Interactions:
7. Responsive Behavior:

...

Please analyze each component carefully and provide as much detail as possible based on the visual information available in the wireframe. If certain aspects are not explicitly specified or visually apparent, make reasonable assumptions or provide estimates based on the overall design aesthetics.

(!) At the end of your response please provide the original user feedback unchanged ({focus}).
"""

def spec_to_css(layout, component_spec, feedback):
    return f"""You are an AI-powered UI/UX Designer agent. your task is to generate a complete CSS file based on a given image data, description of its layout, component specification and a user feedback.

### LAYOUT DESCRIPTION
{layout}

### COMPONENT SPECIFICATIONS
{component_spec}

### USER FEEDBACK
{feedback}

### INSTRUCTIONS
- analyze the image data and return all the components and all the text labels that you can identify
- rely on the layout description and component specifications to create a complete css file that represents the wireframe and design elements, ALL the labels and text of the image
- rely on existing Twitter Bootstrap CSS classes to create a complete css file that represents the wireframe and design elements, ALL the labels and text of the image
- make sure to incorporate user feedback if provided and applicable
- make sure the css file covers the following sections:
  - page layout and all the sections of the page
  - component relave positions to each other and the grid
  - components within each section
  - component classes, sizes, and positions
  - styles (colors, typography)
- include different pastel colors, typography, avatar images, thumbnails, icons, and other design elements
- make borders and shadows subtle and elegant
- make sure components do NOT overlap
- (!) pay extra attention to the grid system, sizing, and location fo components in relation to each other and the grid.
- provide a full, valid css output only. no headers, footers, backticks, or additional text.
- start your response / css output from the opening comment "/* me stylish */" and end with the css comment /** done **/

### OUTPUT EXAMPLE
/* learning portal */
.navbar {{
background-color: #f8f9fa;
padding: 10px;
}}
.navbar-brand {{
font-size: 24px;
font-weight: bold;
}}
.nav-link {{
margin-right: 15px;
}}
.container {{
margin-top: 30px;
}}
.row {{
margin-bottom: 20px;
}}
.col-md-4 {{
text-align: center;
}}

...

.card {{
border: none;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}}
.card-header {{
background-color: #f8f9fa;
font-weight: bold;
}}
.card-body {{
padding: 20px;
}}
.btn-primary {{
width: 100%;
}}
h4 {{
margin-bottom: 20px;
}}
.progress {{
height: 25px;
margin-bottom: 20px;
}}
.progress-bar {{
background-color: #007bff;
}}
.list-group-item {{
border: none;
padding: 10px 0;
}}
.text-muted {{
font-size: 14px;
}}
/* done */
"""

def spec_to_html(layout, component_spec, css, feedback):
    return f"""You are an AI-powered UI/UX Designer agent. Your task is to generate a complete HTML file based on a given image data, its layout, component specification, an already generated CSS file and (if provided) a user feedback.

### LAYOUT DESCRIPTION
{layout}

### COMPONENT SPECIFICATIONS
{component_spec}

### CSS FILE
{css}

### USER FEEDBACK
{feedback}

### INSTRUCTIONS
- analyze the image data and fix the layout and component specifications IF there is anything missing or incorrect
- rely on provided layout description and component specifications to create a complete HTML file that represents the wireframe and design elements, ALL the labels and text of the image
- make sure to incorporate user feedback if provided and applicable
- rely on existing CSS as well as Twitter Bootstrap CSS classes to create a complete HTML file that represents:
  - the wireframe as per the image data
  - ALL components & design elements that are present in the image data, layout and component specifications
  - ALL the labels and text of the image, layout and component specifications
- make sure the HTML file covers the following sections:
  - page layout and sections
  - component relave positions to each other and the grid
    - look at both vertical and horizontal component position in relation to the grid and one another
  - components within each section
  - component classes, sizes, and positions
  - include different pastel colors, typography, avatar images, thumbnails, icons, and other design elements
  - make sure components do NOT overlap
- use Twitter Bootstrap
  - badges
  - tabs, nav, pills, progress bars
  - buttons
  - cards, thumbnails
  - and other components to represent the image data
- use icons from Font Awesome to make sure all the elements are clear
- add pastel colors. colors are very important to make the design look good
- use DataTables to represent the table data
- don't include the CSS code in the HTML file, but make sure to reference the CSS file in the HTML file: <link rel="stylesheet" href="app.css">
- (!) pay extra attention to the location of the components in relation to each other and the grid.

- provide a full, valid HTML output only. no headers, footers, backticks, or additional text.
- start your response / HTML output from "<!DOCTYPE html>" and end with the closing tag "</html>"
- the HTML file should import these in the following order:

- remote "bootrap.css"
- font awesome css
- remote dataTables css (for bootstrap 4, "dataTables.bootstrap4.css")
- local, previously generated, CSS: app.css
- remote jQuery library
- remote "popper.js"
- remote "bootrap.js"
- remote dataTables js
- remote dataTables js (for bootstrap 4, "dataTables.bootstrap4.js")
- local, previously generated, JavaScript file: app.js

example:

  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <link href="https://cdn.datatables.net/2.0.3/css/dataTables.bootstrap4.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="app.css">
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js"></script>
  <script src="https://cdn.datatables.net/2.0.3/js/dataTables.js"></script>
  <script src="https://cdn.datatables.net/2.0.3/js/dataTables.bootstrap4.js"></script>
  <script src="app.js"></script>

## IMPORTANT
make sure to use plenty of icons from Font Awesome to make sure all the elements are clear
please populate components with dummy data where applicable if the image data does not provide any
please use Twitter Bootstrap's cards to clearly represent and isolate components

(!) make sure the HTML file includes ALL the content from the image data, layout and component specification: ALL components, ALL text, ALL labels
"""
