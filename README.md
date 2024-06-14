Uses Machine learning to detect the quality of Water using the values of dissolved oxygen(do) in water and pH of Water.

To run this project:


**step 1:** Create a virtual environment to separate your global enviornment `pip3 install pipenv`

**step 2:** install all the required dependencies `pip3 install requirements.txt`

**step 3:** To run the project use `python manage.py runserver`

**step 4:** set your value of dissolved oxygen in range 0-100 mg/L 

**step 5:** set the value of pH in range 1-14 

**step 6:** You will get the quality of Water either Good, Bad or Very Bad.


- This is a Machine Learning project that I tried and along with that I made a website to see the result.
- Water quality data was collected from the Government of India website.
- Then train those using ML algorithms like Multi linear regression, logistic regreesion and Random Forest classifier.
- With the help of R2_score and accuracy it was found that Random Forest classifier is the best for our use case. 
- It was based on Supervised Learning techniques as we were given the labelled data.
- We had to manually collect those data as we didn't find any api to collect them.
