# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
import numpy.polynomial.polynomial as nppoly


def roots_20(coef: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja wyznaczająca miejsca zerowe wielomianu funkcją
    `nppoly.polyroots()`, najpierw lekko zaburzając wejściowe współczynniki 
    wielomianu (N(0,1) * 1e-10).

    Args:
        coef (np.ndarray): Wektor współczynników wielomianu (n,).

    Returns:
        (tuple[np.ndarray, np. ndarray]):
            - Zaburzony wektor współczynników (n,),
            - Wektor miejsc zerowych (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(coef, np.ndarray):
            return None
        
        #zaburzenia = np.random.normal(0, 1, size=) * (1e-10)
        zaburzenia = np.random.random_sample(coef.shape)*(1e-10)
        coef_zaburzone = coef + zaburzenia
        miejsca_zerowe = nppoly.polyroots(coef_zaburzone)

        return coef_zaburzone, miejsca_zerowe
    
    except Exception:
        return None


def frob_a(coef: np.ndarray) -> np.ndarray | None:
    """Funkcja służąca do wyznaczenia macierzy Frobeniusa na podstawie
    współczynników jej wielomianu charakterystycznego:
    w(x) = a_n*x^n + a_{n-1}*x^{n-1} + ... + a_2*x^2 + a_1*x + a_0

    Testy wymagają poniższej definicji macierzy Frobeniusa (implementacja dla 
    innych postaci nie jest zabroniona):
    F = [[       0,        1,        0,   ...,            0],
         [       0,        0,        1,   ...,            0],
         [       0,        0,        0,   ...,            0],
         [     ...,      ...,      ...,   ...,          ...],
         [-a_0/a_n, -a_1/a_n, -a_2/a_n,   ..., -a_{n-1}/a_n]]

    Args:
        coef (np.narray): Wektor współczynników wielomianu (n,).

    Returns:
        (np.ndarray): Macierz Frobeniusa o rozmiarze (n,n).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(coef, np.ndarray):
            return None
        if len(coef.shape) != 1 or len(coef) < 2:
            return None
        if coef[-1] == 0:
            return None
        n = len(coef) - 1
        FrobA = np.zeros((n,n), dtype = float)
        for i in range(n-1):
            FrobA[i][i+1] = 1
        a_n = coef[-1]
        for j in range(n):
            FrobA[n-1][j] = -coef[j] / a_n
        return FrobA

        
    except Exception:
        return None


def is_nonsingular(A: np.ndarray) -> bool | None:
    """Funkcja sprawdzająca czy podana macierz NIE JEST singularna. Przy
    implementacji należy pamiętać o definicji zera maszynowego.

    Args:
        A (np.ndarray): Macierz (n,n) do przetestowania.

    Returns:
        (bool): `True`, jeżeli macierz A nie jest singularna, w przeciwnym 
            wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    
    try:
        if not isinstance(A, np.ndarray):
            return None
        if len(A.shape) != 2:
            return None
        if A.shape[0] != A.shape[1]:
            return None
        
        det = np.linalg.det(A)
        epsilon = np.finfo(float).eps
        if abs(det) < epsilon:
            return False
        else:
            return True
    except Exception:
        return None
