# CS50’s Introduction to Programming with Python.
# Problem Set 8 - Shirtificate.


from fpdf import FPDF

def main() :

    # Get the user's name.
    name = input( 'Name: ' ).strip()

    # Creat an FPDF object - portrait and A4 size.
    pdf = FPDF( orientation='P', unit='mm', format='A4' )

    # Add a page to the FPDF object.
    pdf.add_page()

    # Specify font - name, style, size.
    pdf.set_font( 'Helvetica', 'B', 48 )

    # Add a text cell to the page - width, height, border, text, alignment.
    pdf.cell( w=190, h=20, border=0, txt='CS50 Shirtificate', align='C' )

    # Add an image  to the page- file, x, y, width, height.
    pdf.image( 'shirtificate.png', 10, 50, 190, 190 )

    # Specify new cursor position, text color and font.
    pdf.set_x(0)
    pdf.set_y(130)
    pdf.set_text_color( 255, 255, 255 )
    pdf.set_font( 'Helvetica', 'I', 24 )

    # Add another text cell to the page  - width, height, border, text, alignment.
    pdf.cell( w=190, h=10, border=0, txt=f'{name} took CS50', align='C' )

    # Output PDF file.
    pdf.output( 'shirtificate.pdf' )
    
if __name__ == '__main__' :
    main()