import base64

import chardet as chardet

s = 'pQQRIiKAIWiJmA0AGj0ftOZBYAAAAj6zMzM+TMzNPczMzQAAHrYS'
data = base64.b64decode(s)
#data = base64.b64decode(s)
#result = chardet.detect(data)

#print(result['encoding'])

print(data)