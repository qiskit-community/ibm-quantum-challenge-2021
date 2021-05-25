#  Hints for solving Challenge Exercises

## Exercise 1 - Toffoli gate

![Hint 1](images/ex1_hint.png)

## Exercise 3 - Quantum error correction

For ex3, you can solve it in three ways:
1. Use the given circuit and given initial layout and fit it according to the layout.
1. Change the initial layout and fit the given circuit according to your new layout.
1. Create a new code that can detect bit and phase flip errors on two code qubits (“error_qubits”).

**Fitting to the layout:** For a two-qubit gate to be a perfect fit, the qubits involved should be directly connected in the backend.

**Using the swap:** If a two-qubit gate is between two distant qubits which are not connected directly, you can use two swaps to connect them. For example, if you want to use a cnot from qubit 0 to 2 and connectivity is like 0-1-2, then to make it perfect fit, you can:
1. First put a swap from 1-2.
1. Then a cnot from 0-1.
1. Then a swap again from 1-2 to restore.