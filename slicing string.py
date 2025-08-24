# Slicing = create a substring by extracting elements from the substring
       #     indexing[] or slice()
       #      [start:stop:step]
from main import first_name

name = "Kalyani Nelluri"
first_name  = name[:7]   #[0:7]
last_name = name[8:]      #[8:end]
funky_name = name[ : : 11]   #[0:end:6]
print(funky_name)
