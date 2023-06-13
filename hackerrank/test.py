import requests
import PyPDF2 as pdf_reader

file = open('Resume.pdf', 'rb', )
reader = pdf_reader.PdfReader(file)
print(len(reader.pages))

page = reader.pages[0]
lst = f'{page.extract_text()}'

lst = lst.replace(' ', '')
print(lst)