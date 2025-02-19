CREATE TABLE stocks (
    Title TEXT NOT NULL,
    Date DATE NOT NULL,
    Open REAL,
    High REAL,           
    Low REAL,            
    Close REAL,
    Adj_close REAL,          
    Volume INTEGER,
    PRIMARY KEY (Date, Title)    
);
