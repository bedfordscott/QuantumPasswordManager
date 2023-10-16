# Quantum Encryption Password Manager

This repository contains a basic and theoretical representation of a quantum encryption password manager using the Qiskit framework. It is intended for educational purposes and is NOT suitable for real-world cryptographic applications.

## Overview

The code demonstrates the BB84 quantum key distribution protocol to generate a shared secret key between two parties (emulated as Alice and Bob). The key is then used for encrypting and decrypting passwords using a simple XOR operation.

## Requirements

- Python 3.6+
- Qiskit

You can install Qiskit using:

```bash
pip install qiskit
```
## Usage

To run the demonstration:
```
bash
Copy code
python quantum_password_manager.py
This will show an encrypted password and its decrypted counterpart.
```
## Disclaimer
This is a basic and theoretical representation of quantum encryption. It does not cover potential vulnerabilities, error corrections, or the intricacies of a full-fledged password manager. Always work with cryptography and quantum experts when designing real-world applications. Use this code at your own risk.

## Contributing
Feel free to submit pull requests or raise issues if you find any. Your contributions are welcome!

## License
This project is open-sourced under the MIT License. See the LICENSE file for details.
