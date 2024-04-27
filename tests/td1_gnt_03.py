import unittest
from mrz.generator.td1 import TD1CodeGenerator, dictionary


class TestCase10(unittest.TestCase):

    def test_td1_generator(self):
        # test truncation. Example adopted from:
        # https://www.icao.int/publications/Documents/9303_p5_cons_en.pdf
        td1_generator = TD1CodeGenerator("id", "THA", "955555546", "680229", "f", "130724", "THA",
                                         "NILAVADHANANANDA", "CHAYAPA DEJTHAMRONG KRASUANG", "2902968000000")

        result = ("IDTHA95555554612902968000000<<\n"
                  "6802295F1307245THA<<<<<<<<<<<6\n"
                  "NILAVADHANANANDA<<CHAYAPA<DE<K")

        self.assertEqual(str(td1_generator), result)


if __name__ == '__main__':
    unittest.main()