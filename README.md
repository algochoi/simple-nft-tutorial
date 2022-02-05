# A Simple NFT Tutorial for Algorand Hackers

Let's make a simple NFT on the Algorand TestNet! We'll use the [Purestake API](https://www.purestake.com/), [NFT Storage](https://nft.storage/#getting-started), and the [Algorand Python SDK](https://github.com/algorand/py-algorand-sdk) to programmatically create some NFTs on the fly. [^disclaimer]

## Pre-requisites
* You should hopefully know how to use the terminal. On MacOS or Ubuntu (any Linux-based OS), just open up your terminal. If you are on Windows, I recommend you install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install), and you will be able to run a Ubuntu terminal on your machine. 
* Your machine should have `git` and `python` installed.

## Clone this repo 
Open up your terminal and do the following:
```
git clone [this-repo-link]
cd [this repo]
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Create your first [Algorand account](https://developer.algorand.org/docs/get-details/accounts/)
An account consists of a `public key` and a `private key`. 
* The `public key` (aka `wallet address`, or `Algorand address`, which is an encoded form of the public key) is like your banking number that people can use to send you money. This is okay to share with your friends.
* The `private key` (aka `secret`, or sometimes `mnemonic`, which refers to a set of English words that can be translated into a private key) is like your banking PIN. It's probably not a good idea to share your PIN in real life either, so **DO NOT** share your `private key` with anyone![^1]

> **tldr;** run `python create_account.py` in this directory and note down your public and private key. 

## Fund your address
For TestNet, we have a bank/faucet that gives you free Algos to test out your program. Go to the [faucet](https://bank.testnet.algorand.network/), enter your `address` and get some free money. The funds may take ~10 seconds to settle, but you can check out your funds on the blockchain using [AlgoExplorer](https://testnet.algoexplorer.io/). Enter your `address` in the search bar and confirm that your balances are set to 10. 
![algoexplorer screenshot](img/algoexplorer.png)

> **tldr;** Go to the [faucet](https://bank.testnet.algorand.network/), enter your `address` and get some free money. 

[^disclaimer]: As a disclaimer, the opinions expressed are solely my own and do not express the views or opinions of my employer. This is meant to be a short, fun, and somewhat insecure guide to NFTs for beginners in a hackathon setting.

[^1]: Note that in this tutorial, we care more about speed so we may do potentially unsafe stuff with your `private key`. If you are using real funds, make sure you are using [kmd](https://developer.algorand.org/docs/clis/kmd/) or some other secure way for storing your secrets.
