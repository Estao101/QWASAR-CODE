# Welcome to My Open The Iris
***

## Task
The project aims to analyze the classic Iris flower dataset through:
1. Data loading and inspection
2. Statistical summarization
3. Visualization (both univariate and multivariate)
4. Machine learning model evaluation

The main difficulty was ensuring exact output formatting for the dataset summary to match automated test expectations
Implementing multiple ML models with consistent evaluation metrics
Creating informative visualizations of the multivariate data

## Description
The solution involves:
1. Data Loading
   - Simple CSV loading with pandas
   - Returns the dataset for further processing

2. Data Summarization
   - Comprehensive statistical summary
   - Class distribution analysis
   - Formatted output matching exact test requirements

3. Visualization
   - Univariate histograms for feature distributions
   - Multivariate scatter matrix showing feature relationships

4. Model Evaluation
   - Implements 6 classification models:
     - Decision Tree
     - Naive Bayes
     - K-Nearest Neighbors
    Logistic Regression
    Linear Discriminant Analysis
    SVM
   Uses k-fold cross validation
   Reports mean accuracy and standard deviation

  Execution
   Main workflow combining loading and visualization

## Installation
Install requirements:
pip install pandas matplotlib scikit-learn seaborn
Ensure iris.csv is in the working directory

## Usage
Run cells in order:
Load data
dataset = load_dataset()

View summary statistics
summarize_dataset(dataset)

Generate visualizations
print_plot_univariate(dataset)  # Histograms
print_plot_multivariate(dataset)  # Scatter matrix

Evaluate models
my_print_and_test_models(dataset)
Expected outputs:

Formatted dataset statistics
Histograms of each feature
Scatter plot matrix
Model performance comparisons
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
