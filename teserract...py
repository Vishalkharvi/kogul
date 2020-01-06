#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pytesseract as py
from gtts import gTTS
from PIL import Image
py.pytesseract.tesseract_cmd= r'C:\Users\vishalkharvi\Downloads\tesseract.exe'
extracted_text_from_image=" "
images=["page8.jpg","page9.jpg","page10.jpg","page11.jpg","page12.jpg","page13.jpg","page14.jpg","page15.jpg","page16.jpg","page17.jpg"]
for image in images:
    Opened_image=Image.open(image)
    Texts_from_image=py.image_to_string(Opened_image,lang='kan')
    extracted_text_from_image=extracted_text_from_image+str(Texts_from_image)
print(extracted_text_from_image)


audio_file=gTTS(text=tess, slow=False, lang='kn')
audio_file.save('audio.mp3')


# In[ ]:




