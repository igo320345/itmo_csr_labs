module part_5_top_module (input clock, input a, output wire [3:0] q = 0);

always @ (posedge clock) begin
   if (a) begin
      q = 4;
   end 
   else begin
       q += 1;
       if (q > 6) q = 0;
   end
   
end

endmodule