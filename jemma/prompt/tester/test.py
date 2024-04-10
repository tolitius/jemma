## TODO: test it in a headless environment
# def test_code(role, requirements, html, css, js):

def review_code(role, requirements, html, css, js):
    return f"""
you are {role}

#INSTRUCTIONS
given the following requirements, a CSS file, a JavaScript file, and an HTML file, your task is to review the HTML file to ensure it meets ALL the requirements and integrates correctly with the CSS and JavaScript files.

#REQUIREMENTS
{requirements}

#CSS FILE
{css}

#JAVASCRIPT FILE
{js}

#HTML FILE
{html}

#REVIEW CRITERIA
1. Document Structure:
   - Verify that the HTML file has a valid structure with the correct doctype, head, and body elements.
   - Check if the CSS and JavaScript files are correctly linked in the HTML file.
   - Ensure that the file paths for the CSS and JavaScript files are relative and accurate.
   - Confirm that the required data is not hidden and visible.
2. Requirements Compliance:
   - Ensure that all CSS, JavaScript and HTML files addresses ALL the specified requirements from the user story.
3. Find errors and bugs
   - The main objective of this review is to find errors and bugs in these 3 files: FIND THEM ALL

#REVIEW RESPONSE
- Provide an actionable list of fixes and improvements for all three files (HTML, CSS, and JavaScript) based on the requirements.
- Make sure to include any missing elements, incorrect implementations, or potential enhancements to meet the user story requirements.
- There is always room for improvement, so be thorough in your review and provide detailed feedback.
- The idea is no to include new features, but to make sure the existing ones are implemented correctly.
- (!) after comminicating step by step thinking ONLY share ERRORS, BUGS and IMPROVEMENTS

(!) Before responding with the actual review, THINK STEP BY STEP what you would do to review the files and then provide the feedback.
    """
