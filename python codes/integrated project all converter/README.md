# THERE ARE 9 ROUTES IN THIS APP 

1. ## '/'
    - ### HOMEPAGE 
        THIS PAGE RENDERS `INDEX.HTML`.
2. ## '/ocr/'
    - ### IMAGE TO MICROSOFT WORD CONVERSION PAGE 
        THIS PAGE RENDERS `OCR.HTML`.
3. ## '/pdf/'
    - ### GSTR 3B PDF TO EXCEL CONVERSION PAGE 
        THIS PAGE RENDERS `pdf to excel.html`.
4. ## '/json_/'
    - ### GSTR 1 JSON TO EXCEL CONVERSION PAGE
        THIS PAGE RENDERS `json to excel.html`.
5. ## '/excel/'
    - ### EXCEL TO TALLY XML CONVERSION PAGE
        THIS PAGE RENDERS `excel to tally.html`.
6. ## '/convert_excel/'
    - ### EXCEL TO TALLY XML OUTPUT PAGE
        - THIS PAGE RENDERS `excel to tally.html`.
        - THE CODE EXECUTION STARTS FROM THE FUNCTION `CONVERT_EXCEL()` AND USES THE CUSTOM FUNCTIONS OF `XML_TREE_GENERATOR.PY FILE`.THERE ARE 5 FUNCTIONS IN THIS FILE.
           -  `READ_EXCEL()` THIS FUNCTION READS THE EXCEL AND EXTRACTS DATA FROM IT.
           -  `CONVERT_DATE_FORMAT()` THIS FUNCTION CONVERTS THE FORMAT OF THE DATE FROM Month-day-year TO YEARMONTHDAY(in number for example 20240403).
           -  `CREATE_DIRECTORY()` THIS FUNCTION CREATES A DIRECTORY IN LOCAL SERVER WHERE THE CONVERTED FOLDER/FILE WILL BE STORED.
           -  `XML_DATA()` THIS FUNCTION CREATES ALL THE LEDGER ENTRIES FROM THE DATA WE RECIEVED .
           -  `XML_GENRATOR()` THIS FUNCTION GENERATES THE XML TREE .
7. ## '/convert_pdf/'
    - ### GSTR 3B PDF TO EXCEL OUTPUT PAGE
        - THIS PAGE RENDERS `pdf to excel.html`. AND SHOWS CONVERSION RESULT. 
        - THE CODE EXECUTION STARTS FROM THE FUNCTION `CONVERT_PDF()` AND USES THE CUSTOM FUNCTIONS OF `EXCEL_TO_PDF.PY FILE`.THERE ARE 5 FUNCTIONS IN THIS FILE.
            - `PDF_CONVERTER()` THIS FUNCTION CONVERTS THE PDF INTO EXCEL.
            - `CREATE_DIRECTORY()` THIS FUNCTION CREATES A DIRECTORY IN LOCAL SERVER WHERE THE CONVERTED FOLDER/FILE WILL BE STORED.
            - `SCAN_DIRECTORY()` THIS FUNCTION CHECKS THE INPUT URL DIRECTORY AND FINDS ALL THE PDF INSIDE IT .
            - `PDF_FILE_VALIDATOR()` THIS FUNCTION CHECKS IF ALL THE 12 PDF FILES ARE PRESENT OR NOT IF ALL ARE PRESENT THEN CONSOLIDATED EXCEL SHEET WILL BE GENERATED ELSE NOT.
            - `CONSOLIDATED_SHEET_GENERATOR()` THIS FUNCTION GENERATES THE CONSOLIDATED SHEET .
8. ## '/convert_json/'
    - ### GSTR 1 JSON TO EXCEL OUTPUT PAGE
        - THIS PAGE RENDERS `json to excel.html`.
        - THE CODE EXECUTION STARTS FROM THE FUNCTION `CONVERT_JSON()` AND USES THE CUSTOM FUNCTIONS OF `B2B.PY , B2B_LINE_ITEMS.PY , NIL.PY , B2CS.PY FILES`.THERE ARE 4 FUNCTIONS IN THESE FILES.
            - `B2B_GENERATER()` THIS FUNCTION GENERATES THE B2B SHEET .
            - `B2B_LINE_ITEMS_GENERATER()` THIS FUNCTION GENERATES B2B LINE ITEMS SHEET .
            - `B2CS_GENERATOR()` THIS FUNCTION GENERATES THE B2CS SHEET .
            - `NIL_GENERATER()` THIS FUNCTION GENERATES THE NIL SHEET .
9. ## '/generate_ocr/'
    - ### IMAGE TO MICROSOFT WORD OUTPUT PAGE
        - THIS PAGE RENDERS `OCR.HTML`.
        - THE CODE EXECUTION STARTS FROM THE FUNCTION `GENERATE_OCR()` AND USES THE CUSTOM FUNCTIONS OF `OCR.PY FILE`.THERE ARE 2 FUNCTIONS IN THIS FILE.
            - `CREATE_DIRECTORY()` THIS FUNCTION CREATES A DIRECTORY IN LOCAL SERVER WHERE THE CONVERTED FOLDER/FILE WILL BE STORED.
            - `OCR_CONVERTER()` THIS FUNCTION CONVERTS THE TEXT INSIDE THE IMAGE TO MICROSOFT WORD FILE

