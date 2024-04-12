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

<very comprehensive requirements>

<focus>
{focus}
"""
