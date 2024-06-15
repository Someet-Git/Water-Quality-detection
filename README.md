- Uses Machine learning to detect the quality of Water using the values of dissolved oxygen(do) in water and pH of Water.
- Then deployed on Django web framework for visualization.
- Used HTML, CSS and Javascript for making the components of website.

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

## General Range for Water Quality Parameters for Calculating WQI

### 1. Dissolved Oxygen (DO)
- **Ideal Range**: 7 - 14.6 mg/L (depends on temperature)
- **Standard Range**: >5 mg/L (for healthy aquatic life)
- **Polluted Range**: <5 mg/L (indicates poor water quality)

### 2. pH Level
- **Ideal Range**: 6.5 - 8.5
- **Standard Range**: 6.5 - 8.5 (slightly varies by region)
- **Polluted Range**: <6.5 or >8.5 (too acidic or too alkaline)

### 3. Conductivity (CO)
- **Ideal Range**: 0 - 500 µS/cm
- **Standard Range**: 0 - 1500 µS/cm (varies with water use; lower for drinking)
- **Polluted Range**: >1500 µS/cm (indicates high TDS)

### 4. Biological Oxygen Demand (BOD)
- **Ideal Range**: <1 mg/L
- **Standard Range**: <3 mg/L (good quality); <5 mg/L (moderate quality)
- **Polluted Range**: >5 mg/L (high organic pollution)

### 5. Nitrate (NA)
- **Ideal Range**: 0 - 1 mg/L
- **Standard Range**: <10 mg/L (EPA standard for drinking water)
- **Polluted Range**: >10 mg/L (risk of eutrophication)

### 6. Total Coliform (TC)
- **Ideal Range**: 0 MPN/100 mL
- **Standard Range**: <1000 MPN/100 mL (for recreational water)
- **Polluted Range**: >1000 MPN/100 mL (indicates potential health risk)

## Calculation of WQI
$$ q_i = \left( \frac{V_i - V_{ideal}}{V_{standard} - V_{ideal}} \right) \times 100 $$     

- V_i is the observed value of parameter
- V_ideal is the ideal value of the parameter (often 0 for contaminants, 7 for pH, etc.).
- V_standard is the standard permissible value of the parameter as per guidelines (e.g., WHO, EPA).                                                                                            


$$ SI_i = q_i \times W_i $$
- q_i​ is the quality rating for the parameter.
- 𝑊_𝑖​ is the weight assigned to the parameter.


$$ WQI = \frac{\sum (SI_i)}{\sum (W_i)} $$
- SI_i is the sub-index for the parameter.
- 𝑊_𝑖​ is the weight assigned to the parameter.

--------------

- This is a Machine Learning project that I tried and along with that I made a website to see the result.
- Water quality data was collected from the Government of India website (different parameters are explained above.
- Then train those using ML algorithms like Multi linear regression, logistic regreesion and Random Forest classifier.
- With the help of R2_score and accuracy it was found that Random Forest classifier is the best for our use case. 
- It was based on Supervised Learning techniques as we were given the labelled data.
- We had to manually collect those data as we didn't find any api to collect them.
