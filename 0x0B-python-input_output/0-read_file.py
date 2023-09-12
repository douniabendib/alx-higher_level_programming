#!/usr/bin/python3
def read_file(filename=""):
  try:
  	with open(filename, 'r', encoding="utf-8") as f:
		read_file = f.read()
		print(read_file)
  except Exception as e:
	print(f"An error {str(e)}")
