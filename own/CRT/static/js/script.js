var val = 100
var $circle = $('#svg #bar');
var r = $circle.attr('r');
var c = Math.PI*(r*2);
              
    if (val < 0) { val = 0;}
    if (val > 100) { val = 100;}
                
    var pct = ((100-val)/100)*c;
                
        $circle.css({ strokeDashoffset: pct});
               
        $('#cont').attr('data-pct',val);

 



