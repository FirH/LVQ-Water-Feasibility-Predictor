import numpy as np
import argparse
import math
import pandas as pd

def predict_func(x, W) :
    W, c = W
    d = [math.sqrt(sum((w-x) ** 2)) for w in W]
    return c[np.argmin(d)]

def predict(df) :
    W = (
    np.array([[7.11874420e+00, 1.97113764e+02, -1.52575719e-02,
            7.08054386e+00, 3.34387568e+02, 4.24853002e+02,
            1.43565611e+01, 6.66842167e+01, 3.96161509e+00],
           [1.55779336e+01, 4.57396606e+02, 5.72362148e+00,
            1.03520935e+00, -1.82232547e+02, 5.01973053e+02,
            1.56515547e+01, -1.05343292e+02, 1.21037625e+01]]),
    np.array([0., 1.])
    )
    
    predicted = []
    for i in df.values :
        predicted.append(predict_func(i,W))
    
    return predicted[0]

def input_preprocessor(ph=0,Hardness=0,Solids=0,Chloramines=0,Sulfate=0,Conductivity=0,Organic_carbon=0,Trihalomethanes=0,Turbidity=0) :
    df = pd.DataFrame()
    df['ph'] = [ph]
    df['Hardness'] = [Hardness]
    df['Solids'] = [Solids]
    df['Chloramines'] = [Chloramines]
    df['Sulfate'] = [Sulfate]
    df['Conductivity'] = [Conductivity]
    df['Organic_carbon'] = [Organic_carbon]
    df['Trihalomethanes']= [Trihalomethanes]
    df['Turbidity'] = [Turbidity]
    return df

def main () :
    parser = argparse.ArgumentParser(description='LVQ Based Water Potability Model')
    parser.add_argument('--ph', type=float, nargs='+', help='pH value')
    parser.add_argument('--Hardness', type=float, nargs='+', help='Hardness value')
    parser.add_argument('--Solids', type=float, nargs='+', help='Solids value')
    parser.add_argument('--Chloramines', type=float, nargs='+', help='Chloramines value')
    parser.add_argument('--Sulfate', type=float, nargs='+', help='Sulfate value')
    parser.add_argument('--Conductivity', type=float, nargs='+', help='Conductivity value')
    parser.add_argument('--Organic_carbon', type=float, nargs='+', help='Organic Carbon value')
    parser.add_argument('--Trihalomethanes', type=float, nargs='+', help='Trihalomethanes value')
    parser.add_argument('--Turbidity', type=float, nargs='+', help='Turbidity value')
    args = parser.parse_args()
    df = input_preprocessor(args.ph[0], args.Hardness[0], args.Solids[0], args.Chloramines[0],
                           args.Sulfate[0], args.Conductivity[0], args.Organic_carbon[0],
                           args.Trihalomethanes[0], args.Turbidity[0])
    prediction = predict(df)
    
    if prediction == 1 :
        print('Air Layak Diminum')
    else :
        print('Air Tidak Layak Diminum')

if __name__ == "__main__" :
    main()

    