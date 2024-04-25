from django.test import TestCase
import jwt
from .views import decode_jwt_token  # Adjust the import according to your project structure

class DecodeJWTTokenTests(TestCase):

    def setUp(self):
        # This token is crafted for the purpose of testing
        self.jwt_token = jwt.encode({
            'sub': '1234567890',
            'aud': 'your-audience',
            'scope': 'read:messages'
        }, 'secret', algorithm='HS256')

    def test_decode_jwt_token(self):
        """ Test that the JWT token is decoded correctly. """
        decoded_data = decode_jwt_token(self.jwt_token)
        self.assertEqual(decoded_data['sub'], '1234567890')
        self.assertEqual(decoded_data['aud'], 'your-audience')
        self.assertEqual(decoded_data['scope'], 'read:messages')

    def test_decode_jwt_token_with_missing_fields(self):
        """ Test decoding a JWT with some fields missing. """
        # Creating a JWT with a missing 'aud' field
        incomplete_jwt_token = jwt.encode({
            'sub': '1234567890',
            'scope': 'read:messages'
        }, 'secret', algorithm='HS256')

        with self.assertRaises(KeyError):
            decode_jwt_token(incomplete_jwt_token)

    def test_decode_jwt_token_invalid(self):
        """ Test the function with an invalid token. """
        invalid_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.HokynJmnx_8LX9NB_fvhegadLldoDLAIdZ5o9EVGsQg'
        decoded_data = decode_jwt_token(invalid_token)
        self.assertEqual(decoded_data, {})
