`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_5_tb;
    reg clock = 1, a;
    reg [3:0] q;

    always #5 clock += 1;
    // a = 1;

	part_5_top_module top0
	(
		.clock(clock),
        .a(a),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_5_tb);
        # 20 a = 1;
        # 20 a = 0;
        # 115 a = 1;
        # 25 a = 0;
  
		#40 $finish();
	end

	initial begin
		$monitor("t=%-4d: clock =  %d, a = %d, q = %d", $time, clock, a, q);
	end
endmodule