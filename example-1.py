def ist_schaltjahr(jahr: int) -> bool:
    """
    Überprüft, ob ein gegebenes Jahr ein Schaltjahr ist.

    Args:
    jahr (int): Das zu überprüfende Jahr.

    Returns:
    bool: True, wenn das Jahr ein Schaltjahr ist, ansonsten False.
    """

    return (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)


year = 2000
print(ist_schaltjahr(year))

