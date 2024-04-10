cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/outliers.py"]
hints:
  DockerRequirement:
    dockerPull: pegaz13/python-env-iv
inputs:
  csv_file:
    type: File
    inputBinding:
      position: 1

outputs:
  data:
    type: stdout
stdout: data.csv
