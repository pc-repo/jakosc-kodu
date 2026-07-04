import urllib.request
import xml.etree.ElementTree as ET
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QTimer, QDateTime, QDate, QTime
from ui_gui_beta import Ui_MainWindow

# --- Stałe konfiguracyjne ---
NBP_URL = 'https://static.nbp.pl/dane/kursy/xml/LastA.xml'
XML_FILENAME = 'kurs.xml'
DATE_FORMAT_XML = "yyyy-MM-dd"
DATETIME_DISPLAY_FORMAT = "yyyy-MM-dd HH:mm:ss"

# --- Funkcje pomocnicze ---
def _show_error_message(parent, title, message):
    """Wyświetla okno dialogowe z komunikatem o błędzie."""
    QMessageBox.critical(parent, title, message)

def _show_warning_message(parent, title, message):
    """Wyświetla okno dialogowe z komunikatem ostrzegawczym."""
    QMessageBox.warning(parent, title, message)

def _parse_float_input(text_input: str, field_name: str, parent=None) -> float | None:
    """Parsuje tekst na float, obsługując przecinki i wyświetlając błędy."""
    if not text_input:
        return 1.0 # Domyślna wartość dla pustych pól marży
    try:
        return float(text_input.replace(',', '.'))
    except ValueError:
        _show_warning_message(parent, "Błąd danych",
                              f"Wartość '{field_name}' musi być liczbą. Użyj kropki lub przecinka jako separatora dziesiętnego.")
        return None

# --- Funkcje pobierania i parsowania danych ---
def get_exchange_rates_xml(url: str, filename: str) -> ET.ElementTree | None:
    """
    Pobiera plik XML z kursami walut NBP i zapisuje go lokalnie.
    Zwraca obiekt ElementTree po pomyślnym pobraniu i sparsowaniu.
    """
    try:
        urllib.request.urlretrieve(url, filename)
        return ET.parse(filename)
    except urllib.error.URLError as e:
        _show_error_message(None, "Błąd połączenia", f"Nie udało się połączyć z serwerem NBP: {e}")
        return None
    except ET.ParseError as e:
        _show_error_message(None, "Błąd parsowania XML", f"Nie udało się sparsować pliku XML: {e}")
        return None
    except Exception as e: # Catch any other unexpected errors
        _show_error_message(None, "Nieoczekiwany błąd", f"Wystąpił nieoczekiwany błąd podczas pobierania: {e}")
        return None

def parse_exchange_rates(root: ET.Element) -> tuple[dict, str | None]:
    """
    Parsuje dane walutowe z elementu głównego XML i zwraca słownik.
    Przekazuje także datę publikacji aktualnych kursów.
    """
    waluty = {}
    data_pub = None

    data_tag = root.find('data_publikacji')
    if data_tag is not None and data_tag.text:
        data_pub = data_tag.text

    for pozycja in root.findall('pozycja'):
        try:
            name = pozycja.find('nazwa_waluty').text
            code = pozycja.find('kod_waluty').text.upper()
            rate_str = pozycja.find('kurs_sredni').text
            rate = float(rate_str.replace(',', '.'))
            unit = int(pozycja.find('przelicznik').text)

            if all([name, code, rate_str, rate, unit is not None]): # Sprawdzenie czy wszystkie kluczowe dane istnieją
                waluty[code] = {
                    'nazwa': name,
                    'kurs': rate,
                    'jednostka': unit
                }
            else:
                print(f"Ostrzeżenie: Brak kompletnych danych dla waluty w pozycji: {ET.tostring(pozycja, encoding='unicode').strip()}")
        except (AttributeError, TypeError) as e:
            print(f"Ostrzeżenie: Błąd parsowania elementu waluty (brakujący tag lub wartość None): {e} w pozycji: {ET.tostring(pozycja, encoding='unicode').strip()}")
        except ValueError as e:
            print(f"Ostrzeżenie: Błąd konwersji danych dla waluty (np. kurs, jednostka): {e} w pozycji: {ET.tostring(pozycja, encoding='unicode').strip()}")
    return waluty, data_pub

