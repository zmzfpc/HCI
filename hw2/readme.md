# Start Image Search Engine
Run python rest-server.py

Make sure that the folders **database**,**static**,**imagenet**  are in the same directory as the rest-server.py file.

Make sure that the files **neighbor\_list\_recom.pickle**,**search.py** are in the same directory as the rest-server.py file.

When the python-file rest-server.py is running,access http://localhost:8000/ to get the UI.

There are only a few hundred test images in the database. If the function is not fully displayed, please use the original image data set to cover the database folder.

# Development Environment

- **Development Environment:** Win 10

- **Development Software:**

  1. **PyCharm** *2021.1.1*
  2. **Visual Studio Code** 1.56.2.0

- **Development Language:**

  1. python3
  2. HTML
  3. JavaScript
  4. CSS
  5. jQuery
  6. Bootstrap

- **Mainly Reference Count:**

  1. flask (Flask, jsonify)
  2. flask_httpauth (HTTPBasicAuth)
  3. tensorflow
  4. numpy

- **Others:**

  Use some **third-party library  - UI Kits** to enhance the interface.

# Project Structure

```
│  readme.md    
│  lab2-1854116-report.pdf 
|  
└─lab2-1854116-code   
    │  rest-server.py   
     |	
    │  search.py  
     |
    ├─database   
    │  ├─dataset   
    │  └─tag   
    └─static   
       ├─css   
       │      imgtable.css   
       │      imgtag.css   
       │      bootstrap.css
        |      coming-sssoon.css
        |      coming-sssoon-demo.css
        |      fileinput.css
        |      theme.css
        |    
       ├─images  
        |
       ├─index.html
        |
       ├─search.html
        | 
       ├─assets  
       │      
       ├─js   
       │      favorites.js   
       │      imgSearch.js   
       │      randColor.js   
       │      showSource.js   
       │      slide.js   
       │      tag.js   
       │      toggleImgSize.js   
       │      theme.js
        |      fileinput.js
        |      bootstrap.min.js
        |        
       └─result      
```