import os

print("""
    This is a Postcss TailwindCSS 3.x Boilerplate Creator
    Have fun!

    """)

project_name = input("Name of the Project: ")

code_html = f"""
<!doctype html>
<html>
<head>
<title>{project_name}</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="/dist/output.css" rel="stylesheet">
</head>
<body>
<h1 class="text-3xl font-bold underline">
    Hello world!
</h1>
</body>
</html>
"""

code_css = """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""

code_postcss = """
    module.exports = {
    plugins: {
        tailwindcss: {},
        autoprefixer: {},
    }
    }
"""

def install_tailwind():
    install_tailwind = input("Install TailwindCSS 3.x y/n?: ")
    if install_tailwind == "y": 
            os.system("npm install -D tailwindcss postcss autoprefixer")
            os.system("npx tailwindcss init")
    else:
        exit

def init_tailwind():
    init_tailwind = input("Do you want to initialise TailwindCSS? y/n: ")
    if init_tailwind == "y":
        filename = os.path.join(dirname, "scripts", "tailwind-watch.bat")
        os.system(f"start {filename}")
    else:
        exit

def write_template_path(file_name, line_num, text):
    lines = open(file_name, 'r+').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def create_files():
    postcss_file = open("postcss.config.js", "w")
    postcss_file.write(code_postcss)
    os.makedirs("src/css")
    os.mkdir("dist")
    open("dist/output.css", "w")
    index_file = open("src/index.html", "w")
    index_file.write(code_html)
    css_file1 = open("src/input.css", "w")
    css_file1.write(code_css)
    install_tailwind()
    write_template_path("tailwind.config.js", 1, 'content: ["./src/**/*.{html,js}"],')

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(dirname)

create_files()

init_tailwind()