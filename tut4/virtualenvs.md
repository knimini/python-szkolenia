# Virtualenvs

Virtualenvy pozwalają nam na posiadanie osobnych środowisk dla wszystkich projektów. Dzięki temu nie mamy problemów z różnymi wersjami bibliotek, różnymi wersjami pip-a i różnymi wersjami pythona we wszystkich naszych projektach. Za każdym razem kiedy tworzymy nowego virtualenva dostajemy nową binarkę pythona (w podanej przez nas wersji) bez żadnych zainstalowanych bibliotek. Umożliwia nam to package `virtualenv` którego obsługę ułatwimy sobie packagem `virtualenvwrapper` - dzięki niemu nasze virtualenvy będą przetrzymywane w jednym katalogu a dostęp do nich będziemy mieli z dowolnego miejsca w naszym systemie.

### Instalacja

1) Instalujemy `virtualenv`
```
sudo pip install virtualenv
```
2) Tworzymy katalog w którym przetrzymywać będziemy nasze virtualenvy
To jedno z wymagań dla `virtualenvwrapper`, katalog możecie sobię stworzyć gdzie chcecie i nazwać go jak chcecie, ja zawsze tworzę go w moim katalogu domowym i nazywam `.virtualenvs`.
Wpisujemy
```
mkdir ~/.virtualenvs
```
3) Instalujemy `virtualenvwrapper`
```
sudo pip install virtualenvwrapper
```
4) Pokazujemy `virtualenvwrapper` katalog, który stworzyliśmy dla niego na nasze envy
W tym celu musimy dodać nową zmienną środowiskową w naszym systemie. Robimy to wpisując.
```
export WORKON_HOME=~/.virtualenvs
```
Nie jest to jednak idealne rozwiązanie bo kiedy zakończymy nasza sesję terminala (czyli go zamkniemy) to przy następnym otwarciu system nie będzie tej zmiennej pamiętał. Aby zmienna została "zapamiętana" musimy ją poprostu eksportować za każdym razem, kiedy uruchamiamy terminal. Osiągniemy to dodając tą komendę na końcu naszego pliku `~/.bashrc`.
Otwieramy więc plik `.bashrc`:
```
vim ~/.bashrc
```
jak nie macie `vim`-a to pewnie macie `nano` albo `vi`, w czym otworzycie nie ma znaczenia. Na końcu tego pliku dodajecie naszą komendę
```
export WORKON_HOME=~/.virtualenvs

```
i tyle. Zapisujecie zmiany.

5) Uruchamiamy `virtualenvwrapper`
W tym celu ponownie musimy edytować nasz plik `~/.bashrc`. Na końcu, zaraz pod naszymi ostatnimi zmianami, dodajemy
```
. /usr/local/bin/virtualenvwrapper.sh
```
To wczyta wszystkie komendy `virtualenvwrapper`. Zapisujemy zmiany, zamykamy terminal, otwieramy terminal.

6) Gotowe


### Komendy

1) `mkvirtualenv <nazwa_virtualenva> [-p python[wersja]]`
tworzy virtualenva o podanej nazwie. Opcjonalnie możemy podać konkretną wersję pythona jaka nas interesuje. Np:
```
mkvirtualenv projekt1
```
```
mkvirtualenv projekt2 -p python3.5
```
```
mkvirtualenv projekt3 -p python2.7
```
Od razu też aktywuje virtualenva.

2) `deactivate`
wychodzi z virtualenva

3) `workon <nazwa_virtualenva>`
aktywuje virtualenva

4) `rmvirtualenv <nazwa_virtualenva>`
usuwa virtualenva


To tyle. Całkiem proste :D
