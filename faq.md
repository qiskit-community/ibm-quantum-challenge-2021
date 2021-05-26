# Frequently Asked Questions
## General
#### How to submit an answer?

Within each exercise notebook, on the [challenge portal](http://ibm.co/iqc2021), you will find guidelines to submit an answer. For example in exercise 1 notebook:

```python
# Check your answer using following code
from qc_grader import grade_ex1
grade_ex1(qc)
```

```python
# Submit your answer. You can re-submit at any time.
from qc_grader import submit_ex1
submit_ex1(qc)
```

#### Can I run the exercise notebooks on a local computer?

Yes it is possible. But we strongly recommend you to solve the exercises on the [challenge portal](http://ibm.co/iqc2021). If you really want to run the exercises locally, you can download the notebooks from the [challenge repository](https://github.com/qiskit-community/ibm-quantum-challenge-2021) and run using Jupyter notebook.

#### Can we check answers on a local computer?

Yes it is possible. But similar to the above question, we strongly recommend you to solve the exercises and check answers on the [challenge portal](http://ibm.co/iqc2021). If you really want to check answers on a local computer, you need to install the [grading client](https://github.com/qiskit-community/Quantum-Challenge-Grader) in addition to downloading the notebooks.

#### Do we need to download the notebooks from github?

No , you can run all exercises on the [challenge portal](http://ibm.co/iqc2021) itself.

#### Do I need to take the exercises in order?

We encourage you to take the exercises in the given order to fall along the theme of 5 important milestones in the history of quantum computing - as the exercises are arranged in chronological order of the discovery of a given milestone. However, you may take the exercises in any order - keeping in mind that you need to solve at least one exercise before getting special access for exercise 4.

#### What is the range of  “estimated time to complete”?

The “estimated time to complete” varies depending on the knowledge and experience of an individual participant. It is given to provide a sense of relative difficulty among the exercises.

#### Is “estimated time to complete” the max time limit to attempt the problem? After that we can't submit? How does it work?

There isn’t a max time limit to attempt a given problem. You may submit answers to any of the 5 exercises at any time before the Challenge ends. The Challenge ends at *9 PM EDT, 26 May, 2021* - after which no answers will be accepted.

#### I encountered “Server error”. What should I do?

We have a lot of participants at the moment. Please be patient, wait and try again.

#### I encountered this error `401 : Unauthorized You are not Authenticated to do this (1)` What should I do?

Please try the following on a notebook on Quantum Lab?
```python
import os
os.environ['QXToken'] = 'your token'
print(os.getenv('QXToken'))
```
You can find your token here: https://quantum-computing.ibm.com/account. Make sure the output matches the token you copied from the account page.

Run the code below to check if authentication is working. If you see a long string in the output, it means 401 error has been resolved.

```python
from qc_grader.api import get_access_token
get_access_token()
```

## Exercise 1 - Toffoli Gate

#### I have the exact same truth table as a CCX but the grader doesn't validate my circuit?

If the grader shows an error in validating your answer, check your answer again by making sure the circuit implements the CCX function for any arbitrary input state with minimal phase difference upto a global phase and keeping in mind that only CX, RZ, SX and X gates are allowed .

#### I get the following error
```
Circuit contains invalid instruction {“instruction”: {measure}} for “unitary” method
```
This error occurs if you use anything besides  CX, RZ, SX and X gates . Please do not add measurement gate at the end of the circuit.

#### What is the lowest cost for this exercise?

The lowest cost discussed so far is 71.

## Exercise 2 - Shor's Algorithm

#### I get the following error
```
Circuit contains invalid instructions {"gates": {ccircuit-459}} for "unitary" method'
```
This error occurs if you use gates other than the allowed gates i.e CNOT and U gates.

#### What is the lowest cost for this exercise?

The lowest cost discussed so far is 6.

## Exercise 3 - Quantum Error Correction

#### I get the following error
```
 “Oops! Circuit did provide a single output. Please review your answer and try again"
```

It means that your circuit is providing multiple outputs. It should give one output in order to find which errors are there on code qubits.

#### What does it mean that the circuit should be designed for the layout?

The qubits in a quantum circuit must be mapped to the physical qubits in a quantum processor. Superconductor based quantum processors only have connectivity between certain qubits (there is no all-qubit connectivity). So, if for example you have a CNOT gate between q0 and q1, but these are not connected to each other, then SWAP gates need to be introduced to connect them. This process is typically done by the transpiler. The addition of additional SWAP gates introduces a lot of error, so it is important to make sure you design your circuit in a way where you avoid the introduction of these SWAPs as much as possible.
In ex3 you have to do precisely that. Tell the transpiler which circuit qubits to map to the physical qubits to minimize the addition of SWAP gates by the transpiler. In order to get it right, you need to modify the original circuit (or create your own) so that the mapping works.

#### I get the following error
```
Please make sure the circuit is created to the initial layout
```
The transpiler assigns your circuit’s qubits to each of physical qubit numbers specified in initial_layout list.
So, for example, the initial_layout list provided in the notebook is currently [0,2,6,10,12,1,5,7,11]. This means that:
q0 in your circuit is assigned to physical qubit 0,
q1 in your circuit is assigned to physical qubit 2,
q2 in your circuit is assigned to physical qubit 6,
You have to design your circuit in a manner ensuring that the qubits which are connected by a CNOT in the quantum circuit are also physically connected in the processor by selecting the right initial_layout so that the transpiler doesn’t introduce any additional gates.

## Exercise 4 - Transmon Qubit

#### I am unable to access this exercise.

You need to solve atleast one other exercise before getting special provider access needed to solve this exercise. See [here](https://github.com/qiskit-community/ibm-quantum-challenge-2021)

#### I get the following error
```python
"401 Client Error : Unauthorized for url... Login with some authorised provider required."
```
Check the following video to resolve the error

[![Exercise 4](https://yt-embed.herokuapp.com/embed?v=Nul1ld2ekOY)](https://www.youtube.com/watch?v=Nul1ld2ekOY)
