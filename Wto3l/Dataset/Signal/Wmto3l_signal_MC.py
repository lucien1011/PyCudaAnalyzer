import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/signal/new"
tree_path_in_file = "passedEvents"

mass_points = [15,20,30,45,60]
wm_xs_dict = {
	15: 0.4504013, 
	20: 0.2425901, 
	30: 0.07259808, 
	45: 0.00989203, 
	60: 0.0008656826,
	}
epsilon = 1.0

# ____________________________________________________________________________________________________________________________________________ ||
wm_sample_dict = {}
for m in mass_points:
	wm_sample_dict[m] = CMSDataset(
		"WmTo3l_ZpM"+str(m),
		[TFile(os.path.join(input_dir,"WmTo3l_ZpM%s.root"%str(m)),tree_path_in_file,),],
		xs = wm_xs_dict[m]*epsilon**2,
		plot_name = "WmTo3l_ZpM"+str(m),
		isSignal = True,
		)
	wm_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"WmTo3l_ZpM%s.txt"%str(m)))
# ____________________________________________________________________________________________________________________________________________ ||

wm_signal = [wm_sample_dict[15],wm_sample_dict[20],wm_sample_dict[30],wm_sample_dict[45],wm_sample_dict[60],]

for m,sig in wm_sample_dict.items():
	sig.branches = [
		"genWeight",
        "sumweight",
        "passedFullSelection",
        "passedZXCRSelection",
        "dataMCWeight",
        "pileupWeight",
        "k_qqZZ_qcd_M",
        "k_qqZZ_ewk",
        "idL1",
        "idL2",
        "idL3",
        "pTL1",
        "pTL2",
        "pTL3",
        "etaL1",
        "etaL2",
        "etaL3",
        "phiL1",
        "phiL2",
        "phiL3",
        "massL1",
        "massL2",
        "massL3",
        "IsoL1",
        "IsoL2",
        "IsoL3",
        "MomIdL1",
        "MomIdL2",
        "MomIdL3",
        "met",
        "met_phi",
        "dR12",
        "dR13",
        "dR23",
        "m3l",
        "mt",
		]
