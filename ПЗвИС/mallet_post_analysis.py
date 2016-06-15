from openpyxl import load_workbook
wb=load_workbook(filename = r"C:\Users\802925\Downloads\30topics.xlsx")
ws1=wb['1']
ws2=wb['2']
ws3=wb['3']
topics=[]
for x in range(0,30):
    topics.append(ws1.columns[4][x].value)
for r in ws2.rows:
    for x in range(2,32):
        if( float(r[x].value) > 0.7):
            print( r[1].value, r[x].value, topics[x-2])
print("Infer topics:")
row_values=[]
for r in ws3.rows:
    tmp_topics=[]
    for x in range(2,32):
        if( float(r[x].value) > 0.3):
            print( r[1].value, r[x].value, topics[x-2])
            tmp_topics.append(" ".join([topics[x-2],r[x].value]))
    if(len(tmp_topics)>0):
        r[0].value=" | ".join(tmp_topics)
    else:
        r[0].value="Unknown"
wb.save(r"C:\Users\802925\Downloads\30topics_analysed.xlsx")
