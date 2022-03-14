
from tkinter import *
import tkinter.font as font
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os


# Define Function to do the Split Operation
def Spliter():
    # Display the root window of the Extractor's Task
    root1 = Tk()
    root1.geometry('500x100')
    root1.title("PDF Tools")

    # Make the Label Widget to Enter The PDF's Path
    lroot1 = Label(root1, text="PDF's Path", fg='#000000')
    f1 = font.Font(weight="bold", size=2)
    lroot1.grid(row=0, column=0, columnspan=1)
    lroot1.configure(font=f1)

    # Make an Input Field to take the PDF's Path
    e1 = Entry(root1, width=60, borderwidth=5)
    e1.insert(0, "PDF's Path")
    e1.grid(row=0, column=2, columnspan=3)

    def gosplit():
        # Display the root window of the confirmation message
        root2 = Tk()
        root2.title("PDF Tools")

        # The Path Of the Folder Spliter in the project
        path = os.path.join(os.getcwd(), 'Spliter')

        def final():
            # Assign path_pdf to the path of the PDF
            path_pdf = e1.get()

            # Stores the PDF's Contents in the variable pdf_file
            pdf_file = PdfFileReader(path_pdf)

            # loop in all the Pages of the PDF
            for page in range(pdf_file.numPages):
                # Initialize a PDF file writer object
                spliter = PdfFileWriter()

                # Add Every page's Contents to the file writer object
                spliter.addPage(pdf_file.getPage(int(page)))

                with open(os.path.join(path, 'Page_{0}.pdf'.format(int(page) + 1)), 'wb') as f:
                    # store Every Page in a particular pdf's file
                    spliter.write(f)
                    f.close()

            # Display the root window to Print the Success of the operation
            root3 = Tk()
            root3.title("PDF Tools")
            suc = Label(root3,
                        text="The PDF Is Splited Successfully at\n {0}".format(os.path.join(path,
                                                                                            "After_Splited.pdf")),
                        font=14)
            suc.grid(row=0, column=0, columnspan=4)
            root3.mainloop()

        # Make the confirmation message and putting it onto screen
        l1 = Label(root2, text="Are you want to proceed", font=12).grid(row=0, column=0, columnspan=4)
        l2 = Label(root2, text="").grid(row=1, column=0)

        # Make 2 Buttons; one for YES option and the other for NO
        b1 = Button(root2, text="YES", command=final)  # if he Clicks YES, Program 'll go to function final()
        b1.grid(row=1, column=1)
        l3 = Label(root2, text="").grid(row=1, column=2)
        b2 = Button(root2, text="NO",
                    command=root2.quit)  # if he Clicks NO, Program 'll Close this confirmation Message
        b2.grid(row=1, column=3)
        l4 = Label(root2, text="").grid(row=1, column=4)

        root2.mainloop()

    # Make a Button to do the Extract
    split = Button(root1, text="Split Now!", command=gosplit, bg='#0052cc', font=14, fg='#ffffff')  # if he clicks
    f2 = font.Font(family='Helvetica', size=20, weight='bold')  # the Button, the program 'll go to gosplit()
    split.grid(row=1, column=1, columnspan=4)
    split['font'] = f2

    root1.mainloop()


