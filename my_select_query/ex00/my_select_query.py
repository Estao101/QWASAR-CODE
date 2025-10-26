import csv
from io import StringIO

class MySelectQuery:
    def __init__(self, csv_content):
        """
        Initialize the query object with given CSV content (as a string).
        Parses the first row as headers and the remaining as data rows.
        """
        self.headers = []   
        self.rows = []      
        self.raw_rows = []  

        # Use csv.reader to handle CSV parsing (handles commas, quotes, etc.)
        reader = list(csv.reader(StringIO(csv_content.strip())))
        self.headers = reader[0]  

        
        for row in reader[1:]:
            self.raw_rows.append(",".join(row))  # Reconstruct the original row as a comma-separated string
            self.rows.append(dict(zip(self.headers, row)))  # Convert row into dictionary using headers

    def where(self, column_name, value):
        """
        Return a list of strings (original CSV lines) where the specified column matches the given value.
        """
        result = []

        
        for row_dict, raw in zip(self.rows, self.raw_rows):
            if column_name in row_dict and row_dict[column_name] == value:
                result.append(raw)  # Match found: return original CSV line

        return result  


#if __name__ == "__main__":
#    csv_data = """name,year_start,year_end,position,height,weight,birth_date,college
#Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University
#Zaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University
#Kareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'
#Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University"""

#    query = MySelectQuery(csv_data)
#    results = query.where("name", "Alaa Abdelnaby")

#   for r in results:
#        print(r)