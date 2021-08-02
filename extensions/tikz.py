import uuid
import os
import shutil
import contextlib
import subprocess

def code_to_svg(code, file_path):
    file_path = os.path.abspath(file_path)
    with temporary_directory('.tex') as directory:
        pdf_file_path = code_to_pdf(code)
        svg_file_path = pdf_to_svg(pdf_file_path)
        shutil.move(svg_file_path, file_path)

def code_to_pdf(code):
    tex_file_path = 'main.tex'
    pdf_file_path = 'main.pdf'

    with open(tex_file_path, 'w', encoding='utf8') as file:
        file.write(code)

    process = subprocess.Popen(['xelatex', tex_file_path])
    process.communicate()
    if not os.path.isfile(pdf_file_path):
        raise Exception
    return os.path.abspath(pdf_file_path)

def pdf_to_svg(pdf_file_path):
    svg_file_path = 'main.svg'
    process = subprocess.Popen(['pdf2svg', pdf_file_path, svg_file_path])
    process.communicate()

    if not os.path.isfile(svg_file_path):
        raise Exception
    return os.path.abspath(svg_file_path)

@contextlib.contextmanager
def temporary_directory(directory=None):
    directory = directory or str(uuid.uuid1())
    os.makedirs(directory, exist_ok=True)
    current_directory = os.path.abspath(os.curdir)
    os.chdir(directory)
    yield directory
    os.chdir(current_directory)
    shutil.rmtree(directory)
