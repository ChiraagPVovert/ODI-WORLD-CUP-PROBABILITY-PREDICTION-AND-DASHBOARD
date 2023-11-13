import pandas as pd
from sklearn import preprocessing
import joblib
import ann_lr_bat,ann_lr_bowl,ann_lr_all_round
import numpy as np
import knn_algorithm_prediction
import logistic_regression_algorithm_prediction
import svm_algorithm_prediction


def model_predictions(team,model_algorithm):
    #df = pd.read_excel('All_odi_players_from_2019.xlsx')


    if model_algorithm == 'KNN':
        final_bat_and_wk_proba = knn_algorithm_prediction.bat(team)
        final_bowler_proba = knn_algorithm_prediction.bowl(team)
        final_all_rounder_proba = knn_algorithm_prediction.all_round(team)

    elif model_algorithm == 'ANN':
        final_bat_and_wk_proba = ann_lr_bat.model_predictions(team,2021)
        final_bowler_proba = ann_lr_bowl.model_predictions(team,2022)
        final_all_rounder_proba = ann_lr_all_round.model_predictions(team,2021)

    elif model_algorithm == 'SVM':
        final_bat_and_wk_proba = svm_algorithm_prediction.bat(team)
        final_bowler_proba = svm_algorithm_prediction.bowl(team)
        final_all_rounder_proba = svm_algorithm_prediction.all_round(team)

    elif model_algorithm == 'LR':
        final_bat_and_wk_proba = logistic_regression_algorithm_prediction.bat(team)
        final_bowler_proba = logistic_regression_algorithm_prediction.bowl(team)
        final_all_rounder_proba = logistic_regression_algorithm_prediction.all_round(team)



    return final_bat_and_wk_proba,final_bowler_proba,final_all_rounder_proba


#bat,bowl,all_round = model_predictions(team,model_algorithm,year)

#display(bat)