from math import ceil

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np



path = "./countries.csv"
df = pd.read_csv(path)

income = df["income"].to_numpy()
income_log2 = np.log2(income)

life_expectancy = df["life_expectancy"].to_numpy()
education = df["education"].to_numpy()

education3 = 3*education
 


def section_d(education, life_expectancy, filed ):

    var_x = np.var(education)
    cov_x_y = np.cov(education, life_expectancy)[0][1]
    x_avg = education.sum() / education.size
    y_avg = life_expectancy.sum() / life_expectancy.size
    b_LS = cov_x_y / var_x
    a_LS = y_avg - b_LS * x_avg

    x_LS = np.linspace(np.amin(education), np.amax(education))
    y_LS = a_LS + b_LS * x_LS
    print(a_LS, b_LS)
    correlation_x_y = np.corrcoef(education, life_expectancy)[0][1]
    R_squared = correlation_x_y ** 2
    print("R^2 (" + filed+ " & Life Expectancy)", R_squared)

    pl.scatter(x=education, y=life_expectancy, color="black", marker=".")

    pl.plot(x_LS, y_LS, "blue")
    pl.title("Correlation btw " +  filed + " & Life Expectancy, RSS")
    pl.xlabel(str(filed))
    # pl.xscale("log")
    pl.ylabel("Life Expectancy")
    pl.show()




section_d(income_log2 , life_expectancy, "Income")