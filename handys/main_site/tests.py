from django.test import TestCase
# Create your tests here.

phones = open(r'C:\Users\lexalexa\Desktop\phones.txt')

for r in phones:
    print(r.replace('\n', ''))