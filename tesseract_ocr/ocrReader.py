from PIL import Image
import sys
import pyocr
import pyocr.builders
import matplotlib.pyplot as plt

tools = pyocr.get_available_tools()

if len(tools) == 0:
  print("No OCR tool found")
  sys.exit(1)

tool = tools[0]
print("using tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

lang = langs[0]
print("using lang %s"%lang)
# load image
img = Image.open('./images/SCORE.png')
txt = tool.image_to_string(
    img,
    lang,
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)
plt.imshow(img)
plt.show()