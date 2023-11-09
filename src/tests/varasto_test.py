import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nolla_tilavuus(self):
        wh_zero = Varasto(0)
        self.assertAlmostEqual(wh_zero.tilavuus, 0)

    def test_konstruktori_saldo_neg(self):
        wh_zero = Varasto(0, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_saldo_gt_tilavuus(self):
        wh_zero = Varasto(0, 1)
        self.assertAlmostEqual(wh_zero.tilavuus, 0)
        self.assertAlmostEqual(wh_zero.saldo, 0)

    def test_lisays_lisaa_saldoa_neg(self):
        pre_qty = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, pre_qty)

    def test_lisays_lisaa_saldoa_yli_volyymin(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_neg(self):
        qty_saldo = self.varasto.saldo
        qty_otto = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(qty_otto, 0)
        self.assertAlmostEqual(self.varasto.saldo, qty_saldo)

    def test_ottaminen_yli_saldon(self):
        qty_saldo = self.varasto.saldo
        qty_otto = self.varasto.ota_varastosta(1)

        self.assertAlmostEqual(qty_saldo, 0)
        self.assertAlmostEqual(qty_otto, 1)

    def test_varasto_toString(self):
        print(self.varasto)
