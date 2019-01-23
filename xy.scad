
module xy_curve_png(diode_nb, height){
    filename = str("./data/DIODE (",diode_nb,").png");
    translate([0,0,height/2])
    difference(){
        cube([54*2,52*2,height], center=true);  
        translate([0,0,height-100])
            surface(file=filename, center=true, invert=false, convexity=10);
    }
}
module xy_curve_dxf(diode_nb, height=2, width=1){
    filename = str("./data/DIODE (",diode_nb,").dxf");
    
    linear_extrude(height){
        difference(){
            offset(width/2)
                import(file=filename);
            offset(-width/2)
                import(file=filename);
        }
    }
}

//*
for(i= [1:100]){
translate([1, 1, 1*(i-1)])
    xy_curve_dxf(101-i, 1, 1);
}//*/

//scale([100,100,1])
//import(file="./data/DIODE (1).dxf");
//xy_curve_dxf(1,2,1);