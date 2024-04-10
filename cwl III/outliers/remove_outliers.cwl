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

outputs:
  output_csv:
    type: stdout
stdout: output.csv