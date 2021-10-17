import numpy as np
# import pickle
# import matplotlib
import matplotlib.pyplot as plt
# import string
# import random


def compare_plot(x1: np.ndarray, y1: np.ndarray, x2: np.ndarray, y2: np.ndarray,
                 xlabel: str, ylabel: str, title: str, label1: str, label2: str):
    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """
    if len(x1) == len(y1) and len(x2) == len(y2) and len(x1) > 1 and len(x2) > 1:
        fig = plt.figure()
        plt.plot(x1, y1, 'b-', linewidth=4, label=label1)
        plt.plot(x2, y2, 'r-', linewidth=2, label=label2)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        return fig
    return None


def parallel_plot(x1: np.ndarray, y1: np.ndarray, x2: np.ndarray, y2: np.ndarray,
                  x1label: str, y1label: str, x2label: str, y2label: str, title: str, orientation: str):
    """Funkcja służąca do stworzenia dwóch wykresów typu plot w konwencji subplot wertykalnie lub chorycontalnie. 
    Szczegółowy opis w zadaniu 5.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    x1label(str): opis osi x dla pierwszego wykresu,
    y1label(str): opis osi y dla pierwszego wykresu,
    x2label(str): opis osi x dla drugiego wykresu,
    y2label(str): opis osi y dla drugiego wykresu,
    title(str): tytuł wykresu,
    orientation(str): parametr przyjmujący wartość '-' jeżeli subplot ma posiadać dwa wiersze albo '|' jeżeli ma posiada
    ć dwie kolumny.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 5
    """
    if len(x1) == len(y1) and len(x2) == len(y2) and len(x1) > 1 and len(x2) > 1:
        if len(set(x1)) == len(x1) and len(set(x2)) == len(x2):
            if orientation == '|':
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.0))
            elif orientation == '-':
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.0, 10.0))
            else:
                return None

            ax1.plot(x1, y1)
            ax1.set(xlabel=x1label, ylabel=y1label, title=title)
            ax2.plot(x2, y2)
            ax2.set(xlabel=x2label, ylabel=y2label, title=title)

            return fig

    return None


def log_plot(x: np.ndarray, y: np.ndarray, xlabel: np.ndarray, ylabel: str, title: str, log_axis: str):
    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
    if len(x) == len(y) and len(x) > 1:
        fig = plt.figure()
        if log_axis == 'x':
            plt.semilogx(x, y)

        elif log_axis == 'y':
            plt.semilogy(x, y)

        elif log_axis == 'xy':
            plt.loglog(x, y)

        else:
            return None

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        return fig

    return None
