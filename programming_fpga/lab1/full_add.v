module full_add ( 
    input a, b, cin,
    output sum, cout );

    assign sum = a + b + cin;
    assign cout = (a & b) | (a & cin) | (b & cin);


endmodule