# Car-Price-Prediction-model-Airflow
A repository of my project for ML-prediction-model working in Airflow with schedule 

The pbjective of the model is to predict the price category of the cars.

Metric is Accuracy.

pipeline.py contains a complete cycle of data preporation - useles feuture droping and outlier handling, feutre engineering, data normalization and encoding, model training and selecting the best among them via cross-validation with further saving of the best model.

predict.py contains code to make the predictions from a .json file and write the results to a prediction.csv.

hw_dag.py is a DAG script, so Airflow could schedule the pipeline + prediction cycle.