# Define Function to do the Extract Operation
def Extractor():
    # Display the root window of the Extractor's Task
    root1 = Tk()
    root1.title("PDF Tools")

    # Make the First Label Widget to Enter The PDF's Path
    lroot1 = Label(root1, text="PDF's Path")
    f1 = font.Font(weight="bold", size=2)
    lroot1.grid(row=0, column=0, columnspan=2)
    lroot1.configure(font=f1)

    # Make an Input Field to take the PDF's Path
    e1 = Entry(root1, width=60, borderwidth=5)
    e1.insert(0, "PDF's Path")
    e1.grid(row=0, column=2, columnspan=3)

    # Make the Second Label Widget to Enter The Page Number
    lroot2 = Label(root1, text="Page Number")
    lroot2.grid(row=1, column=0, columnspan=2)
    lroot2.configure(font=f1)

    # Make an Input Field to take the Page Number
    e2 = Entry(root1, width=60, borderwidth=5)
    e2.insert(0, "Page Number")
    e2.grid(row=1, column=2, columnspan=3)

    def goextract():
        # Display the root window of the confirmation message
        root2 = Tk()

        root2.title("PDF Tools")

        # Define Function final to Extract the Page From the PDF
        def final():
            # Assign path_pdf, page to the pdf path and the page in order
            path_pdf = e1.get()
            page = e2.get()

            # The Path Of the Folder Extractor in the project
            path = os.path.join(os.getcwd(), 'Extractor')

            # Store the pdf in variable pdf_file
            pdf_file = PdfFileReader(path_pdf)

            # Initialize a PDF file writer object
            extractor = PdfFileWriter()

            # Write the page's Contents in the file writer object
            extractor.addPage(pdf_file.getPage(int(page) - 1))

            # The Result Will Place in one PDF (The_Extracted_Page.pdf)
            with open(os.path.join(path, 'The_Extracted_Page.pdf'), 'wb') as f:
                # Write the page's Contents in The_Extracted_Page.pdf
                extractor.write(f)
                f.close()

            # Display the root window to Print the Success of the operation
            root3 = Tk()
            root3.title("PDF Tools")
            suc = Label(root3,
                        text="The Page {0} Are Extracted Successfully at\n {1}".format(page,
                                                                                       os.path.join(path,
                                                                                                    "The_Extracted_Page.pdf")),
                        font=14)
            suc.grid(row=0, column=0, columnspan=4)
            root3.mainloop()

        # Make the confirmation message and putting it onto screen
        l1 = Label(root2, text="Are you want to proceed", font=12).grid(row=0, column=0, columnspan=4)
        l2 = Label(root2, text="").grid(row=1, column=0)

        # Make 2 Buttons; one for YES option and the other for NO
        b1 = Button(root2, text="YES", command=final)  # if he Clicks YES, Program 'll go to function final()
        b1.grid(row=1, column=1)
        l3 = Label(root2, text="").grid(row=1, column=2)
        b2 = Button(root2, text="NO",
                    command=root2.quit)  # if he Clicks NO, Program 'll Close this confirmation Message
        b2.grid(row=1, column=3)
        l4 = Label(root2, text="").grid(row=1, column=4)

        root2.mainloop()

    # Make a Button to do the Extract
    extract = Button(root1, text="Extract Now!", command=goextract, font=14, bg='#0052cc', fg='#ffffff')  # if he clicks
    f2 = font.Font(family='Helvetica', size=20, weight='bold')  # the Button, the program 'll go to goextract()
    extract.grid(row=2, column=1, columnspan=3)
    extract['font'] = f2

    root1.mainloop()


