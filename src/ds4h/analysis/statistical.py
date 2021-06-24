import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import shapiro, kstest

def create_dataframe(df, group_variable, group_name, group_cidade):
    dfgrouped = df[df['MUNNAME'] == group_cidade]
    dfgrouped = dfgrouped.groupby(['YEAR', group_variable]).count().reset_index()
    dfgrouped = dfgrouped[dfgrouped[group_variable] == group_name] 
    dfgrouped["ISPANDEMIC"] = dfgrouped.YEAR.apply(lambda x: x in (2017,2020)) 
    dfgrouped["ISWHITE"] = dfgrouped.RACACORMAE == "White" 
    return dfgrouped

def create_dataframeraca(df, group_variable, group_name, group_cidade):
    dfgrouped = df[df['MUNNAME'] == group_cidade]
    dfgrouped["ISWHITE"] = dfgrouped.RACACORMAE == "White" 
    dfgrouped = dfgrouped.groupby(['YEAR', group_variable]).count().reset_index()
    dfgrouped = dfgrouped[dfgrouped[group_variable] == group_name] 
    dfgrouped["ISPANDEMIC"] = dfgrouped.YEAR.apply(lambda x: x in (2017,2020))     
    return dfgrouped

def create_dataframestatus(df, group_variable, group_name, group_cidade):
    dfgrouped = df[df['MUNNAME'] == group_cidade]
    dfgrouped["ISMARRIED"] = dfgrouped.ESTCIVMAE.apply(lambda x: x in ("Married","Stable union")) 
    dfgrouped = dfgrouped.groupby(['YEAR', group_variable]).count().reset_index()
    dfgrouped = dfgrouped[dfgrouped[group_variable] == group_name] 
    dfgrouped["ISPANDEMIC"] = dfgrouped.YEAR.apply(lambda x: x in (2017,2020))     
    return dfgrouped

def create_dataframeesc(df, group_variable, group_name, group_cidade):
    dfgrouped = df[df['MUNNAME'] == group_cidade]
    dfgrouped["ISSEVEN"] = dfgrouped.ESCMAE.apply(lambda x: x in ("1 to 3 years","4 to 7 years")) 
    dfgrouped = dfgrouped.groupby(['YEAR', group_variable]).count().reset_index()
    dfgrouped = dfgrouped[dfgrouped[group_variable] == group_name] 
    dfgrouped["ISPANDEMIC"] = dfgrouped.YEAR.apply(lambda x: x in (2017,2020))     
    return dfgrouped

def create_dataframeesceight(df, group_variable, group_name, group_cidade):
    dfgrouped = df[df['MUNNAME'] == group_cidade]
    dfgrouped["ISEIGHT"] = dfgrouped.ESCMAE.apply(lambda x: x in ("8 to 11 years","12 or more years")) 
    dfgrouped = dfgrouped.groupby(['YEAR', group_variable]).count().reset_index()
    dfgrouped = dfgrouped[dfgrouped[group_variable] == group_name] 
    dfgrouped["ISPANDEMIC"] = dfgrouped.YEAR.apply(lambda x: x in (2017,2020))     
    return dfgrouped

