from app import app
import unittest


class ErrorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_pagenotfound_statuscode(self):
        result = self.app.get('/missing-page/')

        self.assertEqual(result.status_code, 404)

    # def test_pagenotfound_data(self):
    #     result = self.app.get('/missing-page/')
    #
    #     self.assertIn('Page Not Found', result.data)

    # def test_unhandledexception_code(self):
    #     result = self.app.put('/undhandled-exception')
    #
    #     self.assertEqual(result.status_code, 500)

    # def test_unhandledexception_data(self):
    #     result = self.app.put('/undhandled-exception')
    #
    #     self.assertIn('Something Went Wrong', result.data)


if __name__ == '__main__':
    print('Loading unittests...')
    unittest.main()  # '-v'
