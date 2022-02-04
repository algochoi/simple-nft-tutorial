# A Simple NFT Tutorial for Algorand Hackers

Let's make a simple NFT on the Algorand TestNet! We'll use the [Purestake API](https://www.purestake.com/), [NFT Storage](https://nft.storage/#getting-started), and the [Algorand Python SDK](https://github.com/algorand/py-algorand-sdk) to programmatically create some NFTs on the fly.

## Pre-requisites
* You should hopefully know how to use the terminal. On MacOS or Ubuntu (any Linux-based OS), just open up your terminal. If you are on Windows, I recommend you install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install), and you will be able to run a Ubuntu terminal on your machine. 
* Your machine should have `git` and `python` installed.

## Create your first [Algorand account](https://developer.algorand.org/docs/get-details/accounts/)
An account consists of a `public key` and a `private key`. 
* The `public key` (aka `wallet address`, or `Algorand address`, which is an encoded form of the public key) is like your banking number that people can use to send you money. This is okay to share with your friends.
* The `private key` (aka `secret`, or sometimes `mnemonic`, which refers to a set of English words that can be translated into a private key) is like your banking PIN. It's probably not a good idea to share your PIN in real life either, so **DO NOT** share your `private key` with anyone![^1]

tldr; run `create_account.py` in this directory and note down your public and private key. 

## Disclaimer
As a disclaimer, the opinions expressed are solely my own and do not express the views or opinions of my employer. This is meant to be a short, fun, and somewhat insecure guide to NFTs for beginners in a hackathon setting.

## Extra notes

[^1]: Note that in this tutorial, we care more about speed so we may do potentially unsafe stuff with your `private key`. If you are using real funds, make sure you are using [kmd](https://developer.algorand.org/docs/clis/kmd/) or some other secure way for storing your secrets.