# --- Klasa głównego okna aplikacji ---
class Convert(QMainWindow):

    def __init__(self):
        """
        Inicjalizuje główne okno aplikacji konwertera walut.
        Konfiguruje interfejs użytkownika, łączy sygnały z slotami
        i ustawia początkowy stan aplikacji.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.waluty_data: dict = {}
        self.data_pub: str | None = None

        self._connect_signals_slots()
        self._setup_timer()
        self._set_initial_ui_state()

        # Załaduj dane walut przy starcie aplikacji
        # self.load_data() # Odkomentuj, jeśli chcesz ładować dane przy starcie

    def _connect_signals_slots(self):
        """Łączy sygnały z odpowiednimi slotami."""
        self.ui.synchroBtn.clicked.connect(self.load_data)
        self.ui.exitBtn.clicked.connect(QApplication.quit)
        self.ui.convertBtn.clicked.connect(self._handle_conversion)

    def _setup_timer(self):
        """Konfiguruje i uruchamia timer do aktualizacji bieżącej daty i czasu."""
        self.ui.dateNow.setDisplayFormat(DATETIME_DISPLAY_FORMAT)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._update_current_datetime)
        self.timer.start()
        self._update_current_datetime() # Ustaw od razu

    def _set_initial_ui_state(self):
        """Ustawia początkowy stan elementów interfejsu użytkownika."""
        self.ui.radioPLN.setChecked(True)
        self.ui.inputKota.setFocus()

    def load_data(self):
        """
        Pobiera plik XML z kursami walut, parsuje go i aktualizuje dane w aplikacji.
        Odświeża listę rozwijaną walut i datę publikacji.
        """
        QApplication.processEvents() # Odśwież UI, aby użytkownik widział status

        tree = get_exchange_rates_xml(NBP_URL, XML_FILENAME)
        if tree:
            root = tree.getroot()
            self.waluty_data, self.data_pub = parse_exchange_rates(root)
            if self.waluty_data:
                self._populate_currency_dropdown()
                self._set_publication_time()
            else:
                _show_warning_message(self, "Brak danych", "Nie znaleziono danych walutowych w pliku XML.")
        else:
            print("Błąd ładowania kursów walut.") # Komunikat już został wyświetlony przez get_exchange_rates_xml

    def _populate_currency_dropdown(self):
        """Wypełnia QComboBox dostępnymi walutami."""
        self.ui.listaWalut.clear()
        if self.waluty_data:
            for code in sorted(self.waluty_data.keys()):
                self.ui.listaWalut.addItem(f"{code} - {self.waluty_data[code]['nazwa']}", code)
        else:
            self.ui.listaWalut.addItem("Brak dostępnych walut")

    def _validate_inputs(self) -> tuple[str | None, float | None, float | None, float | None]:
        """
        Waliduje dane wejściowe z pól GUI (kwota, marże) i zwraca je.
        Wyświetla QMessageBox w przypadku błędu walidacji.
        """
        selected_code = self.ui.listaWalut.currentData()
        if not selected_code or selected_code not in self.waluty_data:
            _show_warning_message(self, "Błąd", "Wybierz prawidłową walutę.")
            return None, None, None, None

        kwota = _parse_float_input(self.ui.inputKota.text(), "Kwota do przeliczenia", self)
        if kwota is None: return None, None, None, None # Błąd w parsing kwoty

        marginS = _parse_float_input(self.ui.inputS.text(), "Marża sprzedaży", self)
        if marginS is None: return None, None, None, None

        marginK = _parse_float_input(self.ui.inputK.text(), "Marża kupna", self)
        if marginK is None: return None, None, None, None

        return selected_code, kwota, marginS, marginK

    def _perform_conversion(self, selected_code: str, kwota: float, marginS: float, marginK: float):
        """
        Wykonuje przeliczenie waluty i aktualizuje pola wyjściowe w GUI.
        """
        try:
            currency_info = self.waluty_data[selected_code]
            kurs = currency_info['kurs']
            jednostka = currency_info['jednostka']

            if self.ui.radioPLN.isChecked():
                # Przeliczanie z waluty obcej na PLN
                pln_base = (kwota / jednostka) * kurs
                self.ui.inputWartosc.setText(f"{pln_base:.2f}")
                self.ui.inputS_2.setText(f"{pln_base * marginS:.2f}")
                self.ui.inputK_2.setText(f"{pln_base * marginK:.2f}")
            elif self.ui.radioObca.isChecked():
                # Przeliczanie z PLN na walutę obcą
                obca_base = kwota / kurs * jednostka
                self.ui.inputWartosc.setText(f"{obca_base:.2f}")
                self.ui.inputS_2.setText(f"{obca_base * marginS:.2f}")
                self.ui.inputK_2.setText(f"{obca_base * marginK:.2f}")
        except KeyError:
            _show_error_message(self, "Błąd danych", f"Nie znaleziono danych dla wybranej waluty: {selected_code}")
        except Exception as e:
            _show_error_message(self, "Błąd obliczeń", f"Wystąpił nieoczekiwany błąd podczas przeliczania: {e}")

    def _handle_conversion(self):
        """
        Slot dla przycisku 'Przelicz'.
        Pobiera i waliduje dane wejściowe, a następnie wywołuje funkcję przeliczającą.
        """
        selected_code, kwota, marginS, marginK = self._validate_inputs()

        if selected_code is not None: # Jeśli walidacja przeszła pomyślnie
            self._perform_conversion(selected_code, kwota, marginS, marginK)

    def _update_current_datetime(self):
        """
        Aktualizuje bieżącą datę i godzinę wyświetlaną w interfejsie użytkownika.
        Metoda wywoływana cyklicznie przez QTimer.
        """
        self.ui.dateNow.setDateTime(QDateTime.currentDateTime())

    def _set_publication_time(self):
        """
        Ustawia datę publikacji kursów walut NBP w odpowiednim polu interfejsu użytkownika.
        Parsuje datę z formatu tekstowego na obiekt QDate i QDateTime.
        Obsługuje błędy parsowania daty.
        """
        if not self.data_pub:
            _show_warning_message(self, "Brak daty", "Brak daty publikacji kursów w pliku XML.")
            return

        try:
            q_date = QDate.fromString(self.data_pub, DATE_FORMAT_XML)
            if q_date.isValid():
                # Tworzymy QDateTime z QDate i stałą godziną 12:00, ponieważ XML NBP nie zawiera godziny
                q_datetime = QDateTime(q_date, QTime(12, 0))
                self.ui.dateKurs.setDateTime(q_datetime)
            else:
                _show_warning_message(self, "Błąd daty", f"Nieprawidłowy format daty publikacji z XML: {self.data_pub}")
        except Exception as e:
            _show_error_message(self, "Błąd ustawienia daty", f"Nie udało się ustawić daty kursu: {e}")

# --- Główna część programu ---
if __name__ == "__main__":
    app = QApplication([])
    window = Convert()
    window.show()
    app.exec()