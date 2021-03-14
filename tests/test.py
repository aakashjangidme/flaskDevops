try:
    import unittest
    from api import create_app
except Exception as e:
    print("Error importing modules %s"%(e))


class FlaskAppTest(unittest.TestCase):
    #executed prior each test
    def setUp(self):
        # the app instance
        app = create_app()
        # some app config
        app.config['TESTING'] = True
        app.config['Debug'] = False
        # assin unittest class the instance of the app's test_client
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### Tests ####
    ###############

    def test_main_route(self):
        response = self.app.get('api/')
        self.assertEqual(response.status_code, 200)

    def test_main_route_response(self):
        response = self.app.get('api/')
        self.assertEqual(response.json['message'], "Hello There world")



if __name__ == "__main__":
    unittest.main()
