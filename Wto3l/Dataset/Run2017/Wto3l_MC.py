import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/2017/new/"
tree_path_in_file = "passedEvents"

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_2017 = CMSDataset(
    "DYJetsToLL_M10To50",
    [TFile(os.path.join(input_dir,"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
    xs = 15810.0,
    sumw = 39505108.0,
    plot_name = "DYJetsToLL_M10To50"
    )
# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_2017 = CMSDataset(
	"DYJetsToLL_M50",
	[TFile(os.path.join(input_dir,"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
	xs = 5343.0,
	sumw = 48655356.0,
	plot_name = "DYJetsToLL_M50"
	)
# ____________________________________________________________________________________________________________________________________________ ||
TTJets_2017 = CMSDataset(
	"TTJets",
	[TFile(os.path.join(input_dir,"TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
	xs = 54.23,
	sumw = 15005665.0,
	plot_name = "TTJets"
	)
# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_2017 = CMSDataset(
	"WZTo3LNu",
	[TFile(os.path.join(input_dir,"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"),tree_path_in_file,),],
	xs = 5.052,
	sumw = 10536966.0,
	plot_name = "WZTo3LNu"
	)
# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples_2017 = [WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M10To50_2017,DYJetsToLL_M50_2017]

for b in bkgSamples_2017:
    b.branches = [
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
