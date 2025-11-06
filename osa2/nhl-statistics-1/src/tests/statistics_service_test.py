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
        # Tarkista, että lukija on tallennettu 
        self.assertIsInstance(self.stats._reader, PlayerReaderStub)

        # Varmista, että pelaajia on 5 (Määritelty PlayerReaderStub:issa)
        players_list = self.stats._players
        self.assertEqual(len(players_list), 5)

        # Varmista, että listan ensimmäinen pelaaja on se, mitä odotetaan
        self.assertEqual(players_list[0].name, "Semenko")
        self.assertEqual(players_list[0].team, "EDM")
        self.assertEqual(players_list[0].goals, 4)
        self.assertEqual(players_list[0].assists, 12)

    def test_etsi_onnistuu(self):
        "find metodi onnistuu"
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")
        self.assertEqual(player.team, "PIT")

    def test_etsi_ei_onnistu(self):
        "find metodi ei onnistu"
        player = self.stats.search("eiole")
        self.assertIsNone(player)

    def test_listaa_joukkueen_pelaajat(self):
        "team metodi testaus: listaa joukkueen pelaajat"
        # varmistetaan että EDM joukkueesta löytyy 3 pelaajaa.
        # team metod on statistics servicen etsijä metodi
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        # tarlostetaan ensimmäienn ja viimeinen pelaaja
        self.assertEqual(edm_players[0].name, "Semenko")
        self.assertEqual(edm_players[2].name, "Gretzky")
        # varmistetaan myös että kaikki pelaajat ovat EDM:stä
        for player in edm_players:
            self.assertEqual(player.team, "EDM")

    def test_pelaaja_piste_listaus(self):
        """
        top-metodi testi.
        """
        top_3 = self.stats.top(2)

        # Varmistetaan, että palautuslista on oikean kokoinen
        self.assertEqual(len(top_3), 3)

        # Varmistetaan, että ensimmäinen on Gretzky (124 pistettä)
        self.assertEqual(top_3[0].name, "Gretzky") 

        # Varmistetaan, että kolmas on Yzerman (98 pistettä)
        self.assertEqual(top_3[2].name, "Yzerman")
