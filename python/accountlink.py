#! /usr/bin/env python
# coding: utf-8

import pprint
import datetime
import paypayopa

def accountLink(client):

  payload = {
    "scopes": [
      "direct_debit",
      "pending_payments",
      "get_balance",
      "preauth_capture_transaction",
      "continuous_payments",
      "cashback",
      "preauth_capture_native"
    ],
    "nonce": "abc",
    "redirectType": "WEB_LINK",
    "redirectUrl": "https://www.paypay-corp.co.jp",
    "referenceId": "12345678",
    "phoneNumber": ""
  }

  client.Account.create_qr_session(payload)

if __name__ == "__main__":

  API_KEY = ""
  API_SECRET = ""
  MERCHANT_ID = ""

  #Set True for Production Environment. By Default this is set False for Sandbox Environment.
  client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
  client.set_assume_merchant(MERCHANT_ID)

  accountLink(client)