# Define Function to do the Merge Operation
def Merger():
    # Display the root window of the Merger's Task
    root1 = Tk()

    root1.title("PDF Tools")

    # Make the First Label Widget to Enter The PDF's Path 1
    f1 = font.Font(weight="bold", size=2)
    lroot1 = Label(root1, text="PDF's Path 1")
    lroot1.configure(font=f1)
    lroot1.grid(row=0, column=0, columnspan=2)

    # Make an Input Field to take the PDF's Path 1
    e1 = Entry(root1, width=60, borderwidth=5)
    e1.insert(0, "PDF's Path 1")
    e1.grid(row=0, column=2, columnspan=3)

    # Make the Second Label Widget to Enter The PDF's Path 2
    lroot2 = Label(root1, text="PDF's Path 2")
    lroot2.configure(font=f1)
    lroot2.grid(row=1, column=0, columnspan=2)

    # Make an Input Field to take the PDF's Path 2
    e2 = Entry(root1, width=60, borderwidth=5)
    e2.insert(0, "PDF's Path 2")
    e2.grid(row=1, column=2, columnspan=3)

    def gomerge():
        # Display the root window of the confirmation message
        root2 = Tk()
        root2.title("PDF Tools")
        global m1
        global m2

        # Assign m1, m2 to the 2 PDFs path
        m1 = e1.get()
        m2 = e2.get()

        # Define Function final to merge the 2 PDFs
        def final():
            pdfs_list = [m1, m2]

            # Initialize a PDF file merger object
            tool = PdfFileMerger()

            for pdf in pdfs_list:
                # Add Each PDF to the File Merger object
                tool.append(pdf)

            # The Path Of the Folder Merger in the project
            path = os.path.join(os.getcwd(), "Merger")

            # The Result Will Place in one PDF (After_Merged.pdf)
            tool.write(os.path.join(path, "After_Merged.pdf"))
            tool.close()

            # Display the root window to Print the Success of the operation
            root3 = Tk()
            root3.title("PDF Tools")
            suc = Label(root3,
                        text="The Two PDFs Merged Successfully at\n {0}".format(os.path.join(path, "After_Merged.pdf")),
                        font=14)
            suc.grid(row=0, column=0, columnspan=4)

            root3.mainloop()

        # Make the confirmation message and putting it onto screen
        l1 = Label(root2, text="Are you want to proceed", font=12).grid(row=0, column=0, columnspan=4)
        l2 = Label(root2, text="").grid(row=1, column=0)

        # Make 2 Buttons; one for YES option and the other for NO
        b1 = Button(root2, text="YES", command=final)  # if he Clicks YES, Program 'll go to function final()
        b1.grid(row=1, column=1)
        l3 = Label(root2, text="").grid(row=1, column=2)
        b2 = Button(root2, text="NO",
                    command=root2.quit)  # if he Clicks NO, Program 'll Close this confirmation Message
        b2.grid(row=1, column=3)
        l4 = Label(root2, text="").grid(row=1, column=4)

        root2.mainloop()

    # Make a Button to do the Merge
    merge = Button(root1, text="Merge Now!", command=gomerge, font=14, bg='#0052cc', fg='#ffffff')  # if he clicks the
    f2 = font.Font(family='Helvetica', size=20, weight='bold')  # Button the program 'll go to the function gomerge
    merge['font'] = f2
    merge.grid(row=2, column=1, columnspan=3)

    # 2 Variables to hold the two PDFs' Paths
    global m1
    global m2

    root1.mainloop()


# Display Main root window
root = Tk()

root.title("PDF Tools")

# Put icon for the App
root.iconphoto(True, PhotoImage(file='books.png'))

# Make the Welcome Message
frame = LabelFrame(root, text="", padx=5, pady=5, bg='#000000')
frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
welcome = Label(frame, text="Welcome to PDF Separator and Merger Application", font=20, borderwidth=10, bg='#000000',
                fg='#ffffff', )
Font_style = ("Comic Sans MS", 20, "bold")
welcome.configure(font=Font_style)

# finally, put the message onto screen
welcome.grid(row=0, column=0, columnspan=4)

# Make Frames to hold the button
frame1 = LabelFrame(root, text="", padx=5, pady=5, bg='#0052cc')
frame2 = LabelFrame(root, text="", padx=5, pady=5, bg='#0052cc')
frame3 = LabelFrame(root, text="", padx=5, pady=5, bg='#0052cc')
frame4 = LabelFrame(root, text="", padx=5, pady=5, bg='#0052cc')

# Put the Frames onto the screen
frame1.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
frame2.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
frame3.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
frame4.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

# Make The Buttons
task1 = Button(frame1, text="Merge Two PDFs", command=Merger, padx=34, pady=10, bg='#0052cc', fg='#ffffff')
task2 = Button(frame2, text="Extract a page from PDF", command=Extractor, padx=15, pady=10, bg='#0052cc', fg='#ffffff')
task3 = Button(frame3, text="Split a PDF", command=Spliter, padx=50, pady=10, bg='#0052cc', fg='#ffffff')
task4 = Button(frame4, text="Exit", command=root.quit, padx=69, pady=10, bg='#0052cc', fg='#ffffff')
font_style = font.Font(family='Helvetica', weight='bold')
task1['font'] = font_style
task2['font'] = font_style
task3['font'] = font_style
task4['font'] = font_style

# Putting the Buttons onto the screen
task1.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
task2.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
task3.grid(row=3, column=1, columnspan=2, padx=2, pady=2)
task4.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

root.mainloop()
