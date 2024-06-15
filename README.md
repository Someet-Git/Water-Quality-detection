- Uses Machine learning to detect the quality of Water using the values of dissolved oxygen(do) in water and pH of Water.
- Then deployed on Django web framework for visualization.
- Used HTML, CSS and Javascript for making the components od website.

----------------

To run this project:

**step 1:** Create a virtual environment to separate your global enviornment `pip3 install pipenv`

**step 2:** install all the required dependencies `pip3 install requirements.txt`

**step 3:** To run the project use `python manage.py runserver`

**step 4:** set your value of dissolved oxygen in range 0-100 mg/L 

**step 5:** set the value of pH in range 1-14 

**step 6:** You will get the quality of Water either Good, Bad or Very Bad.

----------------

Let's talk about the dataset.
- _**Dissolved Oxygen (DO):**_ This is the amount of oxygen dissolved in water, essential for aquatic life. Higher DO levels generally indicate better water quality.
  
- _**pH Level:**_ This measures the acidity or alkalinity of water. A pH of 7 is neutral; values lower than 7 are acidic, and values higher than 7 are alkaline. Most aquatic life thrives in a pH range of 6.5 to 8.5.
  
- _**Conductivity (CO):**_ This measures the water's ability to conduct electricity, which correlates with the concentration of ions in the water. It is an indicator of the total dissolved solids (TDS) in the water.
  
- _**Biological Oxygen Demand (BOD):**_ This represents the amount of oxygen that microorganisms require to decompose organic matter in water. High BOD values indicate high levels of organic pollution.

- _**Nitrate (NA):**_ This is a measure of nitrate concentration in water. High nitrate levels can lead to eutrophication, which depletes oxygen in water bodies and harms aquatic life.

- _**Total Coliform (TC):**_ This is a measure of coliform bacteria in water, indicating potential contamination by pathogens. Higher TC counts suggest poor water quality and potential health risks.

- _**Water Quality Index (WQI):**_ This is a composite score that integrates various water quality parameters into a single number to indicate overall water quality. Higher values typically represent better water quality

--------------

- This is a Machine Learning project that I tried and along with that I made a website to see the result.
- Water quality data was collected from the Government of India website (different parameters are explained above.
- Then train those using ML algorithms like Multi linear regression, logistic regreesion and Random Forest classifier.
- With the help of R2_score and accuracy it was found that Random Forest classifier is the best for our use case. 
- It was based on Supervised Learning techniques as we were given the labelled data.
- We had to manually collect those data as we didn't find any api to collect them.
