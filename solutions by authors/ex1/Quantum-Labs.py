provider = IBMQ.get_provider(
	hub='HUB',
	group='GROUP',
	project='PROJECT'
)

options = {
	'backend_name': 'BACKEND'
}

runtime_inputs = {
	# An instance of FeatureMap in
  # dictionary format used to map
  # classical data into a quantum
  # state space.
  'feature_map': None, # dict (required)
	
	# NxD array of training data,
  # where N is the number
  # of samples and D is
  # the feature dimension.
  'data': None, # numpy.ndarray (required)
	
	# Nx1 array of +/-1 labels
  # of the N training samples.
  'labels': None, # numpy.ndarray (required)
	
	# Initial parameters of the quantum
  # kernel. If not specified, an
  # array of randomly generated numbers
  # is used.
  'initial_kernel_parameters': None, # numpy.ndarray
	
	# Number of SPSA optimization steps.
  # Default is 1.
  'maxiters': None, # int
	
	# Penalty parameter for the soft-margin
  # support vector machine. Default is
  # 1.
  'C': None, # float
	
	# Initial position of virtual qubits
  # on the physical qubits of
  # the quantum device. Default is
  # None.
  'initial_layout': None # list or dict
}

job = provider.runtime.run(
	program_id='quantum-kernel-alignment',
	options=options,
	inputs=runtime_inputs
)

# Job id
print(job.job_id())
# See job status
print(job.status())

# Get results
result = job.result()
