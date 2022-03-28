def czy_palindrom(slowo: str) -> bool:
    slowo = slowo.lower()
    odwr = reversed(slowo)
    if list(slowo) == list(odwr):
        return True
    return False


x = "Kajak"
print(czy_palindrom(x))
