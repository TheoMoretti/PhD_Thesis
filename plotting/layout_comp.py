import ROOT
from array import array
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Global style improvements
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetTitleFont(42, "XYZ")
ROOT.gStyle.SetLabelFont(42, "XYZ")
ROOT.gStyle.SetTitleSize(0.045, "XYZ")
ROOT.gStyle.SetLabelSize(0.04, "XYZ")
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetGridStyle(3)
ROOT.gStyle.SetGridColor(ROOT.kGray+2)

# Create canvas
c = ROOT.TCanvas("c", "Percent Histogram Comparison", 900, 700)
c.SetGrid()
c.SetLeftMargin(0.12)
c.SetBottomMargin(0.12)

# Define bin edges
bins = [0, 1, 2, 3, 4, 5, 6]
h1 = ROOT.TH1F("h1", "", len(bins)-1, array('f', bins))
h2 = ROOT.TH1F("h2", "", len(bins)-1, array('f', bins))
h3 = ROOT.TH1F("h3", "", len(bins)-1, array('f', bins))

# Bin contents (scaled to percent)
contents1 = [754, 178, 27, 15, 9, 9]
contents2 = [576, 226, 106, 40, 23, 10]
contents3 = [756, 140, 63, 25, 10, 10]

for i, val in enumerate(contents1): h1.SetBinContent(i+1, val * 0.1)
for i, val in enumerate(contents2): h2.SetBinContent(i+1, val * 0.1)
for i, val in enumerate(contents3): h3.SetBinContent(i+1, val * 0.1)

# Styling
colors = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+2]
styles = [20 ,21, 22]
for hist, color , style in zip([h1, h2, h3], colors, styles):
    hist.SetLineColor(color)
    hist.SetLineWidth(2)
    hist.SetMarkerColor(color)
    hist.SetMarkerStyle(style)
    hist.SetMarkerSize(1)

# Axis formatting
h2.GetXaxis().SetTitle("Detector plane")
h2.GetYaxis().SetTitle("Event rate [%]")
h2.GetXaxis().CenterTitle(False)
h2.GetYaxis().CenterTitle(False)
h2.SetMaximum(80)
h2.SetMinimum(0)

# Draw histograms

h2.Draw("HIST")
h3.Draw("HIST SAME")
h1.Draw("HIST SAME")

h2.Draw("P SAME")
h3.Draw("P SAME")
h1.Draw("P SAME")

# Legend with white background
legend = ROOT.TLegend(0.50, 0.72, 0.88, 0.88)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(h1, "W = 2x6 mm + 4x2 mm", "l")
legend.AddEntry(h2, "W = 6x3.5 mm", "l")
legend.AddEntry(h3, "W = 1x6 mm + 5x3 mm", "l")
legend.SetBorderSize(0)
legend.SetFillColor(ROOT.kWhite)
legend.SetFillStyle(1001)
legend.Draw()

# Save as PDF
c.SaveAs("output/conversion_plane.pdf")
