import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir	= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/data2017/new/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
data2017 = CMSDataset(
        "Data2017",
        [TFile(os.path.join(input_dir,"total_data_no_dupe.root"),tree_path_in_file,),],
        isMC = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||

data2017.branches = [
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
