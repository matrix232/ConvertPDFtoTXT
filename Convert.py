# pdfplumber - to work with convert from PDF to Word
import pdfplumber


class Converting:

    def __init__(self, infile):
        self.infile = infile

    def file_convert(self):
        try:
            with pdfplumber.open(r"{0}".format(self.infile)) as  infile, open("outfile.txt", "w") as out_file:
                # get text from  pages
                PagesNum = infile.pages
                for i in range(len(PagesNum)):
                    first_page = infile.pages[i]
                    # extracting text
                    out_file.write(first_page.extract_text())


        except FileNotFoundError:
            print("ERROR! FILE NOT FOUND!")
        except:
            print("ERROR!")
