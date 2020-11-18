import numpy as np
import pickle,os

from Common.Module import Module

class SignalRegionSkimmer(Module):
	def analyze(self,data,dataset,cfg):
		cfg.collector.selection_weight = np.abs(data["idL1"]) == 13
		cfg.collector.selection_weight *= np.abs(data["idL2"]) == 13
		cfg.collector.selection_weight *= np.abs(data["idL3"]) == 13
		cfg.collector.selection_weight *= (data["M1"] < 80.) | (data["M1"] > 100.)
		cfg.collector.selection_weight *= (data["M2"] < 80.) | (data["M2"] > 100.)
		cfg.collector.selection_weight *= (data["mt"] < 150.)
		cfg.collector.selection_weight *= (data["M1"] > 0.)
		cfg.collector.selection_weight *= (data["M2"] > 0.)
