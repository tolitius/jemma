import webbrowser, requests
import os, argparse, sys, re, base64

from datetime import datetime

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   GRAY_DARK = '\033[38;5;232m'
   GRAY_ME = '\033[38;5;239m'
   GRAY_DIUM = '\033[38;5;240m'
   GRAY_MEDIUM = '\033[38;5;244m'
   GRAY_MEDIUM_LIGHT = '\033[38;5;248m'
   GRAY_LIGHT = '\033[38;5;250m'
   GRAY_VERY_LIGHT = '\033[38;5;254m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def say(who, message,
        who_color = color.PURPLE,
        message_color = color.CYAN,
        newline=True):
   print("\n" + color.BLUE + "> " + color.BOLD + who_color + color.UNDERLINE + who + color.END + ": ", end="")
   if newline:
      print(message_color + message + color.END)
   else:
      print(message_color + message + color.END, end="")

def jemma_say(message,
              message_color = color.GRAY_ME):
   say("[jemma]",
       message,
       color.GRAY_DIUM,
       message_color,
       False)

def read_file(path):
    with open(path, 'r') as file:
        data = file.read()
    return data

def name_to_file_name(name, extension="txt"):

    clean_name = re.sub(r'[^a-zA-Z0-9\s-]', '', name).replace(' ', '-').lower()

    timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S-%f")[:-3]
    return f"{clean_name}.{timestamp}.{extension}"

def record_prototype(path, prototype):

   os.makedirs(path, exist_ok=True)

   # write the CSS file
   css_file_path = os.path.join(path, "app.css")
   with open(css_file_path, "w") as css_file:
      css_file.write(prototype["css"])

   if "js" in prototype:
      # write the JavaScript file
      js_file_path = os.path.join(path, "app.js")
      with open(js_file_path, "w") as js_file:
         js_file.write(prototype["js"])

   # write the HTML file
   html_file_path = os.path.join(path, "index.html")
   with open(html_file_path, "w") as html_file:
      html_file.write(prototype["html"])

   print("\nprototype files created successfully:")
   print(f"- {path}/index.html")
   if "js" in prototype:
      print(f"- {path}/app.js")
   print(f"- {path}/app.css")


def open_local_browser(dir_path):
   current_dir = os.getcwd()
   try:
      # Get the absolute path of the file
      abs_path = os.path.abspath(dir_path)

      # Check if the file exists
      if os.path.exists(abs_path):
         # Open the file in the default web browser
          webbrowser.open(f"file://{abs_path}/index.html")
          print(f"opened {dir_path} in the web browser")
      else:
         print(f"can't find a file system path to open in the browser: {file_path}")
   finally:
      os.chdir(current_dir)

def deploy(prototype, path="prototype"):
   record_prototype(path, prototype)
   open_local_browser(path)
   return {"deployed": True, "deploy_path": path}

def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description='jemma takes in a prompt or a file with requirements and builds a working prototype based on it\n'
               '      then it helps you to iterate on it',
        formatter_class=argparse.RawTextHelpFormatter,
        usage='%(prog)s [-h] [--requirements path-to-file] [--prompt prompt] [--build-prototype]\n'
              '                 [--claude [model name]] [--openai [model name]] [--ollama [model name]] [--replicate [model name]] [--custom [url]]',
        epilog='thoughts in, software out'
    )

    parser.add_argument('--compose', metavar='actions', type=str, nargs='*', default=None,
                        help='provide a set of actions to compose (e.g., \'--compose get-milk feed-kids launch-mars-expedition\')')

    parser.add_argument('--requirements', metavar='path', type=str, help='path to a text file with requirements')
    parser.add_argument('--prompt', metavar='prompt', type=str, help='short idea to convert to creation')
    parser.add_argument('--sketch', metavar='sketch', type=str, help='a mockup or a hand drawn sketch to convert to a prototype')

    parser.add_argument('--user-stories', action='store_true', help='create and refine user stories')
    parser.add_argument('--build-user-stories', action='store_true', help='build prototype on combined (non-refined) user stories')

    parser.add_argument('--build-prototype', action='store_true', help='build prototype')
    parser.add_argument('--test-prototype', action='store_true', help='test prototype')

    parser.add_argument('--claude', metavar='model name', nargs='?', const=True, default=None, help='choose a claude model (optional, can be provided without a value)')
    parser.add_argument('--openai', metavar='model name', nargs='?', const=True, default=None, help='choose an open ai model (optional, can be provided without a value)')
    parser.add_argument('--ollama', metavar='model name', nargs='?', const=True, default=None, help='choose an ollama model (optional, can be provided without a value)')
    parser.add_argument('--replicate', metavar='model name', nargs='?', const=True, default=None, help='choose a model from Replicate (optional, can be provided without a value)')
    parser.add_argument('--custom', metavar='url', nargs='?', const=True, default=None, help='choose a model running at a custom url (optional, can be provided without a value)')

    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.compose:
       tasks = [task.strip() for task in args.compose]
       args.tasks = tasks
    else:
       args.tasks = None

    return args


def file_to_utf8(path):

   with open(path, "rb") as file:
      image_data = file.read()
      encoded = base64.b64encode(image_data)
      return encoded.decode("utf-8")

def image_path_to_type(path):

    extension = path.split(".")[-1].lower()

    media_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "bmp": "image/bmp",
        "tiff": "image/tiff",
        "webp": "image/webp",
        "svg": "image/svg+xml"
    }

    if extension not in media_types:
        raise ValueError(f"could not determine an image type. image path: {path}")

    return media_types[extension]

def image_path_to_data(path):

   return {"image_data": file_to_utf8(path),
           "image_type": image_path_to_type(path)}

def send_post_request(prompt,
                      url="http://localhost:4242/api"):

    payload = {"prompt": prompt}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # raise an exception for 4xx or 5xx status codes

        # process the response
        if response.status_code == 200:
            # print(f"response {response.text}")
            return response.text
        else:
            print(f"request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"an error occurred: {e}")
