# Dappley-SDK-Python

[![Licence](https://img.shields.io/github/license/dappley/dappley-java.svg)](https://github.com/dappley/dappley-java/blob/master/LICENSE)

Project dapplay-sdk-python is built for applications of Dappley project base on python language.

## Dependent Environment
1. python：version 2.7。

## Installation
using pip:
```shell
    pip install dappleyPython
```
using source:  
step 1:
```git
    git clone https://github.com/dappley/dappley-sdk-python.git
```
step2:
> __then copy dappleyPython floder to your project.__
## Getting Started
step1: 
You need deploy a contract to dappley blockchain.   
step2: 
You can read [test.py](https://github.com/dappley/dappley-sdk-python/blob/master/examples/test.py) in examples floder to know how to send trasaction to dappley.

## Introducation
   Dappley(ip,port): method is to connect  to dappley blockchain with grpc. Firstly you need to know the dappley grpc ip and port. when you connected successfully,it will return the instance of Dappley client.

   send_transaction(from_address, to_address, amount, private_key, tip, gas_limit, gas_price, contract): it allow you to send transaction to dappley blockchain. If you want to read more about dappley contract ,please to go to this [link](https://github.com/dappley/go-dappley/wiki/SC-Development)
## License
The dappley-java project is licensed under the [GNU Lesser General Public License Version 3.0 (“LGPL v3”)](https://www.gnu.org/licenses/lgpl-3.0.en.html).