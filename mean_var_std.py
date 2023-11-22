import numpy as np


def calculate(data_list):
    if len(data_list) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    data_list = np.array(data_list).reshape(3, 3)
    calculations["mean"] = [
        np.mean(data_list, axis=0).tolist(),
        np.mean(data_list, axis=1).tolist(),
        np.mean(data_list.flatten()).tolist(),
    ]
    calculations["variance"] = [
        np.var(data_list, axis=0).tolist(),
        np.var(data_list, axis=1).tolist(),
        np.var(data_list.flatten()).tolist(),
    ]
    calculations["standard deviation"] = [
        np.std(data_list, axis=0).tolist(),
        np.std(data_list, axis=1).tolist(),
        np.std(data_list.flatten()).tolist(),
    ]
    calculations["max"] = [
        np.max(data_list, axis=0).tolist(),
        np.max(data_list, axis=1).tolist(),
        np.max(data_list.flatten()).tolist(),
    ]
    calculations["min"] = [
        np.min(data_list, axis=0).tolist(),
        np.min(data_list, axis=1).tolist(),
        np.min(data_list.flatten()).tolist(),
    ]
    calculations["sum"] = [
        np.sum(data_list, axis=0).tolist(),
        np.sum(data_list, axis=1).tolist(),
        np.sum(data_list.flatten()).tolist(),
    ]
    return calculations
