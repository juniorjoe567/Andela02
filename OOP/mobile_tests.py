import unittest
from mobile import MobilePhone, Samsung, Nokia, SamsungS5

class MobilePhoneTests(unittest.TestCase):

    """ Test for sub-class being an instance of super class """
    def test_is_phone(self):
        samsung_phone = Samsung('galaxy note')
        samsung_s5 = SamsungS5()
        assert(isinstance(samsung_phone, MobilePhone))
        assert(isinstance(samsung_s5, Samsung))

    """ Test polymorphism """
    def test_polymorphism(self):
        samsung_phone = Samsung('galaxy note')
        nokia_phone = Nokia('3310')
        assert(isinstance(samsung_phone.getIMEIcode(), str))
        assert(isinstance(nokia_phone.getIMEIcode(1), str))

    """ Test inheritance """
    def test_inheritance(self):
        samsung_s5 = SamsungS5()
        self.assertEqual(samsung_s5.getIMEIcode(), 'SAMS123455667', msg='IMEI should be SAMS123455667')

if __name__ == '__main__':
    unittest.main()
