# import os
# base_path=os.path.dirname(__file__)
# folder_path=os.path.join(base_path,"clean_clutter")
# # # os.mkdir(folder_path)

# files=[
#     "riya.png",
#     "sachet.png",
#     "ichchya.png",
#     "anuj.png"
# ]

# for file in files:
#     file_path=os.path.join(folder_path,file)

#     with open(file_path ,"w") as f:
#         pass

# files=os.listdir(folder_path)
# count=1
# for file in files:
#     old_path=os.path.join(folder_path,file)
#     new_name= f"{count}.png"
#     new_path=os.path.join(folder_path,new_name)
#     os.rename(old_path,new_path)
#     count+=1


# import os
# base_path=os.path.dirname(__file__)
# folder_path=os.path.join(base_path,"PDF")
# # # os.mkdir(folder_path)



# pdfs=[
#     "page1.pdf",
#     "page2.pdf",
#     "page3.pdf"
# ]

# for pdf in pdfs:
#     file_path=os.path.join(folder_path, pdf)

#     with open(file_path,"w") as f:
#         pass

import os
from pypdf import PdfWriter

base_path = os.path.dirname(__file__)

folder_path = os.path.join(base_path, "PDF")

files = ["book1.pdf", "book2.pdf"]

merger = PdfWriter()

for pdf in files:
    pdf_path = os.path.join(folder_path, pdf)
    print(pdf_path)
    merger.append(pdf_path)

merger.write(os.path.join(folder_path, "merger-output.pdf"))
merger.close()