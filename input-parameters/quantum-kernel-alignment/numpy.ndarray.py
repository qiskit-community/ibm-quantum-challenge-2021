### quantum-kernel-alignment
feature_map	dict	
An instance of FeatureMap in dictionary format used to map classical data into a quantum state space.
data	numpy.ndarray	
NxD array of training data, where N is the number of samples and D is the feature dimension.
labels	numpy.ndarray	
Nx1 array of +/-1 labels of the N training samples.
initial_kernel_parameters	numpy.ndarray	
Initial parameters of the quantum kernel. If not specified, an array of randomly generated numbers is used.
maxiters	int	
Number of SPSA optimization steps. Default is 1.
C	float	
Penalty parameter for the soft-margin support vector machine. Default is 1.
initial_layout
