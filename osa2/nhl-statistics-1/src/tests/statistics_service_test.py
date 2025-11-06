import unittest
from statistics_service import StatisticsService
from player import Player

# --- Stub-luokka (korvaa verkkoyhteyden) ---
class PlayerReaderStub:
    "CLASS DOCSTRING"
    def get_players(self):
        "Function or method docstring"
        # Kovakoodattu pelaajalista testejä varten
        # name, team, goals, assists) ovat pelaajien tiedot.
        return [
            Player("Semenko", "EDM", 4, 12),    # 16 pistettä
            Player("Lemieux", "PIT", 45, 54),   # 99 pistettä
            Player("Kurri",   "EDM", 37, 53),   # 90 pistettä
            Player("Yzerman", "DET", 42, 56),   # 98 pistettä
            Player("Gretzky", "EDM", 35, 89)    # 124 pistettä (ENITEN PISTEITÄ)
        ]


class TestStatisticService(unittest.TestCase):
    "CLASS DOCSTRING"
    # setUp nimeäminen ja sijoitus luokkaan, joka perii unittest.
    # tarkoittaa sitä, että setUp ajetaan jokaiselle testille uudestaan.
    def setUp(self):
        """Suoritetaan ennen jokaista testimetodia. Alustaa testattavan olion."""
        # injektoidaan stub StatisticsService-oliolle
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_statistics_service_alustus(self):
        """
        TÄMÄ ON DOCSTRING
        Testaa, että __init__-metodi toimii:
        1. Varmistaa riippuvuuden injektoinnin (self._reader).
        2. Varmistaa datan lataamisen (self._players).
        """

        # Tarkista, että lukija on tallennettu (assertIsInstance toimii nyt)
        self.assertIsInstance(self.stats._reader, PlayerReaderStub)

        # Tarkista, että pelaajat on ladattu
        players_list = self.stats._players

        # Varmista, että pelaajia on 5 (Määritelty PlayerReaderStub:issa)
        self.assertEqual(len(players_list), 5)

        # Varmista, että listan ensimmäinen pelaaja on se, mitä odotetaan
        self.assertEqual(players_list[0].name, "Semenko")
        self.assertEqual(players_list[0].team, "EDM")
        self.assertEqual(players_list[0].goals, 4)
        self.assertEqual(players_list[0].assists, 12)
 