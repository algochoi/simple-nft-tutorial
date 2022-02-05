from algosdk import account

private_key, public_key = account.generate_account()

# Use string format for <3.7 compatibility
print("Public key: {}".format(public_key))

# Not the wisest idea to expose this, but feel free to uncomment.
# print("Private key: {}".format(private_key))

with open(".env", "w") as f:
    f.write('ALGORAND_ADDRESS="{}"\n'.format(public_key))
    f.write('ALGORAND_SECRET="{}"\n'.format(private_key))
    f.write('PURESTAKE_KEY=""\n')
    f.write('SECOND_ADDRESS="{}"\n'.format(public_key))
    f.write('SECOND_SECRET="{}"\n'.format(private_key))
