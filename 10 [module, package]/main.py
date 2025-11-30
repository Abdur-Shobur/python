""" 

import my_module

print(my_module.greet("Shobur"))
"""

"""

from my_module import greet, pi

print(pi)
print(greet("SHOVON")) 
"""

# pip install requests
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 200
