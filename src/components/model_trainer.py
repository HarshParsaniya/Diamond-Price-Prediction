import os
import sys

from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def intitate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            logging.info('Train Array Shape : {}'.format(train_array.shape))
            logging.info('Test Array Shape : {}'.format(test_array.shape))
            X_train, X_test, y_train, y_test = (
                train_array[:, :-1],
                test_array[:, :-1],
                train_array[:, -1],
                test_array[:, -1]
            )

            logging.info('Dependent and Independent variables splitted successfully')
            # Multiple Model Training
            models = {
                'LinearRegression' : LinearRegression(),
                'Ridge' : Ridge(),
                'Lasso' : Lasso(),
                'ElasticNet' : ElasticNet()
            }
            logging.info('Models Initialized Successfully')
            model_report:dict=evaluate_model(X_train,X_test,y_train,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )


        except Exception as e:
            logging.info('Exception occured at Model Training stage')
            raise CustomException(e, sys)