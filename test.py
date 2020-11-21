
import helper
from helper import getChain

sigchain_tuple = getChain()
sigchain = sigchain_tuple[0]
sigchain_nevents = sigchain_tuple[1]




#Signal_2016.GetListOfBranches().ls()
for i in range(number_events):
	Signal_2016.GetEntry(i)
	event = Signal_2016.GetLeaf('event').GetValue()

var=[ nPhoton, Photon_eta, Photon_pt, Photon_phi, Photon_hoe, Photon_mvaID, Photon_sieie, nJet, Jet_btagCMVA, Jet_btagCSVV2,Jet_btagDeepB,Jet_btagDeepC, Jet_btagDeepFlavB, Jet_btagDeepFlavC, Jet_eta, Jet_phi, Jet_pt, Jet_puIdDisc, Jet_jetId, Jet_puId ]

for n in range(var):
	h = ROOT.TH1D('h_tmp', 'h_tmp', 30,-3,3)
	Signal_2016.Draw("n")
	cb = ROOT.TCanvas("cb","cb",564,232,600,600)
	cb.cd()
	h.Draw()
	cb.Draw()
	cb.SaveAs(plots/pngs/n+'.png')
	cb.SaveAs(plots/pdfs/n+'.pdf')
	cb.SaveAs(plots/roots/n+'.root')

