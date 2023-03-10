def adfuller_test(series):
    result = stattools.adfuller(series.dropna(), autolag='AIC')
    labels = ['ADF Test Statistic', 'p-value', 'Number of Lags Used', 'Number of Observations Used']
    out = pd.Series(result[0:4], index=labels)
    for key, value in result[4].items():
        out[f'Critical Value ({key})'] = value
    
    print(out.to_string())
    print('-' * 20)
    if result[1] <= 0.05:
        print('Strong evidence; reject the null. Series has no unit root and is stationary.')
    else:
        print('Weak evidence against null hypothesis. Series has a unit root, it is non-stationary.')
