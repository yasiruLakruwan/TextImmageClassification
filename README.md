<pre> ```bash # Folder Structure file_directry/ ├── models/ │ └── text_classifire1.h5 ├── utils/ │ └── preprocessor.py ├── .gitignore ├── main.py ├── README.md └── requirements.txt ``` </pre>

# step 1 ----------> create folder structure as above

# step 2-----------> create a virtual environment
   run this command  "python -m venv venv"
# step 3-----------> activate the virtual environment 
   run this command   "venv\Scripts\activate" 
# step 4------------> run fastapi server 
   run this command    "uvicorn main:app --reload "
# the fast api server will runn on http://127.0.0.1:8000/docs

# drive link for project material ----------------> https://drive.google.com/drive/folders/1v_de8eDbFazO0VxF3lNBp9_BKudU4Knk?usp=sharing

# saved model used for api --------------> https://drive.google.com/drive/folders/10YXXYTwKv1HrNGKEVsHFHK4IlliMwNJD?usp=sharing

# model building has been done using google colab -------------->https://drive.google.com/drive/folders/1IXGikC8zCbMBfOWUBNFCvE3PR_78X76g?usp=sharing

# custom dataset -------------------> https://drive.google.com/drive/folders/1VPhsHNUcEQg1sQokoWhgxVG8JXzZ5vCi?usp=sharing

# main dataset used for custom --------> https://www.kaggle.com/datasets/ananthakrishnanpv/rvl-cdip-validation-dataset
