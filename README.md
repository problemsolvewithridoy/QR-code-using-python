
# QR Code Generator

This is a Python script that allows you to generate QR codes easily. QR codes are two-dimensional barcodes that can store information such as URLs, text, or contact information. This script uses the qrcode library to generate QR codes
let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
pip install qrcode

```
    
## Deployment

To deploy this project run

```bash
#please subscribe "Problem Solve With Ridoy" youtube channel

# For create multipole QR code 

import qrcode
with open("site.csv") as file:
    for i in file:
        data = i.strip("\n")
        new_data = data.split(",")
        img = qrcode.make(f"{new_data[1]}")
        img.save(f"{new_data[0]}.jpg")
print("all QR code create completed")
```
```bash
# For create one QR code

import qrcode
img = qrcode.make("give your information")
img.save("file_name.jpg")
print("QR code create completed")
```





## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

