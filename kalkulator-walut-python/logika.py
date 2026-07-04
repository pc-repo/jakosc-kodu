import urllib.request
import xml.etree.ElementTree as ET
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox, QTextEdit
from PySide6.QtCore import Qt, QTimer, QDateTime, QDate, QTime
from ui_gui_beta import Ui_MainWindow  # Importuję klasę wygenerowaną z .ui

# --- Funkcja pobieraj z www ---
def get_from_www(url, filename='kurs.xml'):
    """
    Pobiera plik XML z kursami walut NBP i zapisuje go lokalnie.
    Zwraca obiekt ElementTree po pomyślnym pobraniu i sparsowaniu.
    """
    try:
        urllib.request.urlretrieve(url, filename)
        return ET.parse(filename)
    except Exception as e:
        QMessageBox.critical(None, "Błąd pobierania", f"Nie udało się pobrać lub sparsować pliku XML: {e}")
        return None

# --- Funkcja parsuj dane ---
def parsing(root):
    """
    Parsuje dane walutowe z elementu głównego XML i zwraca słownik.
    Przekazuje także datę publikacji aktualnych kursów. 
    """
    # Tablica przechowująca kursy
    waluty = {}

    # Ustalenie daty publikacji kursów
    data_pub = None
    data_tag = root.find('data_publikacji')
    if data_tag is not None:
        data_pub = data_tag.text # Pobieramy datę jako string

    # Zapełnienie tablicy wartości
    for i, pozycja in enumerate(root.findall('pozycja')):
        try:
            name = pozycja.find('nazwa_waluty').text
            code = pozycja.find('kod_waluty').text.upper()
            rate_str = pozycja.find('kurs_sredni').text
            rate = float(rate_str.replace(',', '.'))
            unit = int(pozycja.find('przelicznik').text)

            # Kluczem będzie kod waluty dla łatwiejszego dostępu w ComboBox
            waluty[code] = {
                'nazwa': name,
                'kurs': rate,
                'jednostka': unit
            }
        except AttributeError as e:
            print(f"Ostrzeżenie: Błąd parsowania elementu waluty (brakujący tag?): {e}")
        except ValueError as e:
            print(f"Ostrzeżenie: Błąd konwersji danych dla waluty: {e}")
    return waluty, data_pub

