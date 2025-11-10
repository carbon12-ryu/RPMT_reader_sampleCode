import os
import RPMTreader

current = os.path.dirname(os.path.abspath(__file__))

t0_pulse, neutrons, tof_data, total_count = RPMTreader.EDRread(
  filePath = os.path.join(current, "edrFiles", "rpmt_run0.edr"),
  # belows are optional
  mapGraphPath = os.path.join(current, "mapGraph", "rpmt_run0_map.png"),
  tofGraphPath = os.path.join(current, "tofGraph", "rpmt_run0_tof.png"),
  eventCsvPath = os.path.join(current, "eventCsv", "rpmt_run0_event.csv"),
  tofCsvPath = os.path.join(current, "tofCsv", "rpmt_run0_tof.csv"),
  # xSwap = True,
  # ySwap = True,
  tofBinTime = 100e-6 # default value is 10e-6
)

# read event csv and set rectanglar position ROI
t0_pulse, masked_neutrons, tof_data, total_count = RPMTreader.rectROI(
  eventCsvPath = os.path.join(current, "eventCsv", "rpmt_run0_event.csv"),
  xmin = 0.78,
  xmax = 0.85,
  ymin = 0.54,
  ymax = 0.63,
  # belows are optional
  mapGraphPath = os.path.join(current, "mapGraph", "rpmt_run0_map_rectROI.png"),
  tofGraphPath = os.path.join(current, "tofGraph", "rpmt_run0_tof_rectROI.png"),
  tofCsvPath = os.path.join(current, "tofCsv", "rpmt_run0_tof_rctOI.csv"),
  timeROImin = 0.05,
  timeROImax = 0.06,
  tofBinTime = 100e-6 # default value is 10e-6
)

# read event csv and set circular position ROI
t0_pulse, masked_neutrons, tof_data, total_count = RPMTreader.circleROI(
  eventCsvPath = os.path.join(current, "eventCsv", "rpmt_run0_event.csv"),
  xcenter = 0.82,
  ycenter = 0.585,
  radius=0.03,
  # belows are optional
  mapGraphPath = os.path.join(current, "mapGraph", "rpmt_run0_map_circleROI.png"),
  tofGraphPath = os.path.join(current, "tofGraph", "rpmt_run0_tof_circleROI.png"),
  tofCsvPath = os.path.join(current, "tofCsv", "rpmt_run0_tof_circleROI.csv"),
  # timeROImin = 0.04,
  # timeROImax = 0.06,
  tofBinTime = 100e-6 # default value is 10e-6
)