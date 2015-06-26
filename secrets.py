# Twilio account credentials

import os

def secrets_account():
	os.environ["account"] = "AC2aead1a6f426bc77734fed0ae25e3075"
	account = os.environ.get('account', 1)
	return account

def secrets_token():
	os.environ["token"] = "4a9e4e9121311ee2429e30fd789e9f9b"
	token = os.environ.get('token', 1)
	return token