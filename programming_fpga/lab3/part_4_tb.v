`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_4_tb;
    reg clock, a;
    reg p, q;

    always #30 clock += 1;
    always #5 a += 1;

	part_4_top_module top0
	(
		.clock(clock),
        .a(a),
        .p(p),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_4_tb);
        # 70 clock = 0; a = 1;

        # 75 a = 1;
        # 5 a = 1;
        # 5 a = 1;
        # 5 a = 1;
        # 5 a = 1;

        # 45 a = 1;
        #10 a = 0;
        #30 a = 1;
        #10 a = 0;
        # 10 a = 1;
  
		#10 $finish();
	end

	initial begin
		$monitor("t=%-4d: clock =  %d, a = %d, p = %d, q = %d", $time, clock, a, p, q);
	end
endmodule