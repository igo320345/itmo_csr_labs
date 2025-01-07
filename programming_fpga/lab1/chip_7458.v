module chip_7458 ( 
    input p1a, p1b, p1c, p1d, p1e, p1f,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y );

    wire x, y, z, w;

    assign x = p2a && p2b;
    assign y = p2c && p2d;
    assign z = p1a && p1b && p1c;
    assign w = p1d && p1e && p1f;

    assign p2y = x || y;
    assign p1y = z || w;

endmodule