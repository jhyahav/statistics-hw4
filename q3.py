from math import ceil

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np



path = "./countries.csv"
df = pd.read_csv(path)

income = df["income"].to_numpy()
life_expectancy = df["life_expectancy"].to_numpy()
education = df["education"].to_numpy()
 
def section_d_income(income, life_expectancy):

    var_x = np.var(income)
    cov_x_y = np.cov(income, life_expectancy)[0][1]
    x_avg = income.sum() / income.size
    y_avg = life_expectancy.sum() / life_expectancy.size
    b_LS = cov_x_y / var_x
    a_LS = y_avg - b_LS * x_avg

    x_LS = np.linspace(0, 1000000)
    y_LS = a_LS + b_LS * x_LS

    correlation_x_y = np.corrcoef(income, life_expectancy)[0][1]
    R_squared = correlation_x_y ** 2
    print("R^2 (Income & Life Expectancy)", R_squared)

    pl.scatter(x=income, y=life_expectancy, color="black", marker=".")
    pl.plot(x_LS, y_LS, "blue")
    pl.title("Correlation btw Income & Life Expectancy, RSS")
    pl.xlabel("Income")
    pl.ylabel("Life Expectancy")
    pl.show()

def section_d_education(education, life_expectancy):

    var_x = np.var(education)
    cov_x_y = np.cov(education, life_expectancy)[0][1]
    x_avg = education.sum() / education.size
    y_avg = life_expectancy.sum() / life_expectancy.size
    b_LS = cov_x_y / var_x
    a_LS = y_avg - b_LS * x_avg

    x_LS = np.linspace(0, 20)
    y_LS = a_LS + b_LS * x_LS
    correlation_x_y = np.corrcoef(education, life_expectancy)[0][1]
    R_squared = correlation_x_y ** 2
    print("R^2 (Education & Life Expectancy)", R_squared)

    pl.scatter(x=education, y=life_expectancy, color="black", marker=".")

    pl.plot(x_LS, y_LS, "blue")
    pl.title("Correlation btw Education & Life Expectancy, RSS")
    pl.xlabel("education")
    pl.ylabel("Life Expectancy")
    pl.show()




section_d_income(income , life_expectancy)