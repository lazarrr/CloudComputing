cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python"]
hints:
  DockerRequirement:
    dockerPull: pegaz13/cwl_python_env
inputs:
  python_file:
   type: File
   inputBinding:
    position: 1
  csv_file:
    type: File
    inputBinding:
      position: 2
  training_ratio:
    type: float
    inputBinding:
      position: 3
  column_name:
    type: string
    inputBinding:
      position: 4

outputs:
  output_metrics:
    type: stdout
stdout: metrics.txt
