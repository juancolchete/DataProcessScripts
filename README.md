# DataProcessScripts
 Process data provided raw

## Process PicPay PDF data
When we want to export a bank statement, on PicPay we have some troubles because we get the data written in a raw PDF that is not easy to convert to CSV or put on a spreadsheet, to solve problem as created the `process_picpay.py` that is a script which allow transform this on CSV.

### Steps to run
1. Create ENV variable `FILE_PATH`
2. Fill `FILE_PATH` with full path of PDF file with PicPay data
3. Run the script `python process_picpay.py`