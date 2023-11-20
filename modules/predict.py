import logging
import json
import os
import dill
import pandas as pd


path = os.environ.get('PROJECT_PATH', '.')


def predict() -> None:
    with open(f'{path}/data/models/cars_pipe.pkl', 'rb') as file:
        model = dill.load(file)

    df_predicted = pd.DataFrame(columns=['car_id', 'predicted_category'])

    for jsonfile in os.listdir(f'{path}/data/test'):
        with open(os.path.join(f'{path}/data/test', jsonfile), 'r') as j:
            data = json.load(j)
            df = pd.DataFrame([data])
            prediction = model.predict(df)
            x = {'car_id': df.id, 'predicted_category': prediction}
            df_n = pd.DataFrame(x)
            df_predicted = pd.concat([df_predicted, df_n], axis=0)

    prediction_filename = f'{path}/data/predictions/prediction.csv'

    df_predicted.to_csv(prediction_filename)

    logging.info(f'Predictions are saved as {prediction_filename}')


if __name__ == '__main__':
    predict()
