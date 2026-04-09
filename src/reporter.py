from fpdf import FPDF

def duration_report(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Analysis of Media Content Durations", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    
    pdf.set_y(190) 
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This report visualizes the runtime trends across the library. It compares the average "
                         "minutes for feature films against the average number of seasons for television series, "
                         "highlighting the typical consumption time required for different content formats.")
    pdf.output("Duration_Report.pdf")


def report_content_distribution(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Global Content Portfolio Distribution", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This breakdown illustrates the balance between Movies and TV Shows within the dataset. "
                         "The visualization identifies which medium dominates the current catalog, providing "
                         "insight into production focus and library diversity.")
    pdf.output("Content_Distribution.pdf")


def report_yearly_trend(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Historical Release Volume Trends", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
   
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This chart tracks the growth of the entertainment industry over time. By observing the "
                         "volume of releases per year, we can identify periods of rapid expansion and the "
                         "evolving pace at which new content is added to global platforms.")
    pdf.output("Yearly_Trends.pdf")


def report_top_countries(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Leading Nations in Global Content Production", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
   
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This report identifies the top 10 countries with the highest output of movies and shows "
                         "over the last several decades. It highlights the major geographic hubs of the "
                         "entertainment industry and their comparative contribution to the global market.")
    pdf.output("top_countries.pdf")


def report_rating_distribution(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Audience Demographics & Rating Classification", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
   
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This distribution maps content to specific age-based maturity ratings. It provides a "
                         "clear overview of whether the library is geared toward family-friendly viewing, "
                         "teen audiences, or restricted adult content.")
    pdf.output("rating_distribution.pdf")
