CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Date DATE NOT NULL,
    Open REAL,
    High REAL,           
    Low REAL,            
    Close REAL,
    Adj_close REAL,          
    Volume INTEGER    
);
