import nbformat as nbs
path = r"fileedittest/text.ipynb"
file = open(path,"r",encoding="utf-8")
data = nbs.read(file,4)

print(f"This is the Data we find in {path}")

print(f"No of Cell in the Notebook: {len(data['cells'])}")
Cells = data["cells"] #Cells is a list
print("Code -:")
for i in Cells: print(i['source'] if len(i['source']) != 0 else "No Code")
print("Outputs -:")
for i in Cells: print(i['outputs'] if len(i['outputs']) else "No Output")