def statistical_report(df):

    print("Análise: Diferença entre anos de pandemia (2017, 2020) e outros anos.\n\n")

    print("Comparação para:\n")

    print("Mulheres brancas")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        dfWhite = create_dataframe(df, "RACACORMAE", "White",cidade)
        f_val, p_val = stats.ttest_ind(
            dfWhite[dfWhite.ISPANDEMIC == True]["DTNASC"],
            dfWhite[dfWhite.ISPANDEMIC == False]["DTNASC"],
        )
        print ("\t\tOne-way ANOVA P =", p_val)
    print()

    print("Mulheres não-brancas")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        dfBrown = create_dataframeraca(df, "ISWHITE",False,cidade)
        f_val, p_val = stats.ttest_ind(
            dfBrown[dfBrown.ISPANDEMIC == True]["DTNASC"],
            dfBrown[dfBrown.ISPANDEMIC == False]["DTNASC"],
        )
        print ("\t\tOne-way ANOVA P =", p_val)
    print()

    for age_group in ("A1", "A2", "A3"):
        print(f"Mulheres em AGEGROUP {age_group}")
        for cidade in df.MUNNAME.unique():
            print("\t" + cidade)
            dfA1 = create_dataframe(df, "AGEGROUP", age_group,cidade)
            f_val, p_val = stats.ttest_ind(
                dfA1[dfA1.ISPANDEMIC == True]["DTNASC"],
                dfA1[dfA1.ISPANDEMIC == False]["DTNASC"],
            )

            X = dfA1['DTNASC'].values
            shap_stat, spvalue = shapiro(X)
            k_stat, kpvalue = kstest((X - X.mean())/X.std(), "norm", N=len(X))
            print("\t\tShapiro-Wilk statistic: {:.4f} (p={:.4f})".format(shap_stat, spvalue)) 
            print("\t\tKolmogorov-Smirnov test statistic: {:.4f} (p={:.4f})".format(k_stat, kpvalue)) 

            print ("\t\tOne-way ANOVA P =", p_val)
        print()

    print("Mulheres Casadas ou em União Estável")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        dfMarried = create_dataframestatus(df,"ISMARRIED",True,cidade)
        f_val, p_val = stats.ttest_ind(
            dfMarried[dfMarried.ISPANDEMIC == True]["DTNASC"],
            dfMarried[dfMarried.ISPANDEMIC == False]["DTNASC"],
        )

        X = dfMarried['DTNASC'].values
        shap_stat, spvalue = shapiro(X)
        k_stat, kpvalue = kstest((X - X.mean())/X.std(), "norm", N=len(X))
        print("\t\tShapiro-Wilk statistic: {:.4f} (p={:.4f})".format(shap_stat, spvalue)) 
        print("\t\tKolmogorov-Smirnov test statistic: {:.4f} (p={:.4f})".format(k_stat, kpvalue)) 

        print ("\t\tOne-way ANOVA P =", p_val)
    print()

    print("Mulheres Solteiras")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        dfSingle = create_dataframe(df, "ESTCIVMAE", "Single",cidade)
        f_val, p_val = stats.ttest_ind(
            dfSingle[dfSingle.ISPANDEMIC == True]["DTNASC"],
            dfSingle[dfSingle.ISPANDEMIC == False]["DTNASC"],
        )

        X = dfSingle['DTNASC'].values
        shap_stat, spvalue = shapiro(X)
        k_stat, kpvalue = kstest((X - X.mean())/X.std(), "norm", N=len(X))
        print("\t\tShapiro-Wilk statistic: {:.4f} (p={:.4f})".format(shap_stat, spvalue)) 
        print("\t\tKolmogorov-Smirnov test statistic: {:.4f} (p={:.4f})".format(k_stat, kpvalue)) 

        print ("\t\tOne-way ANOVA P =", p_val)
    print()


    print("Mulheres com 7 ou menos anos de estudos")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        df12 = create_dataframeesc(df, "ISSEVEN", True,cidade)
        f_val, p_val = stats.ttest_ind(
            df12[df12.ISPANDEMIC == True]["DTNASC"],
            df12[df12.ISPANDEMIC == False]["DTNASC"],
        )

        X = df12['DTNASC'].values
        shap_stat, spvalue = shapiro(X)
        k_stat, kpvalue = kstest((X - X.mean())/X.std(), "norm", N=len(X))
        print("\t\tShapiro-Wilk statistic: {:.4f} (p={:.4f})".format(shap_stat, spvalue)) 
        print("\t\tKolmogorov-Smirnov test statistic: {:.4f} (p={:.4f})".format(k_stat, kpvalue)) 

        print ("\t\tOne-way ANOVA P =", p_val)
    print()

    print("Mulheres com 8 ou mais anos de estudos")
    for cidade in df.MUNNAME.unique():
        print("\t" + cidade)
        df8 = create_dataframeesceight(df, "ISEIGHT", True,cidade)
        f_val, p_val = stats.ttest_ind(
            df8[df8.ISPANDEMIC == True]["DTNASC"],
            df8[df8.ISPANDEMIC == False]["DTNASC"],
        )

        X = df8['DTNASC'].values
        shap_stat, spvalue = shapiro(X)
        k_stat, kpvalue = kstest((X - X.mean())/X.std(), "norm", N=len(X))
        print("\t\tShapiro-Wilk statistic: {:.4f} (p={:.4f})".format(shap_stat, spvalue)) 
        print("\t\tKolmogorov-Smirnov test statistic: {:.4f} (p={:.4f})".format(k_stat, kpvalue)) 

        print("\t\tOne-way ANOVA P =", p_val)
    print()
