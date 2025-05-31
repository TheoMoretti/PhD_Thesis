# import numpy as np
# import matplotlib.pyplot as plt
# import os

# # Create output directory if it doesn't exist
# os.makedirs("output", exist_ok=True)

# # Define the range of radiation lengths (1 to 7 X0)
# x = np.linspace(1, 7, 100)
# x_markers = np.arange(1, 8, 1)

# # Photon conversion probability formula: P = 1 - exp(-7/9 * X0)
# single_photon_prob = 1 - np.exp(-7/9 * x)
# single_photon_markers = 1 - np.exp(-7/9 * x_markers)

# # Probability that both of two photons convert independently
# two_photon_prob = single_photon_prob**2
# two_photon_markers = single_photon_markers**2

# # Plotting
# plt.figure(figsize=(9.8, 8.1))
# plt.plot(x, single_photon_prob, label="1 Photon", color='blue', linewidth=2)
# plt.plot(x, two_photon_prob, label="2 Photons", color='red', linewidth=2)
# plt.plot(x_markers, single_photon_markers, 'o', color='blue')
# plt.plot(x_markers, two_photon_markers, 'o', color='red')

# plt.xlabel(r"Material Thickness [$X_0$]", fontsize=16)
# plt.ylabel("Conversion Probability", fontsize=16)
# plt.ylim(0, 1.05)
# # plt.title("Photon Conversion Probability vs Radiation Length", fontsize=16)
# plt.grid(True)
# plt.legend(loc = "lower right", framealpha=1, fontsize=14)
# plt.tight_layout()

# # Save as PDF
# plt.savefig("output/photon_conversion_probability.pdf")

# plt.show()

import ROOT 
import math
from array import array

# Create canvas
c = ROOT.TCanvas("c", "Photon Conversion", 800, 700)
c.SetGrid()
c.SetRightMargin(0.08)
c.SetLeftMargin(0.12)
c.SetBottomMargin(0.12)

# Define X values
x_vals = [i for i in range(1, 8)]
n = len(x_vals)

# Compute Y values
y1_vals = [1 - math.exp(-7.0/9 * x) for x in x_vals]
y2_vals = [y**2 for y in y1_vals]

# Create graphs
g1 = ROOT.TGraph(n, array('d', x_vals), array('d', y1_vals))
g2 = ROOT.TGraph(n, array('d', x_vals), array('d', y2_vals))

# Style for g1 (single photon)
g1.SetLineColor(ROOT.kBlue + 1)
g1.SetMarkerColor(ROOT.kBlue + 1)
g1.SetLineWidth(2)
g1.SetMarkerStyle(20)
g1.SetMarkerSize(1.2)

# Style for g2 (two photons)
g2.SetLineColor(ROOT.kRed + 1)
g2.SetMarkerColor(ROOT.kRed + 1)
g2.SetLineWidth(2)
g2.SetMarkerStyle(21)
g2.SetMarkerSize(1.2)

# Create frame histogram for axis setup
frame = ROOT.TH1F("frame", "", 100, 0.9, 7.1)
frame.SetStats(0)
frame.GetYaxis().SetRangeUser(0, 1.05)
frame.SetTitle("Photon Conversion Probability vs Material Thickness")
frame.GetXaxis().SetTitle("X_{0}")
frame.GetYaxis().SetTitle("Conversion Probability")
frame.GetXaxis().SetTitleOffset(1.1)
frame.GetXaxis().SetTitleSize(0.045)
frame.GetYaxis().SetTitleSize(0.045)
frame.GetXaxis().SetLabelSize(0.045)
frame.GetYaxis().SetLabelSize(0.045)
frame.Draw()

# Draw graphs
g1.Draw("LP SAME")
g2.Draw("LP SAME")

# Legend
legend = ROOT.TLegend(0.65, 0.15, 0.88, 0.25)
legend.AddEntry(g1, "1 Photon", "lp")
legend.AddEntry(g2, "2 Photons", "lp")
legend.SetBorderSize(0)
legend.SetFillStyle(1001)
legend.Draw()

# Save as PDF
c.SaveAs("output/photon_conversion_probability_root.pdf")
