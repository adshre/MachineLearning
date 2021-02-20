# What is Linear Regression 
  Linear regression is a machine learning algorithm that finds the best linear-fit relationship on any given data, between independent and dependent variables.

# Assumptions and Outcomes on voilation - made in Linear Regression 
## 1 . 
  - ***Assumption*** : There **should be a linear and additive relationship** between dependent (response) variable and independent (predictor) variable(s).
    - A linear relationship suggests that a change in response Y due to one unit change in X is constant, regardless of the value of X. 
    - An additive relationship suggests that the effect of X on Y is independent of other variables.
  - ***Outcome*** : If we fit a linear model to a non-linear and non-additive data set, the regression algorithm would **fail to capture the trend mathematically**, 
    thus resulting in an inefficient model. Also, this will result in **erroneous predictions on an unseen data set**.
## 2.
 - ***Assumption*** : **Independent Variables** should not be correlated. Thus are **not Multicollinear**
 - ***Outcome*** : 
    - For example, while training Y using X1 and X2, if X1 and X2 are closely related then the effect of X1 on Y would be hard to distinguish from the effect of X2 on Y. 
      This may hinder the learning process.In other words, it becomes **difficult to find out which variable is actually contributing** to predict the response variable.
    - Moreover, with presence of correlated predictors, the **standard errors tend to increase**. 
      And, with large standard errors, the **confidence interval becomes wider leading to less precise estimates of slope parameters**.
## 3.
 - ***Assumption*** : Linear Regression expects our **errors** to be **Independent** (not multicollinear), **Normally Distributed** and having **Equal variances**.
- ***Outcome*** : 
    - **Autocorrelation** occurs when the residuals are not independent from each other.
      In other words when the value of y(x+1) is not independent from the value of y(x).
      The presence of correlation in error terms drastically **reduces model’s accuracy**. 
      This usually **occurs in time series models** where the next instant is dependent on previous instant. 
      If the error terms are correlated, the **estimated standard errors tend to underestimate the true standard error**. 
      If this happens, it causes **confidence intervals and prediction intervals to be narrower**.
    - The presence of **non-constant variance** in the error terms results in **heteroskedasticity**. Generally, non-constant variance arises in presence of outliers. 
      It looks like that these values get too much weight, thereby disproportionately influences the model’s performance.
      When this phenomenon occurs, **the confidence interval tends to be unrealistically wide or narrow**.
    - If the error terms are **non- normally distributed, confidence intervals may become too wide or narrow**.
      Presence of non — normal distribution suggests that there are a few unusual data points which must be studied closely to make a better model.

# What is Linear Regression with one variable
  In simple terms, it is a straightforward Supervised learning approach for predicting a quantitative response Y on the basis of a single predictor variable X. 
