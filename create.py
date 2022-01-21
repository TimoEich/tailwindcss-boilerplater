import os

print("""
    This is a CLI TailwindCSS 3.x Boilerplate Creator
    Have fun! megageil

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

code_readme = f"""
    <div align="center">
        <img alt="Logo" src="PATH TO LOGO" width="100" />
    </div>
    <h1 align="center">
        {project_name}
    </h1>
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
        os.system("npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch")

# def delete_template_path_line():
#     with open("tailwind.config.js", "r+") as tailwind_config:
#         new_tailwind_config = tailwind_config.readlines()
#         tailwind_config.seek(0)
#         for i in new_tailwind_config:
#             if i != "content: [],":
#                 tailwind_config.write(i)
#         tailwind_config.truncate()

def write_template_path(file_name, line_num, text):
#    delete_template_path_line()
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
    readme_file = open("README.md", "w")
    readme_file.write(code_readme)
    install_tailwind()
    write_template_path("tailwind.config.js", 1, 'content: ["./src/**/*.{html,js}"],')

create_files()

init_tailwind()