import unittest
import v3

class test_suite_v3(unittest.TestCase):
    def test_verify_local(self):
        #Test verifying file
        self.assertFalse(v3.verify_local("Nonexistent_file"))

    def test_verify_local2(self):
        self.assertTrue(v3.verify_local("test.mp4"))

    def test_verify_youtube(self):
        #Test verifying Youtube
        self.assertFalse(v3.verify_youtube("http://google.com"))

    def test_verify_youtube2(self):
        self.assertTrue(v3.verify_youtube("http://www.youtube.com/watch?v=otpFNL3yem4"))

    def test_local(self):
        #Test the preplayer
        self.assertFalse(v3.local("Nonexistent_url"))

    def test_local2(self):
        self.assertTrue(v3.local("test.mp4"))

    def test_youtube(self):
        #Test the preplayer
        self.assertFalse(v3.youtube("http://google.com"))

    def test_youtube2(self):
        self.assertTrue(v3.youtube("http://www.youtube.com/watch?v=otpFNL3yem4"))

if __name__ == '__main__':
    unittest.main()
