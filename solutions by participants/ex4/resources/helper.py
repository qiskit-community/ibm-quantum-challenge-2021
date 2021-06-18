import numpy as np
import matplotlib.pyplot as plt
from qiskit.pulse import AcquireChannel
#from qiskit.visualization import SchedStyle
from qiskit.ignis.characterization.fitters import IQFitter

# backend/job-specific constants
scale_factor = 1e-7
num_shots = 512
num_spec01_freqs = 71
num_rabi_amps = 71
num_spec12_freqs = 71

spec_range = 0.300 # GHz

# SI unit conversion factors
GHz = 1.0e9 # Gigahertz
MHz = 1.0e6 # Megahertz
kHz = 1.0e3 # kilohertz
us = 1.0e-6 # microseconds
ns = 1.0e-9 # nanoseconds

job_params = {
    'meas_level': 1,
    'meas_return': 'avg',
    'shots': num_shots
}


# Pulse visualization style
#style = SchedStyle(figsize=(4, 4),
#                    axis_font_size=8,
#                    label_font_size=10,
#                    title_font_size=12,
#                    icon_font_size=8)

def get_exc_chans(gv):
    return [AcquireChannel(i) for i in range(gv['backend_config'].n_qubits)]

def get_spec01_freqs(center_freqs, qubit):
    center_freq = round(center_freqs[qubit], -8) # 2 significant digits
    return np.linspace(center_freq/GHz - spec_range/2,
        center_freq/GHz + spec_range/2, num_spec01_freqs)

def get_rabi_amps(max_rabi_amp):
    return np.linspace(0, max_rabi_amp, num_rabi_amps)

def get_spec12_freqs(f01, qubit):
    return np.linspace(f01 - spec_range/2, f01 + spec_range/2, num_spec12_freqs)

# center data around 0
#def center_data(values):
#    return np.array(values) - np.mean(values)

def get_params(exp_type, gv):

  exp_dict = {}

  if exp_type == 'spec01':
    exp_dict = {
      'experiments': gv['spec_schedules'],
      'backend': gv['backend'],
      'qubit_lo_freq': gv['center_frequency'],
      'meas_level': 1,
      'meas_return': 'avg',
      'shots': num_shots
      }

  if exp_type == 'rabi':
    exp_dict = {
      'experiments': gv['rabi_scheds'],
      'backend': gv['backend'],
      'qubit_lo_freq': gv['center_frequency'],
      'meas_level': 1,
      'meas_return': 'avg',
      'shots': num_shots
      }

  if exp_type == 'spec12':
    exp_dict = {
      'experiments': gv['spec_schedules'],
      'backend': gv['backend'],
      'qubit_lo_freq': gv['center_frequency'],
      'meas_level': 1,
      'meas_return': 'avg',
      'shots': 2048
      }

  return exp_dict

def sinusoid(x, A, B, drive_period, phi):
  return A*np.cos(2*np.pi*x/drive_period - phi) + B

def fit_sinusoid(x_vals, y_vals, init_params):
  from scipy.optimize import curve_fit

  fit_params, conv = curve_fit(sinusoid, x_vals, y_vals, init_params)
  y_fit = sinusoid(x_vals, *fit_params)

  return fit_params, y_fit

def lorentzian(x, A, q_freq, B, C):
  return (A/np.pi)*(B/((x-q_freq)**2 + B**2)) + C

def fit_lorentzian(x_vals, y_vals, init_params):
  from scipy.optimize import curve_fit

  fit_params, conv = curve_fit(lorentzian, x_vals, y_vals, init_params)
  y_fit = lorentzian(x_vals, *fit_params)

  return fit_params, y_fit

def get_values_from_result(exp_result, qubit):

  exp_values = []
  for ii in range(len(exp_result.results)):
      exp_values.append(exp_result.results[ii].data.memory[qubit][0])

  return exp_values


class SpecFitter(IQFitter):
    """ Spectroscopy Experiment fitter"""

    def __init__(self, backend_result, xdata, qubits, fit_p0, fit_bounds=None):
        """
            See BaseCalibrationFitter __init__
            fit_p0 is [amp, freq, scale, offset]
        """

        schedule_names = []
        for _, xval in enumerate(xdata):
            schedule_names.append("Spec Pulse at %.3f GH" % xval)

        IQFitter.__init__(self, 'Spec',
                          backend_result, xdata,
                          qubits,
                          lorentzian,
                          fit_p0, fit_bounds,
                          circuit_names=schedule_names,
                          series=['z'])

    def spec_freq(self, qind, series='z'):
        return self._params[series][qind][1]

    def plot(self, qind, series='z', ax=None, show_plot=False):
        """
        Plot the data and fit

        Args:
            qind (int): qubit index
            series (str): data series to plot (for rabi data always '0')
            ax (Axes): matploblib axes (if none created)
            show_plot (bool): do plot.show

        Returns:
            Axes: Plot axes
        """

        fig, ax = plt.subplots(1, 1, figsize=(8,5))

        ax = IQFitter.plot(self, qind, series, ax,
                           show_plot)

        ax.set_ylabel("IQ Signal (au)")
        ax.set_xlabel("Drive Frequency")

        return ax
