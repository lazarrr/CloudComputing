cwlVersion: v1.2
class: Workflow
inputs:
 outliers: File
 train: File
 in_csv: File
 col_name: string
 tr_ratio: float

outputs:
  metrics:
   type: File
   outputSource: step_two/output_metrics

steps:
 step_one:
  run: remove_outliers.cwl
  in:
    python_file: outliers
    csv_file: in_csv
  out: [output_csv]

 step_two:
  run: train.cwl
  in:
   python_file: train
   csv_file: step_one/output_csv
   training_ratio: tr_ratio
   column_name: col_name
  out: [output_metrics]
