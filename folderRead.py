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