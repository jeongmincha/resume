import unittest
from test import support

class TestCheckFormatResume(unittest.TestCase):
    def setUp(self):
        self.resume_en = open('./en/README.md', encoding='utf-8')
        self.resume_ko = open('./ko/README.md', encoding='utf-8')
        self.resume_en_text = self.resume_en.read()
        self.resume_ko_text = self.resume_ko.read()
        self.resume_en.close()
        self.resume_ko.close()
    
    def testSamsNumberAsterisks(self):
        self.assertEqual(self.resume_en_text.count('*'), self.resume_ko_text.count('*'))
    
    # TODO: make new test considering the hierarchy of the documents


if __name__ == '__main__':
    unittest.main()