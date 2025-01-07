`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_3_tb;

	wire [3:0] q;
    reg [3:0] a, b, c, d, e;

    always #5 c += 1;

	part_3_top_module top0
	(
		.a(a),
        .b(b),
        .c(c),
        .d(d),
        .e(e),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_3_tb);
        #10 a = 10; b = 11; c = -1; d = 13; e = 14;

        #95 c = 1;
        #5 a = 1; b = 2; d = 3; e = 4; c = -1;
        
        #45 c = 7;
        #5 a = 5; b = 6; d = 7; e = 8; c = -1;

		#40 $finish();
	end

	initial begin
		$monitor("t=%-4d: a = %d, b = %d, c = %d, d = %d, e=%d, q = %d", $time, a, b, c, d, e, q);
	end
endmodule