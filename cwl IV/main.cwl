cwlVersion: v1.2
class: Workflow
requirements:
 ScatterFeatureRequirement: {}
inputs:
 in_csv: File
 col_name: string
 k: int

outputs:
 metrics:
   type: File
   outputSource: gather/res

steps:
 remove_outliers:
  run: remove_outliers.cwl
  in:
    csv_file: in_csv
  out: [data]

 generate_k:
  run: generate_k.cwl
  in:
   k: k
  out: [k_list]

 train:
  in:
    dataset: remove_outliers/data
    k: generate_k/k_list
    column_name: col_name
  scatter: [k]
  run: train.cwl
  out: [fold]

 gather:
  in:
   errs: train/fold
  run: gather.cwl
  out: [res]