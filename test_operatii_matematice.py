from operatii_matematice import (
    este_par,
    calculeaza_pret_final,
    converteste_temperatura
)


def test_este_par():
    assert este_par(4) is True
    assert este_par(7) is False


def test_calculeaza_pret_final():
    assert calculeaza_pret_final(100, 10) == 90
    assert calculeaza_pret_final(200, 25) == 150


def test_converteste_temperatura():
    assert converteste_temperatura(0) == 32
    assert converteste_temperatura(100) == 212