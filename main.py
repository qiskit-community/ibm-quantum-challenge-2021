# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=
# 👋 QISKIT RUNTIME PROGRAM: `quantum-kernel-alignment`
# https://app.quantumcomputing.com/runtime/quantum-kernel-alignment
#
# This examples calls the `quantum-kernel-alignment` runtime program.
#
# Quantum Kernel Alignment is an iterative quantum-classical algorithm 
# to massage 💆‍♀️ data to align it better for Support Vector Machines 
# Classification problems by learning from a family of kernels.


import pandas as pd 
import numpy as np
from qka_files.qka import FeatureMap
import strangeworks.qiskit
from strangeworks.qiskit.provider import StrangeworksProvider


# --------------------------------
# ✅ SETUP YOUR PROVIDER
#
# Assuming you've enabled Runtime, this should automatically work.
# If not, 👉 https://app.quantumcomputing.com/runtime/enable
provider = StrangeworksProvider(
    hub="strangeworks-hub",
    group="qc-com",
    project="runtime")

# --------------------------------
# ✅ SELECT A BACKEND

# You can run on the simulator 💻 (🐇)
options = {'backend_name': "ibmq_qasm_simulator"}

# But hardware has been chilled ❄️ for your enjoyment (🐢)
# options = {'backend_name': "ibm_nairobi"}
# Be patient with hardware, it takes a long time, and it is sometimes spotty.

# --------------------------------
# ✅ READ IN SOME DATA
df = pd.read_csv('qka_files/dataset_graph7.csv',sep=',', header=None) 

# this date is the one that will be used for the classification problem
data = df.values

# choose number of training and test samples per class 👩‍🏫:
num_train = 5
num_test = 5

# extract training and test sets and sort them by class label
train = data[:2*num_train, :]
test = data[2*num_train:2*(num_train+num_test), :]

ind=np.argsort(train[:,-1])
x_train = train[ind][:,:-1]
y_train = train[ind][:,-1]

ind=np.argsort(test[:,-1])
x_test = test[ind][:,:-1]
y_test = test[ind][:,-1]

# feature dimension is twice the qubit number
d = np.shape(data)[1]-1     

# we'll match this to the 7-qubit graph
em = [[0,2],[3,4],[2,5],[1,4],[2,3],[4,6]]    


# define the feature map
fm = FeatureMap(feature_dimension=d, entangler_map=em)

# set the initial parameter for the feature map    
initial_point = [0.1]   

# SVM soft-margin penalty
C = 1                                                           
maxiters = 10    

initial_layout = [0, 1, 2, 3, 4, 5, 6]     

# Setup a callback for our interim result
def interim_result_callback(job_id, interim_result):
    print(f"interim result: {interim_result}\n")

# Set our inputs
program_inputs = {
    'feature_map': fm,
    'data': x_train,
    'labels': y_train,
    'initial_kernel_parameters': initial_point,
    'maxiters': maxiters,
    'C': C,
    'initial_layout': initial_layout
}

# --------------------------------
# ✅ RUN THE PROGRAM

job = provider.runtime.run(program_id="quantum-kernel-alignment",
                              options=options,
                              inputs=program_inputs,
                              callback=interim_result_callback,
                              )


print("🖼 Circuit for the feature map:")
strangeworks.qiskit.extract_diagram(fm.construct_circuit(x=x_train[0], parameters=initial_point))


# --------------------------------
# ✅ GET THE FINAL RESULT

# Execution will pause here until the result returns
result = job.result()

# And finally, we'll display the output
strangeworks.print(result, type="log", label="Final Result")

# 🎉 Yay, Runtime success!
#
# ⏭ Try other programs here:
# https://app.quantumcomputing.com/runtime/