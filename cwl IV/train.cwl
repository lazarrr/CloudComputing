cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/train.py"]
hints:
  DockerRequirement:
    dockerPull: pegaz13/python-env-iv
inputs:
  dataset:
    type: File
    inputBinding:
      position: 1
  k:
    type: int
    inputBinding:
      position: 2
  column_name:
    type: string
    inputBinding:
      position: 3


outputs:
  fold:
    type: string
    outputBinding:
     glob: res_string
     loadContents: true
     outputEval: $(self[0].contents)

stdout: res_string