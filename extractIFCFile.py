import ifcopenshell
import time

start_time = time.time()
ifc_file_path = "02-211101-4800000773-BHD-MEP-MDL-200002.ifc"
ifc_file = ifcopenshell.open(ifc_file_path)

objects = ifc_file.by_type('IfcObject')
print(f"Total of {len(objects)} objects were found in this ifc file")
print(type(objects[0]))

types = map(lambda x: x.is_a(), objects)
obj_types = set(types)
for x in obj_types:
    print(x)

# for x in objects:
#     print(type(x))
#     print(x.is_a())
#     break


print(f"Time taken {(time.time()-start_time):.2f} seconds")

