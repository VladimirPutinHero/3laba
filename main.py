import ky
import osnova
import rere

ky.Ky()
filename = "aaa"
try:
    osnova.Osnova(filename)
    rere.Rere(filename)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
