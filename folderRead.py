import os
import RPMTreader

# folder_pathで指定した場所にあるedrファイルをすべて読み込みcsvに変換

current = os.path.dirname(os.path.abspath(__file__))
folder_path = "E:\\NAME\\NAME"

print(folder_path)
for root, dirs, files in os.walk(folder_path):
    for f in files:
      if f.endswith(".edr"):
        print(f)
        name = os.path.splitext(f)[0]
        RPMTreader.EDRread(
          filePath = os.path.join(root, f),
          mapGraphPath = os.path.join(current, "mapGraph", name+".png"),
          eventCsvPath = os.path.join(current, "eventCsv", name+".csv"),
        )
                
        RPMTreader.rectROI(
          eventCsvPath = os.path.join(current, "eventCsv", name+".csv"),
          xmin = 0.78,
          xmax = 0.85,
          ymin = 0.54,
          ymax = 0.63,
          # belows are optional
          mapGraphPath = os.path.join(current, "mapROIGraph", name+"_ROI_map.png"),
          tofGraphPath = os.path.join(current, "tofROIGraph", name+"_ROI_tof.png"),
          tofCsvPath = os.path.join(current, "tofROICsv", name+"_ROI_tof.csv"),
          tofBinTime = 100e-6
        )