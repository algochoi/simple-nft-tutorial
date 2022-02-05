from algosdk import account, mnemonic

private_key, public_key = account.generate_account()
print("Public key: {}".format(public_key))
# Not a wise idea to expose this, but feel free to uncomment.
# print("Private key: {}".format(private_key))

with open(".env", "w") as f:
    f.write('ALGORAND_ADDRESS="{}"\n'.format(public_key))
    f.write('ALGORAND_SECRET="{}"'.format(private_key))
