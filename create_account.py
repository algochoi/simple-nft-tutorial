from algosdk import account, mnemonic

private_key, public_key = account.generate_account()
print("Public key: {}".format(public_key))
print("Private key: {}".format(private_key))
