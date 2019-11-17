# importing
import time

import requests
import json

# get request from local server


def get_balance(id):
    req = requests.get("https://api-sandbox.starlingbank.com/api/v2/accounts/" + id + "/balance",
                       headers={
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJQUzI1NiJ9.eyJpc3MiOiJhcGktZGVtby5zdGFybGluZ2JhbmsuY29tIiwic3ViIjoiZGFlOGM3YjEtY2IyYi00NGU0LWFjMjctMzhkNmE2ZGJjZDBmIiwiZXhwIjoxNTc0MDIzODUwLCJpYXQiOjE1NzM5Mzc0NTAsInNjb3BlIjoiYWNjb3VudC1ob2xkZXItbmFtZTpyZWFkIGFjY291bnQtaG9sZGVyLXR5cGU6cmVhZCBhY2NvdW50LWlkZW50aWZpZXI6cmVhZCBhY2NvdW50LWxpc3Q6cmVhZCBhY2NvdW50OnJlYWQgYWRkcmVzczplZGl0IGFkZHJlc3M6cmVhZCBhdHRhY2htZW50OnJlYWQgYXR0YWNobWVudDp3cml0ZSBhdXRob3Jpc2luZy1pbmRpdmlkdWFsOnJlYWQgYmFsYW5jZTpyZWFkIGNhcmQtY29udHJvbDplZGl0IGNhcmQ6cmVhZCBjb25maXJtYXRpb24tb2YtZnVuZHM6cmVhZCBjdXN0b21lcjpyZWFkIGVtYWlsOmVkaXQgbWFuZGF0ZTpkZWxldGUgbWFuZGF0ZTpyZWFkIG1hcmtldGluZy1wcmVmZXJlbmNlczpyZWFkIG1hcmtldGluZy1wcmVmZXJlbmNlczp3cml0ZSBtZXJjaGFudDpyZWFkIG1ldGFkYXRhOmNyZWF0ZSBtZXRhZGF0YTplZGl0IHBheWVlOmNyZWF0ZSBwYXllZTpkZWxldGUgcGF5ZWU6ZWRpdCBwYXllZS1pbWFnZTpyZWFkIHBheWVlOnJlYWQgcGF5LWxvY2FsOmNyZWF0ZSBwYXktbG9jYWwtb25jZTpjcmVhdGUgcGF5LWxvY2FsOnJlYWQgcHJvZmlsZS1pbWFnZTplZGl0IHByb2ZpbGUtaW1hZ2U6cmVhZCByZWNlaXB0OnJlYWQgcmVjZWlwdHM6cmVhZCByZWNlaXB0OndyaXRlIHNhdmluZ3MtZ29hbDpjcmVhdGUgc2F2aW5ncy1nb2FsOmRlbGV0ZSBzYXZpbmdzLWdvYWw6cmVhZCBzYXZpbmdzLWdvYWwtdHJhbnNmZXI6Y3JlYXRlIHNhdmluZ3MtZ29hbC10cmFuc2ZlcjpkZWxldGUgc2F2aW5ncy1nb2FsLXRyYW5zZmVyOnJlYWQgc3RhbmRpbmctb3JkZXI6Y3JlYXRlIHN0YW5kaW5nLW9yZGVyOmRlbGV0ZSBzdGFuZGluZy1vcmRlcjpyZWFkIHN0YXRlbWVudC1jc3Y6cmVhZCBzdGF0ZW1lbnQtcGRmOnJlYWQgdHJhbnNhY3Rpb246ZWRpdCB0cmFuc2FjdGlvbjpyZWFkIiwiYWNjb3VudEhvbGRlclVpZCI6Ijg0ZTM1MjhlLTFjNTctNDA5Mi04ZTZiLTU2YTZiZjYyZmM5MSIsInRva2VuVWlkIjoiNDVlMmMwZjItNWZhNy00OGIyLTgxNjEtZjAwODAzZWU3NTk3IiwiYXBpQWNjZXNzVWlkIjoiYmNjYjFhNmQtYmM1NC00OGU1LTg5ZTMtZWI4YWMzMjdkNTI2In0.jynX28MydgRYcSM00Y32xHCoMtWL7f1pOS9qU2W49mUCam6Gvbiq3bmgF1qrQYFEbxZgb0KlLqrK_2TlEctajnZDQWB_6S9zktHI9h3yOTTgXQi6-vlO1EayoGCL2hJDMWJ7fGX_oyvXqfO8V5r8qF_4A0Qyp1k5OJZst05-ZVdGwA1phfoDTh_WArlDfdiZwnMLGATXfq4_l49FCOfSHCgmftoReE7rWTBfkRTBWXHGRefLCCvGO9OzRCx4Bf8v26iNdctNEsyXhvjDweJyXM6OQj3dGyoE8HkUW878sf5qOUVlp_5etuC39sEPZna53x2RINRKxf2yueyIEkJg1lciTeeuUvIsEdFzjQiFnPeyQa-DgzHzfhTeiQlbFtLCuQFpK7_fmJgsunQJzZHlsXbaJSxaysRVcpgHHdAYSUaonNRLdo8EAOTs0r9FBgf3DE-8bThc2HDiS0RUf3TQM7ywSOiFG9IlyR-9AbhqUCnkgwSuYCR_px4SP3Zl59Iolwxlm-UdH_jSwqnVbvjjr40gElErqRmaJnWBP5z25C-lJuo-ehiHWbM6hQooNfm82JfLHBVh8yBjhloi41KpANtBXWTIQsrkt6xeIQfQccQ-Gat79_dpNn2NUuO-RrH0qh67Aky0cJdTHYNNTGhTM91DS04Ey8bxfXJs2nn211o"
  })
    balances = req.json()
    print(balances)
    balance = balances['availableToSpend']['minorUnits'] / 100
    return balance


