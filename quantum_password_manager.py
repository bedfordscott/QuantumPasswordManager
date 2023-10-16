# Quantum Encryption Password Manager
# NOTE: This is a theoretical and educational representation. NOT for real-world use.

import random
from qiskit import QuantumCircuit, Aer, assemble
from qiskit.providers.aer import QasmSimulator

class QuantumPasswordManager:

    def __init__(self, bitstring_length=16):
        self.bitstring_length = bitstring_length
        self.key = self.bb84_key_distribution()

    def bb84_key_distribution(self):
        alice_bits = [random.randint(0, 1) for _ in range(self.bitstring_length)]
        alice_bases = [random.randint(0, 1) for _ in range(self.bitstring_length)]
        qc = QuantumCircuit(self.bitstring_length)
        
        for q in range(self.bitstring_length):
            if alice_bases[q] == 1:
                qc.h(q)
            if alice_bits[q] == 1:
                qc.x(q)
        
        bob_bases = [random.randint(0, 1) for _ in range(self.bitstring_length)]
        for q in range(self.bitstring_length):
            if bob_bases[q] == 1:
                qc.h(q)
        
        qc.measure_all()
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(qc)
        result = aer_sim.run(qobj).result()
        counts = result.get_counts(qc)
        bob_bits = list(counts.keys())[0]

        key = []
        for i in range(self.bitstring_length):
            if alice_bases[i] == bob_bases[i]:
                key.append(bob_bits[i])

        return ''.join(key)

    def encrypt(self, message):
        return ''.join([str(int(m) ^ int(k)) for m, k in zip(message, self.key[:len(message)])])

    def decrypt(self, encrypted_message):
        return ''.join([str(int(m) ^ int(k)) for m, k in zip(encrypted_message, self.key[:len(encrypted_message)])])

if __name__ == "__main__":
    manager = QuantumPasswordManager()
    encrypted = manager.encrypt("0011001100110011")
    decrypted = manager.decrypt(encrypted)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
