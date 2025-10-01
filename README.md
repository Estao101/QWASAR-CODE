# Welcome to My Mobapp Studio
***

## Task
The task was to analyze the **Google Play Store Apps dataset** from Kaggle and generate insights about app categories, installs, pricing, and popularity.  
The challenge lies in cleaning messy data (e.g., installs like `10,000+`, prices like `$2.99`, sizes like `19M`), handling missing values, and presenting clear visualizations that answer key questions such as:
- Which paid family apps are the most popular?
- What genres dominate among paid family apps?
- How are installs distributed across categories?
- What are the pricing trends by category?

## Description
To solve the problem:
- Data loading & cleaning: Converted text fields (`Installs`, `Price`, `Size`) into numeric form, removed duplicates, and handled missing values.  
- Analysis functions: Created reusable Python functions to summarize, clean, and plot data.  
- Visualizations: Produced six key plots:
  1. Most popular paid Family apps (bar chart)  
  2. Popular genres in paid Family apps (pie chart)  
  3. Installs per category (pie chart)  
  4. Mean price per category (bar chart)  
  5. Most expensive apps per category (bar chart)  

Each plot is saved as a `.png` file for reporting or embedding in https://mobappstudioblog.wordpress.com/

## Installation
Clone the repository or download the script and dataset.  
Make sure you have Python 3.x installed, then install dependencies:
pip install pandas matplotlib seaborn

## Usage
Open jupyter to be able to view complete file and also the various prints statements and charts
The script will:
Clean the dataset

Print summaries to the console
Save analysis plots as images (.png) in an external folder
```
./my_mobapp_studio
```

### The Core Team
NOUBISSI SOH FRESSIE MEGANE and
TAMAMBANG NJI FRU DUNA

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
