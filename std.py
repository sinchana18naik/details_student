import sys

if len(sys.argv) == 3:
  script_name=sys.argv[0]
  name=sys.argv[1]
  roll_no=sys.argv[2]
  print("user provided input values:")
else:
  script_name=sys.argv[0]
  name="sinchana"
  roll_no="169"
  print("no input given == using default values")

print("script name:",script_name)
print("student name:",name)
print("student roll number:",roll_no)
