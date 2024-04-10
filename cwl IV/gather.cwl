cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/gather.py"]
hints:
  DockerRequirement:
    dockerPull: pegaz13/py-env-iv
inputs:
  errs:
   type: string[]
   inputBinding:
    position: 1

outputs:
  res:
    type: stdout
stdout: final_rmse.txt