def get_feed(id, cat):
    req = requests.get("https://api-sandbox.starlingbank.com/api/v2/feed/account/" + id + "/category/" + cat,
                       headers={
                           "Accept": "application/json",
                           "Content-Type": "application/json",
                           "Authorization": "Bearer eyJhbGciOiJQUzI1NiJ9.eyJpc3MiOiJhcGktZGVtby5zdGFybGluZ2JhbmsuY29tIiwic3ViIjoiZGFlOGM3YjEtY2IyYi00NGU0LWFjMjctMzhkNmE2ZGJjZDBmIiwiZXhwIjoxNTc0MDIzODUwLCJpYXQiOjE1NzM5Mzc0NTAsInNjb3BlIjoiYWNjb3VudC1ob2xkZXItbmFtZTpyZWFkIGFjY291bnQtaG9sZGVyLXR5cGU6cmVhZCBhY2NvdW50LWlkZW50aWZpZXI6cmVhZCBhY2NvdW50LWxpc3Q6cmVhZCBhY2NvdW50OnJlYWQgYWRkcmVzczplZGl0IGFkZHJlc3M6cmVhZCBhdHRhY2htZW50OnJlYWQgYXR0YWNobWVudDp3cml0ZSBhdXRob3Jpc2luZy1pbmRpdmlkdWFsOnJlYWQgYmFsYW5jZTpyZWFkIGNhcmQtY29udHJvbDplZGl0IGNhcmQ6cmVhZCBjb25maXJtYXRpb24tb2YtZnVuZHM6cmVhZCBjdXN0b21lcjpyZWFkIGVtYWlsOmVkaXQgbWFuZGF0ZTpkZWxldGUgbWFuZGF0ZTpyZWFkIG1hcmtldGluZy1wcmVmZXJlbmNlczpyZWFkIG1hcmtldGluZy1wcmVmZXJlbmNlczp3cml0ZSBtZXJjaGFudDpyZWFkIG1ldGFkYXRhOmNyZWF0ZSBtZXRhZGF0YTplZGl0IHBheWVlOmNyZWF0ZSBwYXllZTpkZWxldGUgcGF5ZWU6ZWRpdCBwYXllZS1pbWFnZTpyZWFkIHBheWVlOnJlYWQgcGF5LWxvY2FsOmNyZWF0ZSBwYXktbG9jYWwtb25jZTpjcmVhdGUgcGF5LWxvY2FsOnJlYWQgcHJvZmlsZS1pbWFnZTplZGl0IHByb2ZpbGUtaW1hZ2U6cmVhZCByZWNlaXB0OnJlYWQgcmVjZWlwdHM6cmVhZCByZWNlaXB0OndyaXRlIHNhdmluZ3MtZ29hbDpjcmVhdGUgc2F2aW5ncy1nb2FsOmRlbGV0ZSBzYXZpbmdzLWdvYWw6cmVhZCBzYXZpbmdzLWdvYWwtdHJhbnNmZXI6Y3JlYXRlIHNhdmluZ3MtZ29hbC10cmFuc2ZlcjpkZWxldGUgc2F2aW5ncy1nb2FsLXRyYW5zZmVyOnJlYWQgc3RhbmRpbmctb3JkZXI6Y3JlYXRlIHN0YW5kaW5nLW9yZGVyOmRlbGV0ZSBzdGFuZGluZy1vcmRlcjpyZWFkIHN0YXRlbWVudC1jc3Y6cmVhZCBzdGF0ZW1lbnQtcGRmOnJlYWQgdHJhbnNhY3Rpb246ZWRpdCB0cmFuc2FjdGlvbjpyZWFkIiwiYWNjb3VudEhvbGRlclVpZCI6Ijg0ZTM1MjhlLTFjNTctNDA5Mi04ZTZiLTU2YTZiZjYyZmM5MSIsInRva2VuVWlkIjoiNDVlMmMwZjItNWZhNy00OGIyLTgxNjEtZjAwODAzZWU3NTk3IiwiYXBpQWNjZXNzVWlkIjoiYmNjYjFhNmQtYmM1NC00OGU1LTg5ZTMtZWI4YWMzMjdkNTI2In0.jynX28MydgRYcSM00Y32xHCoMtWL7f1pOS9qU2W49mUCam6Gvbiq3bmgF1qrQYFEbxZgb0KlLqrK_2TlEctajnZDQWB_6S9zktHI9h3yOTTgXQi6-vlO1EayoGCL2hJDMWJ7fGX_oyvXqfO8V5r8qF_4A0Qyp1k5OJZst05-ZVdGwA1phfoDTh_WArlDfdiZwnMLGATXfq4_l49FCOfSHCgmftoReE7rWTBfkRTBWXHGRefLCCvGO9OzRCx4Bf8v26iNdctNEsyXhvjDweJyXM6OQj3dGyoE8HkUW878sf5qOUVlp_5etuC39sEPZna53x2RINRKxf2yueyIEkJg1lciTeeuUvIsEdFzjQiFnPeyQa-DgzHzfhTeiQlbFtLCuQFpK7_fmJgsunQJzZHlsXbaJSxaysRVcpgHHdAYSUaonNRLdo8EAOTs0r9FBgf3DE-8bThc2HDiS0RUf3TQM7ywSOiFG9IlyR-9AbhqUCnkgwSuYCR_px4SP3Zl59Iolwxlm-UdH_jSwqnVbvjjr40gElErqRmaJnWBP5z25C-lJuo-ehiHWbM6hQooNfm82JfLHBVh8yBjhloi41KpANtBXWTIQsrkt6xeIQfQccQ-Gat79_dpNn2NUuO-RrH0qh67Aky0cJdTHYNNTGhTM91DS04Ey8bxfXJs2nn211o"
                       })
    feed = req.json()
    return feed

def get_last_transaction_from_feed(id, cat):
    feed = get_feed(id, cat)
    for item in feed['feedItems']:
        if item['source'] == 'DIRECT_DEBIT' or item['status'] == 'UPCOMING':
            continue
        else:
            print(item)
            return item


def assess_last_transaction(id, cat, last):
    last = get_last_transaction_from_feed(id, cat)
    amount = last['amount']['minorUnits'] / 100
    direction = last['direction']
    name = last['counterPartyName']
    category = last['spendingCategory']
    return (amount, direction, name, category)



uid = '62f3071c-7e72-423a-9dcc-72870b5b8f89'
category = "6ffaa2d3-eb66-4050-9f3e-91a3b7c1f310"
print(get_balance(uid))
last = get_last_transaction_from_feed(uid, category)
verdict = assess_last_transaction(uid, category, last)
while True:
    new_last = get_last_transaction_from_feed(uid, category)
    if new_last == last:
        time.sleep(15)
    else:
        last = get_last_transaction_from_feed(uid, category)
        verdict = assess_last_transaction(uid, category, last)
        print(verdict)
        #####MEMEAGE