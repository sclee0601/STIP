import httplib2
import xlsxwriter
import json


if __name__ == '__main__':
    fname = input("Enter the file name:")
    syear = input("Enter the session: ex)2020")

    h = httplib2.Http(".cache")
    #list Customers
    resp, content = h.request("http://localhost:8000/listBills/"+syear, "GET")
    str_content  = content.decode('utf-8')
    bill_list = json.loads(str_content)

    headings = ["Bill Number", "Bill Title", "Chamber Introduction", "Bill/Resolution Summary", "Cheif Patron","Bill Lead Sponsor District","House Patrons","Senate Patrons", "Fulltext Intro", "Fulltext Passed", "Session"]

    workbook = xlsxwriter.Workbook(fname+'.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for item in headings:
        worksheet.write(row,col, item)
        col+=1 

    bill_len = len(bill_list)
    for i in range(0,bill_len):
        col = 0
        row += 1

        temp = bill_list[i]
        print(temp['bill_number'])
        bill_data = [temp['bill_number'],temp['bill_title'],temp['chamber_intro'],temp['summary'],temp['chief_patron'],temp['district'],
                     temp['house_patrons'],temp['senate_patrons'],temp['fulltext_i'],temp['fulltext_p'],temp['session']]
        for data in bill_data:
            worksheet.write(row, col, data)
            col+=1
    workbook.close()