# --- Klasa głównego okna aplikacji ---
class Convert(QMainWindow):

    # --- Funkcja inicjująca ---
    def __init__(self):

        """
        Inicjalizuje główne okno aplikacji konwertera walut.
        Konfiguruje interfejs użytkownika, łączy sygnały z slotami
        i ustawia początkowy stan aplikacji.
        """

        super().__init__()

        # Inicjalizuj interfejs użytkownika z pliku .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kontener na dane
        self.waluty_data = {} 

        # Przycisk synchronizacji
        self.ui.synchroBtn.clicked.connect(self.load_data)

        # Przycisk zamykania
        self.ui.exitBtn.clicked.connect(QApplication.quit)

        # Obsługa zegara
        self.ui.dateNow.setDateTime(QDateTime.currentDateTime())
        self.ui.dateNow.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.timer = QTimer(self) 
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self.forTimer)
        self.timer.start()
        self.forTimer()

        # Połącz przycisk "Przelicz" z funkcją przeliczającą
        self.ui.convertBtn.clicked.connect(self.onClick)
        
        # Domyślnie wybrana opcja radio
        self.ui.radioPLN.setChecked(True)

        # Wskazanie kursora na pole
        self.ui.inputKota.setFocus() 
     
        # Załaduj dane walut przy starcie aplikacji
        # self.load_data()

    # --- Funkcja ładuj strukturę ---
    def load_data(self):
        """
        Pobiera plik na pomocą prywatnej funkcji <get_from_www>.
        Parsuje drzewoo XML do zmiennej (tablicy roboczej) <waluty_data> funkcją <parsing>
        Obsługuje wyjątki ewentualnych błędów.
        """
        NBP_URL = 'https://static.nbp.pl/dane/kursy/xml/LastA.xml'
        XML_FILENAME = 'kurs.xml'

        QApplication.processEvents() # Odśwież UI, aby użytkownik widział status

        tree = get_from_www(NBP_URL, XML_FILENAME)
        if tree:
            root = tree.getroot()
            self.waluty_data, self.data_pub = parsing(root) # Wywołanie funkcji parsowania
            self.pub_time()
            self.combo_dropdown()

        else:
            print("Błąd ładowania kursów walut.")

    # --- Funkcja obsługi listy rozwijanej ---
    def combo_dropdown(self):
        """
        Wypełnia QComboBox dostępnymi walutami.
        """

        self.ui.listaWalut.clear()
        if self.waluty_data:
            for code in sorted(self.waluty_data.keys()): # Sortowanie dla lepszej czytelności
                self.ui.listaWalut.addItem(f"{code} - {self.waluty_data[code]['nazwa']}", code)
        else:
            self.ui.listaWalut.addItem("Brak dostępnych walut")

    # --- Funkcja obliczeń ---
    def calculations(self):
        """
        Pobiera wartości z pól wejściowych interfejsu użytkownika (kwotę, marże) i waliduje je.
        Zwraca kod wybranej waluty, kwotę, marżę S i marżę K (sprzedaż i kupna) po walidacji.
        W przypadku błędu walidacji wyświetla QMessageBox i zwraca wartości None.
        """
        selected_code = self.ui.listaWalut.currentData() # Pobierz dane z ComboBoxa (kod waluty)

        try:
            kwota_str = self.ui.inputKota.text().replace(',', '.')
            kwota = float(kwota_str)

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Wprowadź prawidłową kwotę (liczbę).")
            return None, None, None, None


        try:
            marginS_str = self.ui.inputS.text()
            if not marginS_str: # Sprawdź, czy pole nie jest puste
                marginS = 1.0 # Ustaw na 0.0 lub inną wartość domyślną, jeśli puste
            else:
                marginS = float(marginS_str.replace(',', '.')) # Konwersja na float, obsługa przecinka
        except ValueError:
            QMessageBox.warning(self, "Błąd danych", "Wartość 'Marża S' musi być liczbą. Użyj kropki lub przecinka jako separatora dziesiętnego.")
            return # Zakończ funkcję, jeśli dane są nieprawidłowe
        

        try:
            marginK_str = self.ui.inputK.text()
            if not marginK_str: # Sprawdź, czy pole nie jest puste
                marginK = 1.0 # Ustaw na 0.0 lub inną wartość domyślną, jeśli puste
            else:
                marginK = float(marginK_str.replace(',', '.')) # Konwersja na float, obsługa przecinka
        except ValueError:
            QMessageBox.warning(self, "Błąd danych", "Wartość 'Marża K' musi być liczbą. Użyj kropki lub przecinka jako separatora dziesiętnego.")
            return # Zakończ funkcję, jeśli dane są nieprawidłowe


        if not selected_code or selected_code not in self.waluty_data:
            QMessageBox.warning(self, "Błąd", "Wybierz prawidłową walutę.")
            return

        return selected_code, kwota, marginS, marginK
    
    # --- Funkcja wypełniająca formularz ---
    def fillLab(self, selected_code, kwota, marginS, marginK):
        
        """
        Wykonuje przeliczenie waluty na podstawie podanych danych (wybrana waluta, kwota, marża S, marża K)
        Wyświetla wyniki w odpowiednich polach tekstowych interfejsu. Obsługuje przeliczanie z PLN na walutę 
        obcą i odwrotnie, uwzględniając również marże. Obsługuje także pola radioButtons, które mówią o kierunku 
        przeliczenia.
        """
                

        # Dane do przeliczenia
        currency_info = self.waluty_data[selected_code]
        kurs = currency_info['kurs']
        jednostka = currency_info['jednostka']

        # Przeliczenie waluta obca na PLN
        if self.ui.radioPLN.isChecked():
                
            try:
        
                pln_value = (kwota / jednostka) * kurs
                self.ui.inputWartosc.setText(f"{pln_value:.2f}")

                pln_value_s = (kwota / jednostka) * kurs * marginS
                self.ui.inputS_2.setText(f"{pln_value_s:.2f}")

                pln_value_k = (kwota / jednostka) * kurs * marginK
                self.ui.inputK_2.setText(f"{pln_value_k:.2f}")

            except ValueError:
                QMessageBox.warning(self, "Błąd", "Wprowadź prawidłową kwotę (liczbę).")
            except Exception as e:
                QMessageBox.critical(self, "Błąd", f"Wystąpił nieoczekiwany błąd podczas przeliczania: {e}")


        # Przeliczenie PLN na walutę obcą  
        elif self.ui.radioObca.isChecked():

            try:
                
                obca_value = kwota / kurs * jednostka
                self.ui.inputWartosc.setText(f"{obca_value:.2f}")

                obca_value_s = kwota / kurs * jednostka * marginS
                self.ui.inputS_2.setText(f"{obca_value_s:.2f}")

                obca_value_k = kwota / kurs * jednostka * marginK
                self.ui.inputK_2.setText(f"{obca_value_k:.2f}")

            except ValueError:
                QMessageBox.warning(self, "Błąd", "Wprowadź prawidłową kwotę (liczbę).")
            except Exception as e:
                QMessageBox.critical(self, "Błąd", f"Wystąpił nieoczekiwany błąd podczas przeliczania: {e}")

    # --- Funkcja obsługi nasłuchiwacza ---
    def onClick(self):

        """
        Slot dla przycisku 'Przelicz'.
        Pobiera dane z pól wejściowych, wykonuje walidację, a następnie
        wywołuje funkcję do wypełnienia pól wynikowych.
        """
        selected_code, kwota, marginS, marginK = self.calculations()  # Wywołanie funkcji przeliczającej

        if selected_code is None: # Jeśli selected_code jest None, oznacza to błąd walidacji w calculations
            return # Zakończ działanie, jeśli dane są niepoprawne
        
        self.fillLab(selected_code, kwota, marginS, marginK)          # Wywołanie funkcji wyświetlania

    # --- Funkcja obsługi zegara ---
    def forTimer(self):
        """
        Aktualizuje bieżącą datę i godzinę wyświetlaną w interfejsie użytkownika.
        Metoda wywoływana cyklicznie przez QTimer.
        """
        self.ui.dateNow.setDateTime(QDateTime.currentDateTime())
    
    # --- Funkcja ustawienia daty publikacji ---
    def pub_time(self):
        """
        Ustawia datę publikacji kursów walut NBP w odpowiednim polu interfejsu użytkownika.
        Parsuje datę z formatu tekstowego na obiekt QDate i QDateTime.
        Obsługuje błędy parsowania daty.
        """

        try:
            q_date = QDate.fromString(self.data_pub, "yyyy-MM-dd")
            if q_date.isValid():
                # Tworzymy QDateTime z QDate i stałą godziną 12:00
                q_datetime = QDateTime(q_date, QTime(12, 0))
                self.ui.dateKurs.setDateTime(q_datetime)
            else:
                QMessageBox.warning(self, "Błąd daty", f"Nieprawidłowy format daty publikacji z XML: {self.data_pub}")
        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Nie udało się ustawić daty kursu: {e}")




# --- Główna część programu ---
if __name__ == "__main__":
    app = QApplication([])
    window = Convert()
    window.show()
    app.exec()